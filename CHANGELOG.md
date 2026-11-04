# Changelog

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y
[versionado semántico](https://semver.org/lang/es/).

## [1.3.0] - 2026-11-04

### Añadido
- Skill `test-engineer`: qué probar, con qué tipo de test y cuánto, según el riesgo y la etapa.
- El validador comprueba los campos obligatorios de `plugin.json`, que `marketplace.json`
  liste el plugin, que cada skill aparezca en el README y que el total de skills declarado coincida.
- `.gitattributes` para normalizar los finales de línea a LF.
- `CHANGELOG.md`.
- Ejecución manual del CI (`workflow_dispatch`).

### Cambiado
- Repo renombrado a `adaptive-engineering-skills` (homepage, badge de CI, comando de instalación).
- Nombre visible del proyecto: "Adaptive Engineering Skills".
- La plantilla de `skill-creator` incluye el frontmatter (`name`, `description`) que exige el CI.

### Corregido
- Las plantillas de issues no tenían el `---` inicial del frontmatter, así que GitHub no las reconocía.

## [1.2.0]

- Versión publicada en el repo anterior `adaptive-ai-engineering-system`.
