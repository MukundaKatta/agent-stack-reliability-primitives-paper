"""Generate Agents Assemble cover image (1200x675) for the agent-stack submission."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 675
out = "/tmp/agent-stack-cover.png"

# Dark background palette
BG = (15, 17, 23)            # near black
FG = (235, 240, 248)
ACCENT = (102, 178, 255)     # blue
SUBTLE = (140, 152, 170)
CARD_BG = (24, 28, 38)
NPMRED = (203, 56, 55)

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# Font helpers (fall back if a face is unavailable)
def font(size, bold=False, mono=False):
    if mono:
        return ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", size)
    if bold:
        return ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", size, index=1)
    return ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", size, index=0)

# Title
draw.text((60, 50), "agent-stack", fill=FG, font=font(64, bold=True))
draw.text((60, 130), "Six reliability primitives for production MCP agents",
          fill=SUBTLE, font=font(26))

# Tagline pill
pill_y = 180
pill_h = 36
pill_text = "TypeScript  ·  Python  ·  MCP"
tw = draw.textlength(pill_text, font=font(18))
draw.rounded_rectangle((60, pill_y, 60 + int(tw) + 40, pill_y + pill_h),
                       radius=18, fill=CARD_BG, outline=ACCENT, width=2)
draw.text((80, pill_y + 6), pill_text, fill=ACCENT, font=font(18))

# 3x2 grid of cards
libs = [
    ("AgentFit",    "context-window fitting"),
    ("AgentGuard",  "network egress allowlist"),
    ("AgentSnap",   "tool-call snapshot tests"),
    ("AgentVet",    "tool-arg validation"),
    ("AgentCast",   "structured output enforcer"),
    ("AgentBudget", "token + dollar caps"),
]

GRID_TOP = 250
GRID_LEFT = 60
CARD_W = 360
CARD_H = 110
GAP_X = 22
GAP_Y = 18

for i, (name, desc) in enumerate(libs):
    col = i % 3
    row = i // 3
    x = GRID_LEFT + col * (CARD_W + GAP_X)
    y = GRID_TOP + row * (CARD_H + GAP_Y)
    draw.rounded_rectangle((x, y, x + CARD_W, y + CARD_H),
                           radius=14, fill=CARD_BG, outline=(40, 46, 62), width=1)
    # Accent stripe on left edge
    draw.rectangle((x, y + 14, x + 4, y + CARD_H - 14), fill=ACCENT)
    draw.text((x + 22, y + 22), name, fill=FG, font=font(28, bold=True))
    draw.text((x + 22, y + 64), desc, fill=SUBTLE, font=font(18))

# Footer line: DOI + paper anchor
footer_y = H - 64
draw.text((60, footer_y), "DOI 10.5281/zenodo.20074702",
          fill=SUBTLE, font=font(18, mono=True))
draw.text((60, footer_y + 26), "github.com/MukundaKatta/agent-stack   ·   npm @mukundakatta/agent*",
          fill=SUBTLE, font=font(16, mono=True))

img.save(out, "PNG", optimize=True)
print(f"Wrote {out}  size={img.size}  bytes={os.path.getsize(out)}")
