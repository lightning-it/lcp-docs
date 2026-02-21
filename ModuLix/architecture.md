# ModuLix Architecture

## Execution model

- Default execution path:
  - `modulix-automation/ansible/scripts/ansible-nav`
  - toolbox container runtime
  - ansible-navigator execution (exact flags defined in runtime contract docs)
- Base collections are provided by the configured EE image.

## Components

- ModuLix automation repo (`modulix-automation`): release-coupled execution contract and RPM delivery source.
- Toolbox image: wrapper runtime environment.
- EE image: Ansible + collection execution payload.
- lcp-docs: curated operator guidance, runbooks, troubleshooting and architecture narrative.

## Documentation boundary

- Release-coupled contract docs remain in `modulix-automation`.
- Operator workflows and long-form guides remain in `lcp-docs`.
