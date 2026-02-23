# Risk Management Model

## Purpose

This document defines the LCP ISMS risk model and treatment workflow.

## Risk register model

Each risk entry should include:

- `risk_id`: stable identifier
- `title`: concise risk statement
- `description`: scenario and impact narrative
- `asset_or_service`: affected scope
- `owner`: accountable role
- `likelihood`: rating scale value
- `impact`: rating scale value
- `risk_level`: calculated rating
- `treatment_option`: avoid, reduce, transfer, or accept
- `treatment_plan`: actions, due dates, and assignees
- `status`: open, in-treatment, accepted, closed
- `review_date`: next mandatory review date

## Rating model

Use a 1-5 scale for both likelihood and impact:

- `1` very low
- `2` low
- `3` medium
- `4` high
- `5` very high

Risk level is calculated as `likelihood x impact`.

## Treatment workflow

1. Identify risk and record owner and scope.
2. Assess likelihood and impact.
3. Select treatment option and define treatment plan.
4. Obtain governance approval for treatment or acceptance.
5. Track actions to completion.
6. Reassess risk on scheduled cadence or major change.

## Governance rules

- no accepted risk without accountable owner approval
- no open high risk without active treatment plan
- all accepted risks require expiry or planned revalidation
- risk register must be reviewed at least quarterly

