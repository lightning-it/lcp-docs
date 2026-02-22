# Linux Workstation Requirements

## Runtime and platform requirements

| Area | Requirement | Source |
| --- | --- | --- |
| Host profile | RHEL 9 workstation VM with GUI | `../../runbooks/linux-workstation.md` |
| Target inventory group | `workstations` | `ansible-inventory-lit/inventories/corp/inventory.yml` |
| Execution mode | Execution Environment with required collections | `../../runbooks/automation.md` |
| GUI role | `lit.rhel.gui` | `modulix-automation/ansible/playbooks/stage-2b/11-workstation.yml` |
| XRDP role | `lit.rhel.xrdp` | `modulix-automation/ansible/playbooks/stage-2b/11-workstation.yml` |

## Automation prerequisites

- Execute through `./scripts/ansible-nav` (see [`../../runbooks/automation.md`](../../runbooks/automation.md)).
- Ensure inventory and host vars are defined for workstation hosts.
- Ensure firewall vars are present if host firewall role should run.

## Service policy requirements

- XRDP should be restricted to the management zone/network.
- Use least-privilege firewall exposure for remote admin protocols.
- Do not commit plaintext credentials or secret material.

## Networking and firewall

- Baseline firewall model is documented in [`firewall-rules.md`](firewall-rules.md).
