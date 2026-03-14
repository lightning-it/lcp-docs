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

Generic Ansible automation guidance is maintained in [`automation.md`](../03-automation.md):

- Runtime wrapper usage and flags: [`automation.md#use-the-runtime-wrapper`](../03-automation.md#use-the-runtime-wrapper)
- Collection and Execution Environment prerequisites: [`automation.md#install-collections`](../03-automation.md#install-collections)
- Runtime input prerequisites: [`automation.md#runtime-input-prerequisites`](../03-automation.md#runtime-input-prerequisites)
- Shared secret handling: [`automation.md#secret-input-contract`](../03-automation.md#secret-input-contract)

---

## Service specification

Service-specific architecture and policy details are documented under
[`../20-services/30-linux-workstation/`](../20-services/30-linux-workstation/00-index.md):

- Architecture: [`../20-services/30-linux-workstation/10-architecture.md`](../20-services/30-linux-workstation/10-architecture.md)
- Requirements: [`../20-services/30-linux-workstation/20-requirements.md`](../20-services/30-linux-workstation/20-requirements.md)
- Firewall rules: [`../20-services/30-linux-workstation/30-firewall-rules.md`](../20-services/30-linux-workstation/30-firewall-rules.md)

---

## Running the Linux Workstation playbook

### Linux Workstation (VM + RHEL9) setup

```bash
./scripts/ansible-nav run playbooks/stage-1/infrastructure-platform-vsphere/20-vm-template.yml \
  -i inventories/<inventory-name>/inventory.yml --limit <workbench-host-fqdn>

./scripts/ansible-nav run playbooks/stage-2a/traditional-operating-systems/rhel9/01-base-setup.yml \
  -i inventories/<inventory-name>/inventory.yml --limit <workbench-host-fqdn>

./scripts/ansible-nav run playbooks/stage-2b/11-workbench.yml \
  -i inventories/<inventory-name>/inventory.yml --limit <workbench-host-fqdn>
```

> Notes:
> - Adjust `--limit` to your workbench FQDN(s).
> - Stage-2b playbook targets the `workbenches` inventory group.
> - Use restrictive firewall policy for RDP exposure (prefer mgmt/admin zone only).

---

## Linux Workstation playbook: scope and flow

The workbench playbook configures:

- base repositories
- host firewall policy (when firewall vars are provided)
- GUI stack (GNOME/XFCE via role vars)
- XRDP service for remote administration
- optional Cloudflare WARP client enrollment for private/admin connectivity

### High-level execution order (`playbooks/stage-2b/11-workbench.yml`)

1. `lit.rhel.repos`
2. `fedora.linux_system_roles.firewall` *(only when `firewall` vars are set)*
3. `lit.rhel.gui`
4. `lit.rhel.xrdp`
5. `lit.supplementary.cloudflare_warp` *(optional, inventory-driven)*
