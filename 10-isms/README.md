# lcp-isms

LCP ISMS component (Governance and Security): certification-ready information
security governance with clear ownership, policy framework, risk analysis, and
audit preparation.

## Purpose

This folder is the entry point for the ISMS layer of Lightning IT Control
Platform (LCP).

The ISMS component defines the governance baseline that other LCP components
must follow:

- accountable security roles and responsibilities
- policy and standard structure
- risk-based decision model
- audit-ready documentation and evidence logic

## Start Here

- `00-index.md`
- `10-overview.md`
- `20-governance-raci.md`
- `30-policy-controls.md`
- `40-risk-management.md`
- `50-audit-readiness.md`

## What this component covers

Based on LCP product positioning, the ISMS component provides:

- formal governance and security foundation
- role model for security and compliance ownership
- policy set and governance controls
- risk analysis and treatment model
- preparation model for internal and external audits

## Expected outcomes

- consistent security governance across services
- traceable security decisions and accepted risks
- repeatable audit preparation and evidence collection
- controlled interface between governance requirements and technical delivery

## Audience

- security leadership and governance owners
- information security officers and compliance managers
- IT management responsible for control implementation
- auditors and assurance stakeholders

## Interfaces to other LCP components

- `../20-pgf/` translates governance expectations into operational structures,
  process definitions, and requirement catalogs.
- `../30-modulix/` implements technical controls and policy-driven automation in
  delivery pipelines and runtime operations.

## Adoption model

LCP can be adopted modularly:

- ISMS-first (governance baseline before full automation rollout)
- staged integration with PGF for process reliability
- full-stack implementation with ModuLix for policy-driven technical execution

## Suggested structure for this folder

Use this folder to maintain and evolve:

- governance charter and role/RACI model (`20-governance-raci.md`)
- policy catalog and control objectives (`30-policy-controls.md`)
- risk register model and treatment workflow (`40-risk-management.md`)
- SoA/audit-readiness artifacts and evidence mapping (`50-audit-readiness.md`)

## Source alignment

This refactoring aligns with the current LCP product description:

- `https://www.lightning-it.de/produkte/lcp`
