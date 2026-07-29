# Engineering agent contract

This repository publishes public LCP documentation. Treat `.lit/repository.yml`,
`RELEASE.md`, `TESTING.md`, `SECURITY.md`, and the accepted Lightning IT
Engineering ADRs as the governing repository contract.

- Work through a pull request into `develop`; promote reviewed `develop` to `main`.
- Validate Markdown, internal links, navigation, and repository structure.
- Do not publish credentials, internal-only endpoints, personal data, or customer
  information.
- Keep external GitHub Actions pinned to full commit SHAs and permissions
  least-privilege.
- Preserve managed-file headers and change shared policy at
  `lightning-it/shared-assets-lit`.
- Run `python3 scripts/lit-push-ready.py push-ready` before pushing.
- Required remote checks and branch protection must not be bypassed.
- ADR 70 temporarily allows zero human/CODEOWNER approvals and separately
  documented protected-environment self-approval for immutable exact-SHA
  plan/apply evidence; it does not allow PR self-review or check bypass.
