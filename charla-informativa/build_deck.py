"""
Ensambla la presentación completa (reveal.js):
  - escenas animadas renderizadas con Manim Slides (videos de fondo, con bucles)
  - diapositivas HTML fijas con el formato EAFIT

Uso:
    manim-slides render -qh maestria_ia.py Portada CicloIA Recorrido PlanEstudios
    python build_deck.py            # genera dist/index.html
"""
import html
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
REVEAL = "reveal"  # copia local de reveal.js 5.1.0 (funciona sin internet)

NAVY, CYAN = "#000066", "#009EE2"

# ---------------------------------------------------------------------------
# Piezas comunes
# ---------------------------------------------------------------------------
def band(label="Maestría en Inteligencia Artificial"):
    return f'<div class="band">{label}</div>'

LOGO = '<img class="logo" src="assets/logo_navy.svg" alt="Universidad EAFIT">'
LINEAS = '<img class="lineas" src="assets/lineas.png" alt="">'


def static(body, notes="", cls="", transition="fade", band_label="Maestría en Inteligencia Artificial",
           logo=True, lineas=True):
    chrome = band(band_label) if band_label else ""
    chrome += LOGO if logo else ""
    chrome += LINEAS if lineas else ""
    return (f'<section class="st {cls}" data-transition="{transition}">{chrome}{body}'
            f'<aside class="notes">{notes}</aside></section>')


def frag(i):
    return f'class="fragment fade-up" data-fragment-index="{i}"'


# ---------------------------------------------------------------------------
# Diapositivas fijas
# ---------------------------------------------------------------------------
CONTACTO = static("""
<div class="contact">
  <div class="person">
    <h3>Juan David Martínez Vargas, Ph.D.</h3>
    <p class="role">Jefe del programa</p>
    <p>Área de Computación y Analítica</p>
    <p>Escuela de Ciencias Aplicadas e Ingeniería</p>
  </div>
</div>""", notes="Presentación del equipo del programa.", band_label="", lineas=True)

CONTEXTO = static("""
<h2>La inteligencia artificial hoy</h2>
<div class="stats">
  <div class="stat" {f0}><span class="num">78 %</span><span class="lbl">de las organizaciones adoptó IA en 2024 <em>(55 % en 2023)</em></span></div>
  <div class="stat" {f1}><span class="num">40 %</span><span class="lbl">de los empleos se verá impactado por la IA</span></div>
  <div class="stat" {f2}><span class="num">70 %</span><span class="lbl">de los empleadores busca perfiles en datos e IA</span></div>
  <div class="stat hi" {f3}><span class="num">12 %</span><span class="lbl">de los profesionales TI tiene realmente las habilidades, aunque el 81 % cree que puede usar IA</span></div>
</div>
<div class="quote" {f4}>El mercado no demanda solo expertos técnicos: necesita <strong>líderes que integren la IA</strong> con criterio estratégico, ético y organizacional</div>
<p class="src">Fuentes: WEF, Future of Jobs Report 2025; estudio de mercado de la Dirección de Estrategia, EAFIT</p>
""".format(f0=frag(0), f1=frag(1), f2=frag(2), f3=frag(3), f4=frag(4)),
    notes="La adopción de IA es masiva, pero la brecha de habilidades es enorme: ahí está la oportunidad.",
    band_label="Contexto")

PREGUNTAS = static("""
<h2>Las preguntas que hoy surgen al trabajar con IA</h2>
<div class="qa">
  <div class="q" {q0}>¿Qué modelo uso?</div><div class="a" {a0}><span><strong>Aprendizaje automático:</strong> generalización, métricas, sesgo y varianza</span></div>
  <div class="q" {q1}>¿Cómo sé que funciona en mi caso?</div><div class="a" {a1}><span><strong>Estadística:</strong> diseño de evaluaciones, incertidumbre y comparación rigurosa</span></div>
  <div class="q" {q2}>¿Por qué falla y cómo lo mejoro?</div><div class="a" {a2}><span><strong>Aprendizaje profundo y optimización:</strong> entender el modelo para adaptarlo</span></div>
  <div class="q" {q3}>¿Cómo decide un agente qué hacer?</div><div class="a" {a3}><span><strong>Fundamentos de IA:</strong> búsqueda, planificación y razonamiento</span></div>
  <div class="q" {q4}>¿Qué pasó en cada etapa y cuánto costó?</div><div class="a" {a4}><span><strong>Operaciones en datos e IA:</strong> trazas, evaluaciones continuas y LLMOps</span></div>
</div>
<div class="quote center" {fz}>Usar IA es fácil. <strong>Hacerla confiable exige fundamentos.</strong></div>
""".format(**{f"q{i}": frag(2 * i) for i in range(5)}, **{f"a{i}": frag(2 * i + 1) for i in range(5)}, fz=frag(10)),
    notes="Cada pregunta la responde una base que enseñamos; las asignaturas aparecen luego en el plan de estudios. "
          "Si preguntan por el contexto: Colombia tiene una Política Nacional de IA (CONPES 4144) con la formación de talento como eje, "
          "y esta sería la primera maestría en IA de una universidad antioqueña.",
    band_label="Contexto", lineas=False)

EVOLUCION = static("""
<h2>Evolución del perfil en Inteligencia Artificial</h2>
<div class="evo">
  <div class="col">
    <div class="tag">FORMACIÓN BASE</div>
    <ul>
      <li>Programación en Python</li>
      <li>Matemáticas y estadística</li>
      <li>Análisis de datos</li>
      <li>Entrenamiento de modelos clásicos</li>
    </ul>
  </div>
  <div class="arrow">➜</div>
  <div class="col strong">
    <div class="tag">EVOLUCIÓN REQUERIDA</div>
    <ul>
      <li {f0}>Aprendizaje profundo, visión y PLN</li>
      <li {f1}>IA generativa y agentes</li>
      <li {f2}>Selección y adaptación de modelos fundacionales</li>
      <li {f3}>Evaluación rigurosa de modelos</li>
      <li {f4}>Operación con trazas, costos y observabilidad</li>
      <li {f5}>Ética, gobernanza y liderazgo de proyectos de IA</li>
    </ul>
  </div>
</div>
<div class="quote">El valor ya no está solo en entrenar modelos, sino en elegir, adaptar, evaluar y operar el adecuado</div>
""".format(**{f"f{i}": frag(i) for i in range(6)}),
    notes="El profesional en IA hoy decide qué modelo usar, lo adapta, lo evalúa y lo opera con trazabilidad, cada vez más en forma de agentes.")

PROFUNDIZACION = static("""
<h2>¿Qué es una maestría de profundización?</h2>
<div class="quote lead2">Busca el <strong>desarrollo avanzado de competencias</strong> para resolver problemas y analizar situaciones de carácter disciplinar, interdisciplinario o profesional</div>
<div class="pcards">
  <div class="pc" {f0}><span class="ic">1</span><h4>Saber hacer, con rigor</h4><p>Profundiza en los fundamentos y en el estado del arte para aplicarlos a problemas reales</p></div>
  <div class="pc" {f1}><span class="ic">2</span><h4>Trabajo de grado aplicado</h4><p>Un prototipo funcional, una solución o un modelo implementado</p></div>
  <div class="pc" {f2}><span class="ic">3</span><h4>Para quienes lideran</h4><p>Profesionales que quieren dirigir proyectos de IA en sus organizaciones</p></div>
</div>
""".format(f0=frag(0), f1=frag(1), f2=frag(2)),
    notes="", lineas=False)

GENERALIDADES = static("""
<h2>Generalidades de la maestría</h2>
<div class="cards6">
  <div class="card" {f0}><div class="h">Denominación</div><div class="b">Maestría en Inteligencia Artificial</div></div>
  <div class="card" {f0}><div class="h">Título a otorgar</div><div class="b">Magíster en Inteligencia Artificial</div></div>
  <div class="card" {f0}><div class="h">Modalidad</div><div class="b">Presencial</div></div>
  <div class="card" {f1}><div class="h">Duración</div><div class="b">3 semestres</div></div>
  <div class="card" {f1}><div class="h">Créditos</div><div class="b">36 créditos</div></div>
  <div class="card" {f1}><div class="h">Admisión</div><div class="b">Semestral</div></div>
</div>
<p class="foot">Inicio de clases: marzo de 2027 · Medellín</p>
""".format(f0=frag(0), f1=frag(1)),
    notes="Tres semestres, 36 créditos, modalidad presencial en Medellín.", lineas=False)

PORQUE = static("""
<h2>¿Por qué esta maestría?</h2>
<div class="quote lead">Formamos líderes capaces de <strong>diseñar, integrar y escalar sistemas de IA responsables</strong>, desde el modelo hasta el despliegue</div>
<div class="rows">
  <div class="row" {f0}><span class="ic">1</span><div><strong>Agentes de principio a fin:</strong> desde los agentes clásicos en Fundamentos de IA hasta agentes con LLM en producción</div></div>
  <div class="row" {f1}><span class="ic">2</span><div><strong>El ciclo de vida de la IA:</strong> seleccionar, adaptar, evaluar y observar modelos con MLOps y LLMOps</div></div>
  <div class="row" {f2}><span class="ic">3</span><div><strong>Rigor matemático aplicado:</strong> fundamentos sólidos y aprender haciendo con proyectos integradores</div></div>
  <div class="row" {f3}><span class="ic">4</span><div><strong>IA responsable:</strong> ética, integridad y gobernanza como eje transversal</div></div>
</div>
<p class="tagline" {f4}>No se trata solo de usar IA, sino de diseñar, evaluar y liderar soluciones completas</p>
""".format(**{f"f{i}": frag(i) for i in range(5)}),
    notes="Ya vimos el contexto y el ciclo de vida. Ahora, qué formación permite desarrollar estas capacidades.",
    lineas=False)

ELECTIVAS = static("""
<h2>Asignaturas electivas</h2>
<div class="quote lead2">Las electivas permiten orientar la formación según los intereses de cada estudiante. <strong>Se selecciona una por semestre.</strong></div>
<div class="groups g3">
  <div class="grp" {f0}><h4>Matemáticas y estadística</h4><ul><li>Estadística avanzada</li><li>Optimización</li><li>Métodos numéricos</li></ul></div>
  <div class="grp" {f1}><h4>Desarrollo de software</h4><ul><li>Computación en la nube</li><li>Desarrollo de software para IA</li></ul></div>
  <div class="grp" {f2}><h4>Procesamiento y visualización de datos</h4><ul><li>Visualización de datos</li><li>Almacenamiento y procesamiento de grandes datos</li></ul></div>
</div>
<p class="foot2">Las electivas se abren según la cantidad de estudiantes inscritos</p>
""".format(**{f"f{i}": frag(i) for i in range(3)}),
    notes="", lineas=False)

DIFERENCIALES = static("""
<h2>Diferenciales del programa</h2>
<div class="dsplit">
  <ul class="diff2">
    <li {f0}><strong>Trayectoria académica:</strong> articulación con el Sistema Metro, desde la línea de énfasis en pregrado hasta el doctorado</li>
    <li {f1}><strong>Currículo flexible:</strong> una electiva por semestre y Formación en integridad</li>
    <li {f2}><strong>Aprendizaje práctico:</strong> proyectos integradores en el primer y el segundo semestre</li>
    <li {f3}><strong>Docentes:</strong> con doctorado y de la industria</li>
    <li {f4}><strong>IA actual:</strong> agentes, evaluaciones y LLMOps integrados al plan de estudios</li>
  </ul>
  <div class="acts-box" {f5}>
    <h4>Actividades</h4>
    <ul>
      <li>Charlas con expertos de la industria</li>
      <li>Retos y competencias de IA</li>
      <li>Proyectos con empresas, ONG y entidades públicas</li>
      <li>Seminarios sobre tendencias en IA</li>
    </ul>
  </div>
</div>
<div class="quote dq" {f6}>La primera maestría en IA de una universidad antioqueña, presencial en Medellín</div>
""".format(**{f"f{i}": frag(i) for i in range(7)}),
    notes="Lo que nos diferencia.", lineas=False)

PERFILES = static("""
<h2>Perfiles del programa</h2>
<div class="profiles">
  <div class="pf" {f0}><h4>Perfil de ingreso</h4>
    <p>Profesional de ciencias, ingenierías, finanzas, administración, economía o áreas afines, con conocimientos en matemáticas, estadística y computación, interesado en <strong>liderar</strong> el desarrollo de productos y servicios innovadores basados en IA.</p>
    <div class="pill">Base cuantitativa</div></div>
  <div class="pf" {f1}><h4>Perfil de egreso</h4>
    <p>Diseña soluciones a problemas complejos de diversos sectores mediante la construcción, optimización y evaluación crítica de modelos de IA, y lidera proyectos de desarrollo tecnológico con sostenibilidad, rigor científico y responsabilidad ética.</p>
    <div class="pill">Capacidad de diseñar soluciones de IA</div></div>
  <div class="pf" {f2}><h4>Perfil ocupacional</h4>
    <p>Gestor de proyectos de IA, arquitecto o ingeniero de soluciones de IA y consultor estratégico en IA, en la industria, el sector público y organizaciones de distintos sectores.</p>
    <div class="pill">Roles en la industria</div></div>
</div>
""".format(**{f"f{i}": frag(i) for i in range(3)}),
    notes="Dirigido a profesionales con base cuantitativa que quieren liderar soluciones de IA.", lineas=False)

TRABAJO = static("""
<h2>Trabajo de grado</h2>
<p class="tlead">Es el cierre del programa: el resultado esperado es <strong>saber hacer</strong>, con un prototipo, una solución o un modelo implementado</p>
<div class="mods4">
  <div class="mod" {f0}><span class="ic">1</span><strong>Proyecto aplicado</strong><span>Solución a un problema con dominio del estado del arte</span></div>
  <div class="mod" {f0}><span class="ic">2</span><strong>Artículo en revista indexada</strong><span>En coautoría con el director</span></div>
  <div class="mod" {f0}><span class="ic">3</span><strong>Caso de estudio aplicado</strong><span>Problema real o hipotético con datos y método analítico</span></div>
  <div class="mod" {f0}><span class="ic">4</span><strong>Pasantía</strong><span>En un grupo de investigación, de 3 a 6 meses</span></div>
</div>
""".format(f0=frag(0)),
    notes="El trabajo de grado es el cierre del programa.", lineas=False)

HORARIOS = static("""
<h2>Horarios</h2>
<ul class="diff tight">
  <li>Clases en horarios compatibles con la vida laboral</li>
  <li><strong>Inicio de clases:</strong> primer fin de semana de marzo de 2027</li>
  <li><strong>Entre semana:</strong> a partir de las 5:00 o 6:00 p. m.</li>
  <li><strong>Sábados:</strong> en la mañana</li>
</ul>
<div class="weeks">
  <div class="wk-lbl">Una asignatura obligatoria = 3 fines de semana</div>
  <div class="wk-row">
    <div class="wk fragment fade-right" data-fragment-index="0"><span>Fin de semana 1</span><b>Vie · Sáb</b></div>
    <div class="wk fragment fade-right" data-fragment-index="1"><span>Fin de semana 2</span><b>Vie · Sáb</b></div>
    <div class="wk fragment fade-right" data-fragment-index="2"><span>Fin de semana 3</span><b>Vie · Sáb</b></div>
    <div class="wk next fragment fade-right" data-fragment-index="3"><span>Siguiente asignatura</span><b>→</b></div>
  </div>
</div>
""", notes="Pensado para profesionales que trabajan.")

GRACIAS = (f'<section class="st gracias" data-transition="zoom">'
           f'<img class="photo" src="assets/campus.jpg" alt="Campus EAFIT">{LINEAS}'
           f'<div class="thanks"><h1>¡Gracias!</h1><p>Maestría en Inteligencia Artificial</p>'
           f'<p class="small">Universidad EAFIT · Medellín</p></div>'
           f'<aside class="notes">Cierre e invitación a preguntas.</aside></section>')

# ---------------------------------------------------------------------------
# Orden de la presentación
# ---------------------------------------------------------------------------
ORDER = [
    ("scene", "Portada", None),
    ("html", "CONTACTO", CONTACTO),
    ("scene", "DosEpocas", None),
    ("html", "PREGUNTAS", PREGUNTAS),
    ("scene", "CicloIA", None),
    ("html", "EVOLUCION", EVOLUCION),
    ("html", "PROFUNDIZACION", PROFUNDIZACION),
    ("html", "GENERALIDADES", GENERALIDADES),
    ("html", "PORQUE", PORQUE),
    ("scene", "Recorrido", None),
    ("scene", "PlanEstudios", None),
    ("html", "ELECTIVAS", ELECTIVAS),
    ("html", "DIFERENCIALES", DIFERENCIALES),
    ("html", "PERFILES", PERFILES),
    ("html", "TRABAJO", TRABAJO),
    ("html", "HORARIOS", HORARIOS),
    ("html", "GRACIAS", GRACIAS),
]



# ---------------------------------------------------------------------------
# Guion: notas del presentador desde guion.md
# ---------------------------------------------------------------------------
def load_guion(path=ROOT / "guion.md"):
    """Bloques '## CLAVE' -> HTML de notas. Claves: nombre de diapositiva fija o Escena.N."""
    if not path.exists():
        return {}
    blocks, key, buf = {}, None, []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^##\s+(\S+)\s*$", line)
        if m:
            if key:
                blocks[key] = buf
            key, buf = m.group(1), []
        elif key:
            buf.append(line)
    if key:
        blocks[key] = buf

    def to_html(lines):
        paras = [p.strip() for p in "\n".join(lines).split("\n\n") if p.strip()]
        out = []
        for p in paras:
            p = html.escape(p.replace("\n", " "), quote=False)
            p = re.sub(r"\*\((.+?)\)\*", r'<em class="cue">(\1)</em>', p)
            p = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", p)
            p = p.replace("[clic]", '<b class="clic">[clic]</b>')
            out.append(f"<p>{p}</p>")
        return "".join(out)

    return {k: to_html(v) for k, v in blocks.items()}


def with_notes(section_html, notes_html):
    if not notes_html:
        return section_html
    aside = f'<aside class="notes">{notes_html}</aside>'
    if '<aside class="notes">' in section_html:
        return re.sub(r'<aside class="notes">.*?</aside>', lambda m: aside, section_html, flags=re.S)
    return section_html.replace("</section>", aside + "</section>", 1)


def scene_sections(name, guion=None):
    jf = ROOT / "slides" / f"{name}.json"
    if not jf.exists() or not all((ROOT / x["file"]).exists() for x in json.loads(jf.read_text())["slides"]):
        print("  (falta la escena", name, ")")
        return [f'<section class="st"><h2>[{name}]</h2></section>']
    cfg = json.loads((ROOT / "slides" / f"{name}.json").read_text())
    bg = cfg.get("background_color", "#ffffff")
    out = []
    for i, s in enumerate(cfg["slides"]):
        src = ROOT / s["file"]
        dst = DIST / "videos" / f"{name}_{i:02d}.mp4"
        shutil.copy(src, dst)
        attrs = [f'data-background-video="videos/{dst.name}"', "data-background-video-muted",
                 'data-background-size="contain"', f'data-background-color="{bg}"']
        if s["loop"]:
            attrs.append("data-background-video-loop")
        # continuidad dentro de la escena: sin transición
        if i > 0:
            attrs += ['data-transition="none"', 'data-background-transition="none"']
        else:
            attrs += ['data-transition="fade"', 'data-background-transition="fade"']
        txt = (guion or {}).get(f"{name}.{i}") or s["notes"]
        notes = f'<aside class="notes">{txt}</aside>' if txt else ""
        out.append(f'<section class="mv" {" ".join(attrs)}>{notes}</section>')
    return out


CSS = (ROOT / "deck.css").read_text()


def build():
    if DIST.exists():
        shutil.rmtree(DIST)
    (DIST / "videos").mkdir(parents=True)
    shutil.copytree(ROOT / "assets", DIST / "assets")
    (DIST / "reveal").mkdir()
    shutil.copy(ROOT / "vendor/reveal/dist/reveal.css", DIST / "reveal/reveal.css")
    shutil.copy(ROOT / "vendor/reveal/dist/reveal.js", DIST / "reveal/reveal.js")
    # Vista del presentador: el guion ocupa la mayor parte de la ventana
    notes_js = (ROOT / "vendor/reveal/plugin/notes/notes.js").read_text(encoding="utf-8")
    speaker_css = (
        "<style>"
        "body[data-speaker-layout=\\\"default\\\"] #current-slide{width:36%!important;height:40%!important;left:0!important;top:0!important;}"
        "body[data-speaker-layout=\\\"default\\\"] #upcoming-slide{width:36%!important;height:36%!important;left:0!important;top:42%!important;}"
        "body[data-speaker-layout=\\\"default\\\"] #speaker-controls{left:36%!important;top:0!important;width:64%!important;height:100%!important;font-size:16px!important;}"
        ".speaker-controls-notes{font-size:23px!important;line-height:1.5!important;}"
        ".speaker-controls-notes .value p{margin:0 0 14px;}"
        ".speaker-controls-notes .clic{color:#009EE2;}"
        ".speaker-controls-notes .cue{color:#8a8a8a;font-size:.85em;}"
        ".speaker-controls-notes .num{color:#000066;font-size:.8em;}"
        "#speaker-layout{top:auto!important;bottom:8px!important;right:auto!important;left:8px!important;}"
        "</style>"
    )
    assert "</style>\\n\\t</head>" in notes_js, "plantilla de notas inesperada"
    notes_js = notes_js.replace("</style>\\n\\t</head>", "</style>" + speaker_css + "\\n\\t</head>", 1)
    (DIST / "reveal/notes.js").write_text(notes_js, encoding="utf-8")
    sections = []
    guion = load_guion()
    total = len(ORDER)
    for k, (kind, key, v) in enumerate(ORDER, start=1):
        # número lógico: una escena animada cuenta como una diapositiva aunque tenga varios pasos
        g = {kk: f'<p class="num"><b>Diapositiva {k} de {total}</b></p>' + vv for kk, vv in guion.items()
             if kk == key or kk.startswith(key + ".")}
        secs = scene_sections(key, g) if kind == "scene" else [with_notes(v, g.get(key))]
        sections += [x.replace("<section ", f'<section data-num="{k}" ', 1) for x in secs]
    html = f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Maestría en IA EAFIT</title>
<link rel="stylesheet" href="{REVEAL}/reveal.css">
<style>{CSS}</style></head>
<body><div class="reveal"><div class="slides">
{chr(10).join(sections)}
</div></div>
<div id="num-dia" aria-live="polite"></div>
<div id="guion-btns"><button type="button" id="btn-guion" title="Mostrar u ocultar el guion (tecla N)">Guion</button><button type="button" id="btn-presentador" title="Vista del presentador en otra ventana (tecla S)">Presentador</button></div>
<script src="{REVEAL}/reveal.js"></script>
<script src="{REVEAL}/notes.js"></script>
<script>
Reveal.initialize({{width:1280,height:720,margin:0,minScale:0.2,maxScale:2,center:false,hash:true,
  controls:true,progress:true,slideNumber:false,transition:'fade',backgroundTransition:'fade',
  plugins:[RevealNotes],
  // N: muestra u oculta el guion dentro de la misma ventana (útil para ensayar con una sola pantalla)
  keyboard:{{78:function(){{toggleGuion();}}}}}});
function toggleGuion(){{Reveal.configure({{showNotes:!Reveal.getConfig().showNotes}});document.getElementById('btn-guion').classList.toggle('on',Reveal.getConfig().showNotes);setTimeout(function(){{Reveal.layout();}},50);setTimeout(function(){{Reveal.layout();}},400);}}
document.getElementById('btn-guion').onclick=toggleGuion;
if(window.self!==window.top){{document.getElementById('guion-btns').style.display='none';}}
function numDia(){{var s=Reveal.getCurrentSlide();var n=s&&s.getAttribute('data-num');
  document.getElementById('num-dia').textContent=(n&&n!=='1')?(n+' / {total}'):'';}}
Reveal.on('ready',numDia);Reveal.on('slidechanged',numDia);
document.getElementById('btn-presentador').onclick=function(){{var n=Reveal.getPlugin('notes');if(n)n.open();}};
</script></body></html>"""
    (DIST / "index.html").write_text(html, encoding="utf-8")
    print("OK ->", DIST / "index.html", "|", len(sections), "secciones")


if __name__ == "__main__":
    build()
