# Lightning IT Control Platform (LCP) Docs

<!-- BEGIN LIT_SHARED_RELEASE_MODEL -->

## Release and Quality Model

This repository follows the Lightning IT shared release and quality model.

See [RELEASE.md](./RELEASE.md) for:

- branch and release flow
- required quality checks
- test matrix
- release evidence
- artifact publishing
- supported repository-specific release behavior

Repository classification: **Documentation Repository**.
Required test profiles: `pre-commit, markdown, link-check`.
Publishing targets: `none`.

## Supported and Tested Platforms

| Platform / Product |                  Status | Validation         |
| ------------------ | ----------------------: | ------------------ |
| ubuntu-latest      |               Supported | Repository quality |
| lcp-docs           | Tested where applicable | Repository quality |

<!-- END LIT_SHARED_RELEASE_MODEL -->

<!-- BEGIN LIT_QUALITY_BADGES -->

[![CI](https://github.com/lightning-it/lcp-docs/actions/workflows/repository-quality.yml/badge.svg?branch=develop)](https://github.com/lightning-it/lcp-docs/actions/workflows/repository-quality.yml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/lightning-it/lcp-docs/badge)](https://scorecard.dev/viewer/?uri=github.com/lightning-it/lcp-docs)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

<!-- END LIT_QUALITY_BADGES -->

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

- `10-isms/` - governance and security documentation  
  Start: [`10-isms/README.md`](10-isms/README.md)
- `20-pgf/` - structure and operational reliability documentation  
  Start: [`20-pgf/README.md`](20-pgf/README.md)
- `30-modulix/` - automation and DevSecOps documentation  
  Start: [`30-modulix/README.md`](30-modulix/README.md)

## PGF quick links

- Index: [`20-pgf/00-index.md`](20-pgf/00-index.md)
- Overview: [`20-pgf/10-overview.md`](20-pgf/10-overview.md)
- Requirements: [`20-pgf/20-requirements.md`](20-pgf/20-requirements.md)
- Processes: [`20-pgf/30-processes.md`](20-pgf/30-processes.md)
- Controls: [`20-pgf/40-controls.md`](20-pgf/40-controls.md)

## Security

See [SECURITY.md](./SECURITY.md) for supported versions and vulnerability reporting.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for contribution and review expectations.

## License

See [LICENSE](./LICENSE).

<!-- BEGIN LIT_RELEASE_QUALITY_MODEL -->

## Release and Quality Model

This repository follows the Lightning IT shared release and quality model.
The README shows the current supported and tested matrix.
Exact per-version validation proof is stored with each GitHub Release as `release-evidence.md` and `release-evidence.json`.
Releases are created from the protected `main` branch after a reviewed `develop -> main` release promotion.
Repository checks validate the managed structure, documentation, and release model for this repository type.

See:

- [RELEASE.md](./RELEASE.md)
- [TESTING.md](./TESTING.md)
- [GitHub Releases](../../releases)

Repository classification: **Documentation Repository**.
Required test profiles: `pre-commit, markdown, link-check`.
Publishing targets: `none`.

<!-- END LIT_RELEASE_QUALITY_MODEL -->

<!-- BEGIN LIT_COMPATIBILITY_MATRIX -->

## Compatibility Matrix

| Platform / Product | Status | Validation |
|---|---:|---|
| ubuntu-latest | Supported | Repository quality |
| lcp-docs | Tested where applicable | Repository quality |

Validation proof for each released version is stored in the corresponding GitHub Release evidence.

<!-- END LIT_COMPATIBILITY_MATRIX -->

## Release Evidence

This repository does not publish release artifacts by default; release evidence is recorded when artifact releases are enabled.
The evidence records:

- tested matrix combinations
- GitHub Actions run links
- artifact references
- publish status
- security scan status

See [GitHub Releases](../../releases), [RELEASE.md](./RELEASE.md), and [TESTING.md](./TESTING.md) for the release process and validation model.
