# AAP

The AAP host is a RHEL-based automation control-plane node for deployment,
configuration-as-code, and day-2 operations.

## Generic automation reference

- `../03-automation.md`

## Service specification

- Service index: `../20-services/20-aap/00-index.md`
- Architecture: `../20-services/20-aap/10-architecture.md`
- Requirements: `../20-services/20-aap/20-requirements.md`
- Firewall rules: `../20-services/20-aap/30-firewall-rules.md`

## Running the AAP playbooks

### Recommended: launcher service flow

```bash
modulix-launcher --inventory-dir /path/to/ansible-inventory/inventories \
  services aap -i inventories/<inventory-name>/inventory.yml \
  --limit <aap-host-fqdn>
```

```bash
modulix-launcher --inventory-dir /path/to/ansible-inventory/inventories \
  services aap --rebuild -i inventories/<inventory-name>/inventory.yml \
  --limit <aap-host-fqdn>
```

### Direct stage playbooks (advanced / stage-specific)

#### AAP (VM + RHEL9) setup

```bash
./scripts/ansible-nav run playbooks/stage-1/infrastructure-platform-vsphere/20-vm-template.yml \
  -i inventories/<inventory-name>/inventory.yml --limit <aap-host-fqdn>

./scripts/ansible-nav run playbooks/stage-2a/traditional-operating-systems/rhel9/01-base-setup.yml \
  -i inventories/<inventory-name>/inventory.yml --limit <aap-host-fqdn>

./scripts/ansible-nav run playbooks/stage-2b/13-aap.yml \
  -i inventories/<inventory-name>/inventory.yml --limit <aap-host-fqdn>
```

#### AAP rebuild (single pipeline playbook)

```bash
./scripts/ansible-nav run playbooks/services/02-aap-rebuild.yml \
  -i inventories/<inventory-name>/inventory.yml --limit <aap-host-fqdn>
```

#### Run only specific AAP phases

```bash
./scripts/ansible-nav run playbooks/stage-2b/13-aap.yml \
  -i inventories/<inventory-name>/inventory.yml --limit <aap-host-fqdn> -t aap_deploy

./scripts/ansible-nav run playbooks/stage-2b/13-aap.yml \
  -i inventories/<inventory-name>/inventory.yml --limit <aap-host-fqdn> -t aap_cac

./scripts/ansible-nav run playbooks/stage-2b/13-aap.yml \
  -i inventories/<inventory-name>/inventory.yml --limit <aap-host-fqdn> \
  -t aap_ops -e aap_ops_action=status
```

## AAP Password Input Model

`aap_*` roles must consume inventory-provided inputs.

- Missing required inventory entries should fail.
- If an entry is a literal password, use it directly.
- If an entry is an HCP Vault path reference, resolve from HCP Vault.
- If referenced HCP Vault secret/key is missing:
  non-production bootstrap may create it, production/day-2 must fail and escalate.
- Record every auto-created secret with change ticket, actor, environment, and
  Vault path for audit traceability.
