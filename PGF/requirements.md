# PGF Requirements

## Purpose

This document defines how operational requirements are structured and managed in
PGF.

## Requirement model

Each requirement should include:

- `id`: stable identifier (example: `PGF-REQ-001`)
- `title`: short requirement name
- `description`: concrete expected outcome
- `scope`: services/environments covered
- `owner`: accountable role
- `priority`: `must`, `should`, or `could`
- `verification_method`: how compliance is verified
- `evidence`: where proof is stored
- `review_cadence`: required review frequency

## Baseline requirement areas

Minimum requirement categories for each service:

- Service ownership and RACI clarity
- Onboarding and handover readiness
- Change and release readiness
- Incident and escalation readiness
- Backup/restore and recovery readiness
- Monitoring, alerting, and observability readiness
- Access and authorization operating requirements
- Dependency and interface documentation
- Environment-specific firewall and network requirements

## Traceability

Each requirement should map to:

- at least one operational process in [`processes.md`](processes.md)
- at least one control in [`controls.md`](controls.md)
- evidence artifacts in the team evidence repository

## Review

- Requirement sets must be reviewed at least quarterly.
- Changes must include owner approval and impact statement.
