# okaru-plugins

**English** · [Español](#español)

Plugin store for [OKARU (郁)](https://github.com/MrAndyVF/okaru), a Wayland desktop shell.

No plugin comes preinstalled: each user picks which ones to install from **Settings → Extensions**.

## Layout

- `catalog.toml`: plugin index (one `[[plugin]]` row per folder).
- `<plugin>/plugin.toml`: plugin manifest, next to its `.luau` files, `translations/` and its `LICENSE`.
- `tools/build_catalog.py`: generates `catalog.toml` from the `plugin.toml` files.

## Plugins

| Plugin | Author | License |
|---|---|---|
| [Claude Code Usage](claudecode) | Nicolas Bellamy (Noctalia port of jrohland's work) | MIT |
| [Cursor](cursor) | Vn1k | MIT |
| [Icons](icons) | Vn1k | MIT |

Each plugin keeps its `LICENSE` and original authorship; OKARU maintains and adapts them.

## Contributing a plugin

1. Create `<folder>/` with `plugin.toml` (`id = "<author>/<folder>"`, `name`, `version` MAJOR.MINOR.PATCH,
   `plugin_api`), its files and a `LICENSE`.
2. Run `python3 tools/build_catalog.py` and commit `catalog.toml` in the same pull request.

The GitHub Action checks that `catalog.toml` is up to date and that every plugin has the required files.

The format and the API (`noctalia.*`) are compatible with Noctalia plugins.

## Design rules

OKARU ships a ready-made bar and menus; plugins fit into that design instead of changing it.

- **Menus are always floating** and open next to the bar widget that opened them. The user chooses whether
  they align to the left, center or right of the widget (`menu_align` in `[widget.<name>]`).
- `placement = "attached"` in `plugin.toml` is ignored: the shell treats it as floating. On-screen position
  settings and "open next to the click" are not honored either for panels opened from the bar.
- Persistent panels (`persistent = true`) are not bar menus and keep their on-screen position.

## License

The repository is MIT ([LICENSE](LICENSE)). Each plugin is distributed under the `LICENSE` in its own
folder. By opening a pull request you agree to publish your plugin under the license you include; do not
submit third-party work without permission.

---

## Español

Tienda de plugins de [OKARU (郁)](https://github.com/MrAndyVF/okaru), una shell de escritorio Wayland.

Ningún plugin viene instalado: cada usuario elige cuáles instalar desde **Ajustes → Extensiones**.

### Estructura

- `catalog.toml`: índice de los plugins (una fila `[[plugin]]` por carpeta).
- `<plugin>/plugin.toml`: manifiesto del plugin, junto a sus archivos `.luau`, `translations/` y su `LICENSE`.
- `tools/build_catalog.py`: genera `catalog.toml` a partir de los `plugin.toml`.

### Plugins

| Plugin | Autor | Licencia |
|---|---|---|
| [Claude Code Usage](claudecode) | Nicolas Bellamy (adaptación a Noctalia de jrohland) | MIT |
| [Cursor](cursor) | Vn1k | MIT |
| [Icons](icons) | Vn1k | MIT |

Cada plugin conserva su `LICENSE` y la autoría original; OKARU los mantiene y adapta.

### Aportar un plugin

1. Crea `<carpeta>/` con `plugin.toml` (`id = "<autor>/<carpeta>"`, `name`, `version` MAYOR.MENOR.PARCHE,
   `plugin_api`), sus archivos y un `LICENSE`.
2. Ejecuta `python3 tools/build_catalog.py` y sube `catalog.toml` en el mismo pull request.

La GitHub Action comprueba que `catalog.toml` esté al día y que cada plugin tenga lo obligatorio.

El formato y la API (`noctalia.*`) son compatibles con los plugins de Noctalia.

### Reglas de diseño

OKARU entrega una barra y unos menús listos; los plugins se integran a ese diseño, no lo cambian.

- **Los menús siempre son flotantes** y salen junto al widget de la barra que los abrió. El usuario elige si se alinean a la izquierda, al centro o a la derecha del widget (`menu_align` en `[widget.<nombre>]`).
- `placement = "attached"` en `plugin.toml` se ignora: la shell lo trata como flotante. Tampoco se respetan los ajustes de posición en pantalla ni "abrir junto al clic" de los paneles que se abren desde la barra.
- Los paneles persistentes (`persistent = true`) no son menús de la barra y conservan su posición en pantalla.

### Licencia

El repositorio es MIT ([LICENSE](LICENSE)). Cada plugin se distribuye bajo el `LICENSE` de su propia
carpeta. Al enviar un pull request aceptas publicar tu plugin bajo la licencia que incluyas; no subas trabajo
de terceros sin su permiso.
