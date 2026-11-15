# Changelog

Based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and
[Semantic Versioning](https://semver.org/).

## [2.0.0] - 2026-11-15

### Added
- Expanded to 101 skills organized in 9 categories
- All skills translated to English and improved with examples, tables and verification checklists
- Skills grouped into: engineering, quality, design, devops, security, workflow, optimization, omniroute, memory

### Changed
- Major version bump to 2.0.0
- README restructured with collapsible sections per category
- CI validator updated for nested directory structure

## [1.3.0] - 2026-11-04

### Added
- Skill `test-engineer`: what to test, with which test type, and how much, based on risk and stage.
- CI validator checks required fields in `plugin.json`, `marketplace.json` listing, README references, and skill count consistency.
- `.gitattributes` for LF line endings.
- `CHANGELOG.md`.
- Manual CI trigger (`workflow_dispatch`).

### Changed
- Repo renamed to `adaptive-engineering-skills`.
- `skill-creator` template includes frontmatter (`name`, `description`) required by CI.

### Fixed
- Issue templates missing initial `---` frontmatter delimiter.

## [1.2.0]

- Published under previous repo `adaptive-ai-engineering-system`.
