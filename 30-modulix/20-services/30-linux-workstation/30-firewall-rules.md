# Linux Workstation Firewall Rules

## Source of truth

Current firewall behavior for workbench hosts is composed from:

- `ansible-inventory/inventories/<inventory-name>/group_vars/all/firewall.yml`
- `ansible-inventory/inventories/<inventory-name>/group_vars/workbenches/xrdp.yml`

## Baseline rule set (current inventory defaults)

| Zone | Service/Port | Protocol | State | Permanent | Notes |
| --- | --- | --- | --- | --- | --- |
| `mgmt` | zone presence | n/a | present | n/a | `firewall_base` creates mgmt zone |
| `mgmt` | interface `ens34` | n/a | enabled | true | mgmt interface assignment |
| `mgmt` | `ssh` | TCP/22 | enabled | true | base management access |
| `mgmt` | default zone | n/a | enabled | true | default firewalld zone set to mgmt |
| `mgmt` | XRDP `3389` | TCP/3389 | enabled | role-managed | set by `lit.rhel.xrdp` vars |

## Change process

1. Update base or workbench-specific firewall vars in `ansible-inventory-lit`.
2. Update this document to keep architecture docs aligned.
3. Validate with service runbook execution (`../../30-runbooks/30-linux-workstation.md`).
