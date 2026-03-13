# Service Specifications Index

This is the canonical catalog of ModuLix technology service builds and their
matching deployment runbooks.

Services in this section are technology-specific objects (for example
Wunderbox, AAP, Linux Workstation, OCP). They document what is built and which
technical constraints apply.

- Wunderbox: `10-wunderbox/00-index.md`
- AAP: `20-aap/00-index.md`
- Linux Workstation: `30-linux-workstation/00-index.md`
- OCP: `40-ocp/00-index.md`

## Service map

| ID | Service specification | Deployment runbook | Primary playbooks |
| --- | --- | --- | --- |
| `10` Wunderbox | `10-wunderbox/00-index.md` | `../30-runbooks/10-wunderbox.md` | `playbooks/stage-2b/12-wunderbox.yml`, `playbooks/services/01-wunderbox-rebuild.yml` |
| `20` AAP | `20-aap/00-index.md` | `../30-runbooks/20-aap.md` | `playbooks/stage-2b/13-aap.yml`, `playbooks/services/02-aap-rebuild.yml` |
| `30` Linux Workstation | `30-linux-workstation/00-index.md` | `../30-runbooks/30-linux-workstation.md` | `playbooks/stage-2b/11-workbench.yml` |
| `40` OCP | `40-ocp/00-index.md` | `../30-runbooks/40-ocp.md` | `playbooks/stage-2c/container-platform-ocp4/prepare-ee.yml`, `20-ocp-install.yml`, `21-post-install.yml` |

Service specifications describe the target build. Runbooks define the method to
deploy that build.

## Canonical service rollout order

1. `10-wunderbox`
2. `20-aap`
3. `30-linux-workstation`
4. `40-ocp`
