"""Valida la estructura del plugin: manifiestos JSON, frontmatter de skills y rutas citadas."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
errors = []

manifests = {}
for manifest in (".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"):
    try:
        manifests[manifest] = json.loads((ROOT / manifest).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{manifest}: {exc}")

plugin = manifests.get(".claude-plugin/plugin.json", {})
market = manifests.get(".claude-plugin/marketplace.json", {})
for key in ("name", "description", "version"):
    if not plugin.get(key):
        errors.append(f".claude-plugin/plugin.json: falta '{key}'")
if plugin.get("version") and not re.fullmatch(r"\d+\.\d+\.\d+", plugin["version"]):
    errors.append(".claude-plugin/plugin.json: 'version' debe ser semver (X.Y.Z)")
if plugin.get("name") and plugin["name"] not in [p.get("name") for p in market.get("plugins", [])]:
    errors.append(f".claude-plugin/marketplace.json: no lista el plugin '{plugin['name']}'")

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

# Coherencia: cada skill aparece en el README y el total declarado coincide con las carpetas
skills = sorted(p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md"))
readme = (ROOT / "README.md").read_text(encoding="utf-8")
for skill in skills:
    if f"`{skill}`" not in readme:
        errors.append(f"README.md: falta la skill '{skill}' en la tabla")
sources = {
    "README.md": readme,
    ".claude-plugin/plugin.json": plugin.get("description", ""),
    ".claude-plugin/marketplace.json": " ".join(p.get("description", "") for p in market.get("plugins", [])),
}
for source, text in sources.items():
    declared = {int(a or b) for a, b in re.findall(r"\b(\d+)[+ ]skills\b|skills-(\d+)-", text)}
    for count in declared - {len(skills)}:
        errors.append(f"{source}: dice {count} skills pero hay {len(skills)}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: plugin valido ({len(skills)} skills)")
