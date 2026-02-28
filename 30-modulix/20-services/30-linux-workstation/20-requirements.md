# Linux Workstation Requirements

## Runtime and platform requirements

| Area | Requirement | Source |
| --- | --- | --- |
| Host profile | RHEL 9 workstation VM with GUI | `../../30-runbooks/30-linux-workstation.md` |
| Target inventory group | `workstations` | `ansible-inventory/inventories/<inventory-name>/inventory.yml` |
| Execution mode | Execution Environment with required collections | `../../03-automation.md` |
| GUI role | `lit.rhel.gui` | `modulix-automation/ansible/playbooks/stage-2b/11-workstation.yml` |
| XRDP role | `lit.rhel.xrdp` | `modulix-automation/ansible/playbooks/stage-2b/11-workstation.yml` |

## Automation prerequisites

- Execute through `./scripts/ansible-nav` (see [`../../03-automation.md`](../../03-automation.md)).
- Ensure inventory and host vars are defined for workstation hosts.
- Ensure firewall vars are present if host firewall role should run.

## Service policy requirements

- XRDP should be restricted to the management zone/network.
- Use least-privilege firewall exposure for remote admin protocols.
- Do not commit plaintext credentials or secret material.

## Networking and firewall

- Baseline firewall model is documented in [`30-firewall-rules.md`](30-firewall-rules.md).
