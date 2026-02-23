# Architecture Big Picture

ModuLix is organized around one execution contract and multiple documentation layers:

1. Runtime contract (`scripts/ansible-nav`) in `modulix-automation`
2. Execution containers (toolbox + ansible EE + devtools EE)
3. LIT Ansible collections (`lit.foundational`, `lit.rhel`, `lit.supplementary`, `lit.ocp`)
4. Service playbooks and service specs
5. Operator runbooks
6. Development and troubleshooting guides

Use this architecture section as entry point by domain index:

- Services index: `../20-services/00-index.md`
- Runbooks index: `../30-runbooks/00-index.md`
- Containers index: `../40-containers/00-index.md`
- RPMs index: `../41-rpms/00-index.md`
- Ansible collections index: `../42-ansible-collections/00-index.md`
- Development index: `../50-development/00-index.md`
- Troubleshooting index: `../90-troubleshooting/00-index.md`

Architecture perspective pages remain available when you want a design-focused
summary:

- Containers perspective: `20-containers.md`
- Services perspective: `30-services.md`
- Runbooks perspective: `40-runbooks.md`
- Development perspective: `50-development.md`
- Troubleshooting perspective: `60-troubleshooting.md`
