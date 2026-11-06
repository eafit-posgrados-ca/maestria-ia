# Presentación · Maestría en Inteligencia Artificial (EAFIT)

Presentación híbrida: escenas animadas con **Manim Slides** + diapositivas **HTML fijas** con el formato EAFIT, ensambladas en **reveal.js** (incluido localmente, funciona sin internet).

## Estructura

| Archivo | Qué es |
|---|---|
| `maestria_ia.py` | Escenas animadas: `Portada`, `CicloIA`, `Recorrido` (fundamentos → aplicaciones avanzadas y agentes → despliegue), `PlanEstudios` |
| `build_deck.py` | Diapositivas HTML fijas, orden de la presentación y ensamblado final |
| `guion.md` | Discurso de la charla; se muestra en la vista del presentador |
| `deck.css` | Estilo (colores y tipografía de la plantilla EAFIT) |
| `assets/` | Logo, líneas decorativas y foto del campus tomados de la plantilla |
| `vendor/reveal/` | reveal.js 5.1.0 |
| `dist/` | Presentación lista: abrir `dist/index.html` |

## Requisitos

```bash
pip install "manim==0.19.0" manim-slides   # manim 0.22 aún no es compatible con manim-slides 5.7
# Linux: sudo apt install libpango1.0-dev libcairo2-dev ffmpeg
```

## Render y ensamblado

```bash
manim-slides render -qm maestria_ia.py Portada DosEpocas CicloIA ElegirModelo Recorrido PlanEstudios   # 720p30 (-qh para 1080p60)
python build_deck.py
# servir la carpeta (los videos no cargan bien con file:// en algunos navegadores)
cd dist && python -m http.server 8000   # abrir http://localhost:8000
```

Solo las escenas animadas, con el presentador nativo de Manim Slides:

```bash
manim-slides present Portada DosEpocas CicloIA ElegirModelo Recorrido PlanEstudios
```

## Guion (discurso)

El discurso completo está en `guion.md`, un bloque `## CLAVE` por cada paso de la presentación, con marcas `[clic]` donde hay que avanzar.
`build_deck.py` lo inserta como notas del presentador, así que se ve con la tecla `S`.
Para cambiarlo: editar `guion.md` y ejecutar `python build_deck.py && python build_onefile.py` (no hay que volver a renderizar las animaciones).

## Durante la presentación

- `→` / `espacio`: siguiente paso (las diapositivas fijas revelan sus elementos en orden).
- `S`: vista del presentador con notas.
- `F`: pantalla completa.
- Las diapositivas en bucle (señales en la red, el agente usando herramientas, el ciclo agente–entorno) se repiten hasta avanzar.

## Editar

- Texto de las diapositivas fijas: constantes `CONTACTO`, `CONTEXTO`, … en `build_deck.py`.
- Orden: lista `ORDER` en `build_deck.py`.
- Animaciones: cada `self.next_slide()` en `maestria_ia.py` marca una pausa; `loop=True` la vuelve bucle.
