# modulix-launcher RPM

`modulix-launcher` is the operator-facing launcher for ModuLix service workflows.

It is delivered independently from `modulix-automation-runtime` and focuses on:

- stable command entry point: `modulix-launcher`
- nested runtime execution (`toolbox -> run EE`)
- service commands for `wunderbox` and `aap`
- `toolbox shell` for debugging/editing in the runtime container

## Source of truth

- `https://github.com/lightning-it/modulix-launcher`

## Install path

- `/usr/bin/modulix-launcher`

## Runtime relationship

- `modulix-launcher` orchestrates container execution.
- `modulix-automation-runtime` provides the baseline automation payload under
  `/opt/modulix/ansible`.

Both are part of the operational runtime model and should be versioned and
rolled out with normal change governance.
