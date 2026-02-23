# OCP Requirements

## Runtime and platform requirements

| Area | Requirement | Source |
| --- | --- | --- |
| Execution mode | Execution Environment with required collections/roles | `../../03-automation.md` |
| Stage-2c playbook set | `prepare-ee.yml`, `20-ocp-install.yml`, `21-post-install.yml` | `modulix-automation/ansible/playbooks/stage-2c/container-platform-ocp4/` |
| Lifecycle target group | inventory group/host mapped for OCP lifecycle (typically `ocp`) | `20-ocp-install.yml`, `99-ocp-destroy.yml` |

## Automation prerequisites

- Execute through `./scripts/ansible-nav`.
- Provide environment-specific inventory for OCP stage-2c workflows.
- Ensure required dependencies for stage-2c roles are available before install.

## Credential and secret requirements

- Do not commit plaintext secrets.
- Use vaulted inventory or approved secret backends for cluster credentials.
- Handle kubeconfig and admin credentials using environment-specific secret policies.

## Networking and firewall

- OCP network and firewall policy is environment-specific and documented in
  [`03-firewall-rules.md`](03-firewall-rules.md).
