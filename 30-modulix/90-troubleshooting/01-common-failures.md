# Common Failures

## Missing inventory path in container

- Symptom: inventory file not found under `/runner/project/inventories/...`
- Check inventory mounts and `-i` argument.

## SSH authentication failures

- Symptom: permission denied / no key loaded
- Check `SSH_AUTH_SOCK` and key presence in agent (`ssh-add -L`).
- `modulix-launcher` forwards the SSH agent socket; it does not require a
  host `~/.ssh` bind mount by default.

## Collection/module not found

- Symptom: module resolution failures during run.
- Verify configured EE image contains required collections.
- If developing locally, apply local overlays with `install-local-collections`.

## Vault token / secret failures

- Symptom: forbidden / invalid token.
- Verify token scope and secret path policies for requested action.
