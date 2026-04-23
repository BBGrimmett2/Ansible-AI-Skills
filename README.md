# Ansible AI Skills

A curated collection of AI-powered skills for Ansible automation, designed to enhance Claude Code's capabilities when working with Ansible projects, Red Hat Automation Platform (AAP), and enterprise automation workflows.

## Overview

This repository provides specialized knowledge modules (skills) that enable AI assistants to apply industry best practices, proven patterns, and Red Hat Communities of Practice (CoP) standards when working with Ansible automation projects.

## Available Skills

### 1. Red Hat Ansible CoP Best Practices (`rh-ansible-cop`)

Applies **Good Practices for Ansible (GPA)** from the [Red Hat Communities of Practice](https://github.com/redhat-cop/automation-good-practices) when writing or reviewing Ansible content.

**Use this skill when:**
- Writing or reviewing Ansible roles, playbooks, collections, inventories, or plugins
- Ensuring code follows the Zen of Ansible principles
- Structuring automation projects for maintainability and reusability
- Implementing platform-agnostic roles with proper variable precedence
- Validating YAML coding style and Jinja2 templating patterns

**Key capabilities:**
- Role design and structure validation
- Variable naming and precedence guidance
- Platform and provider abstraction patterns
- Idempotency and check mode support
- Collection packaging best practices
- Inventory design patterns

**Documentation:** [rh-ansible-cop/SKILL.md](rh-ansible-cop/SKILL.md)

### 2. AAP Configuration as Code (`rh-aap-config-as-code`)

Implements **Ansible Automation Platform (AAP) configuration as code** using the `infra.aap_configuration` collection from Red Hat CoP.

**Use this skill when:**
- Managing AAP 2.5+ configuration as YAML
- Working with Automation Controller, Hub, Gateway, or EDA configurations
- Implementing GitOps patterns for AAP platform management
- Migrating from older AAP collections to the unified collection
- Structuring multi-environment AAP configuration repositories

**Key capabilities:**
- Dispatch role orchestration and dependency ordering
- Controller, Hub, Gateway, and EDA object management
- Environment-based configuration organization
- Wildcard variable aggregation patterns
- Secret management and authentication patterns
- Migration from legacy collections

**Documentation:** [rh-aap-config-as-code/SKILL.md](rh-aap-config-as-code/SKILL.md)

## Repository Structure

```
ansible-ai-skills/
├── README.md                          # This file
├── CONTRIBUTING.md                    # Contribution guidelines
├── rh-ansible-cop/                    # Red Hat Ansible CoP skill
│   ├── SKILL.md                       # Skill definition and instructions
│   └── reference.md                   # Quick reference and links
└── rh-aap-config-as-code/            # AAP config-as-code skill
    ├── SKILL.md                       # Skill definition and instructions
    └── reference.md                   # Quick reference and links
```

## Quick Start

### For Claude Code Users

These skills are designed to work seamlessly with [Claude Code](https://claude.com/claude-code). When you reference these skills in your Claude Code project, the AI assistant will automatically apply the appropriate best practices and patterns.

### Using Skills in Your Project

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/ansible-ai-skills.git
   cd ansible-ai-skills
   ```

2. **Reference a skill in your project:**
   Add skill references in your project's `.claude/CLAUDE.md` file or simply mention the skill when working with Claude Code:
   ```markdown
   When working with Ansible content, apply the rh-ansible-cop skill.
   When managing AAP configuration, apply the rh-aap-config-as-code skill.
   ```

3. **Let the AI assistant guide you:**
   The skills provide comprehensive context about best practices, patterns, and anti-patterns to avoid.

## Skill Development

Each skill follows a standard structure:

- **SKILL.md**: Complete skill definition with instructions, patterns, and guidelines
- **reference.md**: Quick reference material, links, and command snippets

### Skill Metadata

Each `SKILL.md` includes YAML frontmatter:

```yaml
---
name: skill-name
description: Brief description of what the skill does and when to use it
---
```

## Use Cases

### Ansible Development
- Create roles following Red Hat CoP standards
- Structure collections for enterprise distribution
- Implement proper variable precedence and naming
- Design maintainable inventory structures
- Write idempotent, check-mode compatible tasks

### AAP Platform Management
- Define Controller job templates, projects, and workflows as code
- Configure Hub namespaces, collections, and execution environments
- Set up Gateway authentication and routing
- Manage EDA rulebook activations and decision environments
- Organize multi-environment configurations

### Code Review and Validation
- Validate Ansible code against industry best practices
- Identify anti-patterns and suggest improvements
- Ensure consistent coding style and structure
- Review AAP configuration for dependency ordering
- Check for security vulnerabilities and secret exposure

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for:
- How to add new skills
- Skill quality guidelines
- Testing and validation requirements
- Code of conduct

## Validation

This repository includes automated validation workflows:
- YAML syntax validation
- Markdown linting
- Skill structure validation
- Link checking
- Documentation completeness checks

All skills must pass validation before merging.

## Resources

### Red Hat Ansible CoP
- [automation-good-practices](https://github.com/redhat-cop/automation-good-practices) - Official GPA documentation
- [Rendered Documentation](https://redhat-cop.github.io/automation-good-practices/)

### AAP Configuration as Code
- [infra.aap_configuration](https://github.com/redhat-cop/infra.aap_configuration) - Unified AAP configuration collection
- [Galaxy Collection](https://galaxy.ansible.com/ui/repo/published/infra/aap_configuration/)

### Ansible Best Practices
- [Ansible Documentation](https://docs.ansible.com/)
- [Ansible Lint](https://ansible-lint.readthedocs.io/)
- [Red Hat Communities of Practice](https://github.com/redhat-cop)

## License

This project is provided as-is for educational and automation purposes. Individual skills may reference external projects with their own licenses.

## Maintainers

- Brian Grimmet (@bgrimmet)

## Acknowledgments

Special thanks to the Red Hat Communities of Practice for maintaining the automation best practices and configuration collections that form the foundation of these skills.
