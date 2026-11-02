# okaru-plugins

Tienda de plugins de [OKARU (郁)](https://github.com/MrAndyVF), una shell de escritorio Wayland.

Ningún plugin viene instalado: cada usuario elige cuáles instalar desde **Ajustes → Extensiones**.

## Estructura

- `catalog.toml`: índice de los plugins (una fila `[[plugin]]` por carpeta).
- `<plugin>/plugin.toml`: manifiesto del plugin, junto a sus archivos `.luau` y `translations/`.

El formato y la API (`noctalia.*`) son compatibles con los plugins de Noctalia.
