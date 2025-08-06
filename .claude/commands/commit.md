# Commit

Create well-formatted commits with conventional commit messages.

## Features:

- Runs pre-commit checks by default (lint, build)
- Automatically stages files if none are staged
- Suggests splitting commits for different concerns

## Usage:

- `/commit` - Standard commit with pre-commit checks
- `/commit --no-verify` - Skip pre-commit checks

## Commit Types:

- feat: New features
- fix: Bug fixes
- docs: Documentation changes
- refactor: Code restructuring without changing functionality
- style: Code formatting, missing semicolons, etc.
- perf: Performance improvements
- test: Adding or correcting tests
- chore: Tooling, configuration, maintenance
- wip: Work in progress
- remove: Removing code or files
- hotfix: Critical fixes
- security: Security improvements

## Process:

1. Check for staged changes (`git status`)
2. If no staged changes, review and stage appropriate files
3. Run pre-commit checks (unless --no-verify)
4. See @.claude/commands/check.md for more details about checks
   4-1. See @web/.claude/commands/check.md for web project. (If you in a web folder, you `cd web` to web project.)
5. Analyze changes to determine commit type
6. Generate descriptive commit message
7. Include scope if applicable: `type(scope): description`
8. Add body for complex changes explaining why
9. Execute commit

## Best Practices:

- Keep commits atomic and focused
- Write in imperative mood ("add feature" not "added feature")
- Explain why, not just what
- Reference issues/PRs when relevant
- Split unrelated changes into separate commits
