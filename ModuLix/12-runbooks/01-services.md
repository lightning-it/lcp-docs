# Service Operations

This runbook is the execution index for service and platform playbooks.

- Generic runtime wrapper behavior: `../03-automation.md`
- Service manuals and design docs: `../13-services/`
- Service-specific execution details: `02-wunderbox.md`, `03-aap.md`, `04-linux-workstation.md`, `05-ocp.md`

## Service map

| ID | Service manual | Execution runbook | Primary playbooks |
| --- | --- | --- | --- |
| `01` Wunderbox | `../13-services/01-wunderbox/README.md` | `02-wunderbox.md` | `playbooks/stage-2b/12-wunderbox.yml`, `playbooks/services/01-wunderbox-rebuild.yml` |
| `02` AAP | `../13-services/02-aap/README.md` | `03-aap.md` | `playbooks/stage-2b/13-aap.yml`, `playbooks/services/02-aap-rebuild.yml` |
| `03` Linux Workstation | `../13-services/03-linux-workstation/README.md` | `04-linux-workstation.md` | `playbooks/stage-2b/11-workstation.yml` |
| `04` OCP | `../13-services/04-ocp/README.md` | `05-ocp.md` | `playbooks/stage-2c/container-platform-ocp4/prepare-ee.yml`, `20-ocp-install.yml`, `21-post-install.yml` |

## Canonical service rollout order

1. `01-wunderbox`
2. `02-aap`
3. `03-linux-workstation`
4. `04-ocp`

## Quick service execution entry points

```bash
./scripts/ansible-nav run playbooks/services/01-wunderbox-rebuild.yml \
  -i inventories/corp/inventory.yml --limit wunderbox01.prd.dmz.corp.l-it.io

./scripts/ansible-nav run playbooks/services/02-aap-rebuild.yml \
  -i inventories/corp/inventory.yml --limit aap01.prd.dmz.corp.l-it.io

./scripts/ansible-nav run playbooks/stage-2b/11-workstation.yml \
  -i inventories/corp/inventory.yml --limit workstation01.prd.dmz.corp.l-it.io

./scripts/ansible-nav run playbooks/stage-2c/container-platform-ocp4/20-ocp-install.yml \
  -i inventories/<env>/inventory.yml --limit <ocp-host-or-group>
```
