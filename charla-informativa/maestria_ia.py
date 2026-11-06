"""
Maestría en Inteligencia Artificial — EAFIT
Escenas animadas (Manim Community + Manim Slides).

Render:
    manim-slides render -qh maestria_ia.py Portada DosEpocas CicloIA Recorrido PlanEstudios
Presentar solo las animadas:
    manim-slides present Portada DosEpocas CicloIA Recorrido PlanEstudios
Construir la presentación completa (animadas + HTML fijas):
    python build_deck.py
"""
from manim import *
from manim_slides import Slide as _Slide


class Slide(_Slide):
    skip_reversing = True  # no se usan videos en reversa (acelera el render)

# ---------- Identidad visual (tomada de la plantilla EAFIT) ----------
NAVY = "#000066"
CYAN = "#009EE2"
LIGHT = "#76D6FF"
PALE = "#E5F5FC"
GRAY = "#A6A6A6"
SOFT = "#EFEFEF"
INK = "#1A2431"
FONT = "Liberation Sans"  # métrica idéntica a Arial

config.background_color = WHITE


def T(s, size=24, color=INK, bold=False, italic=False, **kw):
    return Text(
        s, font=FONT, font_size=size, color=color,
        weight=BOLD if bold else NORMAL,
        slant=ITALIC if italic else NORMAL, **kw,
    )


def fit(mob, max_w):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


def band(label="Maestría en Inteligencia Artificial"):
    """Franja cian superior izquierda, como en la plantilla."""
    rect = Rectangle(width=8.7, height=0.5, fill_color=CYAN, fill_opacity=1, stroke_width=0)
    rect.to_corner(UL, buff=0)
    txt = T(label, 18, WHITE, bold=True).move_to(rect).align_to(rect, LEFT).shift(RIGHT * 0.25)
    return VGroup(rect, txt)


def logo(white=False, width=1.55):
    path = "assets/logo_white.svg" if white else "assets/logo_navy.svg"
    m = SVGMobject(path).scale_to_fit_width(width).to_corner(UR, buff=0.45)
    return m.set_stroke(width=0).set_fill(WHITE if white else NAVY, opacity=1)


def lineas(height=2.6):
    img = ImageMobject("assets/lineas.png").scale_to_fit_height(height)
    img.to_corner(DR, buff=0).shift(DOWN * 0.35 + RIGHT * 0.2)
    return img


def title(s):
    return fit(T(s, 38, INK, bold=True), 10.4).to_corner(UL, buff=0.6).shift(DOWN * 0.35)


def chip(s, w=5.6, h=0.62, fill=PALE, color=NAVY, size=19, bold=False):
    box = RoundedRectangle(width=w, height=h, corner_radius=0.12,
                           fill_color=fill, fill_opacity=1, stroke_width=0)
    t = fit(T(s, size, color, bold=bold), w - 0.4).move_to(box).align_to(box, LEFT).shift(RIGHT * 0.2)
    return VGroup(box, t)


def network(layers, x_gap=1.3, y_gap=0.62, r=0.13, node_color=LIGHT, edge_color=LIGHT, edge_op=0.35):
    cols = []
    for i, n in enumerate(layers):
        col = VGroup(*[Circle(radius=r, fill_color=node_color, fill_opacity=1, stroke_width=0)
                       for _ in range(n)]).arrange(DOWN, buff=y_gap - 2 * r)
        col.move_to(RIGHT * i * x_gap)
        cols.append(col)
    nodes = VGroup(*cols)
    edges = VGroup()
    for a, b in zip(cols[:-1], cols[1:]):
        for u in a:
            for v in b:
                edges.add(Line(u.get_center(), v.get_center(), stroke_width=1.6,
                               color=edge_color, stroke_opacity=edge_op))
    return VGroup(edges, nodes)


# =====================================================================
class Portada(Slide):
    def construct(self):
        self.camera.background_color = ManimColor(NAVY)
        net = network([3, 5, 5, 4, 2], x_gap=1.0, y_gap=0.66).move_to(RIGHT * 4.85 + DOWN * 0.2)
        edges, nodes = net
        t1 = T("Maestría en", 54, WHITE, bold=True)
        t2 = T("Inteligencia Artificial", 54, WHITE, bold=True)
        ttl = VGroup(t1, t2).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(LEFT, buff=1.1).shift(UP * 1.25)
        sub = VGroup(
            T("La Inteligencia Artificial se ha convertido", 22, LIGHT, italic=True),
            T("en un estándar para la transformación", 22, LIGHT, italic=True),
            T("de las organizaciones", 22, LIGHT, italic=True),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        frame = SurroundingRectangle(sub, color=LIGHT, stroke_width=1.2, buff=0.22, corner_radius=0.04)
        subg = VGroup(frame, sub).next_to(ttl, DOWN, buff=0.7, aligned_edge=LEFT)
        year = T("2026", 22, WHITE).to_corner(DR, buff=0.5)
        lg = logo(white=True)

        self.play(LaggedStart(*[GrowFromCenter(n) for n in nodes.family_members_with_points()],
                              lag_ratio=0.03), run_time=1.4)
        self.play(Create(edges, lag_ratio=0.01), run_time=1.4)
        self.play(Write(ttl), run_time=1.6)
        self.play(FadeIn(subg, shift=UP * 0.2), FadeIn(year), FadeIn(lg), run_time=1)

        self.next_slide(loop=True, notes="Bienvenida. La IA ya no es una promesa: es un estándar corporativo.")
        # Señales que recorren la red (bucle)
        flashes = [ShowPassingFlash(e.copy().set_stroke(WHITE, 3.5, opacity=1), time_width=0.6)
                   for e in edges[::3]]
        self.play(LaggedStart(*flashes, lag_ratio=0.02), run_time=2.4)
        self.play(*[Indicate(n, color=WHITE, scale_factor=1.25) for n in nodes[-1]], run_time=0.8)


# =====================================================================
class DosEpocas(Slide):
    """Las herramientas cambian, los fundamentos no: dos flujos sobre una misma base."""

    def construct(self):
        chrome = Group(band("Contexto"), logo())
        ttl = title("Las herramientas cambian, los fundamentos no")
        sub = T("Un mismo problema: clasificar y responder las solicitudes que recibe una empresa", 20, CYAN, bold=True)
        fit(sub, 12.4).next_to(ttl, DOWN, aligned_edge=LEFT, buff=0.22)
        self.add(chrome)
        self.play(FadeIn(ttl, shift=RIGHT * 0.3), FadeIn(sub, shift=RIGHT * 0.3))

        top, bottom = 1.1, -2.15

        def column(items, x, w, fill, txt_color, header, hcolor):
            boxes = VGroup()
            for s in items:
                b = RoundedRectangle(width=w, height=0.48, corner_radius=0.12, fill_color=fill,
                                     fill_opacity=1, stroke_width=0)
                t = fit(T(s, 17, txt_color, bold=True), w - 0.3).move_to(b)
                boxes.add(VGroup(b, t))
            n = len(items)
            ys = np.linspace(top - 0.24, bottom + 0.24, n)
            for b, yy in zip(boxes, ys):
                b.move_to([x, yy, 0])
            arrs = VGroup()
            for i in range(n - 1):
                tri = Triangle(fill_color=hcolor, fill_opacity=1, stroke_width=0).rotate(PI)
                tri.stretch_to_fit_width(0.24).stretch_to_fit_height(0.13)
                tri.move_to((boxes[i].get_bottom() + boxes[i + 1].get_top()) / 2)
                arrs.add(tri)
            head = T(header, 22, hcolor, bold=True).move_to([x, top + 0.42, 0])
            return head, boxes, arrs

        h1, b1, a1 = column(["Etiquetar miles de ejemplos", "Entrenar un modelo propio", "Desplegar"],
                            -3.55, 4.6, SOFT, INK, "Antes", GRAY)
        h2, b2, a2 = column(["Elegir un modelo fundacional", "Adaptar: prompts, RAG o fine-tuning",
                             "Construir un agente con herramientas", "Evaluar en casos propios",
                             "Observar con trazas en producción"],
                            3.0, 5.4, CYAN, WHITE, "Hoy", CYAN)

        self.play(FadeIn(h1, shift=DOWN * 0.2))
        for i, b in enumerate(b1):
            self.play(FadeIn(b, shift=DOWN * 0.15), run_time=0.4)
            if i < len(a1):
                self.play(FadeIn(a1[i], shift=DOWN * 0.1), run_time=0.25)
        self.next_slide(notes="Hace unos años resolver este problema era etiquetar datos y entrenar un modelo propio.")
        self.play(FadeIn(h2, shift=DOWN * 0.2))
        for i, b in enumerate(b2):
            self.play(FadeIn(b, shift=DOWN * 0.15), run_time=0.4)
            if i < len(a2):
                self.play(FadeIn(a2[i], shift=DOWN * 0.1), run_time=0.25)
        self.next_slide(notes="Hoy el flujo es otro: se elige un modelo, se adapta, se construye un agente, se evalúa y se observa.")

        # --- La misma base ---
        pillars_txt = ["Matemáticas", "Estadística", "Aprendizaje\nautomático", "Aprendizaje\nprofundo",
                       "Agentes, búsqueda\ny planificación"]
        pillars = VGroup()
        for s in pillars_txt:
            b = RoundedRectangle(width=2.42, height=0.9, corner_radius=0.1, fill_color=NAVY, fill_opacity=1, stroke_width=0)
            t = VGroup(*[T(l, 16, WHITE, bold=True) for l in s.split("\n")]).arrange(DOWN, buff=0.04)
            fit(t, 2.2).move_to(b)
            pillars.add(VGroup(b, t))
        pillars.arrange(RIGHT, buff=0.13).move_to([0, -3.15, 0])
        base_lbl = T("La misma base", 15, NAVY, bold=True).next_to(pillars, LEFT, buff=0).align_to(pillars, LEFT)
        base_lbl.next_to(pillars, UP, buff=0.06, aligned_edge=LEFT)
        self.play(LaggedStart(*[GrowFromEdge(p, DOWN) for p in pillars], lag_ratio=0.12), run_time=1.2)
        self.play(FadeIn(base_lbl))
        # ambas columnas "se apoyan": un leve asentamiento sobre la base
        self.play(VGroup(h1, b1, a1, h2, b2, a2).animate.shift(DOWN * 0.08), rate_func=there_and_back, run_time=0.6)
        self.next_slide(notes="Los dos flujos se apoyan en lo mismo. Elegir, adaptar y evaluar modelos exige más fundamentos, no menos.")
        for p in pillars:
            self.play(Indicate(p, color=CYAN, scale_factor=1.06), run_time=0.35)


# =====================================================================
def cycle_arrows(center, rx, ry, angles, gap=19):
    arrows = VGroup()
    n = len(angles)
    for i in range(n):
        a0, a1 = np.radians(angles[i] - gap), np.radians(angles[(i + 1) % n] + gap)
        if a1 > a0:
            a1 -= 2 * np.pi
        pts = [center + np.array([rx * np.cos(t), ry * np.sin(t), 0]) for t in np.linspace(a0, a1, 20)]
        arc = TipableVMobject(stroke_color=NAVY, stroke_width=3)
        arc.set_points_smoothly(pts)
        arc.add_tip(tip_length=0.16, tip_width=0.14)
        arrows.add(arc)
    return arrows


def ring_arrows(center, rx, ry, angles_deg, w, h, margin=0.14, color=NAVY):
    """Flechas que siguen la elipse del ciclo (sentido horario), de borde a borde de cada nodo,
    con la punta tangente a la curva."""
    def P(t):
        return center + np.array([rx * np.cos(t), ry * np.sin(t), 0])

    def inside(pt, c):
        return abs(pt[0] - c[0]) <= w / 2 + margin and abs(pt[1] - c[1]) <= h / 2 + margin

    arrows = VGroup()
    th = [np.radians(a) for a in angles_deg]
    n = len(th)
    for i in range(n):
        t0, t1 = th[i], th[(i + 1) % n]
        if t1 > t0:
            t1 -= 2 * np.pi
        c0, c1 = P(t0), P(t1)
        ts = np.linspace(t0, t1, 400)
        a = next(t for t in ts if not inside(P(t), c0))
        b = next(t for t in ts[::-1] if not inside(P(t), c1))
        pts = [P(t) for t in np.linspace(a, b, 40)]
        tip_len = 0.2
        # recortar la curva para dejar espacio a la punta
        end = pts[-1]
        tangent = (pts[-1] - pts[-3]) / np.linalg.norm(pts[-1] - pts[-3])
        body = VMobject(stroke_color=color, stroke_width=3)
        body.set_points_smoothly(pts[:-1] + [end - tangent * tip_len * 0.8])
        tri = Triangle(fill_color=color, fill_opacity=1, stroke_width=0).scale_to_fit_height(tip_len)
        tri.stretch_to_fit_width(tip_len * 0.85)
        tri.rotate(np.arctan2(tangent[1], tangent[0]) - PI / 2)
        tri.move_to(end - tangent * tip_len / 3)
        arrows.add(VGroup(body, tri))
    return arrows


def edge_point(c, d, w, h, margin=0.08):
    """Punto donde la dirección d sale de una caja de w x h centrada en c."""
    d = d / np.linalg.norm(d)
    t = min((w / 2) / abs(d[0]) if abs(d[0]) > 1e-6 else 1e9, (h / 2) / abs(d[1]) if abs(d[1]) > 1e-6 else 1e9)
    return c + d * (t + margin)


def node_arrows(nodes, w, h, bend=-0.45):
    """Flechas curvas entre nodos consecutivos (sentido horario), de borde a borde."""
    arrows = VGroup()
    n = len(nodes)
    for i in range(n):
        a, b = nodes[i].get_center(), nodes[(i + 1) % n].get_center()
        d = b - a
        start, end = edge_point(a, d, w, h), edge_point(b, -d, w, h)
        arrows.add(CurvedArrow(start, end, angle=bend, color=NAVY, stroke_width=3, tip_length=0.16))
    return arrows


class CicloIA(Slide):
    """Ciclo de vida actual: se elige, adapta, evalúa y observa; no siempre se entrena."""

    def construct(self):
        chrome = Group(band(), logo())
        ttl = title("Hacer IA hoy va más allá de entrenar modelos")
        sub = T("Muchas veces no se entrena: se elige, se adapta, se evalúa y se observa", 22, CYAN, bold=True)
        sub.next_to(ttl, DOWN, aligned_edge=LEFT, buff=0.25)

        left = VGroup(
            T("Construir soluciones de IA", 23, INK, bold=True),
            T("es entender el problema,", 23),
            T("elegir o construir el modelo", 23),
            T("adecuado, evaluarlo con rigor", 23),
            T("y operarlo con trazabilidad", 23),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.13).to_edge(LEFT, buff=0.85).shift(DOWN * 0.1)
        foot = VGroup(T("Operación de la IA", 21, INK),
                      T("MLOps · LLMOps · AgentOps", 21, CYAN, bold=True)).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        foot.next_to(left, DOWN, buff=0.6, aligned_edge=LEFT)

        center = np.array([3.25, -0.75, 0])
        rx, ry = 2.85, 2.45
        NW, NH = 1.95, 0.8
        names = ["Definición\ndel problema", "Datos y\ncontexto", "Selección\ndel modelo",
                 "Adaptación\no entrenamiento", "Evaluaciones\n(evals)", "Despliegue", "Trazas y\nobservabilidad"]
        angles = [90 + 180 / 7 - k * 360 / 7 for k in range(7)]  # par simétrico arriba
        nodes = VGroup()
        for k, (n, a) in enumerate(zip(names, angles)):
            p = center + np.array([rx * np.cos(np.radians(a)), ry * np.sin(np.radians(a)), 0])
            col = NAVY if k in (2, 4, 6) else CYAN  # lo que cambió en el panorama actual
            e = RoundedRectangle(width=NW, height=NH, corner_radius=0.4, fill_color=col,
                                 fill_opacity=1, stroke_width=0).move_to(p)
            t = VGroup(*[T(l, 15, WHITE, bold=True) for l in n.split("\n")]).arrange(DOWN, buff=0.04).move_to(p)
            fit(t, NW - 0.2)
            nodes.add(VGroup(e, t))
        arrows = ring_arrows(center, rx, ry, angles, NW, NH)
        hub = VGroup(T("Ciclo de vida", 21, NAVY, bold=True), T("de la IA", 21, NAVY, bold=True)).arrange(DOWN, buff=0.08).move_to(center)

        leg = VGroup(
            VGroup(Square(0.2, fill_color=NAVY, fill_opacity=1, stroke_width=0), T("Énfasis del panorama actual", 15, INK)).arrange(RIGHT, buff=0.1),
        ).next_to(foot, DOWN, buff=0.45, aligned_edge=LEFT)

        self.add(chrome)
        self.play(FadeIn(ttl, shift=RIGHT * 0.3), FadeIn(sub, shift=RIGHT * 0.3))
        self.play(FadeIn(left, shift=UP * 0.2), run_time=0.8)
        self.next_slide(notes="El ciclo actual: muchas veces no entrenamos, elegimos un modelo fundacional, lo adaptamos, lo evaluamos y lo observamos en producción.")
        self.play(FadeIn(hub, scale=0.8))
        for i in range(7):
            self.play(GrowFromCenter(nodes[i]), run_time=0.4)
            self.play(Create(arrows[i]), run_time=0.3)
        self.play(FadeIn(foot, shift=UP * 0.2), FadeIn(leg))
        self.next_slide(loop=True)
        t_start = np.radians(angles[0])
        ts = np.linspace(t_start, t_start - 2 * np.pi, 120)
        path = VMobject().set_points_smoothly([center + np.array([rx * np.cos(t), ry * np.sin(t), 0]) for t in ts])
        dot = Dot(radius=0.11, color=CYAN).move_to(path.get_start())
        self.add(dot)
        self.play(MoveAlongPath(dot, path), run_time=4.5, rate_func=linear)
        self.remove(dot)
        self.next_slide(notes="Zoom en la selección del modelo.")

        # --- Zoom 1: selección del modelo ---
        cyc = VGroup(nodes, arrows, hub)
        self.play(FadeOut(VGroup(left, foot, leg)), cyc.animate.scale(0.6).move_to([-4.1, -0.95, 0]), run_time=1.0)

        def focus(idx):
            return [nodes[k].animate.set_opacity(1 if k == idx else 0.25) for k in range(7)] + \
                   [arrows.animate.set_opacity(0.25)]

        X0 = -1.0
        self.play(*focus(2), run_time=0.6)
        h1 = T("Selección del modelo", 26, NAVY, bold=True).move_to([X0, 1.3, 0]).align_to([X0, 0, 0], LEFT)
        s1 = T("No hay un mejor modelo en abstracto: hay un mejor modelo para una tarea", 17, GRAY, italic=True)
        fit(s1, 7.6).next_to(h1, DOWN, buff=0.12, aligned_edge=LEFT)
        crit = VGroup(*[chip(t, w=7.6, h=0.56, size=17) for t in [
            "Calidad medida en la tarea propia, no en rankings públicos",
            "Costo por consulta y latencia",
            "Privacidad, soberanía de datos y licencia: abierto o comercial",
            "Contexto, herramientas y soporte para agentes",
        ]]).arrange(DOWN, buff=0.14, aligned_edge=LEFT).next_to(s1, DOWN, buff=0.3, aligned_edge=LEFT)
        train = chip("¿Entrenar? Solo si los datos o la tarea lo exigen", w=7.6, h=0.6, fill=NAVY, color=WHITE, size=18, bold=True)
        train.next_to(crit, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(FadeIn(h1, shift=RIGHT * 0.2), FadeIn(s1))
        self.play(LaggedStart(*[FadeIn(c, shift=LEFT * 0.3) for c in crit], lag_ratio=0.15), run_time=1.2)
        self.play(FadeIn(train, shift=UP * 0.2))
        self.next_slide(notes="Zoom en las evaluaciones.")

        # --- Zoom 2: evaluaciones ---
        self.play(FadeOut(VGroup(h1, s1, crit, train)), *focus(4), run_time=0.7)
        h2 = T("Evaluaciones antes de desplegar", 26, NAVY, bold=True).move_to([X0, 1.3, 0]).align_to([X0, 0, 0], LEFT)
        s2 = T("Las pruebas unitarias de la IA moderna", 17, GRAY, italic=True).next_to(h2, DOWN, buff=0.12, aligned_edge=LEFT)
        rows = [("Exactitud en casos de prueba propios", 0.91, "91 %"),
                ("Fidelidad al contexto recuperado (RAG)", 0.88, "0,88"),
                ("LLM como juez: utilidad de la respuesta", 0.86, "4,3 / 5"),
                ("Seguridad, sesgos y datos sensibles", 1.0, "pasa"),
                ("Regresión frente a la versión anterior", 1.0, "sin caídas")]
        table = VGroup()
        BX, BW = 3.35, 1.9
        for k, (name, v, txt) in enumerate(rows):
            yk = 0.2 - k * 0.6
            lbl = fit(T(name, 16, INK), BX - X0 - 0.2).move_to([X0, yk, 0]).align_to([X0, 0, 0], LEFT)
            bg = RoundedRectangle(width=BW, height=0.28, corner_radius=0.14, fill_color=SOFT, fill_opacity=1, stroke_width=0)
            bg.move_to([BX + BW / 2, yk, 0])
            bar = RoundedRectangle(width=BW * v, height=0.28, corner_radius=0.14, fill_color=CYAN, fill_opacity=1, stroke_width=0)
            bar.move_to([BX + BW * v / 2, yk, 0])
            val = T(txt, 15, NAVY, bold=True).next_to(bg, RIGHT, buff=0.15)
            chk = T("✓", 20, "#46C69F", bold=True).next_to(val, RIGHT, buff=0.12)
            table.add(VGroup(lbl, bg, bar, val, chk))
        ok = chip("Listo para desplegar y observar con trazas", w=7.6, h=0.58, fill=NAVY, color=WHITE, size=17, bold=True)
        ok.move_to([X0 + 3.8, -3.05, 0])
        self.play(FadeIn(h2, shift=RIGHT * 0.2), FadeIn(s2))
        for r in table:
            self.play(FadeIn(r[0], shift=RIGHT * 0.15), FadeIn(r[1]), run_time=0.25)
            self.play(GrowFromEdge(r[2], LEFT), FadeIn(r[3]), FadeIn(r[4], scale=1.4), run_time=0.4)
        self.play(FadeIn(ok, shift=UP * 0.2), *[nodes[k].animate.set_opacity(1) for k in (5, 6)], run_time=0.7)


# =====================================================================
class Recorrido(Slide):
    """De los fundamentos a los agentes evaluados y observados en producción."""

    def construct(self):
        chrome = Group(band(), logo())
        ttl = title("De los fundamentos a los agentes en producción")
        self.add(chrome)
        self.play(FadeIn(ttl, shift=RIGHT * 0.3))

        xs = [-4.6, 0.0, 4.6]
        y = 1.9
        track = Line([xs[0], y, 0], [xs[2], y, 0], stroke_color=SOFT, stroke_width=10)
        stops = VGroup(*[Circle(0.2, fill_color=WHITE, fill_opacity=1, stroke_color=GRAY, stroke_width=5).move_to([x, y, 0]) for x in xs])
        labels_txt = [("Fundamentos", "Semestre 1"), ("Aplicaciones avanzadas", "Semestre 2"),
                      ("IA generativa y operación", "Semestre 3")]
        labels = VGroup()
        for (a, b), x in zip(labels_txt, xs):
            g = VGroup(T(a, 20, INK, bold=True), T(b, 16, GRAY)).arrange(DOWN, buff=0.06)
            g.next_to([x, y, 0], DOWN, buff=0.32)
            labels.add(g)
        self.play(Create(track), run_time=0.8)
        self.play(LaggedStart(*[GrowFromCenter(s) for s in stops], lag_ratio=0.25), FadeIn(labels, lag_ratio=0.2))
        self.next_slide(notes="Tres etapas. Los agentes atraviesan todo el recorrido: aparecen en Fundamentos de IA y llegan a producción en el tercer semestre.")

        def activate(i):
            if i > 0:
                seg = Line([xs[i - 1] + 0.22, y, 0], [xs[i] - 0.22, y, 0], stroke_color=CYAN, stroke_width=10)
                self.play(Create(seg), run_time=0.6)
            self.play(stops[i].animate.set_fill(CYAN).set_stroke(CYAN), labels[i][0].animate.set_color(CYAN), run_time=0.5)

        def course_list(items, x=0.55, top=0.25, w=6.3, hi=None, header=None):
            g = VGroup()
            for k, s in enumerate(items):
                if hi is not None and k in hi:
                    c = chip(s, w=w, h=0.54, fill=CYAN, color=WHITE, bold=True)
                elif s.startswith("Electiva"):
                    c = chip(s, w=w, h=0.54, fill=GRAY, color=WHITE, bold=True)
                else:
                    c = chip(s, w=w, h=0.54)
                g.add(c)
            g.arrange(DOWN, buff=0.12, aligned_edge=LEFT)
            g.move_to([x + w / 2, 0, 0]).align_to([0, top, 0], UP)
            if header:
                hd = T(header, 17, GRAY, bold=True).next_to(g, UP, buff=0.14, aligned_edge=LEFT)
                return VGroup(hd, *g)  # hd queda en el índice 0
            return g

        # ================= 1a. Fundamentos de IA: agentes =================
        activate(0)
        fund = course_list([
            "Fundamentos de IA",
            "Matemáticas aplicadas",
            "Estadística aplicada",
            "Aprendizaje automático",
            "Aprendizaje profundo",
            "Electiva 1",
        ], hi=[0], header="Plan de estudios · asignaturas del primer semestre")
        acen = np.array([-3.3, -1.45, 0])
        agent = VGroup(RoundedRectangle(width=2.6, height=1.5, corner_radius=0.2, fill_color=NAVY, fill_opacity=1, stroke_width=0),
                       VGroup(T("Agente", 22, WHITE, bold=True), T("búsqueda · planificación", 13, LIGHT),
                              T("razonamiento", 13, LIGHT)).arrange(DOWN, buff=0.06))
        agent[1].move_to(agent[0])
        agent.move_to(acen + UP * 0.85)
        env = VGroup(RoundedRectangle(width=2.6, height=0.9, corner_radius=0.2, fill_color=PALE, fill_opacity=1, stroke_width=0),
                     T("Entorno", 22, NAVY, bold=True))
        env[1].move_to(env[0])
        env.move_to(acen + DOWN * 1.55)
        perc = CurvedArrow(env.get_left() + UP * 0.1, agent.get_left() + DOWN * 0.2, angle=-PI / 2.2, color=CYAN, stroke_width=4)
        act = CurvedArrow(agent.get_right() + DOWN * 0.2, env.get_right() + UP * 0.1, angle=-PI / 2.2, color=CYAN, stroke_width=4)
        pl = T("percepción", 16, CYAN, bold=True).next_to(perc, LEFT, buff=0.1)
        al = T("acción", 16, CYAN, bold=True).next_to(act, RIGHT, buff=0.1)
        self.play(FadeIn(agent, scale=0.8), FadeIn(env, scale=0.8))
        self.play(Create(perc), FadeIn(pl), Create(act), FadeIn(al), run_time=1.0)
        self.play(LaggedStart(*[FadeIn(c, shift=LEFT * 0.4) for c in fund], lag_ratio=0.15), run_time=1.3)
        self.next_slide(loop=True, notes="Fundamentos de IA: el agente que percibe su entorno, busca, planifica y actúa. Es la base conceptual de los agentes con LLM.")
        sig = Dot(radius=0.1, color=CYAN)
        self.play(MoveAlongPath(sig, perc), run_time=0.9, rate_func=linear)
        self.play(Indicate(agent, color=CYAN, scale_factor=1.05), run_time=0.5)
        self.play(MoveAlongPath(sig, act), run_time=0.9, rate_func=linear)
        self.play(Indicate(env, color=CYAN, scale_factor=1.05), run_time=0.5)
        self.remove(sig)
        self.next_slide()
        agent_grp = VGroup(agent, env, perc, act, pl, al)

        # ================= 1b. ML -> DL =================
        self.play(FadeOut(agent_grp, shift=LEFT * 0.4),
                  fund[1][0].animate.set_fill(PALE), fund[1][1].animate.set_color(NAVY),
                  *[fund[k][0].animate.set_fill(CYAN) for k in (4, 5)],
                  *[fund[k][1].animate.set_color(WHITE) for k in (4, 5)], run_time=0.7)
        eq = T("θ  ←  θ − η ∇L(θ)", 34, NAVY, bold=True).move_to([-3.3, 0.15, 0])
        cap = T("Matemáticas y estadística: el lenguaje de la IA", 17, GRAY, italic=True).next_to(eq, DOWN, buff=0.15)
        rng = np.random.default_rng(3)
        ca = rng.normal([-4.4, -1.55], 0.25, (12, 2))
        cb = rng.normal([-2.2, -3.0], 0.25, (12, 2))
        ca[:, 1] = np.clip(ca[:, 1], -2.2, -1.1)
        cb[:, 1] = np.clip(cb[:, 1], -3.4, -2.5)
        pts = VGroup(*[Dot([a, b, 0], radius=0.07, color=CYAN) for a, b in ca],
                     *[Dot([a, b, 0], radius=0.07, color=NAVY) for a, b in cb])
        ax = VGroup(Line([-5.7, -3.6, 0], [-0.9, -3.6, 0], stroke_color=GRAY, stroke_width=2),
                    Line([-5.7, -3.6, 0], [-5.7, -0.85, 0], stroke_color=GRAY, stroke_width=2))
        bound = Line([-5.4, -2.0, 0], [-1.2, -2.6, 0], stroke_color=INK, stroke_width=4)
        bound_ok = Line([-4.35, -3.55, 0], [-2.25, -1.0, 0], stroke_color=INK, stroke_width=4)
        tag_ml = T("Aprendizaje automático", 16, GRAY, italic=True).next_to(ax, UP, buff=0.05).align_to(ax, RIGHT)
        self.play(Write(eq), FadeIn(cap), run_time=1.0)
        self.play(Create(ax), LaggedStart(*[FadeIn(p, scale=0.3) for p in pts], lag_ratio=0.03), FadeIn(tag_ml), run_time=1)
        self.play(Create(bound))
        self.play(Transform(bound, bound_ok), run_time=1.1)
        net = network([3, 4, 4, 2], x_gap=1.05, y_gap=0.55, node_color=CYAN, edge_color=CYAN, edge_op=0.45)
        net.move_to([-3.3, -2.25, 0])
        tag_dl = T("Aprendizaje profundo", 16, GRAY, italic=True).move_to(tag_ml).align_to(tag_ml, RIGHT)
        self.next_slide(notes="Las bases: matemáticas, estadística, aprendizaje automático y profundo.")
        self.play(FadeOut(VGroup(pts, bound, ax)), FadeIn(net, scale=0.6), ReplacementTransform(tag_ml, tag_dl), run_time=1.1)
        self.play(LaggedStart(*[ShowPassingFlash(e.copy().set_stroke(NAVY, 3, 1), time_width=0.7) for e in net[0]],
                              lag_ratio=0.02), run_time=1.4)
        self.next_slide()
        stage1 = VGroup(eq, cap, net, tag_dl, fund)

        # ================= 2. Aplicaciones avanzadas =================
        self.play(FadeOut(stage1, shift=LEFT * 0.5), run_time=0.6)
        activate(1)
        # Imagen 8x8 con una silueta; un filtro 3x3 la recorre y produce un mapa de características
        pattern = ["........",
                   "...##...",
                   "...##...",
                   "..####..",
                   ".#.##.#.",
                   "...##...",
                   "..#..#..",
                   "..#..#.."]
        CS = 0.29
        grid = VGroup()
        for r in range(8):
            for c in range(8):
                on = pattern[r][c] == "#"
                col = interpolate_color(ManimColor(PALE), ManimColor(NAVY), 0.85 if on else rng.uniform(0.0, 0.18))
                grid.add(Square(CS, stroke_width=0.6, stroke_color=WHITE, fill_color=col, fill_opacity=1))
        grid.arrange_in_grid(8, 8, buff=0).move_to([-4.85, -0.35, 0])
        fmap = VGroup(*[Square(0.22, stroke_width=0.5, stroke_color=WHITE, fill_color=SOFT, fill_opacity=1)
                        for _ in range(36)]).arrange_in_grid(6, 6, buff=0).move_to([-1.55, -0.35, 0])
        conv_arrow = Arrow(grid.get_right() + RIGHT * 0.1, fmap.get_left() + LEFT * 0.1, buff=0, stroke_width=3,
                           color=CYAN, max_tip_length_to_length_ratio=0.2)
        conv_lbl = T("filtro", 14, CYAN, bold=True).next_to(conv_arrow, UP, buff=0.05)
        fm_lbl = T("características", 13, GRAY).next_to(fmap, DOWN, buff=0.08)

        def cell(r, c):
            return grid[r * 8 + c]

        def response(r, c):  # suma de la ventana 3x3 (r, c = esquina superior izquierda)
            return sum(pattern[r + i][c + j] == "#" for i in range(3) for j in range(3)) / 9

        kernel = Square(3 * CS, stroke_color=CYAN, stroke_width=5, fill_opacity=0)

        def kpos(r, c):
            return (cell(r, c).get_center() + cell(r + 2, c + 2).get_center()) / 2

        bbox = Rectangle(width=5 * CS + 0.06, height=7 * CS + 0.06, stroke_color="#46C69F", stroke_width=5)
        bbox.move_to((cell(1, 1).get_center() + cell(7, 6).get_center()) / 2)
        blab = T("persona 0.97", 14, WHITE, bold=True)
        blabel = VGroup(BackgroundRectangle(blab, color="#46C69F", fill_opacity=1, buff=0.05), blab).next_to(bbox, UP, buff=0, aligned_edge=LEFT)
        vtag = T("Visión por computador", 16, GRAY, italic=True).next_to(VGroup(grid, fmap), DOWN, buff=0.12)
        toks = VGroup(*[chip(w, w=len(w) * 0.16 + 0.45, h=0.5, fill=CYAN, color=WHITE, size=17, bold=True)
                        for w in ["La", "IA", "transforma", "organizaciones"]]).arrange(RIGHT, buff=0.12)
        for t in toks:
            t[1].move_to(t[0])
        toks.move_to([-3.3, -3.05, 0])
        atts = VGroup(*[ArcBetweenPoints(toks[i].get_top(), toks[j].get_top(), angle=-PI / 3.4, stroke_color=NAVY,
                                         stroke_width=1 + 4 * w, stroke_opacity=0.35 + 0.6 * w)
                        for i, j, w in [(1, 2, 1.0), (1, 3, 0.6), (0, 1, 0.4), (2, 3, 0.8)]])
        ptag = T("Procesamiento de lenguaje natural", 16, GRAY, italic=True).next_to(toks, DOWN, buff=0.12)
        adv = course_list([
            "Visión por computador · detección y segmentación",
            "Procesamiento de lenguaje natural · transformers",
            "Seminario de proyecto de grado",
            "Formación en integridad · ética en datos e IA",
            "Electiva 2",
        ], header="Asignaturas del segundo semestre")
        self.play(LaggedStart(*[FadeIn(q, scale=0.5) for q in grid], lag_ratio=0.008), FadeIn(vtag), run_time=1)
        self.play(GrowArrow(conv_arrow), FadeIn(conv_lbl), FadeIn(fmap), FadeIn(fm_lbl), run_time=0.6)
        kernel.move_to(kpos(0, 0))
        self.play(Create(kernel), run_time=0.3)
        path = [(0, c) for c in range(6)] + [(2, c) for c in range(5, -1, -1)] + [(4, c) for c in range(6)]
        for (r, c) in path:
            v = response(r, c)
            self.play(kernel.animate.move_to(kpos(r, c)),
                      fmap[r * 6 + c].animate.set_fill(interpolate_color(ManimColor(SOFT), ManimColor(CYAN), min(1, v * 1.8))),
                      run_time=0.12)
        rest = [(r, c) for r in range(6) for c in range(6) if (r, c) not in path]
        self.play(*[fmap[r * 6 + c].animate.set_fill(interpolate_color(ManimColor(SOFT), ManimColor(CYAN), min(1, response(r, c) * 1.8)))
                    for (r, c) in rest], FadeOut(kernel), run_time=0.6)
        self.play(Create(bbox), FadeIn(blabel, shift=UP * 0.1))
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.2) for t in toks], lag_ratio=0.15), FadeIn(ptag))
        self.play(LaggedStart(*[Create(a) for a in atts], lag_ratio=0.2), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(c, shift=LEFT * 0.4) for c in adv], lag_ratio=0.15), run_time=1.2)
        self.next_slide(notes="Segundo semestre: visión por computador y PLN con transformers, la base de los modelos de lenguaje.")
        stage2 = VGroup(grid, fmap, conv_arrow, conv_lbl, fm_lbl, bbox, blabel, vtag, toks, atts, ptag, adv)

        # ================= 3a. IA generativa: del agente clásico al agente con LLM =================
        self.play(FadeOut(stage2, shift=LEFT * 0.5), run_time=0.6)
        activate(2)
        gen = course_list([
            "IA generativa · LLM, RAG y agentes",
            "Operaciones en datos e IA · MLOps, LLMOps y AgentOps",
            "Electiva 3",
            "Trabajo de grado",
        ], hi=[0], header="Asignaturas del tercer semestre")
        cen = np.array([-3.3, -1.35, 0])
        llm = VGroup(Circle(0.72, fill_color=NAVY, fill_opacity=1, stroke_width=0), T("LLM", 24, WHITE, bold=True)).move_to(cen)
        tool_names = ["Búsqueda", "Código", "Bases de datos", "APIs"]
        tpos = [UP * 1.55 + LEFT * 1.55, UP * 1.55 + RIGHT * 1.55, DOWN * 1.55 + RIGHT * 1.55, DOWN * 1.55 + LEFT * 1.55]
        tools = VGroup(*[chip(n, w=1.95, h=0.55, fill=PALE, color=NAVY, size=16, bold=True).move_to(cen + p)
                         for n, p in zip(tool_names, tpos)])
        for t in tools:
            t[1].move_to(t[0])
        links = VGroup(*[DashedLine(llm.get_center(), t.get_center(), stroke_color=CYAN, stroke_width=2.5,
                                    dash_length=0.1).scale(0.62) for t in tools])
        slabels = VGroup(*[T(s, 16, CYAN, bold=True) for s in ["Percibir", "Razonar", "Actuar", "Observar"]])
        for s, a in zip(slabels, [90, 0, -90, 180]):
            s.move_to(cen + 2.65 * np.array([np.cos(np.radians(a)), np.sin(np.radians(a)) * 0.72, 0]))
        slabels[1].shift(RIGHT * 0.15)
        slabels[3].shift(LEFT * 0.15)
        atag = fit(T("Agente con LLM: modelo + herramientas + memoria + planificación", 16, GRAY, italic=True), 6.0).move_to([-3.1, -3.75, 0])
        self.play(GrowFromCenter(llm), LaggedStart(*[FadeIn(c, shift=LEFT * 0.4) for c in gen], lag_ratio=0.15), run_time=1.1)
        self.play(LaggedStart(*[AnimationGroup(Create(l), FadeIn(t, scale=0.7)) for l, t in zip(links, tools)],
                              lag_ratio=0.2), run_time=1.3)
        self.play(LaggedStart(*[FadeIn(s) for s in slabels], lag_ratio=0.3), FadeIn(atag))
        self.next_slide(loop=True, notes="El mismo ciclo percibir–razonar–actuar de Fundamentos de IA, ahora con un LLM que usa herramientas. Es el corazón del curso de IA generativa.")
        for t in tools:
            pkt = Dot(radius=0.09, color=CYAN).move_to(llm)
            self.play(pkt.animate.move_to(t), Indicate(t, color=CYAN, scale_factor=1.08), run_time=0.45)
            self.play(pkt.animate.move_to(llm), run_time=0.35)
            self.remove(pkt)
        self.play(Indicate(llm, color=CYAN, scale_factor=1.1), run_time=0.5)
        self.next_slide()
        agent2 = VGroup(llm, tools, links, slabels, atag)

        # ================= 3b. LLMOps: trazas y evaluaciones =================
        self.play(FadeOut(agent2, shift=LEFT * 0.5), FadeOut(gen), run_time=0.6)
        sec = T("Una traza de un agente en producción", 20, INK, bold=True).move_to([-6.0, 0.55, 0]).align_to([-6.0, 0, 0], LEFT)
        spans = [("agente.run", 0.0, 1.0, NAVY, 0),
                 ("llm.planificar", 0.02, 0.22, CYAN, 1),
                 ("tool.búsqueda", 0.24, 0.48, LIGHT, 1),
                 ("llm.razonar", 0.50, 0.70, CYAN, 1),
                 ("tool.base_de_datos", 0.71, 0.83, LIGHT, 1),
                 ("llm.responder", 0.84, 0.99, CYAN, 1)]
        X0, WW = -3.3, 5.0
        rows = VGroup()
        for k, (nm, a, b, col, lvl) in enumerate(spans):
            yk = -0.05 - k * 0.5
            lab = T(nm, 15, INK, bold=(lvl == 0)).move_to([-6.0 + 0.25 * lvl, yk, 0]).align_to([-6.0 + 0.25 * lvl, 0, 0], LEFT)
            bar = Rectangle(width=max(WW * (b - a), 0.05), height=0.3, fill_color=col, fill_opacity=1, stroke_width=0)
            bar.move_to([X0 + WW * (a + b) / 2, yk, 0])
            rows.add(VGroup(lab, bar))
        axis = VGroup(Line([X0, -3.0, 0], [X0 + WW, -3.0, 0], stroke_color=GRAY, stroke_width=1.5),
                      T("0 s", 13, GRAY).move_to([X0, -3.22, 0]), T("2,4 s", 13, GRAY).move_to([X0 + WW, -3.22, 0]))
        metrics = VGroup(*[chip(s, w=3.2, h=0.5, size=16) for s in
                           ["Latencia: 2,4 s", "Tokens: 3.180", "Costo: USD 0,004", "Llamadas a herramientas: 2"]])
        metrics.arrange(RIGHT, buff=0.15).scale(0.92).move_to([0.0, -3.72, 0])
        self.play(FadeIn(sec))
        self.play(Create(axis[0]), FadeIn(axis[1:]))
        for r in rows:
            self.play(FadeIn(r[0], shift=RIGHT * 0.1), GrowFromEdge(r[1], LEFT), run_time=0.35)
        self.play(LaggedStart(*[FadeIn(m, shift=UP * 0.15) for m in metrics], lag_ratio=0.15), run_time=0.9)

        evals = VGroup(*[chip(s, w=3.9, h=0.5, size=15) for s in
                         ["✓ Exactitud en casos de prueba", "✓ Fidelidad al contexto (RAG)",
                          "✓ LLM como juez", "✓ Seguridad y guardrails", "✓ Regresión entre versiones"]])
        evals.arrange(DOWN, buff=0.1, aligned_edge=LEFT).move_to([4.6, -1.15, 0])
        evt = T("Evaluaciones continuas", 18, CYAN, bold=True).next_to(evals, UP, buff=0.15, aligned_edge=LEFT)
        self.play(FadeIn(evt), LaggedStart(*[FadeIn(e, shift=LEFT * 0.3) for e in evals], lag_ratio=0.15), run_time=1.1)
        self.next_slide(notes="LLMOps y AgentOps: cada ejecución deja una traza con latencia, tokens y costo, y cada versión pasa por evaluaciones.")
        stage3 = VGroup(sec, rows, axis, metrics, evals, evt)

        # ================= Cierre =================
        self.play(FadeOut(stage3, shift=DOWN * 0.3), run_time=0.6)
        msg = VGroup(T("Del modelo al impacto", 46, NAVY, bold=True),
                     T("de los fundamentos matemáticos y los agentes clásicos", 25, INK),
                     T("a agentes con LLM evaluados y observados en producción", 25, CYAN, bold=True)
                     ).arrange(DOWN, buff=0.22).move_to([0, -1.2, 0])
        self.play(*[Indicate(s, color=CYAN) for s in stops], run_time=0.8)
        self.play(LaggedStart(*[FadeIn(m, shift=UP * 0.3) for m in msg], lag_ratio=0.25), run_time=1.3)
        self.next_slide()


# =====================================================================
class PlanEstudios(Slide):
    def construct(self):
        chrome = Group(band())
        ttl = title("Plan de estudios")
        self.add(chrome)
        self.play(FadeIn(ttl, shift=RIGHT * 0.3))

        counter_val = ValueTracker(0)
        cr = T("de 36 créditos", 20, INK).to_corner(UR, buff=0.6).shift(DOWN * 0.3)
        num = always_redraw(lambda: T(f"{int(round(counter_val.get_value()))}", 54, CYAN, bold=True)
                            .next_to(cr, LEFT, buff=0.2).align_to(cr, DOWN).shift(DOWN * 0.04))
        self.add(num)
        self.play(FadeIn(cr))

        leg = VGroup()
        for c, s in [(CYAN, "Obligatoria"), (GRAY, "Electiva"), (NAVY, "Investigación y trabajo de grado")]:
            leg.add(VGroup(Square(0.22, fill_color=c, fill_opacity=1, stroke_width=0), T(s, 16, INK)).arrange(RIGHT, buff=0.12))
        tagdemo = VGroup(RoundedRectangle(width=0.95, height=0.3, corner_radius=0.15, fill_color=NAVY, fill_opacity=1, stroke_width=0),
                         T("agentes", 12, WHITE, bold=True))
        tagdemo[1].move_to(tagdemo[0])
        leg.add(VGroup(tagdemo, T("Énfasis en agentes y LLMOps", 16, INK)).arrange(RIGHT, buff=0.12))
        leg.arrange(RIGHT, buff=0.45).next_to(ttl, DOWN, buff=0.25, aligned_edge=LEFT)
        self.play(FadeIn(leg))

        # (nombre, créditos, tipo, etiqueta)
        sem = [
            [("Matemáticas aplicadas", 2, "o", None), ("Estadística aplicada", 2, "o", None),
             ("Fundamentos de IA *", 2, "o", "agentes"), ("Aprendizaje automático *", 2, "o", None),
             ("Aprendizaje profundo *", 2, "o", None), ("Electiva 1", 2, "e", None)],
            [("Visión por computador", 2, "o", None), ("Procesamiento de lenguaje natural", 2, "o", None),
             ("Seminario de proyecto de grado", 3, "i", None), ("Formación en integridad", 3, "e", None),
             ("Electiva 2", 2, "e", None)],
            [("Operaciones en datos e IA", 2, "o", "LLMOps"), ("IA generativa", 2, "o", "agentes"),
             ("Electiva 3", 2, "e", None), ("Trabajo de grado", 6, "i", None)],
        ]
        xs = [-4.45, 0.0, 4.45]
        W, H, GAP = 4.1, 0.6, 0.15
        top = 1.35
        fills = {"o": CYAN, "e": GRAY, "i": NAVY}
        total = 0
        integ = ["* Proyecto integrador 1", "Proyecto integrador 2", None]
        notes = ["Semestre 1: fundamentos, incluidos los agentes en Fundamentos de IA. Funciona también como línea de énfasis para pregrado.",
                 "Semestre 2: visión, PLN y seminario de proyecto de grado.",
                 "Semestre 3: IA generativa y agentes, operación con MLOps y LLMOps, y trabajo de grado."]
        for k, (courses, x) in enumerate(zip(sem, xs)):
            sc = sum(c[1] for c in courses)
            head = VGroup(T(f"Semestre {k + 1}", 22, INK, bold=True), T(f"{sc} créditos", 16, GRAY)).arrange(RIGHT, buff=0.2)
            head.move_to([x, top + 0.5, 0])
            cards = VGroup()
            for name, c, kind, tag in courses:
                h = H if c < 6 else H * 2 + GAP
                box = RoundedRectangle(width=W, height=h, corner_radius=0.1, fill_color=fills[kind], fill_opacity=1, stroke_width=0)
                crt = T(f"{c} cr", 15, WHITE)
                parts = [box, crt]
                tag_w = 0
                if tag:
                    tg = VGroup(RoundedRectangle(width=len(tag) * 0.1 + 0.4, height=0.3, corner_radius=0.15,
                                                 fill_color=NAVY, fill_opacity=1, stroke_width=1.5, stroke_color=WHITE),
                                T(tag, 12, WHITE, bold=True))
                    tg[1].move_to(tg[0])
                    parts.append(tg)
                t = fit(T(name, 17, WHITE, bold=True), W - 1.0)
                parts.insert(1, t)
                g = VGroup(*parts)
                t.move_to(box).align_to(box, LEFT).shift(RIGHT * 0.2)
                crt.move_to(box).align_to(box, RIGHT).shift(LEFT * 0.2)
                if tag:
                    tg.move_to(box.get_corner(UR) + LEFT * (tg.width / 2 + 0.12))
                cards.add(g)
            yy = top
            for g in cards:
                g.move_to([x, yy - g[0].height / 2, 0])
                yy -= g[0].height + GAP
            self.play(FadeIn(head, shift=DOWN * 0.2), run_time=0.4)
            self.play(LaggedStart(*[FadeIn(g, shift=UP * 0.3) for g in cards], lag_ratio=0.12),
                      counter_val.animate.set_value(total + sc), run_time=1.3)
            total += sc
            if integ[k]:
                pill = VGroup(RoundedRectangle(width=W, height=0.45, corner_radius=0.22, stroke_color=CYAN,
                                               stroke_width=2, fill_opacity=0),
                              T(integ[k], 16, CYAN, bold=True))
                pill[1].move_to(pill[0])
                pill.next_to(cards, DOWN, buff=0.18)
                self.play(Create(pill[0]), FadeIn(pill[1]), run_time=0.5)
            self.next_slide(notes=notes[k])
        foot = VGroup(T("Asignaturas de 2 créditos:", 15, GRAY, italic=True),
                      T("24 h con profesor y 72 h de", 15, GRAY, italic=True),
                      T("trabajo independiente", 15, GRAY, italic=True)).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        foot.move_to([xs[2], -2.9, 0]).align_to([xs[2] - W / 2, 0, 0], LEFT)
        self.play(FadeIn(foot))
