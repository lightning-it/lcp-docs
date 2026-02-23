# OCP

The **OCP** runbook covers OpenShift 4 stage-2c automation entry points used in
the ModuLix Ansible workspace.

This document covers:
- how to run OCP stage-2c playbooks with `scripts/ansible-nav`
- the high-level OCP playbook sequence
- where to find service-specific architecture and requirements

---

## Ansible automation (ModuLix)

OCP automation is orchestrated from the **ModuLix** repository
(`modulix-automation/ansible/`).

Repo (public): https://github.com/lightning-it/modulix-automation

---

## Generic automation reference

Generic Ansible automation guidance is maintained in [`automation.md`](../03-automation.md):

- Runtime wrapper usage and flags: [`automation.md#use-the-runtime-wrapper`](../03-automation.md#use-the-runtime-wrapper)
- Collection and Execution Environment prerequisites: [`automation.md#install-collections`](../03-automation.md#install-collections)
- Inventory and roles layout: [`automation.md#inventory-and-roles`](../03-automation.md#inventory-and-roles)
- Shared secret handling: [`automation.md#secrets`](../03-automation.md#secrets)

---

## Service specification

Service-specific architecture and policy details are documented under
[`../07-services/04-ocp/`](../07-services/04-ocp/README.md):

- Architecture: [`../07-services/04-ocp/01-architecture.md`](../07-services/04-ocp/01-architecture.md)
- Requirements: [`../07-services/04-ocp/02-requirements.md`](../07-services/04-ocp/02-requirements.md)
- Firewall rules: [`../07-services/04-ocp/03-firewall-rules.md`](../07-services/04-ocp/03-firewall-rules.md)

---

## Running OCP playbooks (stage-2c)

```bash
./scripts/ansible-nav run playbooks/stage-2c/container-platform-ocp4/prepare-ee.yml \
  -i inventories/<env>/inventory.yml

./scripts/ansible-nav run playbooks/stage-2c/container-platform-ocp4/20-ocp-install.yml \
  -i inventories/<env>/inventory.yml --limit <ocp-host-or-group>

./scripts/ansible-nav run playbooks/stage-2c/container-platform-ocp4/21-post-install.yml \
  -i inventories/<env>/inventory.yml
```

> Notes:
> - Inventory and host/group model for OCP can differ by environment.
> - Stage-2c playbooks typically target the `ocp` group for cluster lifecycle operations.
> - For teardown workflows, use `99-ocp-destroy.yml` when appropriate.

---

## OCP playbook sequence

Main stage-2c OCP workflow:

1. `prepare-ee.yml`
2. `20-ocp-install.yml`
3. `21-post-install.yml`
4. `99-ocp-destroy.yml` *(teardown path)*
