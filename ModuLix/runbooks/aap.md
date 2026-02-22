# AAP

The **AAP** host is a RHEL-based Automation Controller node used to run and operate
Ansible Automation Platform (AAP) with role-driven deployment, configuration-as-code,
and day-2 operations.

This document covers:
- how to run the AAP automation with `scripts/ansible-nav` in the **Wunder toolbox image**
- the AAP playbook flow and **all roles** it invokes
- AAP password/source-of-truth handling (`inventory` or `vault`)
- inventory and secrets handling

---

## Ansible automation (ModuLix)

AAP automation is orchestrated from the **ModuLix** repository (Ansible workspace under `modulix-automation/ansible/`).
The ModuLix workspace uses `scripts/ansible-nav` as a container wrapper that runs
`ansible-navigator` in the Wunder toolbox image, so local Ansible tooling is not required.

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
[`../services/aap/`](../services/aap/README.md):

- Architecture: [`../services/aap/architecture.md`](../services/aap/architecture.md)
- Requirements: [`../services/aap/requirements.md`](../services/aap/requirements.md)
- Firewall rules: [`../services/aap/firewall-rules.md`](../services/aap/firewall-rules.md)

---

## Running the AAP playbooks

### AAP (VM + RHEL9) setup

```bash
./scripts/ansible-nav run playbooks/stage-1/infrastructure-platform-vsphere/20-vm-template.yml \
  -i inventories/corp/inventory.yml --limit aap01.prd.dmz.corp.l-it.io

./scripts/ansible-nav run playbooks/stage-2a/traditional-operating-systems/rhel9/01-base-setup.yml \
  -i inventories/corp/inventory.yml --limit aap01.prd.dmz.corp.l-it.io

./scripts/ansible-nav run playbooks/stage-2b/13-aap.yml \
  -i inventories/corp/inventory.yml --limit aap01.prd.dmz.corp.l-it.io
```

### AAP rebuild (single pipeline playbook)

```bash
./scripts/ansible-nav run playbooks/services/02-aap-rebuild.yml \
  -i inventories/corp/inventory.yml --limit aap01.prd.dmz.corp.l-it.io
```

> Notes:
> - Adjust `--limit` to your AAP host FQDN(s).
> - Stage-2b playbook targets the `aaps` inventory group.
> - Ensure the configured EE image contains required collections.
> - Secrets must be provided via `ANSIBLE_VAULT_PASSWORD_FILE` or equivalent secret management.

### Run only specific AAP phases (tags)

```bash
# Deploy/update AAP runtime
./scripts/ansible-nav run playbooks/stage-2b/13-aap.yml \
  -i inventories/corp/inventory.yml --limit aap01.prd.dmz.corp.l-it.io -t aap_deploy

# Apply AAP configuration-as-code
./scripts/ansible-nav run playbooks/stage-2b/13-aap.yml \
  -i inventories/corp/inventory.yml --limit aap01.prd.dmz.corp.l-it.io -t aap_cac

# Day-2 operation example (status)
./scripts/ansible-nav run playbooks/stage-2b/13-aap.yml \
  -i inventories/corp/inventory.yml --limit aap01.prd.dmz.corp.l-it.io \
  -t aap_ops -e aap_ops_action=status
```

---

## AAP admin credentials (source of truth)

Use one declared source of truth for AAP admin credentials:
- `inventory` (vaulted vars recommended)
- `vault` (KV2-backed flows)

---

## AAP playbook: scope and flow

The AAP playbook configures the following stack on target AAP hosts:

- AAP shared context and prechecks
- AAP deployment (bundle-based install)
- AAP configuration-as-code tasksets
- Day-2 AAP operations (restart/status/upgrade/password operations)

### High-level execution order (`playbooks/stage-2b/13-aap.yml`)

1. `lit.rhel.repos`
2. `fedora.linux_system_roles.firewall` *(only when `firewall` vars are set)*
3. `lit.supplementary.aap`
4. `lit.supplementary.aap_deploy`
5. `lit.supplementary.aap_cac`
6. `lit.supplementary.aap_ops`

---

## Role reference

### `lit.supplementary.aap`
**Purpose:** Shared AAP context role with prechecks and common variable/password resolution.

**Key behavior:**
- centralizes AAP runtime flags and package defaults
- resolves effective admin passwords for gateway/controller/hub/eda/postgresql
- supports `inventory` or `vault` as source of truth
- publishes effective vars consumed by deploy/ops roles

---

### `lit.supplementary.aap_deploy`
**Purpose:** Install AAP 2.6 in disconnected bundle mode.

**Typical responsibilities:**
- prepare host prerequisites (optional host prep)
- validate and unpack/setup bundle assets
- render/install topology-specific AAP config
- run installer and post-install verification (when enabled)

**Key inputs:**
- `aap_deploy_install_type` (`bundle`)
- `aap_deploy_topology` (`growth` or `enterprise`)
- bundle/archive paths and install user/dir
- resolved admin/password variables from shared AAP context

---

### `lit.supplementary.aap_cac`
**Purpose:** Apply AAP configuration-as-code objects via tasksets.

**Typical responsibilities:**
- authenticate against AAP gateway
- execute `cac_*.yml` tasksets (organizations, credentials, projects, inventories, job templates, hub config)
- run object reconciliation taskset where configured

**Key inputs:**
- `aap_cac_gateway_hostname`
- `aap_cac_collections_profile` and requirements path
- object reconcile scope/security flags

---

### `lit.supplementary.aap_ops`
**Purpose:** Run day-2 AAP operations.

**Supported actions (via `aap_ops_action`):**
- `restart`
- `status`
- `upgrade`
- `sync_hub_password`
- `rotate_password`

**Typical responsibilities:**
- service/package operations for AAP runtime
- synchronize hub password into `aap-config.yml`
- rotate controller admin password with inventory- or Vault-backed state

---

## AAP password and source-of-truth notes

Recommended flow:
- Keep one declared source of truth per environment (`inventory` or `vault`).
- Prefer Vault-backed flows for generated or rotated credentials.
- Avoid ad-hoc generated passwords that are not persisted.

Resolution model used by AAP roles (shared context):
1. explicit role variable
2. Vault KV2 (when source is `vault`)
3. local cache fallback (lab/offline only)
4. generated value (for persisted flows)

Best practice:
- use short-lived, least-privilege Vault tokens/AppRole credentials
- store per-environment values in vaulted inventory or secret manager
- keep role defaults environment-neutral

---
