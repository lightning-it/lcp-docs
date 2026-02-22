# Linux Workstation

The **Linux Workstation** is a RHEL-based GUI host used for operator/admin
workflows with XRDP access.

This document covers:
- how to run Linux Workstation automation with `scripts/ansible-nav`
- the workstation playbook flow and roles
- inventory and firewall context for RDP-enabled workstation hosts

---

## Ansible automation (ModuLix)

Linux Workstation automation is orchestrated from the **ModuLix** repository
(Ansible workspace under `modulix-automation/ansible/`).

Repo (public): https://github.com/lightning-it/modulix-automation

---

## Generic automation reference

Generic Ansible automation guidance is maintained in [`automation.md`](automation.md):

- Runtime wrapper usage and flags: [`automation.md#use-the-runtime-wrapper`](automation.md#use-the-runtime-wrapper)
- Collection and Execution Environment prerequisites: [`automation.md#install-collections`](automation.md#install-collections)
- Inventory and roles layout: [`automation.md#inventory-and-roles`](automation.md#inventory-and-roles)
- Shared secret handling: [`automation.md#secrets`](automation.md#secrets)

---

## Service specification

Service-specific architecture and policy details are documented under
[`../services/linux-workstation/`](../services/linux-workstation/README.md):

- Architecture: [`../services/linux-workstation/architecture.md`](../services/linux-workstation/architecture.md)
- Requirements: [`../services/linux-workstation/requirements.md`](../services/linux-workstation/requirements.md)
- Firewall rules: [`../services/linux-workstation/firewall-rules.md`](../services/linux-workstation/firewall-rules.md)

---

## Running the Linux Workstation playbook

### Linux Workstation (VM + RHEL9) setup

```bash
./scripts/ansible-nav run playbooks/stage-1/infrastructure-platform-vsphere/20-vm-template.yml \
  -i inventories/corp/inventory.yml --limit workstation01.prd.dmz.corp.l-it.io

./scripts/ansible-nav run playbooks/stage-2a/traditional-operating-systems/rhel9/01-base-setup.yml \
  -i inventories/corp/inventory.yml --limit workstation01.prd.dmz.corp.l-it.io

./scripts/ansible-nav run playbooks/stage-2b/11-workstation.yml \
  -i inventories/corp/inventory.yml --limit workstation01.prd.dmz.corp.l-it.io
```

> Notes:
> - Adjust `--limit` to your workstation FQDN(s).
> - Stage-2b playbook targets the `workstations` inventory group.
> - Use restrictive firewall policy for RDP exposure (prefer mgmt/admin zone only).

---

## Linux Workstation playbook: scope and flow

The workstation playbook configures:

- base repositories
- host firewall policy (when firewall vars are provided)
- GUI stack (GNOME/XFCE via role vars)
- XRDP service for remote administration

### High-level execution order (`playbooks/stage-2b/11-workstation.yml`)

1. `lit.rhel.repos`
2. `fedora.linux_system_roles.firewall` *(only when `firewall` vars are set)*
3. `lit.rhel.gui`
4. `lit.rhel.xrdp`
