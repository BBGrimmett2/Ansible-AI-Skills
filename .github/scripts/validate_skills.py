#!/usr/bin/env python3
"""
Validate Ansible AI Skills structure and content.

This script checks that all skills in the repository follow the required
structure and contain all necessary components.
"""

import os
import sys
import yaml
from pathlib import Path


class SkillValidator:
    """Validator for Ansible AI Skills."""

    def __init__(self, repo_root):
        self.repo_root = Path(repo_root)
        self.errors = []
        self.warnings = []

    def log_error(self, message):
        """Log an error message."""
        self.errors.append(f"ERROR: {message}")
        print(f"❌ {message}")

    def log_warning(self, message):
        """Log a warning message."""
        self.warnings.append(f"WARNING: {message}")
        print(f"⚠️  {message}")

    def log_success(self, message):
        """Log a success message."""
        print(f"✅ {message}")

    def find_skill_directories(self):
        """Find all skill directories in the repository."""
        skills = []
        for item in self.repo_root.iterdir():
            if item.is_dir() and not item.name.startswith('.') and not item.name.startswith('_'):
                skill_file = item / 'SKILL.md'
                if skill_file.exists():
                    skills.append(item)
        return skills

    def validate_skill_metadata(self, skill_file):
        """Validate YAML frontmatter in SKILL.md."""
        with open(skill_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for YAML frontmatter
        if not content.startswith('---\n'):
            self.log_error(f"{skill_file}: Missing YAML frontmatter")
            return None

        # Extract frontmatter
        parts = content.split('---\n', 2)
        if len(parts) < 3:
            self.log_error(f"{skill_file}: Invalid YAML frontmatter format")
            return None

        try:
            metadata = yaml.safe_load(parts[1])
        except yaml.YAMLError as e:
            self.log_error(f"{skill_file}: Invalid YAML in frontmatter - {e}")
            return None

        # Validate required fields
        required_fields = ['name', 'description']
        for field in required_fields:
            if field not in metadata:
                self.log_error(f"{skill_file}: Missing required field '{field}' in frontmatter")
            elif not metadata[field] or not isinstance(metadata[field], str):
                self.log_error(f"{skill_file}: Field '{field}' must be a non-empty string")

        return metadata

    def validate_skill_structure(self, skill_dir):
        """Validate that a skill directory has the required structure."""
        skill_name = skill_dir.name
        print(f"\n📋 Validating skill: {skill_name}")

        required_files = ['SKILL.md', 'reference.md']
        for filename in required_files:
            file_path = skill_dir / filename
            if not file_path.exists():
                self.log_error(f"{skill_name}: Missing required file '{filename}'")
            else:
                self.log_success(f"{skill_name}: Found {filename}")

        # Validate SKILL.md metadata
        skill_file = skill_dir / 'SKILL.md'
        if skill_file.exists():
            metadata = self.validate_skill_metadata(skill_file)
            if metadata:
                self.log_success(f"{skill_name}: Valid YAML frontmatter")

                # Check if skill name matches directory
                if metadata.get('name') and metadata['name'] != skill_name:
                    self.log_warning(
                        f"{skill_name}: Skill name '{metadata['name']}' "
                        f"does not match directory name '{skill_name}'"
                    )

    def validate_repository_structure(self):
        """Validate overall repository structure."""
        print("\n📁 Validating repository structure")

        required_files = ['README.md', 'CONTRIBUTING.md', '.gitignore']
        for filename in required_files:
            file_path = self.repo_root / filename
            if not file_path.exists():
                self.log_warning(f"Repository missing recommended file '{filename}'")
            else:
                self.log_success(f"Found {filename}")

        # Check for GitHub workflows
        workflows_dir = self.repo_root / '.github' / 'workflows'
        if not workflows_dir.exists():
            self.log_warning("No .github/workflows directory found")
        else:
            self.log_success("Found .github/workflows directory")

    def run(self):
        """Run all validations."""
        print("🔍 Starting Ansible AI Skills validation...\n")

        # Validate repository structure
        self.validate_repository_structure()

        # Find and validate skills
        skills = self.find_skill_directories()
        if not skills:
            self.log_error("No skill directories found")
            return False

        print(f"\n📦 Found {len(skills)} skill(s)")

        for skill_dir in skills:
            self.validate_skill_structure(skill_dir)

        # Print summary
        print("\n" + "=" * 60)
        print("VALIDATION SUMMARY")
        print("=" * 60)
        print(f"Skills validated: {len(skills)}")
        print(f"Errors: {len(self.errors)}")
        print(f"Warnings: {len(self.warnings)}")

        if self.errors:
            print("\n❌ Validation FAILED with errors:")
            for error in self.errors:
                print(f"  • {error}")
            return False
        elif self.warnings:
            print("\n⚠️  Validation PASSED with warnings:")
            for warning in self.warnings:
                print(f"  • {warning}")
            return True
        else:
            print("\n✅ Validation PASSED - All checks successful!")
            return True


def main():
    """Main entry point."""
    repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    validator = SkillValidator(repo_root)

    success = validator.run()
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
