# Patching and Dependency Management

This document defines how ModuLix handles patch management across automation,
collections, containers, and documentation.

Patch management in ModuLix is automation-first and PR-driven, with Renovate as
the standard update bot.

## 1) Goals

- reduce exposure time for known vulnerabilities
- keep dependencies current without uncontrolled breakage
- make every update traceable and reviewable
- separate routine patch flow from emergency remediation

## 2) Renovate in ModuLix

Renovate continuously scans configured files and opens pull requests for
available updates.

It is used with both native managers and regex/custom managers to track
versions that are pinned in text files, scripts, and docs.

Examples from current repositories:

- `modulix-automation/renovate.json`
  tracks toolbox image references in `docs/runtime-contract.md`,
  `docs/support-matrix.md`, and `ansible/scripts/ansible-nav`.
- `lcp-docs/renovate.json`
  tracks container image tags referenced in `30-modulix/*.md`.
- `ansible-collection-supplementary/renovate.json`
  and `ansible-collection-foundational/renovate.json`
  track `galaxy.yml` collection dependencies.
- `container-ee-wunder-ansible-ubi9/renovate.json`
  tracks Python, Ansible collections, and pinned tool versions via custom
  managers.

## 3) Patch domains

| Domain | Typical artifacts | Managed by |
| --- | --- | --- |
| Automation runtime | `modulix-launcher`, `scripts/ansible-nav`, runtime contract image tags | Renovate PRs + operator review |
| Ansible collections | `galaxy.yml`, collection constraints | Renovate PRs + compatibility checks |
| Container build inputs | Dockerfile/Containerfile args, pip requirements | Renovate PRs + image build/test |
| Documentation references | image tags in docs | Renovate PRs + doc review |

## 4) Standard patch workflow

1. Renovate creates PRs (and dependency dashboard entries where enabled).
2. Maintainers triage by risk and scope:
   patch/minor first, majors with explicit review.
3. CI and repo-specific checks must pass.
4. Operational validation is done where required (for example playbook runs or
   image smoke tests).
5. PR is merged and released using the normal repo release flow.

## 5) Guardrails and constraints

Some dependencies are intentionally constrained to protect compatibility.

Examples in current config:

- `ansible-core` constrained to supported ranges in multiple repos
- `community.vmware` pinned for known compatibility constraints
- grouped updates to reduce noisy PR floods

These guardrails are deliberate and should only be changed with explicit impact
analysis.

## 6) Emergency patching

For critical CVEs or active incidents:

1. create an expedited patch PR (manual or Renovate-assisted)
2. run minimum required validation
3. merge with incident approval path
4. record rationale and follow up with full regression checks

## 7) What Renovate does not replace

Renovate automates update proposals. It does not replace:

- vulnerability scanning
- risk acceptance decisions
- operational change approval
- compliance evidence collection

Use Renovate as the update engine, and keep governance in the normal security
and operations process.
