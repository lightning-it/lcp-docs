# Local Collection Overlays

Local overlays are for development only.

## Workflow

```bash
cd /path/to/modulix-automation/ansible
./scripts/install-local-collections
```

This overlays local `ansible-collection-*` builds in `collections-dev` ahead of bundled collections.

## Guidance

- Keep production and customer runs on the default EE collection set.
- Use overlays for iterative role/module development and testing.
