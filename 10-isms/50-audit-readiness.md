# Audit Readiness and Evidence Model

## Purpose

This document defines how LCP prepares for audits and maintains evidence
traceability.

## Audit-readiness principles

- controls must be linked to accountable owners
- evidence must be reproducible and time-bounded
- findings must be tracked to closure
- exceptions must be approved and documented

## Evidence model

Each evidence record should include:

- `evidence_id`: stable identifier
- `control_id`: linked control objective
- `source`: where evidence is generated
- `period`: date range covered
- `owner`: accountable role
- `storage_location`: canonical repository path
- `integrity_marker`: version, checksum, or immutable reference
- `review_status`: draft, accepted, superseded

## SoA mapping approach

Maintain a statement-of-applicability style matrix with:

- control objective
- applicability decision
- implementation status
- evidence reference
- owner and review date

## Audit cycle workflow

1. Confirm in-scope controls and services.
2. Validate evidence completeness and freshness.
3. Resolve gaps before audit window.
4. Package evidence and mapping references.
5. Record findings and corrective actions.
6. Track remediation to closure.

## Minimum readiness checklist

- all in-scope controls have named owner
- required evidence exists for current review period
- open findings have remediation plans
- exceptions are approved and not expired
- cross-links to `../20-pgf/` and `../30-modulix/` are current

