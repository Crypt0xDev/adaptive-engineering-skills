"""Valida la estructura del plugin: manifiestos JSON, frontmatter de skills y rutas citadas."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
errors = []

for manifest in (".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"):
    try:
        json.loads((ROOT / manifest).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{manifest}: {exc}")

for skill_md in sorted((ROOT / "skills").glob("*/SKILL.md")):
    skill_dir = skill_md.parent
    rel = skill_md.relative_to(ROOT)
    text = skill_md.read_text(encoding="utf-8")

    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        errors.append(f"{rel}: falta frontmatter YAML")
        continue
    front = match.group(1)
    name = re.search(r"^name:\s*(.+)$", front, re.MULTILINE)
    if not name or name.group(1).strip().strip('"') != skill_dir.name:
        errors.append(f"{rel}: 'name' debe coincidir con la carpeta '{skill_dir.name}'")
    if not re.search(r"^description:\s*\S", front, re.MULTILINE):
        errors.append(f"{rel}: falta 'description'")

    # Toda ruta references/... citada en la skill o sus referencias debe existir en esta skill
    for md in [skill_md, *skill_dir.glob("references/**/*.md")]:
        for ref in re.findall(r"`(references/[^`\s]+)`", md.read_text(encoding="utf-8")):
            owner = skill_dir
            # Referencias cruzadas: "skill `otra` → `references/x.md`"
            line = next(l for l in md.read_text(encoding="utf-8").splitlines() if ref in l)
            cross = re.search(r"skill `([a-z0-9-]+)`[^`]*`" + re.escape(ref) + "`", line)
            if cross:
                owner = ROOT / "skills" / cross.group(1)
            if not (owner / ref).exists():
                errors.append(f"{md.relative_to(ROOT)}: no existe {owner.name}/{ref}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("OK: plugin valido")
