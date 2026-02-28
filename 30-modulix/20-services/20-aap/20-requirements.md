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

- Preferred: execute through `modulix-launcher` service mode
  (see `../../03-automation.md`).
- Use `./scripts/ansible-nav` for direct stage/playbook runs.
- Inventory must include target hosts in group `aaps`.
- Execution Environment image must provide required collections.

## Credential and secret requirements

- Required `aap_*` inputs must be present in inventory.
- Inventory value types:
  - literal password value
  - HCP Vault path reference
- For HCP Vault path reference mode:
  - read existing secret/key
  - in non-production bootstrap scope, create secret/key when missing
  - in production/day-2 scope, fail if missing and escalate to secret owner
  - log every create action with ticket/reference, actor, environment, and path
- Do not commit plaintext secrets.

## Networking and firewall

- Baseline service ingress is documented in `30-firewall-rules.md`.
- Environment-specific exceptions must be added in inventory and mirrored here.
