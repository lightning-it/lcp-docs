# modulix-scripts RPM

`modulix-scripts` is the delivery artifact for the ModuLix automation runtime.

The source of truth is the `modulix-automation` repository, where the scripts,
runtime contract, and RPM packaging are maintained.

## Why this RPM exists

The RPM provides a stable and distributable runtime layer for operators:

- installs ModuLix script payload under `/opt/modulix`
- exposes wrapper commands under `/usr/bin` (for example `ansible-nav`)
- gives a versioned package for controlled rollout in enterprise environments
- allows delivery through standard RPM channels (for example COPR)

This avoids copying scripts manually and keeps runtime behavior consistent
across hosts and toolbox environments.

## Relationship to modulix-automation

Primary repository:

- `https://github.com/lightning-it/modulix-automation`

Relevant docs in that repository:

- `README.md` (delivery model: `modulix-scripts` RPM)
- `packaging/rpm/README.md` (build/publish flow)
- `docs/runtime-contract.md` (operator runtime contract)

## Where it is used

- Operator execution path via `scripts/ansible-nav`
- Toolbox image stack where `modulix-scripts` is installed as an RPM

## Operational note

Treat `modulix-scripts` version updates as runtime changes:

1. review release notes/changelog impact
2. validate critical runbooks (`30-runbooks/*`) in target environment
3. roll out with normal patch/change governance
