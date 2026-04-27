# Pull Request Title

<!-- Provide a clear, concise title summarizing the changes -->

## Summary

<!-- Describe the purpose of this pull request. Include relevant context about the problem being solved or the feature being added. -->

## Changes

- [ ] New Skill
- [ ] Skill Enhancement
- [ ] Bug Fix
- [ ] Documentation Update
- [ ] Validation/CI Improvement
- [ ] Other (please specify):

### Description of Changes

<!-- Provide a detailed list of changes, including what was modified, added, or removed. If applicable, mention related issue numbers (e.g., Fixes #123). -->

## Testing

### How Has This Been Tested?

<!-- Describe the testing process. Include details on how the changes were validated. -->

- [ ] All automated validations pass (YAML, Markdown, Spell Check)
- [ ] Skill structure validation passes
- [ ] Links checked and verified
- [ ] Tested skill with Claude Code in a real project
- [ ] Other (please specify):

### Validation Results

<!-- Include output from validation commands if applicable -->

```bash
# Example validation commands:
# yamllint -c .yamllint.yml .
# markdownlint -c .markdownlint.yml **/*.md
# python .github/scripts/validate_skills.py
```

## Checklist

- [ ] I have tested this change and it works as expected
- [ ] I have updated documentation (if applicable)
- [ ] This PR follows the repository's [contribution guidelines](CONTRIBUTING.md)
- [ ] All required files are present (SKILL.md, reference.md for new skills)
- [ ] YAML frontmatter is properly formatted with `name` and `description`
- [ ] All external links are valid and point to stable resources
- [ ] No secrets or sensitive data are included
- [ ] Code blocks have language identifiers where applicable

## Additional Information

<!-- Include any relevant screenshots, examples, or additional context that may help reviewers. -->

### For New Skills

<!-- Complete this section if adding a new skill -->

**Skill Name:** <!-- e.g., rh-ansible-molecule -->

**Trigger Criteria:** <!-- When should this skill be invoked? -->

**Key Capabilities:** <!-- What can this skill help with? -->

**Related Skills:** <!-- Does this complement or overlap with existing skills? -->
