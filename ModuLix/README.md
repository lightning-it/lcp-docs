# ModuLix Documentation

Curated operator and architecture portal for ModuLix in LCP.

## Start here

- Overview: `overview.md`
- Architecture: `architecture.md`
- Getting started: `getting-started.md`

## Runbooks

- Automation workflows: `runbooks/automation.md`
- `01` Wunderbox: `runbooks/wunderbox.md`
- `02` AAP: `runbooks/aap.md`
- `03` Linux Workstation: `runbooks/linux-workstation.md`
- `04` OCP: `runbooks/ocp.md`

## Service Specifications

- `01` Wunderbox service index: `services/wunderbox/README.md`
- `01` Wunderbox architecture: `services/wunderbox/architecture.md`
- `01` Wunderbox requirements: `services/wunderbox/requirements.md`
- `01` Wunderbox firewall rules: `services/wunderbox/firewall-rules.md`
- `02` AAP service index: `services/aap/README.md`
- `02` AAP architecture: `services/aap/architecture.md`
- `02` AAP requirements: `services/aap/requirements.md`
- `02` AAP firewall rules: `services/aap/firewall-rules.md`
- `03` Linux Workstation service index: `services/linux-workstation/README.md`
- `03` Linux Workstation architecture: `services/linux-workstation/architecture.md`
- `03` Linux Workstation requirements: `services/linux-workstation/requirements.md`
- `03` Linux Workstation firewall rules: `services/linux-workstation/firewall-rules.md`
- `04` OCP service index: `services/ocp/README.md`
- `04` OCP architecture: `services/ocp/architecture.md`
- `04` OCP requirements: `services/ocp/requirements.md`
- `04` OCP firewall rules: `services/ocp/firewall-rules.md`

## Troubleshooting

- Common failures: `troubleshooting/common-failures.md`

## Development

- Local overlays and extension patterns: `development/local-overlays.md`
- Devtools container usage (pre-commit, lint/test): `development/devtools-container.md`

## Canonical runtime contract (release-coupled)

Canonical runtime flags and behavior are maintained in the automation repo:

- `https://github.com/lightning-it/modulix-automation/blob/main/docs/runtime-contract.md`
- `https://github.com/lightning-it/modulix-automation/blob/main/docs/support-matrix.md`

For release-specific behavior, use tagged links:
`https://github.com/lightning-it/modulix-automation/blob/<tag>/docs/runtime-contract.md`.

Treat these files as source-of-truth for executable behavior.
