# OCP Firewall Rules

## Source of truth

OCP firewall requirements are environment-specific and depend on:

- selected OCP topology and zone placement
- installer mode and infrastructure provider
- ingress, API, and node communication policies

At the moment, there is no single shared `group_vars/ocp*/firewall.yml` in the
core corp inventory tree for all environments.

## Baseline documentation requirement

For each OCP environment, define and maintain:

- control plane/API exposure policy
- ingress exposure policy
- node-to-node and node-to-infra allow-list rules
- bastion/admin access paths

## Change process

1. Update environment-specific inventory/network policy source of truth.
2. Mirror the effective rule set in this document (or linked environment appendix).
3. Validate with stage-2c runbook execution (`../../runbooks/ocp.md`).
