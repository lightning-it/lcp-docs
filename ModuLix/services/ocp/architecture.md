# OCP Architecture

## Purpose

OCP service documentation covers OpenShift 4 stage-2c lifecycle automation in
ModuLix.

## Execution path

- Service runbook: [`../../runbooks/ocp.md`](../../runbooks/ocp.md)
- Stage-2c workspace: `modulix-automation/ansible/playbooks/stage-2c/container-platform-ocp4/`
- Runtime wrapper and execution contract: [`../../runbooks/automation.md`](../../runbooks/automation.md)

## Playbook composition

Main stage-2c playbooks:

1. `prepare-ee.yml`
2. `20-ocp-install.yml`
3. `21-post-install.yml`
4. `99-ocp-destroy.yml` (teardown path)

## Integration points

- OCP lifecycle playbooks commonly target `ocp` hosts/groups.
- Inventory model may differ by environment and can be separate from core
  service host inventories.
- Post-install flows integrate with platform services (for example GitOps and
  secret backends), depending on environment configuration.

## Boundaries

- Service-specific architecture decisions are documented here.
- Global automation behavior and wrapper flags stay in `runbooks/automation.md`.
