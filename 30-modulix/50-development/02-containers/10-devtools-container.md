# Devtools Container Usage

Use the devtools execution environment for repository checks (for example
`pre-commit`, `ansible-lint`, Molecule, actionlint) without installing those
tools on the host.

## Security Scope (Required)

This workflow mounts the host Podman socket and disables SELinux labeling for
the container runtime path. Treat it as high-trust local developer workflow.

- Use only on trusted developer workstations.
- Do not use on production hosts, shared jump hosts, or regulated operator
  endpoints.
- Do not run this workflow against untrusted repositories/PRs.
- The mounted Podman socket allows container operations with host-user scope
  and can be abused for privilege expansion on the host.

## Run pre-commit in the devtools container

```bash
mkdir -p "$HOME/.cache/pre-commit"
systemctl --user enable --now podman.socket
H="$HOME/.cache/wunder-home"
mkdir -p "$H/.docker"

podman run --rm -it \
  --userns keep-id --user "$(id -u):$(id -g)" \
  --security-opt label=disable \
  -v "$PWD":"$PWD":z \
  -v "$HOME/.cache":"$HOME/.cache":z \
  -v "/run/user/$(id -u)/podman/podman.sock":"/run/user/$(id -u)/podman/podman.sock" \
  -w "$PWD" \
  -e HOME="$H" \
  -e DOCKER_CONFIG="$H/.docker" \
  -e XDG_CACHE_HOME="$HOME/.cache" \
  -e PRE_COMMIT_HOME="$HOME/.cache/pre-commit" \
  -e DOCKER_HOST="unix:///run/user/$(id -u)/podman/podman.sock" \
  -e GIT_CONFIG_COUNT=1 \
  -e GIT_CONFIG_KEY_0=safe.directory \
  -e GIT_CONFIG_VALUE_0="$PWD" \
  quay.io/l-it/ee-wunder-devtools-ubi9:v1.8.0 \
  pre-commit run --all-files
```

## Notes

- The Podman socket mount is required for hooks that run nested containers and
  is the main security-sensitive part of this setup.
- `--security-opt label=disable` is required for this mount model; apply only
  in the trusted local-dev scope described above.
- Keep runtime automation execution separate: run playbooks through the
  Ansible runtime workflow (`modulix-launcher` for service runs;
  `scripts/ansible-nav` in `modulix-automation/ansible` for direct stage/playbook runs).
