---
name: ansible-redhat-cop
description: Applies Good Practices for Ansible (GPA) from the Red Hat Community of Practice (redhat-cop/automation-good-practices) when writing or reviewing roles, playbooks, collections, inventories, and plugins. Use when working with Ansible automation, roles, playbooks, inventories, collections, or when the user references redhat-cop, GPA, or Ansible best practices.
---

# Ansible Best Practices (redhat-cop GPA)

Follow the **Good Practices for Ansible (GPA)** from the [redhat-cop/automation-good-practices](https://github.com/redhat-cop/automation-good-practices) repo. Rendered docs: [redhat-cop.github.io/automation-good-practices](https://redhat-cop.github.io/automation-good-practices/). These are opinionated guidelines—adapt to your use case rather than follow blindly.

---

## Zen of Ansible

- Clear > cluttered. Concise > verbose. Simple > complex. Readability counts.
- Playbooks are not for programming; put logic in roles or custom modules.
- Prefer declarative over imperative. Convention over configuration.
- User experience over ideological purity.
- Every task idempotent; support check mode where possible.

---

## Structures (what to use for what)

| Layer | Purpose |
|-------|---------|
| **Landscape** | Deploy at once (workflow / "playbook of playbooks"). |
| **Type** | One per host type; one playbook fully deploys that type. |
| **Function** | Implemented as a **role**; reusability. |
| **Component** | Task files inside a role (or separate component-roles); maintainability. |

Use roles for logic; keep playbooks as a list of roles. Do not mix `roles:` and `tasks:` (with include_role/import_role) in the same play—pick one style.

---

## Roles

### Design and naming

- Design by **functionality**, not implementation (e.g. "NTP configuration" role, not "chrony role").
- **Variables**: prefix all defaults and role arguments with the role name (e.g. `foo_packages`). Internal vars: prefix with `__`, e.g. `__foo_variable`.
- **Tags**: prefix with role name or a unique descriptive prefix.
- **Role names**: no dashes (problems with collections); use underscores if needed.
- **Custom modules in roles**: prefix with role name, e.g. `foo_module`.
- Do not rely on host group names inside roles; use a (list) variable or make the group a role parameter; set that variable at group level in inventory.

### Vars vs defaults

- **defaults/main.yml**: every external argument gets a default; document in README. Optional keys here; no meaningful default → leave commented and let the role fail if undefined.
- **vars/main.yml**: static/magic values and large lists; not for user-overridable defaults (high precedence). Required packages as `foo_packages`; extra packages as `foo_extra_packages` in defaults (default `[]`).

### Platform and provider

- Avoid distribution/version checks in tasks. Use **vars per platform**: e.g. `vars/RedHat_8.yml`, `vars/Fedora.yml`, loaded via `include_vars` with `role_path` and a loop from least to most specific (`os_family`, `distribution`, `distribution_major_version`, `distribution_version`). Use `ansible_facts['distribution']` (bracket notation), not `ansible_distribution`.
- Multiple implementations: input variable `$ROLENAME_provider`; if unset, detect or choose by OS. Use `$ROLENAME_provider_os_default` for default per OS.
- Platform-specific **tasks**: `lookup('first_found')` with files from most to least specific, with a `default.yml` (or `skip: true`). Use `role_path` for paths.

### Idempotency and check mode

- Roles must be idempotent and report changes correctly. For `command:`/`shell:`, set `changed_when:` explicitly.
- Support check mode when possible; document if not. Avoid relying on registered vars from skipped non-idempotent tasks.

### Files and templates

- Use `{{ role_path }}/vars/...` and `{{ role_path }}/tasks/...` for includes with variable filenames.
- Templates: add `{{ ansible_managed | comment }}` at top; no "Last modified" dates (breaks idempotent change reporting). Prefer `backup: true` unless configurable.
- Document whether the role **replaces** or **modifies** config files.

### Other

- Galaxy-compatible skeleton; semantic versioning for tags (0.y.z until stable). Use FQCN in examples.
- README: purpose, required/optional arguments, idempotent (Y/N), capabilities, example playbooks, rollback if applicable.
- Sub-task names: prefix with a short hint, e.g. `sub | Some task description`.
- From Ansible 2.11+: use `meta/argument_specs.yml` for role argument validation.

---

## Coding style

- **Naming**: `snake_case`; valid Python identifiers. Mnemonic names; name all tasks, plays, blocks. Task names in **imperative** ("Ensure service is running"). No numbering in role/playbook names.
- **YAML**: 2 spaces; list contents indented beyond marker. `.yml` extension. `true`/`false` for booleans. Spell out task arguments in YAML form. Double quotes for YAML strings; single for Jinja2. No quotes for short keywords like `present`, `absent`.
- **Jinja2**: one space inside `{{ }}`. Bracket notation for keys: `item['key']`. Use `| bool` for bare vars in `when:`. Long lines: YAML folding `>-`; break long `when:` into a list. Prefer filter plugins over complex Jinja.
- **Tasks**: prefer dedicated modules over `command`/`shell`; if using them, add a comment and ensure idempotency/check mode. Do not use `meta: end_play` (use `meta: end_host` if needed). Dynamic task names: put Jinja at the **end** (e.g. "Manage device {{ device }}").
- **Debug**: set `verbosity:` on debug tasks so production logs stay clean.

---

## Playbooks

- Keep playbooks **simple**: ideally a list of roles (or import_role/include_role tasks). Put logic in roles.
- Use either **roles** or **tasks** (with import_role/include_role), not both in the same play.
- **Tags**: (1) role-named tags to enable/disable roles, or (2) purpose-level tags safe to run alone. One tag = one meaningful outcome. Document tags. Never tags that are unsafe or meaningless alone.

---

## Collections

- Structure at type or landscape level. Package roles in a collection for distribution and execution environments.
- Collection-wide variables: document them; reference in role defaults, e.g. `alpha_controller_username: "{{ mycollection_controller_username }}"`. Keep role variable naming (e.g. `alpha_*`) so roles stay reusable outside the collection.
- Include root README (purpose, license, supported ansible-core versions, dependencies) and LICENSE or COPYING.

---

## Inventories

- **SSOT**: identify single source of truth (cloud/CMDB/inventory); combine via dynamic inventory; static only for what is not provided elsewhere.
- **As-Is vs To-Be**: keep discovered state (facts) separate from desired state (variables).
- **Structure**: **inventory directory** with `group_vars/`, `host_vars/` (directories per group/host with one or more YAML files). Avoid one monolithic file when combining sources.
- **Loop over hosts**: run plays against inventory groups; use host/group variables. Do not maintain a separate host list and loop over it; use `--limit` and Ansible parallelism instead.

---

## Inventories and variable precedence

- Prefer **inventory variables** for desired state; avoid play/playbook vars and `include_vars` for that. Extra vars for debugging/temporary overrides only.
- Restrict variable types: prefer inventory vars and role defaults; scoped (block/task) vars only when needed.

---

## Plugins

- Document all plugins (parameters, return values, examples). Use reST/Sphinx docstrings and Python type hints. Prefer **pytest** for unit tests. Keep entry files small; move logic to module_utils/ or plugin_utils/. Use ansible.plugin_builder for new plugins. Clear, specific error messages; appropriate verbosity.

---

## Quick checklist

- [ ] Role vars/defaults prefixed with role name; internals with `__`.
- [ ] No hardcoded group names in roles; use variables or parameters.
- [ ] Platform-specific data in vars files; paths use `role_path`.
- [ ] Idempotent tasks; `changed_when:` for command/shell where needed.
- [ ] Playbook simple (roles or import_role list); not mixing roles + tasks.
- [ ] Tags role-level or purpose-level and safe alone.
- [ ] Bracket notation for facts/vars; imperative task names; `.yml`; 2-space indent.
- [ ] Inventory as directory with group_vars/host_vars; desired state in inventory.

---

## Source and reference

- **Repo**: [github.com/redhat-cop/automation-good-practices](https://github.com/redhat-cop/automation-good-practices) (structures, roles, collections, playbooks, inventories, plugins, coding_style).
- **Rendered**: [redhat-cop.github.io/automation-good-practices](https://redhat-cop.github.io/automation-good-practices/).
- More links and section mapping: [reference.md](reference.md).