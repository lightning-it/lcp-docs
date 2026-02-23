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

- Execute through `./scripts/ansible-nav` (see `../../03-automation.md`).
- Inventory must include target hosts in group `aaps`.
- Execution Environment image must provide required collections.

## Credential and secret requirements

- Required `aap_*` inputs must be present in inventory.
- Inventory value types:
  - literal password value
  - HCP Vault path reference
- For HCP Vault path reference mode:
  - read existing secret/key
  - if missing, create secret/key and use it
- Do not commit plaintext secrets.

## Networking and firewall

- Baseline service ingress is documented in `03-firewall-rules.md`.
- Environment-specific exceptions must be added in inventory and mirrored here.
