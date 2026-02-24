# AAP Architecture

## Purpose

AAP provides automation control-plane capabilities for ModuLix:

- platform deployment (bundle-based install)
- configuration as code
- day-2 operations (status, restart, upgrade, password operations)

## Execution path

- Service runbook: `../../30-runbooks/20-aap.md`
- Primary playbook: `modulix-automation/ansible/playbooks/stage-2b/13-aap.yml`
- Runtime wrapper and execution contract: `../../03-automation.md`

## Role composition

High-level role order in `13-aap.yml`:

1. `lit.rhel.repos`
2. `fedora.linux_system_roles.firewall` (if firewall vars exist)
3. `lit.supplementary.aap`
4. `lit.supplementary.aap_deploy`
5. `lit.supplementary.aap_cac`
6. `lit.supplementary.aap_ops`

## Integration points

- Inventory group: `aaps`
- Host/group vars: `ansible-inventory-lit/inventories/corp/...`
- AAP secret inputs are inventory-first:
  - literal password values are accepted
  - HCP Vault path values are resolved (and created when missing)
- Default service ingress policy: HTTPS in DMZ (`30-firewall-rules.md`)

## Boundaries

- Service-specific architecture decisions are documented here.
- Global automation behavior and wrapper flags stay in `../../03-automation.md`.
