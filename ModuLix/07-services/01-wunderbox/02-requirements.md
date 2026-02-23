# Wunderbox Requirements

## Runtime and platform requirements

| Area | Requirement | Source |
| --- | --- | --- |
| Host profile | RHEL 9 core-services VM (no GUI) | `../../06-runbooks/02-wunderbox.md` |
| Target inventory group | `wunderboxes` | `modulix-automation/ansible/playbooks/stage-2b/12-wunderbox.yml` and inventory conventions |
| Execution mode | Execution Environment with required collections | `../../03-automation.md` |

## Automation prerequisites

- Execute playbooks through the supported wrapper/runtime model in
  [`../../03-automation.md`](../../03-automation.md).
- Inventory must contain required host/group vars for the enabled service roles.
- For local collection development, use
  [`../../08-development/01-ansible-collection-development.md`](../../08-development/01-ansible-collection-development.md).

## Credential and secret requirements

- Use vaulted inventory vars and/or Vault-backed flows for secret material.
- Do not commit plaintext secrets.
- For Nexus integrations that read Vault data, provide a short-lived token with only required read permissions.

## Networking and firewall

- Baseline service ingress policy is documented in [`03-firewall-rules.md`](03-firewall-rules.md).
- Add any environment-specific exceptions in inventory first, then reflect them in this document.
