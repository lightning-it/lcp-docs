# Local ModuLix Runtime Containers (Build + Start)

This guide replaces local wrapper-script usage and documents the explicit workflow:

1. Build local images.
2. Point `run-modulix.sh` to those local images.
3. Run services/playbooks.

## Scope

This document is for local development/testing of ModuLix runtime execution with:

- local run EE image (`RUN_EE_IMAGE`)
- local toolbox image (`RUN_TOOLBOX_IMAGE`)
- `modulix-automation/scripts/modulix/run-modulix.sh`

## Container Flow (ASCII)

```text
Host
  |
  |  ./run-modulix.sh --inventory-dir ... services <wunderbox|aap> ...
  v
+---------------------------------------------------------------+
| Toolbox container (RUN_TOOLBOX_IMAGE)                         |
|  process: ansible-nav-local run <playbook>                    |
|                                                               |
|  if RUN_USE_HOST_EE_IMAGE=true:                               |
|    1) receives run-ee tar from host                           |
|    2) podman load -i /tmp/run-ee.tar                          |
|                                                               |
|  then starts nested execution via ansible-navigator           |
+------------------------------+--------------------------------+
                               |
                               | nested podman run
                               v
+---------------------------------------------------------------+
| Run-EE container (RUN_EE_IMAGE)                               |
|  process chain: ansible-navigator -> ansible-runner ->        |
|                 ansible-playbook                              |
|  mounts: project, inventory, vault password file              |
|  reads: collections, roles, playbooks                         |
+------------------------------+--------------------------------+
                               |
                               v
                    Managed target host(s)
```

Runtime dependency order:

1. Host starts toolbox container.
2. Toolbox starts run-EE container.
3. Run-EE executes `ansible-playbook` (via `ansible-runner`).
4. Run-EE connects to managed hosts (SSH/inventory/vault inputs).

## Prerequisites

- Podman installed and working on the host.
- `ssh-agent` running with a loaded key (`ssh-add -L` must show keys).
- Local checkout of:
  - `modulix-automation`
  - `container-ee-wunder-ansible-ubi9`
  - `container-ee-wunder-toolbox-ubi9` (official toolbox repo)
- Inventory directory and Vault password file available in your workspace.

Official toolbox repo:

- `https://github.com/lightning-it/container-ee-wunder-toolbox-ubi9`

## Recommended Local Image Tags

Use stable local tags so commands stay consistent:

```bash
export NEW_ROOT="${NEW_ROOT:-$HOME/sources/lit/NEW}"
export RUN_EE_IMAGE=localhost/ee-wunder-ansible-ubi9-certified:local
export RUN_TOOLBOX_IMAGE=localhost/ee-wunder-toolbox-ubi9:local
```

## 1) Build Local Run EE Image

```bash
cd "$NEW_ROOT/container-ee-wunder-ansible-ubi9"
podman build -t "$RUN_EE_IMAGE" .
```

Quick verification:

```bash
podman run --rm "$RUN_EE_IMAGE" ansible --version
```

## 2) Build Local Toolbox Image

```bash
cd "$NEW_ROOT/container-ee-wunder-toolbox-ubi9"
podman build -t "$RUN_TOOLBOX_IMAGE" .
```

Quick verification:

```bash
podman run --rm "$RUN_TOOLBOX_IMAGE" ansible-nav-local --help
```

If you do not have the toolbox repo locally yet:

```bash
cd "$NEW_ROOT"
git clone https://github.com/lightning-it/container-ee-wunder-toolbox-ubi9.git
cd container-ee-wunder-toolbox-ubi9
podman build -t "$RUN_TOOLBOX_IMAGE" .
```

## 3) Prepare Runtime Environment for `run-modulix.sh`

```bash
cd "$NEW_ROOT/modulix-automation/scripts/modulix"

export INVENTORY_DIR="$NEW_ROOT/ansible-inventory-lit/inventories"
export INVENTORY_NAME=<inventory-name>
export VAULT_PASS_FILE="$NEW_ROOT/modulix-automation/.vault-pass.txt"

# No registry pull needed when both images are localhost/*
export RUN_SKIP_AUTH=true

# Keep enabled so host EE image is transferred into toolbox runtime (recommended)
export RUN_USE_HOST_EE_IMAGE=true

# Optional: if your service playbooks require Vault token
export VAULT_TOKEN="<token>"
```

Sanity checks:

```bash
test -S "${SSH_AUTH_SOCK:-}"
test -s "$VAULT_PASS_FILE"
podman image exists "$RUN_EE_IMAGE"
podman image exists "$RUN_TOOLBOX_IMAGE"
```

## 4) Start Services with Local Images

`--limit` is mandatory in `services` mode.

Inventory flags in this section:

- `--inventory-dir`: inventories root path for the runtime mount.
- `-i/--inventory`: concrete inventory file used by `ansible-playbook`.

Wunderbox deploy:

```bash
./run-modulix.sh --inventory-dir "$INVENTORY_DIR" services wunderbox \
  -i "inventories/$INVENTORY_NAME/inventory.yml" --limit <HOST>
```

Wunderbox rebuild:

```bash
./run-modulix.sh --inventory-dir "$INVENTORY_DIR" services wunderbox --rebuild \
  -i "inventories/$INVENTORY_NAME/inventory.yml" --limit <HOST>
```

AAP deploy:

```bash
./run-modulix.sh --inventory-dir "$INVENTORY_DIR" services aap \
  -i "inventories/$INVENTORY_NAME/inventory.yml" --limit <HOST>
```

AAP rebuild:

```bash
./run-modulix.sh --inventory-dir "$INVENTORY_DIR" services aap --rebuild \
  -i "inventories/$INVENTORY_NAME/inventory.yml" --limit <HOST>
```

Run an explicit playbook path:

```bash
./run-modulix.sh --inventory-dir "$INVENTORY_DIR" services wunderbox \
  --playbook playbooks/services/12-wunderbox-service-stack.yml \
  -i "inventories/$INVENTORY_NAME/inventory.yml" --limit <HOST>
```

## 5) Common Failure Patterns

- `local image not found`:
  build/tag missing, run `podman image ls | grep ee-wunder`.
- `services mode requires -l/--limit`:
  add `--limit <host-or-group>`.
- `SSH_AUTH_SOCK is not set`:
  start agent and load key (`ssh-add`).
- nested EE startup fails with local image:
  keep `RUN_USE_HOST_EE_IMAGE=true` so host image is loaded into toolbox runtime.

## Notes

- Keep local tags explicit (`localhost/...`) to prevent accidental remote pulls.
- `VAULT_TOKEN` is optional for `services`; only set it when required by the target service workflow.
