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
# Imágenes y videos como data URI
html = re.sub(r'(src|data-background-video)="((?:assets|videos)/[^"]+)"',
              lambda m: f'{m.group(1)}="{data_uri(m.group(2))}"', html)

out = Path(__file__).parent / "maestria_ia_presentacion.html"
out.write_text(html, encoding="utf-8")
print(out, f"{out.stat().st_size/1e6:.1f} MB")
