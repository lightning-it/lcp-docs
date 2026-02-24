# Getting Started

## 1) Run with the default runtime wrapper

Run ModuLix playbooks via the wrapper:

```bash
cd /path/to/<example-repo>/ansible
./scripts/ansible-nav run playbooks/<stage-or-service>/<playbook>.yml \
  -i inventories/<env>/inventory.yml --limit <host-or-group>
```

Inventory is environment-specific and maintained by the platform team.
It is required to map the automation run to your real infrastructure topology
and runtime access model.

Current defaults:

- wrapper image: `quay.io/l-it/ee-wunder-toolbox-ubi9:v1.5.0`
- run EE image: `quay.io/l-it/ee-wunder-ansible-ubi9:v1.9.3`

## 2) Container-only mode (no GitHub access)

Use the same wrapper workflow. No host-native `ansible-navigator` installation is required.
Container-only means runtime/tooling is containerized and the automation baseline
is provided by the toolbox image (`modulix-automation-runtime` runtime payload). Operators
provide environment-specific inventory mapping, SSH material, and runtime secrets.

For RPM baseline execution (`/opt/modulix/ansible`), collection bootstrap is
offline-safe by default (`ANSIBLE_TOOLBOX_AUTO_COLLECTIONS=false`). This means
required collections are expected to be pre-installed in the runtime/EE images.
In disconnected environments, ensure the run EE image and required collections
are already available before execution.

For runtime details, flags, and support scope:

- `<example-repo>/ansible/README.md`
- `<example-repo>/docs/runtime-contract.md`
- `<example-repo>/docs/support-matrix.md`

## 3) Runtime input prerequisites

See `03-automation.md` (`Runtime input prerequisites`).

## 4) Use runbooks and references

- `03-automation.md`
- `04-security.md`
- `05-patching.md`
- `30-runbooks/00-index.md` (runbooks index)
- `30-runbooks/10-wunderbox.md` (`10-wunderbox`)
- `30-runbooks/20-aap.md` (`20-aap`)
- `30-runbooks/30-linux-workstation.md` (`30-linux-workstation`)
- `30-runbooks/40-ocp.md` (`40-ocp`)
- `50-development/02-containers/10-devtools-container.md` (for lint/test tooling in container)

## 5) Use the DevOps container for checks

Use the devtools container for repository tooling (`pre-commit`, `ansible-lint`,
Molecule, actionlint) without installing all tools on the host.

- image: `quay.io/l-it/ee-wunder-devtools-ubi9:v1.6.0`
- guide: `50-development/02-containers/10-devtools-container.md`

Keep playbook execution on `./scripts/ansible-nav` (runtime wrapper path).
