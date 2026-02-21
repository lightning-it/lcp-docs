# Getting Started

## 1) Use the default runtime path

Run ModuLix playbooks via the wrapper:

```bash
cd /path/to/modulix/ansible
./scripts/ansible-nav run <playbook.yml> -i <inventory.yml> --limit <host-or-group>
```

## 2) Provide runtime inputs

Depending on playbook:

- inventory
- SSH access/agent
- vault/secret inputs

## 3) Use runbooks

- `runbooks/automation.md`
- `runbooks/wunderbox.md`

## Canonical contract

For exact runtime flags/defaults and support scope, see:

- `https://github.com/lightning-it/modulix/blob/main/docs/runtime-contract.md`
- `https://github.com/lightning-it/modulix/blob/main/docs/support-matrix.md`
