# Wunderbox Firewall Rules

## Source of truth

Current default firewall policy for Wunderbox hosts is defined in:

- `ansible-inventory-lit/inventories/corp/group_vars/wunderboxes/firewall.yml`

## Baseline rule set (current inventory defaults)

| Zone | Service/Port | Protocol | State | Permanent | Notes |
| --- | --- | --- | --- | --- | --- |
| `dmz` | `ssh` | TCP/22 | disabled | true | SSH is explicitly disabled in current defaults |
| `dmz` | `8200/tcp` | TCP/8200 | enabled | true | Vault API |
| `dmz` | `dns` | UDP/TCP 53 | enabled | true | DNS service access |

## Change process

1. Update inventory firewall vars in `ansible-inventory-lit`.
2. Update this document to keep architecture docs aligned.
3. Validate with service runbook execution (`../../runbooks/wunderbox.md`).
