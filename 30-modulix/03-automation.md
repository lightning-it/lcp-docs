# Ansible Automation

ModuLix uses two runtime entry points:

- `modulix-launcher` (preferred operator path for `wunderbox`/`aap` services
  and `toolbox shell`)
- `scripts/ansible-nav` (direct stage/playbook path from
  `modulix-automation/ansible`)

Both paths run containerized automation; no host-native `ansible-navigator`
install is required.

Canonical runtime behavior, supported flags, and support scope are defined in:

- `https://github.com/lightning-it/modulix-automation/blob/main/docs/runtime-contract.md`
- `https://github.com/lightning-it/modulix-automation/blob/main/docs/support-matrix.md`
- `https://github.com/lightning-it/modulix-launcher/blob/main/README.md`
- `04-security.md` (security baseline and compliance alignment intent)
- `05-patching.md` (patch management and Renovate workflow)

## Quick Start

### Service/platform entry points

- `30-runbooks/00-index.md` (execution runbooks)
- `20-services/00-index.md` (canonical service map and rollout order)

Use this file (`03-automation.md`) for generic runtime behavior only (wrapper, contract, and shared automation rules).

## How-To

### Use the runtime wrapper

```bash
modulix-launcher --inventory-dir <inventories-root> services <wunderbox|aap> \
  -i inventories/<inventory-name>/inventory.yml --limit <host-or-group>
```

```bash
./scripts/ansible-nav run <playbook.yml> -i inventories/<inventory-name>/inventory.yml --limit <host-or-group>
```

### Runtime input prerequisites

Depending on playbook and target environment:

- automation baseline content (playbooks, requirements, and configuration),
  provided either by the toolbox image (`modulix-automation-runtime` runtime payload) or by
  a local workspace in engineering/source-based workflows
- inventory (`-i inventories/<inventory-name>/inventory.yml`)
- inventory ownership: this is environment-specific and not shipped as a universal
  ModuLix baseline
- inventory must represent real infrastructure and operating context (host/group
  model, network segmentation, access paths, and runtime input references)
- SSH access (key material and/or ssh-agent)
- secret inputs (Vault token, vault password file, other runtime secrets)

### Install collections

Default runtime installs come from the configured execution environment and the
runtime preflight behavior (`modulix-launcher` and `scripts/ansible-nav`).

In RPM baseline/container-in mode (`/opt/modulix/ansible`), `ansible-nav-local`
defaults to `ANSIBLE_TOOLBOX_AUTO_COLLECTIONS=false` (offline-safe). Required
collections are expected to be pre-installed in the runtime and run EE images.
Enable collection bootstrap only when intentionally refreshing from a connected
source (`ANSIBLE_TOOLBOX_AUTO_COLLECTIONS=true`).

For local `ansible-collection-*` development overlays, see:
`50-development/01-ansible-collections/10-ansible-collection-development.md`.

## Secret Input Contract

For all role secret inputs (passwords, tokens, keys), inventory is the source of truth:

- Required inventory entries must exist; missing required entries fail fast.
- If the inventory value is a plain secret value, use it directly.
- If the inventory value is a backend reference/path, resolve it in inventory via approved lookup plugins.
- If the referenced secret does not exist, follow the environment governance
  rules below (bootstrap get-or-create vs. production fail/escalate).
- Role code consumes resolved effective values only (no backend-specific secret read/write logic in roles).

### Governance Rules for Get-Or-Create

Get-or-create is an operational policy decision, not only a technical fallback.

- Production and day-2 operations:
  missing required secrets must fail; do not auto-create in production paths.
- Non-production bootstrap (for example initial lab/PoC bring-up):
  auto-create may be allowed when ownership and scope are explicitly approved.
- Every secret creation event must be traceable:
  change ticket/approval ID, secret path, environment, actor, and timestamp.
- Prefer pre-provisioning secrets in managed secret backends before production
  rollout.

For `aap_*` password inputs:

- Set `aap_password_active` (alias) or `aap_password_active_slot` (canonical) to control active slot (`active`/`next`).

## Knowledge Base

### Runtime notes

This document intentionally does not duplicate the executable runtime contract.
Use the canonical docs above for runtime defaults and support boundaries.
