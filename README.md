---
tipo: readme
estado: activo
---
# pub_actus-mercator/ — Gestión empresarial: blog satélite del hub `04 index` (repo actus-mercator, actus-mercator.netlify.app)

<!-- GENERADO por `04 index/scripts/pubs.py readme --aplicar` desde `04 index/_pubs/pubs.yml` (2026-09-20); no editar aquí: se regenera desde el hub -->

## Qué es

Administración, estrategia y gestión organizacional. Es uno de los 11 blogs satélite de la familia Quarto de Edison Achalma: un sitio Quarto
con repositorio y sitio Netlify propios, incluido como submódulo git en el hub `04 index` (repo
`website-achalma`) bajo `04 index/_pubs/pub_actus-mercator/`. El mismo blog tiene tres nombres: carpeta `pub_actus-mercator`, repo
GitHub `achalmed/actus-mercator` y dominio `actus-mercator.netlify.app`; el registro de los tres es `04 index/_pubs/pubs.yml`.

El tema visual (SCSS, JS, extensiones, filtros, `scripts/build-page-css.sh`) **no se edita aquí**: vive en el hub y
llega por `04 index/scripts/sync-theme-pubs.sh`. Lo propio de este blog es `_quarto.yml`, `index.qmd`, `_contenido-*.qmd`,
`assets/img/` y las entradas.

## Uso

```bash
quarto preview                              # vista previa local
quarto render                               # regenera _site/ (freeze: true: el código no se re-ejecuta)
git add -A && git commit -m "post: …"       # confirmar AQUÍ primero…
git push                                    # …al remoto propio (ssh git@github.com:achalmed/actus-mercator.git)
cd ../.. && git add _pubs/pub_actus-mercator && git commit -m "pubs: actus-mercator al último commit"   # y mover el puntero en el hub
```

## Estructura

| carpeta | qué es | entradas |
|---|---|--:|
| `inteligencia-comercial/` | sección temática | 1 |
| `posts/` | entradas sin sección temática | 4 |
| `_quarto.yml`, `index.qmd`, `404.qmd`, `_contenido-inicio.qmd`, `_contenido-final.qmd` | configuración y portada propias del blog | |
| `assets/`, `_extensions/`, `_filters/`, `_partials/`, `scripts/` | tema propagado desde el hub (salvo `assets/img/`) | |
| `_site/` | sitio generado por `quarto render`; versionado mientras Netlify lo publique tal cual (D1) | |

5 entradas. Cada entrada es `<sección>/AAAA-MM-DD-slug/index.qmd` con frontmatter apaquarto y fecha ISO;
sus metadatos se editan en masa desde `scripts_quarto_studio` (`metadata_manager`).

## Documentación

Toda la familia se documenta una vez, en el hub: `04 index/README.md` (qué es la familia y cómo se opera),
`04 index/docs/pubs-submodulos.md` (submódulos y flujo de commit), `04 index/docs/publicar-un-post.md` (de
principio a fin), `04 index/docs/despliegue-netlify.md` (cómo publica cada sitio) y `assets/scss/README.md` (el tema).

## Límite honesto

- Este README es el único documento propio del blog y se regenera desde el hub: lo escrito aquí a mano se pierde.
- `_site/` sigue en git: Netlify publica _site/ empujado (sin build); D1 pendiente. 
- Licencia: código MPL-2.0 (`LICENSE`), contenido CC-BY-SA-4.0 según `license.qmd` del hub; unificarlas en los 12 sitios es la decisión D9.
