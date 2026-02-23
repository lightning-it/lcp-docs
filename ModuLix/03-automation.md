# Ansible Automation

This repo uses `scripts/ansible-nav` as a container wrapper that runs
`ansible-navigator` and related commands in the toolbox image, so local
`ansible-navigator` is not required on the host.

Canonical runtime behavior, supported flags, and support scope are defined in:

- `https://github.com/lightning-it/modulix-automation/blob/main/docs/runtime-contract.md`
- `https://github.com/lightning-it/modulix-automation/blob/main/docs/support-matrix.md`

## Quick Start

### 3) Service/platform execution index

- `06-runbooks/01-services.md`

Use this index as the entry point for service-specific execution:

- service map with IDs (`01` Wunderbox, `02` AAP, `03` Linux Workstation, `04` OCP)
- mapping between service manual, execution runbook, and primary playbooks
- canonical rollout order across services
- quick execution entry points per service
- links to deeper service manuals under `07-services/`

Use this file (`03-automation.md`) for generic runtime behavior only (wrapper, contract, and shared automation rules).

## How-To

### Use the runtime wrapper

```bash
./scripts/ansible-nav run <playbook.yml> -i inventories/<env>/inventory.yml --limit <host-or-group>
```

### Install collections

Default runtime installs come from the configured execution environment and the
`scripts/ansible-nav` preflight behavior.

For local `ansible-collection-*` development overlays, see:
`08-development/01-ansible-collection-development.md`.

## Secret Input Contract

For all role secret inputs (passwords, tokens, keys), inventory is the source of truth:

- Required inventory entries must exist; missing required entries fail fast.
- If the inventory value is a plain secret value, use it directly.
- If the inventory value is a backend reference/path, resolve it in inventory via approved lookup plugins.
- If the referenced secret does not exist, use get-or-create behavior in inventory and use the returned value.
- Role code consumes resolved effective values only (no backend-specific secret read/write logic in roles).

For `aap_*` password inputs:

- Set `aap_password_active` (alias) or `aap_password_active_slot` (canonical) to control active slot (`active`/`next`).

## Knowledge Base

### Runtime notes

This runbook intentionally does not duplicate the executable runtime contract.
Use the canonical docs above for runtime defaults and support boundaries.
