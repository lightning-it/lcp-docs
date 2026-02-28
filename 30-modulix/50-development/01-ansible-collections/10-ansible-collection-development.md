# Ansible Collection Development Guide

This guide covers development workflows for local `ansible-collection-*` repositories.

## Scope

- Development overlays only.
- Not required for normal runtime playbook execution.

## Runtime vs Development

Normal runtime path:

```bash
modulix-launcher --inventory-dir <inventories-root> services <wunderbox|aap> \
  -i inventories/<inventory-name>/inventory.yml --limit <host-or-group>
```

```bash
./scripts/ansible-nav run <playbook.yml> -i <inventory.yml> --limit <host-or-group>
```

For this path, do not run local overlay install by default:

- Collections come from the configured EE image.
- For direct stage/playbook runs, RH collection preflight is handled by
  `scripts/ansible-nav`.

Use local overlay installs only when you are actively developing local collection code and need those changes in `collections-dev`.

## Local Overlay Workflow

Run from `modulix-automation/ansible`:

```bash
./scripts/install-local-collections
```

This builds local `ansible-collection-*` repositories and installs them into `collections-dev`.

Install only selected local collections:

```bash
./scripts/install-local-collections foundational rhel
```

## Recommended Input Pattern for Role Development

Prefer one canonical variable name per input and resolve value source in inventory:

1. Plain inventory value (non-secret only)
2. Ansible Vault encrypted variable (`!vault`)
3. HashiCorp Vault lookup plugin value

Role code should consume the effective variable, not embed multiple secret-source strategies when avoidable.

## Secrets

- Do not commit secrets.
- Use Ansible Vault and/or approved secret backends.
