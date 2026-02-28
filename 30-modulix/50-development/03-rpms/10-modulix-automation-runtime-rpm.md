# modulix-automation-runtime RPM Development

This guideline describes how ModuLix runtime scripts are packaged and released
as the `modulix-automation-runtime` RPM.

## Why this matters

- `modulix-automation-runtime` is the delivery artifact for ModuLix runtime tooling.
- It provides stable wrapper commands such as `ansible-nav`.
- `modulix-launcher` is packaged separately and consumes this runtime payload.
- It enables controlled rollout through standard RPM channels.

## Source of truth

- Repository: `https://github.com/lightning-it/modulix-automation`
- Delivery model: `modulix-automation/README.md`
- Packaging docs: `modulix-automation/packaging/rpm/README.md`

## Developer workflow (summary)

1. Change scripts or packaging in `modulix-automation`.
2. Build SRPM via `packaging/rpm/build-srpm.sh`.
3. Validate wrapper behavior (`ansible-nav`, `ansible-nav-local`).
4. Publish through the defined COPR/GitHub workflow.

## Related operator docs

- Runtime artifact overview: `../../41-rpms/10-modulix-automation-runtime.md`
- Patch governance and Renovate flow: `../../05-patching.md`
