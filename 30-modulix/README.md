# ModuLix Documentation

Curated operator and architecture portal for ModuLix in LCP.

## Start Here

Use these first to understand ModuLix scope, bootstrap operator workflows, and
review the baseline automation, security, and patching model.

- `01-overview.md`
- `02-getting-started.md`
- `03-automation.md`
- `04-security.md`
- `05-patching.md`

## Architecture

Architecture documents explain how domains fit together and provide navigation
from high-level views to domain indexes.

- Index: `10-architecture/00-index.md`
- Big picture: `10-architecture/10-big-picture.md`

## Service Specifications

Service specifications define technology-specific service builds (for example
Wunderbox, AAP, Linux Workstation, OCP).

They answer what is built:

- service architecture and component boundaries
- technical requirements and dependencies
- service-specific policy and network/firewall constraints

- Index: `20-services/00-index.md`
- Wunderbox index: `20-services/10-wunderbox/00-index.md` (runbook: `30-runbooks/10-wunderbox.md`)
- AAP index: `20-services/20-aap/00-index.md` (runbook: `30-runbooks/20-aap.md`)
- Linux Workstation index: `20-services/30-linux-workstation/00-index.md` (runbook: `30-runbooks/30-linux-workstation.md`)
- OCP index: `20-services/40-ocp/00-index.md` (runbook: `30-runbooks/40-ocp.md`)

## Runbooks

Runbooks define the deployment method used to deliver a service.

They answer how a service is deployed in a step-by-step, method-first way:

- prepare scope, inventory, and prerequisites
- execute with the standard runtime contract
- validate deployment outcome
- capture follow-up and troubleshooting steps

Runbooks are intentionally non-technology-specific in structure, then mapped to
service-specific entry points.

- Index: `30-runbooks/00-index.md`
- Wunderbox: `30-runbooks/10-wunderbox.md`
- AAP: `30-runbooks/20-aap.md`
- Linux Workstation: `30-runbooks/30-linux-workstation.md`
- OCP: `30-runbooks/40-ocp.md`

## Containers

This section documents execution container images used in ModuLix runtime and
development workflows.

- Index: `40-containers/00-index.md`
- Toolbox: `40-containers/10-toolbox.md`
- Ansible EE: `40-containers/20-ansible.md`
- Devtools EE: `40-containers/30-devtools.md`

## RPMs

RPM docs describe packaged runtime artifacts and their operational role in the
ModuLix delivery model.

- Index: `41-rpms/00-index.md`
- modulix-scripts RPM: `41-rpms/10-modulix-scripts.md`

## Ansible Collections

This catalog lists LIT-provided `lit.*` Ansible collections and their intended
automation scope.

- Index: `42-ansible-collections/00-index.md`
- Foundational: `42-ansible-collections/10-foundational.md`
- RHEL: `42-ansible-collections/20-rhel.md`
- Supplementary: `42-ansible-collections/30-supplementary.md`
- OCP: `42-ansible-collections/40-ocp.md`

## Development

Development guides cover contributor workflows for collections, containerized
tooling, and RPM-related maintenance.

- Index: `50-development/00-index.md`
- Ansible collections guidelines: `50-development/01-ansible-collections/00-index.md`
- Containers guidelines: `50-development/02-containers/00-index.md`
- RPM guidelines: `50-development/03-rpms/00-index.md`
- Devtools container usage: `50-development/02-containers/10-devtools-container.md`

## Troubleshooting

Troubleshooting contains known failure patterns and quick diagnostic guidance
for common operational issues.

- Index: `90-troubleshooting/00-index.md`
- Common failures: `90-troubleshooting/01-common-failures.md`

## Canonical Runtime Contract

These upstream documents are the authoritative source for supported runtime
behavior, defaults, and support scope.

- `https://github.com/lightning-it/modulix-automation/blob/main/docs/runtime-contract.md`
- `https://github.com/lightning-it/modulix-automation/blob/main/docs/support-matrix.md`
