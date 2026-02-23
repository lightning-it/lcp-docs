# Policy Catalog and Control Objectives

## Purpose

This document defines how policies and control objectives are structured in the
LCP ISMS layer.

## Policy catalog model

Each policy should include:

- `policy_id`: stable identifier
- `title`: short policy name
- `purpose`: governance intent
- `scope`: systems, services, and teams in scope
- `owner`: accountable role
- `control_objectives`: linked control objective IDs
- `review_cadence`: required review interval
- `exceptions`: approved exception handling path

## Baseline policy domains

- access management
- change and release governance
- vulnerability and patch governance
- logging and monitoring governance
- backup and recovery governance
- supplier and dependency governance
- incident and problem governance

## Control objective model

Each control objective should define:

- `control_id`: stable identifier
- `objective`: expected secure outcome
- `implementation_expectation`: what must exist
- `verification_method`: how objective is verified
- `evidence_required`: records needed for assurance
- `owner`: accountable role

## Traceability rule

Every control objective must map to:

- one or more policies in this document set
- one or more operational processes in `../20-pgf/`
- one or more technical implementation points in `../30-modulix/`

## Review and change rule

- policy and control objectives must be reviewed at least quarterly
- changes require impact statement and owner approval
- exceptions must include expiry and compensating measures

