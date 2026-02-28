# AAP Firewall Rules

## Source of truth

Current default firewall policy for AAP hosts is defined in:

- `ansible-inventory/inventories/<inventory-name>/group_vars/aaps/firewall.yml`

## Baseline rule set (current inventory defaults)

| Zone | Service/Port | Protocol | State | Permanent | Notes |
| --- | --- | --- | --- | --- | --- |
| `dmz` | `https` | TCP/443 | enabled | true | External AAP HTTPS endpoint |

## Change process

1. Update inventory firewall vars in `ansible-inventory-lit`.
2. Update this document to keep architecture docs aligned.
3. Validate with service runbook execution (`../../30-runbooks/20-aap.md`).
