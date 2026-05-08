# ASE 2026 Tools and Datasets Track — Submission Checklist

**Deadline: 2026-05-11 AoE (UTC-12)** — gives you up to 4 days. AoE means the deadline is the last possible moment somewhere on Earth, which translates to roughly 2026-05-12 12:00 UTC.

## Files in this directory

- `agent-stack-ase-tools-paper.tex` — 4-page short paper in ACM `sigconf,review` format
- `screencast-script.md` — 5-minute screencast script (mandatory per CFP)
- `SUBMIT_CHECKLIST.md` — this file

## Step-by-step submission flow

### 1. Build the PDF

`pdflatex` is not installed on this machine. Two options:

**Option A — Overleaf (fastest, no install):**
1. Open https://www.overleaf.com/project — sign in
2. New Project → Upload Project → drag in `agent-stack-ase-tools-paper.tex`
3. Set "Compiler" to `pdfLaTeX` in Menu → Settings
4. Click "Recompile" — the ACM template auto-loads from CTAN
5. Download PDF

**Option B — Local MacTeX:**
```bash
brew install --cask mactex-no-gui
# new shell after install
cd ~/Documents/.../ase-tools-submission
pdflatex agent-stack-ase-tools-paper.tex
bibtex agent-stack-ase-tools-paper
pdflatex agent-stack-ase-tools-paper.tex
pdflatex agent-stack-ase-tools-paper.tex
```

The output PDF should be **exactly 4 pages** including references. If it overflows:
- Tighten the AgentSnap and AgentVet sections (they're the most compressible)
- Move limitations into a single sentence in the conclusion

### 2. Record the 5-minute screencast

Follow `screencast-script.md` end to end. Total length 4:30–5:00. Upload to YouTube as **Unlisted** for the review phase. You'll switch it to Public for camera-ready.

After upload:
- Copy the YouTube URL (`https://www.youtube.com/watch?v=XXXXXX`)
- In `agent-stack-ase-tools-paper.tex`, replace the placeholder `AGENT_STACK_DEMO` with the real video ID
- Rebuild the PDF

### 3. HotCRP submission

Submission system: **https://ase26-tools-datasets.hotcrp.com**

Fields to fill:
- **Title:** `The Agent Reliability Stack: Six Single-Concern, Zero-Dependency Libraries for LLM Agents`
- **Authors:** `Mukunda Rao Katta` — Independent Researcher — `mukunda.vjcs6@gmail.com` — ORCID `0009-0007-6071-3896`
- **Abstract:** copy the abstract from the .tex file (single paragraph, ~250 words; HotCRP usually gives a 250-word cap)
- **Submission type:** Tools and Datasets — Independent Tool Submission (no associated research paper)
- **Track:** Tools and Datasets
- **Topic / area tags:** select `Software Engineering Tools`, `Software Quality and Reliability`, `Empirical Software Engineering`
- **Conflicts of interest:** none
- **Tool URL:** `https://mukundakatta.github.io/agent-stack/`
- **Source repository URL:** `https://github.com/MukundaKatta/agent-stack-reliability-primitives-paper`
- **Persistent archive (DOI):** `10.5281/zenodo.20074702`
- **Screencast URL:** the YouTube URL from step 2
- **License:** MIT (code), CC-BY-4.0 (manuscript)
- **Upload PDF:** `agent-stack-ase-tools-paper.pdf`

Click **Submit**.

### 4. Post-submission

Save the HotCRP submission ID in `submission-metadata.json` under a new entry:

```json
{
  "platform": "ASE 2026 Tools and Datasets Track",
  "status": "submitted",
  "submission_url": "https://ase26-tools-datasets.hotcrp.com/paper/<id>",
  "deadline": "2026-05-11",
  "notification": "2026-06-17",
  "submitted_date": "2026-05-XX"
}
```

Notification date: **2026-06-17**.

## What happens after notification

- **Accepted:** the camera-ready deadline follows roughly 6 weeks later. ASE wants the screencast public by then. The tool URL must remain accessible.
- **Rejected:** ASE Tools rejection is rarely about the tool itself; common reasons are missing screencast, format violations, or scope mismatch. The same paper can be reshaped for ICSME 2026 Tool Demonstration track or SPLASH/ISSTA 2026 Tool Demonstration track without a major rewrite.

## Why this submission is on solid ground

1. **Independent submission explicitly welcomed** — CFP says so directly. No accepted-research-paper gate.
2. **Persistent archive requirement met** — Zenodo DOI registered with DataCite, status `findable`, DOI minted today.
3. **Open license** — MIT for code, CC-BY-4.0 for manuscript. Matches the recommended licensing.
4. **No prior demo publication** — no prior peer-reviewed venue has run this artifact. Preprint deposits do not count as prior demo publications under ASE's definition.
5. **Tool URL is live** — `mukundakatta.github.io/agent-stack/` is up and lists every package.
6. **Screencast is the only blocker on your side** — everything else is paste-ready.

Total submission time once the screencast is recorded: ~10 minutes.
