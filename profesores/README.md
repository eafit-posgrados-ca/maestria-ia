# Profesores de la Maestría en Inteligencia Artificial

El archivo [profesores.json](profesores.json) es el catálogo de perfiles académicos de la maestría. Se mantiene desde el repositorio y puede servir como fuente para un directorio en la web.

## Ficha de un profesor

Cada entrada representa a una persona. Usa un identificador único en minúsculas, con guiones y sin tildes. Conserva el mismo identificador aunque cambie su vinculación.

| Campo | Contenido |
| --- | --- |
| `id` | Identificador estable, por ejemplo `ana-ejemplo`. |
| `nombre` | Nombre completo para mostrar en el directorio. |
| `vinculacion` | `planta` o `catedra`. Usa `null` mientras se confirma la vinculación con la maestría. |
| `areas` | Lista opcional de áreas de docencia o investigación. |
| `biografia` | Reseña académica breve y opcional. |
| `perfil_url` | Enlace HTTPS opcional a un perfil institucional o académico público. |

Los campos `id`, `nombre` y `vinculacion` son obligatorios. Este ejemplo ficticio muestra una entrada dentro de la lista:

```json
[
  {
    "id": "ana-ejemplo",
    "nombre": "Ana Ejemplo",
    "vinculacion": "catedra",
    "areas": ["Aprendizaje automático", "Visión por computador"],
    "biografia": "Docente e investigadora en aplicaciones de visión por computador."
  }
]
```

Para incorporar un perfil, agrega su ficha a la lista y revisa el cambio en Git. Puedes verificar la sintaxis desde esta carpeta con `python3 -m json.tool profesores.json`. Si una persona pasa de cátedra a planta, actualiza `vinculacion` en su ficha. Git conserva el historial del cambio.

## Directorio web y hojas de vida

La [presentación existente](../charla-informativa/README.md) genera un sitio estático en `charla-informativa/dist/`. Si ese es el contenido que se publica, el directorio puede añadirse como una página `profesores/index.html` dentro de esa salida. El ensamblado exportaría los perfiles aprobados para publicación cuya vinculación esté confirmada y la presentación enlazaría al directorio. La página podría filtrar por planta y cátedra a partir de `vinculacion`.

Usa el catálogo para información académica apta para publicación. Las hojas de vida completas se guardan localmente en `cvs/`, que está excluida de Git. Para compartir esos documentos con el equipo, usa un espacio institucional con acceso restringido.
