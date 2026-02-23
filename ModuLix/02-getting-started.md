# Getting Started

## 1) Use the default runtime path

Run ModuLix playbooks via the wrapper:

```bash
cd /path/to/modulix-automation/ansible
./scripts/ansible-nav run <playbook.yml> -i <inventory.yml> --limit <host-or-group>
```

Current defaults:

- wrapper image: `quay.io/l-it/ee-wunder-toolbox-ubi9:v1.5.0`
- run EE image: `quay.io/l-it/ee-wunder-ansible-ubi9:v1.9.3`

## 2) Provide runtime inputs

Depending on playbook:

- inventory
- SSH access/agent
- vault/secret inputs

## 3) Use runbooks

- `03-automation.md`
- `06-runbooks/01-services.md` (service and platform execution index)
- `06-runbooks/02-wunderbox.md` (`01-wunderbox`)
- `06-runbooks/03-aap.md` (`02-aap`)
- `06-runbooks/04-linux-workstation.md` (`03-linux-workstation`)
- `06-runbooks/05-ocp.md` (`04-ocp`)
- `08-development/02-devtools-container.md` (for lint/test tooling in container)

## Canonical contract

For exact runtime flags/defaults and support scope, see:

- `https://github.com/lightning-it/modulix-automation/blob/main/docs/runtime-contract.md`
- `https://github.com/lightning-it/modulix-automation/blob/main/docs/support-matrix.md`

## 4) Use the DevOps container for checks

Use the devtools container for repository tooling (`pre-commit`, `ansible-lint`,
Molecule, actionlint) without installing all tools on the host.

- image: `quay.io/l-it/ee-wunder-devtools-ubi9:v1.6.0`
- guide: `08-development/02-devtools-container.md`

Keep playbook execution on `./scripts/ansible-nav` (runtime wrapper path).
