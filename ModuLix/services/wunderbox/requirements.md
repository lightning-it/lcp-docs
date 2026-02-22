# Wunderbox Requirements

## Runtime and platform requirements

| Area | Requirement | Source |
| --- | --- | --- |
| Host profile | RHEL 9 core-services VM (no GUI) | `../../runbooks/wunderbox.md` |
| Target inventory group | `wunderboxes` | `modulix-automation/ansible/playbooks/stage-2b/12-wunderbox.yml` and inventory conventions |
| Execution mode | Execution Environment with required collections | `../../runbooks/automation.md` |

## Automation prerequisites

- Execute playbooks through the supported wrapper/runtime model in
  [`../../runbooks/automation.md`](../../runbooks/automation.md).
- Inventory must contain required host/group vars for the enabled service roles.
- For local collection development, use overlays as documented in `automation.md`.

## Credential and secret requirements

- Use vaulted inventory vars and/or Vault-backed flows for secret material.
- Do not commit plaintext secrets.
- For Nexus integrations that read Vault data, provide a short-lived token with only required read permissions.

## Networking and firewall

- Baseline service ingress policy is documented in [`firewall-rules.md`](firewall-rules.md).
- Add any environment-specific exceptions in inventory first, then reflect them in this document.
