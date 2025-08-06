# Check

Perform comprehensive code quality and security checks.

See @pyproject.toml for more details.

## Tasks:

Run following commands and resolve any resulting errors.

- `poe lint`: Run linting checks
- `poe lint-fix`: Fix linting errors
- `poe format`: Fix code formatting

## Important:

- DO NOT commit any code during this process
- DO NOT change version numbers
- Focus only on fixing issues identified by checks

## Common Checks Include:

1. **Linting**: Code style and syntax errors
2. **Code Formatting**: Style consistency
3. **Build Verification**: Compilation errors

## Process:

1. Run the check command
2. Analyze output for errors and warnings
3. Fix issues in priority order:
   - Build-breaking errors first
   - Test failures
   - Linting errors
   - Warnings
4. Re-run checks after each fix
5. Continue until all checks pass
