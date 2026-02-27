# Devtools Container Usage

Use the devtools execution environment for repository checks (for example
`pre-commit`, `ansible-lint`, Molecule, actionlint) without installing those
tools on the host.

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
  quay.io/l-it/ee-wunder-devtools-ubi9:v1.7.1 \
  pre-commit run --all-files
```

## Notes

- The Podman socket mount is required for hooks that run nested containers.
- Keep runtime automation execution separate: run playbooks through the
  Ansible runtime workflow (`scripts/ansible-nav` in `modulix-automation/ansible`).
