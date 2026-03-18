# Linux Workstation Architecture

## Purpose

Linux Workstation provides a managed RHEL GUI host for operator/admin workflows
with controlled XRDP access.

## Execution path

- Service runbook: [`../../30-runbooks/30-linux-workstation.md`](../../30-runbooks/30-linux-workstation.md)
- Primary playbook: `modulix-automation/ansible/playbooks/stage-2b/11-workbench.yml`
- Runtime wrapper and execution contract: [`../../03-automation.md`](../../03-automation.md)

## Role composition

High-level role order in `11-workbench.yml`:

1. `lit.rhel.repos`
2. `fedora.linux_system_roles.firewall` (if firewall vars exist)
3. `lit.rhel.gui`
4. `lit.rhel.xrdp`
5. `lit.supplementary.cloudflare_warp` (optional for Cloudflare-admin connectivity)

## Integration points

- Inventory group: `workbenches`
- Group vars: `ansible-inventory/inventories/<inventory-name>/group_vars/workbenches/`
- Host vars: `ansible-inventory/inventories/<inventory-name>/host_vars/workbench*.yml`
- Cloudflare WARP enrollment for cloud workbenches can be supplied through
  `group_vars/workbenches/cloudflare_warp.yml` and per-host WARP enrollment vars.
- XRDP policy and zone behavior are documented in [`30-firewall-rules.md`](30-firewall-rules.md)

## Boundaries

- Service-specific architecture decisions are documented here.
- Global automation behavior and wrapper flags stay in `03-automation.md`.
