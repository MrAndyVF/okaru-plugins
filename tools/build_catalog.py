#!/usr/bin/env python3
"""Genera catalog.toml a partir de <plugin>/plugin.toml (formato que lee OKARU).

Uso:
    python3 tools/build_catalog.py           # escribe catalog.toml
    python3 tools/build_catalog.py --check   # falla si catalog.toml no está al día
"""
import json
import os
import re
import sys
import tomllib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG = os.path.join(ROOT, "catalog.toml")
VERSION = re.compile(r"^\d+\.\d+\.\d+$")
FIELDS = ("id", "name", "version", "plugin_api", "author", "license", "icon", "description", "tags", "dependencies")
HEADER = (
    "# Catálogo de plugins de OKARU (郁). Generado por tools/build_catalog.py: no editar a mano.\n"
    "# Una fila [[plugin]] por cada subcarpeta de plugin; el plugin.toml de cada una manda.\n"
)


def build():
    rows, errors = [], []
    for sub in sorted(os.listdir(ROOT)):
        manifest = os.path.join(ROOT, sub, "plugin.toml")
        if sub.startswith(".") or not os.path.isfile(manifest):
            continue
        with open(manifest, "rb") as f:
            meta = tomllib.load(f)
        pid = meta.get("id", "")
        # La shell busca el plugin "autor/x" en la carpeta x/.
        if pid.partition("/")[2] != sub:
            errors.append(f"{sub}: id «{pid}» no termina en /{sub}")
        if not meta.get("name"):
            errors.append(f"{sub}: falta name")
        if not VERSION.match(str(meta.get("version", ""))):
            errors.append(f"{sub}: version debe ser MAYOR.MENOR.PARCHE")
        if not isinstance(meta.get("plugin_api"), int) or meta["plugin_api"] < 1:
            errors.append(f"{sub}: plugin_api debe ser un entero positivo")
        if not os.path.isfile(os.path.join(ROOT, sub, "LICENSE")):
            errors.append(f"{sub}: falta LICENSE")
        rows.append({k: meta[k] for k in FIELDS if k in meta})
    return rows, errors


def render(rows):
    out = [HEADER]
    for row in rows:
        out.append("\n[[plugin]]\n")
        for key, value in row.items():
            # JSON es TOML válido para cadenas, enteros y listas de cadenas.
            out.append(f"{key} = {json.dumps(value, ensure_ascii=False)}\n")
    return "".join(out)


def main():
    rows, errors = build()
    for e in errors:
        print("error:", e, file=sys.stderr)
    text = render(rows)
    if "--check" in sys.argv:
        current = open(CATALOG, encoding="utf-8").read() if os.path.exists(CATALOG) else ""
        if current != text:
            print("catalog.toml no está al día: ejecuta python3 tools/build_catalog.py", file=sys.stderr)
            return 1
        return 1 if errors else 0
    with open(CATALOG, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"{len(rows)} plugins en catalog.toml")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
