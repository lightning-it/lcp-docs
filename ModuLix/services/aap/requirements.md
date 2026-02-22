# AAP Requirements

## Runtime and platform requirements

| Area | Requirement | Source |
| --- | --- | --- |
| OS major support | RHEL `9` and `10` | `ansible-collection-supplementary/roles/aap/defaults/main.yml` |
| Install mode | `bundle` only | `ansible-collection-supplementary/roles/aap_deploy/defaults/main.yml` |
| Minimum memory check | `15000` MB when check is enabled | `ansible-collection-supplementary/roles/aap_deploy/defaults/main.yml` |
| Bundle archive default | `/opt/aap/aap-containerized-setup.tar.gz` | `ansible-collection-supplementary/roles/aap_deploy/defaults/main.yml` |
| Bundle directory default | `/opt/aap/setup/bundle` | `ansible-collection-supplementary/roles/aap_deploy/defaults/main.yml` |

## Automation prerequisites

- Execute through `./scripts/ansible-nav` (see [`../../runbooks/automation.md`](../../runbooks/automation.md)).
- Inventory must include target hosts in group `aaps`.
- Execution Environment image must provide required collections.

## Credential and secret requirements

- Use one declared source-of-truth for AAP admin credentials:
- `inventory` (vaulted vars recommended)
- `vault` (KV2-backed flows)
- Do not commit plaintext secrets.

## Networking and firewall

- Baseline service ingress is documented in [`firewall-rules.md`](firewall-rules.md).
- Any environment-specific exceptions must be added in inventory and mirrored in this document.
