"""Empaqueta dist/ en un único HTML autocontenido (videos, imágenes, CSS y JS incrustados).
Uso: python build_deck.py && python build_onefile.py  ->  maestria_ia_presentacion.html
"""
import base64, mimetypes, re
from pathlib import Path

DIST = Path(__file__).parent / "dist"
html = (DIST / "index.html").read_text(encoding="utf-8")

def data_uri(rel):
    p = DIST / rel
    mime = mimetypes.guess_type(p.name)[0] or "application/octet-stream"
    if p.suffix == ".svg":
        mime = "image/svg+xml"
    return f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode()

# CSS y JS en línea
html = re.sub(r'<link rel="stylesheet" href="([^"]+)">',
              lambda m: "<style>" + (DIST / m.group(1)).read_text(encoding="utf-8") + "</style>", html)
html = re.sub(r'<script src="([^"]+)"></script>',
              lambda m: "<script>" + (DIST / m.group(1)).read_text(encoding="utf-8").replace("</script", "<\\/script") + "</script>", html)
# Imágenes como data URI
html = re.sub(r'src="(assets/[^"]+)"', lambda m: f'src="{data_uri(m.group(1))}"', html)

# Videos: reveal.js separa data-background-video por comas, y un data URI lleva una coma.
# Se guardan en base64 y, antes de iniciar reveal.js, se convierten en blob: URLs (sin comas).
videos = {}
def stash(m):
    rel = m.group(1)
    videos.setdefault(rel, base64.b64encode((DIST / rel).read_bytes()).decode())
    return f'data-bgv="{rel}"'
html = re.sub(r'data-background-video="(videos/[^"]+)"', stash, html)
loader = "<script>(function(){const V={" + ",".join(f'"{k}":"{v}"' for k, v in videos.items()) + "};" + \
    "document.querySelectorAll('[data-bgv]').forEach(function(s){const k=s.getAttribute('data-bgv');" + \
    "if(!V[k])return;if(typeof V[k]==='string'){const b=atob(V[k]);const u=new Uint8Array(b.length);" + \
    "for(let i=0;i<b.length;i++)u[i]=b.charCodeAt(i);V[k]=URL.createObjectURL(new Blob([u],{type:'video/mp4'}));}" + \
    "s.setAttribute('data-background-video',V[k]);});})();</script>"
html = html.replace("<script>\nReveal.initialize", loader + "\n<script>\nReveal.initialize", 1)
assert loader in html, "no se encontró Reveal.initialize"

out = Path(__file__).parent / "maestria_ia_presentacion.html"
out.write_text(html, encoding="utf-8")
print(out, f"{out.stat().st_size/1e6:.1f} MB")
