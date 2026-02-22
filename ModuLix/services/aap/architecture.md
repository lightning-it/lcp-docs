# AAP Architecture

## Purpose

AAP provides automation control-plane capabilities for ModuLix:

- platform deployment (bundle-based install)
- configuration as code
- day-2 operations (status, restart, upgrade, password operations)

## Execution path

- Service runbook: [`../../runbooks/aap.md`](../../runbooks/aap.md)
- Primary playbook: `modulix-automation/ansible/playbooks/stage-2b/13-aap.yml`
- Runtime wrapper and execution contract: [`../../runbooks/automation.md`](../../runbooks/automation.md)

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
- Host vars and group vars: `ansible-inventory-lit/inventories/corp/...`
- Optional secret backend: Vault KV2 for admin password source-of-truth (`vault`)
- Default service ingress policy: HTTPS in DMZ (see [`firewall-rules.md`](firewall-rules.md))

## Boundaries

- Service-specific architecture decisions are documented here.
- Global automation behavior and wrapper flags stay in `runbooks/automation.md`.
