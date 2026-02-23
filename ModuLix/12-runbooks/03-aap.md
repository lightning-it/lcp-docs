# AAP

The AAP host is a RHEL-based automation control-plane node for deployment,
configuration-as-code, and day-2 operations.

## Generic automation reference

- `../03-automation.md`

## Service specification

- Service index: `../13-services/02-aap/README.md`
- Architecture: `../13-services/02-aap/01-architecture.md`
- Requirements: `../13-services/02-aap/02-requirements.md`
- Firewall rules: `../13-services/02-aap/03-firewall-rules.md`

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

### Run only specific AAP phases

```bash
./scripts/ansible-nav run playbooks/stage-2b/13-aap.yml \
  -i inventories/corp/inventory.yml --limit aap01.prd.dmz.corp.l-it.io -t aap_deploy

./scripts/ansible-nav run playbooks/stage-2b/13-aap.yml \
  -i inventories/corp/inventory.yml --limit aap01.prd.dmz.corp.l-it.io -t aap_cac

./scripts/ansible-nav run playbooks/stage-2b/13-aap.yml \
  -i inventories/corp/inventory.yml --limit aap01.prd.dmz.corp.l-it.io \
  -t aap_ops -e aap_ops_action=status
```

## AAP Password Input Model

`aap_*` roles must consume inventory-provided inputs.

- Missing required inventory entries should fail.
- If an entry is a literal password, use it directly.
- If an entry is an HCP Vault path reference, resolve from HCP Vault.
- If referenced HCP Vault secret/key is missing, create it and then use it.
