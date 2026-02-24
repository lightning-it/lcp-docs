# Runbooks Index

Runbooks in this section standardize the deployment method across services.

They are step-by-step operator guides that focus on how to deploy, validate,
and operate a service, independent from technology details.

## Standard runbook method

1. Define scope and prerequisites.
2. Prepare inventory and required inputs.
3. Execute deployment with the standard runtime wrapper.
4. Validate outcomes and record evidence.
5. Document follow-up, rollback, or troubleshooting actions.

Inventory is always environment-specific and is not delivered as a single
generic ModuLix baseline. Each platform team must model its own infrastructure,
grouping, and runtime input references in inventory.

## Service runbook map

- Wunderbox: `10-wunderbox.md` (spec: `../20-services/10-wunderbox/00-index.md`)
- AAP: `20-aap.md` (spec: `../20-services/20-aap/00-index.md`)
- Linux Workstation: `30-linux-workstation.md` (spec: `../20-services/30-linux-workstation/00-index.md`)
- OCP: `40-ocp.md` (spec: `../20-services/40-ocp/00-index.md`)
