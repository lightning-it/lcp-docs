# Local ModuLix Runtime Containers (Build + Start)

This guide replaces local wrapper-script usage and documents the explicit workflow:

1. Build local images.
2. Point `modulix-launcher` to those local images.
3. Run services/playbooks or open a toolbox debug shell.

## Scope

This document is for local development/testing of ModuLix runtime execution with:

- local run EE image (`RUN_EE_IMAGE`)
- local toolbox image (`RUN_TOOLBOX_IMAGE`)
- `modulix-launcher` (command in `PATH`)

## Container Flow (ASCII)

```text
Host
  |
  |  modulix-launcher --inventory-dir ... <services|toolbox shell> ...
  v
+---------------------------------------------------------------+
| Toolbox container (RUN_TOOLBOX_IMAGE)                         |
|  process: ansible-nav-local run <playbook> OR /bin/bash       |
|  loads run EE tar from host (podman load)                     |
|  starts run EE via internal Podman (nested container run)     |
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
2. Host exports RUN_EE image tar (`podman save`).
3. Toolbox imports RUN_EE image tar (`podman load`).
4. Toolbox starts run-EE container with internal Podman (`pull policy: never`).
5. Run-EE executes `ansible-playbook` (via `ansible-runner`).
6. Run-EE connects to managed hosts (SSH/inventory/vault inputs).

## Prerequisites

- Podman installed and working on the host.
- `ssh-agent` running with a loaded key (`ssh-add -L` must show keys).
- Local checkout of:
  - `modulix-launcher`
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

## 3) Prepare Runtime Environment for `modulix-launcher`

```bash
cd "$NEW_ROOT"

export INVENTORY_DIR="$NEW_ROOT/ansible-inventory-lit/inventories"
export INVENTORY_NAME=<inventory-name>
export VAULT_PASS_FILE="$NEW_ROOT/modulix-automation/.vault-pass.txt"
```

Adjust `INVENTORY_DIR` if your inventory repository has a different local name
(for example `ansible-inventory-lit`).

If you use remote image tags instead of local `localhost/...` tags, preload
them once in a connected environment:

```bash
podman login quay.io
podman pull "$RUN_EE_IMAGE"
podman pull "$RUN_TOOLBOX_IMAGE"
```

If your registry requires authentication, run `podman login <registry>` on the host before using `modulix-launcher`.
`modulix-launcher` does not execute registry login and does not manage auth files.

For Vault-backed workflows, `VAULT_TOKEN` can be set on the host.
`modulix-launcher` forwards it only when set; unset variables are not forwarded.

Secret hygiene (required):

- Protect Vault password file permissions (`chmod 600 "$VAULT_PASS_FILE"`).
- Do not pass tokens/secrets via CLI extra-vars (for example `-e vault_token=...`)
  because they leak into process listings and shell history.
- Prefer short-lived session export for `VAULT_TOKEN`, then `unset VAULT_TOKEN`
  after the run.
- Rotate Vault tokens/password material according to your environment policy.

Example for interactive token input without shell-history exposure:

```bash
read -rsp "VAULT_TOKEN: " VAULT_TOKEN
echo
export VAULT_TOKEN
```

After the run:

```bash
unset VAULT_TOKEN
```

Sanity checks:

```bash
test -S "${SSH_AUTH_SOCK:-}"
test -s "$VAULT_PASS_FILE"
chmod 600 "$VAULT_PASS_FILE"
ls -l "$VAULT_PASS_FILE"
command -v modulix-launcher >/dev/null
podman image exists "$RUN_EE_IMAGE"
podman image exists "$RUN_TOOLBOX_IMAGE"
```

## 4) Start Services with Local Images

`modulix-launcher` supports:

- `services wunderbox`
- `services aap`
- `toolbox shell`

`--limit` is mandatory in `services` mode.

Inventory flags in this section:

- `--inventory-dir`: inventories root path for the runtime mount.
- `-i/--inventory`: concrete inventory file used by `ansible-playbook`.

Open toolbox shell (debug/edit in toolbox container):

```bash
modulix-launcher --inventory-dir "$INVENTORY_DIR" toolbox shell
```

Wunderbox deploy:

```bash
modulix-launcher --inventory-dir "$INVENTORY_DIR" services wunderbox \
  -i "inventories/$INVENTORY_NAME/inventory.yml" --limit <HOST>
```

Wunderbox rebuild:

```bash
modulix-launcher --inventory-dir "$INVENTORY_DIR" services wunderbox --rebuild \
  -i "inventories/$INVENTORY_NAME/inventory.yml" --limit <HOST>
```

AAP deploy:

```bash
modulix-launcher --inventory-dir "$INVENTORY_DIR" services aap \
  -i "inventories/$INVENTORY_NAME/inventory.yml" --limit <HOST>
```

AAP rebuild:

```bash
modulix-launcher --inventory-dir "$INVENTORY_DIR" services aap --rebuild \
  -i "inventories/$INVENTORY_NAME/inventory.yml" --limit <HOST>
```

Run an explicit playbook path:

```bash
modulix-launcher --inventory-dir "$INVENTORY_DIR" services wunderbox \
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
- nested Podman startup fails in toolbox:
  ensure host allows `--privileged` toolbox run and required kernel features.
- remote registry unavailable during first run:
  preload both images once in connected environment (`podman pull`) before offline runs.

## Notes

- Keep local tags explicit (`localhost/...`) to prevent accidental remote pulls.
- Runtime is single-path: run EE is always transferred host->toolbox via tar load.
