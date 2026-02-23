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
- `04-security.md`
- `05-patching.md`
- `30-runbooks/00-index.md` (runbooks index)
- `30-runbooks/10-wunderbox.md` (`10-wunderbox`)
- `30-runbooks/20-aap.md` (`20-aap`)
- `30-runbooks/30-linux-workstation.md` (`30-linux-workstation`)
- `30-runbooks/40-ocp.md` (`40-ocp`)
- `50-development/02-containers/10-devtools-container.md` (for lint/test tooling in container)

## Canonical contract

For exact runtime flags/defaults and support scope, see:

- `https://github.com/lightning-it/modulix-automation/blob/main/docs/runtime-contract.md`
- `https://github.com/lightning-it/modulix-automation/blob/main/docs/support-matrix.md`

## 4) Use the DevOps container for checks

Use the devtools container for repository tooling (`pre-commit`, `ansible-lint`,
Molecule, actionlint) without installing all tools on the host.

- image: `quay.io/l-it/ee-wunder-devtools-ubi9:v1.6.0`
- guide: `50-development/02-containers/10-devtools-container.md`

Keep playbook execution on `./scripts/ansible-nav` (runtime wrapper path).
