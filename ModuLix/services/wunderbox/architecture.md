# Wunderbox Architecture

## Purpose

Wunderbox is the internal "core services" host in ModuLix and provides:

- CoreDNS
- DHCP
- Vault
- MinIO
- Nexus
- NGINX

## Execution path

- Service runbook: [`../../runbooks/wunderbox.md`](../../runbooks/wunderbox.md)
- Primary playbook: `modulix-automation/ansible/playbooks/stage-2b/12-wunderbox.yml`
- Runtime wrapper and execution contract: [`../../runbooks/automation.md`](../../runbooks/automation.md)

## Role composition

High-level role order in `12-wunderbox.yml`:

1. `lit.rhel.repos`
2. `fedora.linux_system_roles.firewall`
3. `lit.supplementary.coredns_deploy`
4. `lit.supplementary.dhcp_deploy`
5. Vault stack (`vault_deploy`, `vault_bootstrap`, `vault_validate`, `vault_config`)
6. MinIO stack (`minio_deploy`, `minio_bootstrap`)
7. `lit.supplementary.nexus`
8. NGINX stack (`nginx_deploy`, `nginx_config`)

## Integration points

- Inventory group: `wunderboxes`
- Host vars and group vars: `ansible-inventory-lit/inventories/corp/...`
- Vault is used as secret control-plane for downstream service integrations
- Default service ingress policy is documented in [`firewall-rules.md`](firewall-rules.md)

## Boundaries

- Service-specific architecture decisions are documented here.
- Global automation behavior and wrapper flags stay in `runbooks/automation.md`.
