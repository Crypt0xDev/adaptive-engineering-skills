<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:D97757,100:6B4FBB&height=170&section=header&text=Adaptive%20Engineering%20Skills&fontSize=36&fontColor=ffffff&animation=fadeIn&fontAlignY=36" alt="Adaptive Engineering Skills" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1200&color=D97757&center=true&vCenter=true&width=560&lines=El+contexto+define+la+soluci%C3%B3n;18+skills+para+Claude+Code;Simple+primero%2C+complejo+solo+si+hace+falta;Calidad+y+seguridad+siempre" alt="El contexto define la solución"/>

<p>
  <img src="https://img.shields.io/badge/Claude_Code-plugin-D97757?style=for-the-badge&logo=anthropic&logoColor=white" alt="Claude Code plugin"/>
  <img src="https://img.shields.io/badge/skills-18-6B4FBB?style=for-the-badge&logo=bookstack&logoColor=white" alt="18 skills"/>
  <img src="https://img.shields.io/github/actions/workflow/status/Crypt0xDev/adaptive-engineering-skills/ci.yml?style=for-the-badge&logo=githubactions&logoColor=white&label=CI" alt="CI"/>
  <img src="https://img.shields.io/badge/licencia-MIT-2EA44F?style=for-the-badge" alt="MIT"/>
</p>

</div>

## 💡 ¿Qué es?

Un plugin para Claude Code con skills de ingeniería de software. Antes de proponer algo, Claude
**mira el contexto real de tu proyecto** y elige la solución más simple que funcione. Nada de
microservicios para un MVP de dos personas.

## ⚡ Instalación

```
/plugin marketplace add Crypt0xDev/adaptive-engineering-skills
/plugin install adaptive-engineering@crypt0xdev
```

Listo. Las skills aparecen como `adaptive-engineering:<skill>` y Claude las usa solo cuando toca.

## 🧩 Skills

<details>
<summary><b>🧑‍💻 Roles senior (13)</b></summary>

| | Skill | Para qué |
|:-:|-------|----------|
| 🏛️ | `software-architect` | Arquitectura mínima según el contexto |
| 🗄️ | `database-architect` | Modelo de datos y motor |
| 🔐 | `security-engineer` | Seguridad según el riesgo |
| 🔍 | `code-reviewer` | Revisión de calidad y seguridad |
| 🚀 | `devops-engineer` | Despliegue según la etapa |
| ⚡ | `performance-engineer` | Optimizar midiendo, no adivinando |
| 🧪 | `test-engineer` | Qué probar y cuánto, según el riesgo |
| 🎨 | `ux-designer` | Flujos simples para el usuario |
| 📋 | `product-manager` | MVP y prioridades |
| 📝 | `business-analyst` | Requisitos claros y verificables |
| 💼 | `startup-advisor` | Velocidad y validación |
| 🔬 | `researcher` | Comparar tecnologías antes de elegir |
| 🛠️ | `skill-creator` | Estándar para crear skills |

</details>

<details>
<summary><b>⚙️ Proceso (5)</b></summary>

| | Skill | Para qué |
|:-:|-------|----------|
| 🧭 | `decisiones-tecnicas-fundamentadas` | Preguntar el contexto antes de decidir |
| 🧱 | `buenas-practicas-ingenieria` | SOLID y estructura, con criterio |
| 🔗 | `graphql-evaluacion-implementacion` | ¿GraphQL o REST? y cómo hacerlo bien |
| 📄 | `ahorro-tokens-archivos` | Leer PDF, Word, Excel y PPT gastando poco |
| 🎓 | `redaccion-academica` | Informes con citas y fuentes reales |

</details>

## 🧠 Filosofía

```
Entender → Analizar contexto → Evaluar complejidad → Solución más simple → Justificar
```

> SOLID, DDD y patrones no son reglas fijas: se usan si el proyecto lo pide.
> **Calidad y seguridad del código, siempre.**

## 🤝 Contribuir

Cada skill vive en `skills/<skill>/` con su `SKILL.md` y una carpeta `references/` opcional.
Sigue el estándar de `skill-creator`. El CI valida todo automáticamente
(`python3 .github/scripts/validate_plugin.py`). Los cambios por versión están en [CHANGELOG.md](CHANGELOG.md).

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6B4FBB,100:D97757&height=90&section=footer" alt="" width="100%"/>

Hecho por [Crypt0xDev](https://github.com/Crypt0xDev) · MIT

</div>
