# PGF Processes

## Purpose

This document defines the core operational processes used to fulfill PGF
requirements.

## Core process catalog

| Process ID | Process | Trigger | Owner | Output | Evidence |
| --- | --- | --- | --- | --- | --- |
| `PGF-PRC-001` | Service onboarding | New service or major redesign | Service owner | Approved service operating profile | Onboarding checklist and approvals |
| `PGF-PRC-002` | Change management | Planned service change | Service owner and operations lead | Change decision and implementation record | Change ticket and rollback plan |
| `PGF-PRC-003` | Release readiness | Deployment/release window | Service owner and release lead | Go/no-go decision | Release checklist and sign-off |
| `PGF-PRC-004` | Incident response | Service degradation/outage | On-call and incident lead | Restored service and incident summary | Incident ticket and timeline |
| `PGF-PRC-005` | Problem management | Repeated incidents or major incident | Service owner | Root-cause and permanent fix plan | Problem record and action list |
| `PGF-PRC-006` | Backup and restore validation | Scheduled test window | Service owner | Verified restore capability | Test log and restore result |
| `PGF-PRC-007` | Operational review | Periodic cadence | Service owner | Improvement decisions | Review notes and action tracking |

## Process quality expectations

- Defined owner and fallback owner
- Inputs and outputs documented
- Clear completion criteria
- Evidence captured and retained
- Findings tracked to closure

## Interfaces

- Security/compliance gates are aligned with `../10-isms/`.
- Technical execution steps are aligned with `../30-modulix/`.
