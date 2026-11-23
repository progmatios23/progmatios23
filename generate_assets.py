"""
SVG Asset Generator for progmatios23 GitHub Profile
Generates pixel/retro beveled headings and technology block icons.
"""

from pathlib import Path

OUT_DIR = Path("/home/fkode/projetos/progmatios23/imgs")
HEADINGS_DIR = OUT_DIR / "headings"
ICONS_DIR = OUT_DIR / "icons"
HEADINGS_DIR.mkdir(parents=True, exist_ok=True)
ICONS_DIR.mkdir(parents=True, exist_ok=True)


def make_heading(index_str: str, title_str: str, width: int = 240, height: int = 44) -> str:
    """
    Creates a retro 3D-beveled heading badge with high contrast.
    """
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" shape-rendering="crispEdges">
  <defs>
    <style>
      .num {{ font-family: 'Courier New', Courier, monospace; font-size: 15px; font-weight: 900; fill: #ffffff; }}
      .txt {{ font-family: 'Courier New', Courier, monospace; font-size: 15px; font-weight: 800; fill: #111111; letter-spacing: 1.5px; }}
    </style>
  </defs>
  <!-- Drop shadow -->
  <rect x="3" y="3" width="{width-3}" height="{height-3}" fill="#0d1117" rx="0"/>
  
  <!-- Outer border -->
  <rect x="0" y="0" width="{width-3}" height="{height-3}" fill="#111111"/>
  
  <!-- Inner face -->
  <rect x="2" y="2" width="{width-7}" height="{height-7}" fill="#f6f5f0"/>
  
  <!-- Top/Left 3D Bevel highlight -->
  <rect x="2" y="2" width="{width-7}" height="2" fill="#ffffff"/>
  <rect x="2" y="2" width="2" height="{height-7}" fill="#ffffff"/>
  
  <!-- Bottom/Right 3D Bevel shadow -->
  <rect x="2" y="{height-7}" width="{width-7}" height="2" fill="#b4b0a4"/>
  <rect x="{width-7}" y="2" width="2" height="{height-7}" fill="#b4b0a4"/>
  
  <!-- Number tag box (dark contrast badge) -->
  <rect x="8" y="8" width="34" height="{height-19}" fill="#111111"/>
  <rect x="9" y="9" width="32" height="{height-21}" fill="#1b2430"/>
  <text x="25" y="24" class="num" text-anchor="middle">{index_str}</text>
  
  <!-- Label text -->
  <text x="52" y="24" class="txt">{title_str}</text>
</svg>"""


def make_block_icon(label: str, sub: str, accent_color: str = "#111111") -> str:
    """
    Creates a 60x60 retro block icon with crisp beveled edges.
    """
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64" shape-rendering="crispEdges">
  <defs>
    <style>
      .main {{ font-family: 'Courier New', Courier, monospace; font-size: 15px; font-weight: 900; fill: #111111; }}
      .sub {{ font-family: 'Courier New', Courier, monospace; font-size: 9px; font-weight: 800; fill: {accent_color}; letter-spacing: 0.5px; }}
    </style>
  </defs>
  <!-- Drop shadow -->
  <rect x="3" y="3" width="58" height="58" fill="#0d1117"/>
  
  <!-- Outer border -->
  <rect x="0" y="0" width="58" height="58" fill="#111111"/>
  
  <!-- Inner face -->
  <rect x="2" y="2" width="54" height="54" fill="#fbfaf6"/>
  
  <!-- 3D Bevel Highlight -->
  <rect x="2" y="2" width="54" height="2" fill="#ffffff"/>
  <rect x="2" y="2" width="2" height="54" fill="#ffffff"/>
  
  <!-- 3D Bevel Shadow -->
  <rect x="2" y="54" width="54" height="2" fill="#b9b5aa"/>
  <rect x="54" y="2" width="2" height="54" fill="#b9b5aa"/>
  
  <!-- Accent top bar -->
  <rect x="5" y="6" width="48" height="3" fill="{accent_color}"/>
  
  <!-- Center glyph / text -->
  <text x="29" y="33" class="main" text-anchor="middle">{label}</text>
  <text x="29" y="47" class="sub" text-anchor="middle">{sub}</text>
</svg>"""


# Generate Headings
headings = [
    ("01", "STACK", "stack.svg", 180),
    ("02", "REPOSITORIES", "projects.svg", 240),
    ("03", "KERNEL / INTERNALS", "kernel.svg", 280),
    ("04", "CONNECT", "contact.svg", 200),
]

for idx, title, fname, width in headings:
    content = make_heading(idx, title, width=width)
    (HEADINGS_DIR / fname).write_text(content, encoding="utf-8")
    print(f"Created heading: {fname}")

# Generate Icons
icons = [
    ("C", "LANG", "#00599c", "lang-c.svg"),
    ("C++", "C++20", "#004482", "lang-cpp.svg"),
    ("RUST", "no_std", "#b7410e", "lang-rust.svg"),
    ("ASM", "x86_64", "#4a154b", "lang-asm.svg"),
    ("RING0", "KERNEL", "#c0392b", "lang-kernel.svg"),
    ("RE", "DEBUG", "#8e44ad", "lang-re.svg"),
    ("LINUX", "POSIX", "#d35400", "lang-linux.svg"),
    ("PY", "TOOLING", "#27ae60", "lang-python.svg"),
    ("GIT", "SOURCE", "#16a085", "icon-git.svg"),
    ("MAIL", "PING", "#2980b9", "icon-mail.svg"),
]

for label, sub, color, fname in icons:
    content = make_block_icon(label, sub, accent_color=color)
    (ICONS_DIR / fname).write_text(content, encoding="utf-8")
    print(f"Created icon: {fname}")
