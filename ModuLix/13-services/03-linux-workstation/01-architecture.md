# Linux Workstation Architecture

## Purpose

Linux Workstation provides a managed RHEL GUI host for operator/admin workflows
with controlled XRDP access.

## Execution path

- Service runbook: [`../../12-runbooks/04-linux-workstation.md`](../../12-runbooks/04-linux-workstation.md)
- Primary playbook: `modulix-automation/ansible/playbooks/stage-2b/11-workstation.yml`
- Runtime wrapper and execution contract: [`../../03-automation.md`](../../03-automation.md)

## Role composition

High-level role order in `11-workstation.yml`:

1. `lit.rhel.repos`
2. `fedora.linux_system_roles.firewall` (if firewall vars exist)
3. `lit.rhel.gui`
4. `lit.rhel.xrdp`

## Integration points

- Inventory group: `workstations`
- Group vars: `ansible-inventory-lit/inventories/corp/group_vars/workstations/`
- Host vars: `ansible-inventory-lit/inventories/corp/host_vars/workstation*.yml`
- XRDP policy and zone behavior are documented in [`03-firewall-rules.md`](03-firewall-rules.md)

## Boundaries

- Service-specific architecture decisions are documented here.
- Global automation behavior and wrapper flags stay in `03-automation.md`.
