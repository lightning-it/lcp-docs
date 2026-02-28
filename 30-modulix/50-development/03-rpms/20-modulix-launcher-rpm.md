# modulix-launcher RPM Development

This guideline describes how `modulix-launcher` is packaged and released as an
independent RPM.

## Why this matters

- Separates operator launcher lifecycle from `modulix-automation`.
- Enables controlled rollout of launcher fixes without rebuilding the full
  automation payload.
- Provides a stable host command (`modulix-launcher`) in `/usr/bin`.

## Source of truth

- Repository: `https://github.com/lightning-it/modulix-launcher`
- Packaging docs: `modulix-launcher/packaging/rpm/README.md`
- Container artifact docs: `modulix-launcher/packaging/container/README.md`

## Developer workflow (summary)

1. Change launcher script or packaging in `modulix-launcher`.
2. Build SRPM via `packaging/rpm/build-srpm.sh`.
3. Validate launcher behavior:
   - `modulix-launcher --inventory-dir ... services <wunderbox|aap> ...`
   - `modulix-launcher --inventory-dir ... toolbox shell`
4. Publish via repository CI/release workflow.

## Related operator docs

- RPM overview: `../../41-rpms/20-modulix-launcher.md`
- Local runtime flow: `../02-containers/20-local-modulix-runtime.md`
- Patch governance and update process: `../../05-patching.md`
