# okaru-plugins

Tienda de plugins de [OKARU (郁)](https://github.com/MrAndyVF), una shell de escritorio Wayland.

Ningún plugin viene instalado: cada usuario elige cuáles instalar desde **Ajustes → Extensiones**.

## Estructura

- `catalog.toml`: índice de los plugins (una fila `[[plugin]]` por carpeta).
- `<plugin>/plugin.toml`: manifiesto del plugin, junto a sus archivos `.luau`, `translations/` y su `LICENSE`.
- `tools/build_catalog.py`: genera `catalog.toml` a partir de los `plugin.toml`.

## Plugins

| Plugin | Autor | Licencia |
|---|---|---|
| [Claude Code Usage](claudecode) | Nicolas Bellamy (adaptación a Noctalia de jrohland) | MIT |
| [Cursor](cursor) | Vn1k | MIT |
| [Icons](icons) | Vn1k | MIT |

Cada plugin conserva su `LICENSE` y la autoría original; OKARU los mantiene y adapta.

## Aportar un plugin

1. Crea `<carpeta>/` con `plugin.toml` (`id = "<autor>/<carpeta>"`, `name`, `version` MAYOR.MENOR.PARCHE,
   `plugin_api`), sus archivos y un `LICENSE`.
2. Ejecuta `python3 tools/build_catalog.py` y sube `catalog.toml` en el mismo pull request.

La GitHub Action comprueba que `catalog.toml` esté al día y que cada plugin tenga lo obligatorio.

El formato y la API (`noctalia.*`) son compatibles con los plugins de Noctalia.

## Reglas de diseño

OKARU entrega una barra y unos menús listos; los plugins se integran a ese diseño, no lo cambian.

- **Los menús siempre son flotantes** y salen junto al widget de la barra que los abrió. El usuario elige si se alinean a la izquierda, al centro o a la derecha del widget (`menu_align` en `[widget.<nombre>]`).
- `placement = "attached"` en `plugin.toml` se ignora: la shell lo trata como flotante. Tampoco se respetan los ajustes de posición en pantalla ni "abrir junto al clic" de los paneles que se abren desde la barra.
- Los paneles persistentes (`persistent = true`) no son menús de la barra y conservan su posición en pantalla.
