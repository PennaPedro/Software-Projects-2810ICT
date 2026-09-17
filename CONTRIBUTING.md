# Contributing to the XPower Group Project

## Team
- Mohit
- Dev
- Pedro
- Lakshay

## Git workflow
1. Create a branch from `main` for each task or feature.
2. Use clear branch names such as `docs/project-charter`, `feature/data-import`, `feature/flat-rate`, or `test/tariff-functions`.
3. Make focused commits with clear messages.
4. Push the branch and open a Pull Request into `main`.
5. Another team member should review the Pull Request before merge.
6. Do not push project work directly to `main` unless the team has explicitly agreed to an emergency fix.

## Pull Request expectations
Each PR should explain:
- what was completed;
- which Sprint task or project requirement it relates to;
- how the work was tested or checked;
- whether documentation was updated.

## Coding conventions
- Use Python `snake_case` names.
- Keep tariff calculations in `src/xpower/tariffs.py`.
- Keep import/validation logic in `src/xpower/data_import.py`.
- Keep tests inside `tests/`.
- Write short docstrings for public functions.
- Validate inputs before calculation.
- Do not commit personal/customer upload files from `data/uploads/`.

## Project management
The team is using five one-week Sprints. Sprint planning, backlog, review and retrospective material is stored under `agile/`.
