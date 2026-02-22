# PGF Controls

## Purpose

This document defines operational controls that ensure process quality and
service reliability.

## Control model

Each control should define:

- `id`: stable identifier (example: `PGF-CTRL-001`)
- `objective`: control goal
- `scope`: covered services or environments
- `frequency`: cadence (event-based, weekly, monthly, quarterly)
- `owner`: accountable role
- `evidence`: required proof artifacts
- `non_conformance_action`: response if control fails

## Baseline control catalog

| Control ID | Objective | Frequency | Owner | Evidence |
| --- | --- | --- | --- | --- |
| `PGF-CTRL-001` | Critical services have named owner and deputy | Quarterly | Platform governance lead | Service ownership register |
| `PGF-CTRL-002` | Changes use documented review and rollback plan | Per change | Change approver | Change records |
| `PGF-CTRL-003` | Incident handling follows defined escalation path | Per incident | Incident lead | Incident timeline and postmortem |
| `PGF-CTRL-004` | Restore capability is tested successfully | Quarterly | Service owner | Backup/restore test report |
| `PGF-CTRL-005` | Operational KPIs are reviewed and actions tracked | Monthly | Service owner | KPI review notes and action list |
| `PGF-CTRL-006` | Firewall/service exposure matches approved policy | Quarterly | Operations lead | Firewall review record |

## Mapping and alignment

- Controls should be mapped to requirements in [`requirements.md`](requirements.md).
- Controls should reference process outputs from [`processes.md`](processes.md).
- Security-specific controls should be cross-referenced with `../ISMS/`.

## Exceptions

- Any temporary control exception must have owner approval, expiry date, and
  compensating measures.
