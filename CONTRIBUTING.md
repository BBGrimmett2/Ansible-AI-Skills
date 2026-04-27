# Contributing to Ansible AI Skills

Thank you for your interest in contributing to the Ansible AI Skills repository! This document provides guidelines and instructions for contributing new skills, improvements, and fixes.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Adding a New Skill](#adding-a-new-skill)
- [Skill Quality Guidelines](#skill-quality-guidelines)
- [Development Workflow](#development-workflow)
- [Testing and Validation](#testing-and-validation)
- [Commit Message Guidelines](#commit-message-guidelines)

## Code of Conduct

This project follows the principles of respect, collaboration, and constructive feedback. Be kind, be professional, and help create a welcoming environment for all contributors.

## How to Contribute

Contributions can take many forms:

1. **New Skills**: Add new AI skills for Ansible-related technologies
2. **Improvements**: Enhance existing skills with better patterns, examples, or documentation
3. **Bug Fixes**: Correct errors in skill content or structure
4. **Documentation**: Improve README, guides, or references
5. **Validation**: Add or improve automated tests and validation workflows

## Adding a New Skill

### 1. Create the Skill Directory

Create a new directory with a descriptive name using kebab-case:

```bash
mkdir my-new-skill
cd my-new-skill
```

### 2. Create SKILL.md

Every skill must have a `SKILL.md` file with the following structure:

```markdown
---
name: my-new-skill
description: Brief description of what this skill does and when to use it (1-2 sentences)
---

# Skill Title

Detailed description of the skill's purpose and capabilities.

## When to Use This Skill

Clearly define:
- When this skill should be applied
- What types of tasks it helps with
- What technologies or patterns it covers

## Key Capabilities

List the main features:
- Capability 1
- Capability 2
- Capability 3

## Guidelines and Best Practices

Provide detailed guidance on:
- Design patterns
- Common implementations
- Anti-patterns to avoid
- Configuration examples

## Quick Reference

Include a quick reference section with:
- Common commands
- Configuration snippets
- Checklists

## Resources

Link to authoritative sources:
- Official documentation
- Related projects
- Learning resources
```

### 3. Create reference.md

Create a `reference.md` file for quick lookups:

```markdown
# Skill Name Reference

Quick reference material for [skill name].

## Official Sources

| Resource | URL |
|----------|-----|
| Documentation | https://... |
| Repository | https://... |

## Quick Commands

Common commands and snippets...

## Common Patterns

Frequently used patterns...
```

### 4. Validate Your Skill

Run validation locally before submitting:

```bash
# Install validation tools
pip install yamllint pre-commit
npm install -g markdownlint-cli

# Run pre-commit hooks
pre-commit install
pre-commit run --all-files

# Run skill validation
python .github/scripts/validate_skills.py
```

## Skill Quality Guidelines

### Content Requirements

1. **Accuracy**: All information must be accurate and up-to-date
2. **Clarity**: Write in clear, concise language
3. **Completeness**: Cover the topic comprehensively
4. **Practicality**: Include real-world examples and use cases
5. **Authority**: Reference official documentation and authoritative sources

### Structure Requirements

1. **YAML Frontmatter**: Must include `name` and `description`
2. **Headings**: Use proper heading hierarchy (H1 for title, H2 for sections)
3. **Code Blocks**: Use fenced code blocks with language identifiers
4. **Links**: All external links must be valid and point to stable resources
5. **Formatting**: Follow Markdown best practices

### Technical Requirements

1. **No Secrets**: Never include actual credentials, tokens, or sensitive data
2. **Security**: Highlight security best practices
3. **Idempotency**: Emphasize idempotent patterns for Ansible content
4. **Compatibility**: Clearly state version requirements and compatibility

## Development Workflow

### 1. Fork and Clone

```bash
git clone https://github.com/yourusername/ansible-ai-skills.git
cd ansible-ai-skills
```

### 2. Create a Feature Branch

```bash
git checkout -b feature/my-new-skill
```

### 3. Make Your Changes

- Add or modify skills
- Update documentation
- Add tests if applicable

### 4. Validate Locally

```bash
# Run all validations
pre-commit run --all-files

# Test the skill validation
python .github/scripts/validate_skills.py

# Check YAML syntax
yamllint -c .yamllint.yml .

# Check Markdown
markdownlint -c .markdownlint.yml **/*.md
```

### 5. Commit Your Changes

Follow the commit message guidelines (see below):

```bash
git add .
git commit -m "Add new skill for Ansible Molecule testing"
```

### 6. Push and Create Pull Request

```bash
git push origin feature/my-new-skill
```

Then create a Pull Request on GitHub with:

- Clear title describing the change
- Description of what was added/changed
- Reference to any related issues
- Screenshots or examples if applicable

## Testing and Validation

All contributions must pass automated validation:

### YAML Validation

- Syntax correctness
- Proper indentation (2 spaces)
- Valid frontmatter

### Markdown Validation

- Proper formatting
- Valid links
- Heading hierarchy

### Skill Structure Validation

- Required files present (SKILL.md, reference.md)
- Valid YAML frontmatter
- Required metadata fields

### Spell Check

- Technical terms added to `.cspell.json` as needed
- No typos in documentation

## Commit Message Guidelines

Follow these conventions for commit messages:

### Format

```text
<type>: <subject>

<body>

<footer>
```

### Types

- `feat`: New skill or major feature addition
- `fix`: Bug fix or correction
- `docs`: Documentation changes
- `style`: Formatting, missing semicolons, etc.
- `refactor`: Code restructuring without functionality change
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples

```text
feat: Add Ansible Molecule testing skill

- Add comprehensive SKILL.md with testing patterns
- Include reference.md with common commands
- Add examples for different test scenarios

Closes #42
```

```text
fix: Correct AAP configuration variable names

Update variable names in rh-aap-config-as-code skill to match
the latest infra.aap_configuration collection version 2.5.0.
```

## Review Process

1. **Automated Checks**: All CI/CD workflows must pass
2. **Peer Review**: At least one maintainer review required
3. **Testing**: Validate that examples work as documented
4. **Documentation**: Ensure README and references are updated

## Questions or Issues?

- Open an issue for bugs or feature requests
- Start a discussion for questions about best practices
- Tag maintainers for urgent matters

## License

By contributing, you agree that your contributions will be licensed under the same terms as the project.

## Recognition

Contributors will be acknowledged in the project README and commit history. Thank you for helping make Ansible AI Skills better!
