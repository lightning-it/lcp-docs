# Lightning IT Control Platform (LCP) Docs

This repository is the entry point for internal and operator-facing documentation of the **Lightning IT Control Platform (LCP)**.

Product context: https://www.lightning-it.de/produkte/lcp

## What LCP covers

Based on the official product positioning, LCP combines three building blocks:

- **ISMS component (Governance & Security)**: certification-ready security governance (ISO 27001 / BSI), including roles, policies, risk management, and audit preparation.
- **PGF component (Structure & Operational Reliability)**: governance framework with operational handbooks, detailed concepts, and requirement catalogs.
- **ModuLix component (Automation & DevSecOps)**: technical delivery with GitOps, CI/CD, Vault, monitoring, backup, and hardening with compliance-by-design.

## Why this repo exists

The product page explains what LCP is at a high level. This repository exists to document how LCP is implemented and operated in practice:

- versioned architecture and implementation guidance
- reproducible runbooks for operations and automation
- shared governance and security documentation
- traceable documentation updates through Git history

## Benefit for teams

- Single, stable entry point for onboarding and day-2 operations
- Better collaboration across Security, Operations, and Engineering
- Faster reuse of proven patterns instead of re-documenting per project
- Audit-friendly documentation for regulated environments

## Documentation map

- `ISMS/` - governance and security documentation  
  Start: [`ISMS/README.md`](ISMS/README.md)
- `PGF/` - structure and operational reliability documentation  
  Start: [`PGF/README.md`](PGF/README.md)
- `ModuLix/` - automation and DevSecOps documentation  
  Start: [`ModuLix/README.md`](ModuLix/README.md)

## PGF quick links

- Overview: [`PGF/overview.md`](PGF/overview.md)
- Requirements: [`PGF/requirements.md`](PGF/requirements.md)
- Processes: [`PGF/processes.md`](PGF/processes.md)
- Controls: [`PGF/controls.md`](PGF/controls.md)
