# redhat-cop Automation Good Practices — Reference

Links and section mapping for the [redhat-cop/automation-good-practices](https://github.com/redhat-cop/automation-good-practices) repository.

## Official sources

| Resource | URL |
|----------|-----|
| **GPA (rendered)** | https://redhat-cop.github.io/automation-good-practices/ |
| **Repository** | https://github.com/redhat-cop/automation-good-practices |
| **Contributing** | https://github.com/redhat-cop/automation-good-practices/blob/main/CONTRIBUTE.adoc |

## Repo structure (six sections + coding style)

The GPA document is split into six main sections plus coding style. Each has a `README.adoc` in the repo:

| Section | Path in repo | Content |
|---------|--------------|---------|
| **Structures** | `structures/` | What to use for which purpose (landscape, type, function, component). |
| **Roles** | `roles/` | Role design, vars vs defaults, platform/provider, idempotency, files/templates. |
| **Collections** | `collections/` | Packaging, collection-wide variables, README/LICENSE. |
| **Playbooks** | `playbooks/` | Simplicity, roles vs tasks, tags. |
| **Inventories** | `inventories/` | SSOT, as-is vs to-be, directory structure, host/group vars. |
| **Plugins** | `plugins/` | Documentation, testing, module_utils, error messages. |
| **Coding style** | `coding_style/` | Naming, YAML style, Jinja2, tasks, debug. |

## Tooling in the repo

- **.ansible-lint**: Example ansible-lint configuration; can be used as reference for project lint rules.
- **Makefile**: Build/docs targets used by the GPA project itself.

## Terminology

- **GPA**: Good Practices for Ansible (the document/site).
- **redhat-cop**: Red Hat Community of Practice; maintains automation-good-practices and related repos.
- **SSOT**: Single source of truth (for inventory/data).