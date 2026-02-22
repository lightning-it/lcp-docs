# Getting Started

## 1) Use the default runtime path

Run ModuLix playbooks via the wrapper:

```bash
cd /path/to/modulix-automation/ansible
./scripts/ansible-nav run <playbook.yml> -i <inventory.yml> --limit <host-or-group>
```

## 2) Provide runtime inputs

Depending on playbook:

- inventory
- SSH access/agent
- vault/secret inputs

## 3) Use runbooks

- `runbooks/automation.md`
- `runbooks/wunderbox.md` (`01-wunderbox`)
- `runbooks/aap.md` (`02-aap`)
- `runbooks/linux-workstation.md` (`03-linux-workstation`)
- `runbooks/ocp.md` (`04-ocp`)
- `development/devtools-container.md` (for lint/test tooling in container)

## Canonical contract

For exact runtime flags/defaults and support scope, see:

- `https://github.com/lightning-it/modulix-automation/blob/main/docs/runtime-contract.md`
- `https://github.com/lightning-it/modulix-automation/blob/main/docs/support-matrix.md`
