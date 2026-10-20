# Handoff: Teaching with AI in Business Schools (Utah seminar)

Status as of October 17, 2026. The deck is built and in revision. The "Current state" section below is up to date. Everything after it is the October 1 planning record. Read it for background, but where it conflicts with "Current state," "Current state" wins.

---

## Current state (October 17, 2026)

### Files

- The master deck is `utah-mint.qmd`, styled by `mint.scss`. Edit this file directly. `utah.qmd` (the shoji version) is abandoned, and no script syncs the two. This replaces the planning note below that says decks are built with the shoji skill.
- Render with `quarto render utah-mint.qmd`. The output is `utah-mint.html`.
- Check slides with headless Chrome screenshots at 1280×720 (`"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --window-size=1280,720 --screenshot=out.png "file://$PWD/utah-mint.html#/<slide-id>"`). Slide ids are the slugified titles. Quarto adds `-1` to the second slide with the same title.
- `anatomy-of-an-agent-mint.qmd` is the source of the agent diagram. Its SVG is copied inline into the main deck.
- The title slide gives the date as October 22, 2026. The planning notes below say "roughly October 21." Confirm the date.

### Deck outline (35 slides)

1. Title slide, with the Salt Lake City skyline across the top.
2. Opening: The dawn of the PC era (VisiCalc); The future of work (Farley, twice, second with highlights); The new job is managing AI agents (Waldron); What AI can make; two untitled image slides; AI fluency at Eccles.
3. Where AI is untrustworthy (divider, Park City): Verifiable tasks vs judgment (Andrew Ng); Should I walk or drive? (Haiku 4.5 says walk); Should I walk or drive? (Haiku 5.5 says drive); Hallucinations occur but are rare now (Opus 4.8 system prompt).
4. What is AI fluency? (divider, Little Cottonwood): Lisa Su; Human judgment at the core; Not replacing judgment; What we teach in business schools; What's left for people; Selby Jennings fluency-gap chart.
5. Is it over-hyped? (divider, Alta): MIT NANDA ×2; Enterprise adoption; Limits to enterprise adoption; Predicted job losses are not showing up yet; A brief history.
6. Why is AI so good at coding tasks? (divider, Capitol): three reasons; Anatomy of an agent; How Claude checks Office documents; Coding agents arrive (timeline); Code → Cowork → Chat; Andrej Karpathy.

The deck no longer follows the 120-minute outline in the planning notes. Teaching tools, the 638 arc, and the demos are not yet in the deck.

### Theme changes made October 17 (mint.scss)

- `{.no-strip}` removes the mint strip from a slide that keeps its title and lets the content use the full width.
- On `{.no-title}` slides, images are no longer capped at 520 px. Every other slide keeps the cap.
- A new title-slide layout puts a wide photo across the top 405 px with the text full-width below. It applies when `data-background-position: top` is set in `title-slide-attributes`.
- Titles on `{.pull}` slides now wrap before the mint strip. Before this change, long titles ran into it.

### Photos

All photos are grayscale crops from Wikimedia Commons. Dividers use 1040×1440, image panels use 840×1440, and the title band uses 2560×810.

| File | Where used | Credit |
|---|---|---|
| `utah-slc-skyline.jpg` | Title slide | Invictus323, CC BY 4.0 |
| `utah-park-city.jpg` | Where AI is untrustworthy | Don Ramey Logan, CC BY-SA 4.0 |
| `utah-capitol.jpg` | Why is AI so good at coding tasks? | GyozaDumpling, CC BY-SA 4.0 |
| `utah-eccles-building.jpg` | AI fluency at Eccles | Jeff Hitchcock, CC BY 2.0 (credited on slide) |
| `utah-snowbird.jpg` | Human judgment at the core | Don Ramey Logan, CC BY 4.0 (credited on slide) |
| `utah-block-u.jpg` | Not replacing judgment | Not credited on slide; source not recorded |
| `utah-little-cottonwood.jpg`, `utah-alta.jpg` | Dividers | Credits not recorded |
| `utah-timpanogos.jpg` | Not used | Was the title photo |

No divider or title slide carries a photo credit, but CC BY and CC BY-SA require attribution. Unused candidates already checked: Salt Lake Temple (Acroterion, CC BY-SA 4.0), Park City Main Street by day (Ken Lund, CC BY-SA 2.0), Deer Valley (Don Ramey Logan, CC BY 4.0), Solitude cabin (Greg Rakozy, CC0), Capitol dome interior (Farragutful, CC BY-SA 4.0).

### Facts verified October 17

- Datadog, State of AI Engineering: the 63% for OpenAI is a share of organizations, not of usage. Anthropic gained 23 points and Google 20 points year over year. More than 70% of organizations use three or more models. The report gives no open-source figure.
- Cowork, from Anthropic's release notes: launched January 12, 2026 in the desktop app; Pro on January 16; scheduled tasks February 25; computer use March 23; generally available on macOS and Windows April 9; web and mobile July 7; merged into Chat September 16, 2026 ("everything Claude Cowork does available from any conversation"). The merge is rolling out to Pro and Max first.
- Code execution timeline: ChatGPT Code Interpreter, July 2023; Claude analysis tool, October 24, 2024; Claude Code, February 2025; Codex CLI, April 2025; Gemini CLI, June 2025.
- The system-prompt quote on the hallucinations slide appears word for word in the published Opus 4.8 prompt (May 28, 2026) and in the Opus 5.5 and Haiku 5.5 prompts. The published prompts omit the search-tool instructions. `~/repos/course-oct/slides/system-prompt-opus48.txt` holds a fuller Opus 4.8 prompt, with the search rules; those rules key on recency, not on uncertainty.
- The Claude Code source leak happened March 31, 2026 (version 2.1.88, a source map in the npm package). OpenCode came before it and was not derived from it; claw-code was. None of this is on a slide.

### Open items for the deck

1. Datadog row on Enterprise adoption: Anthropic ~46% and Google ~37% do not appear in Datadog's text. They were probably read off a chart. Check them, or show only the point gains.
2. Coding agents timeline: the OpenCode date (sources say April to June 2025) and the Pi date ("late 2025"; Zechner's post is dated November 30, 2025) are uncertain.
3. "A brief history" overlaps the "Coding agents arrive" timeline. Consider cutting or shortening it.
4. Haiku 5.5 slide: the image is 360 px tall and sits at the top, with the lower third empty. It could be centered vertically.
5. Photo credits for the dividers and title slide (see Photos).
6. On the "Why is AI so good at coding tasks?" divider, the mint circle nearly touches the second title line.
7. The planning open items below (demos, ad copy, research corrections) are still open unless noted otherwise.

---

## The engagement

A two-hour seminar for faculty at the David Eccles School of Business, University of Utah. Delivery roughly October 21, 2026 (three weeks out as of September 30).

Decisions already made, do not reopen without asking:

- Audience is business school faculty across disciplines. Not deans, not students, not instructional designers.
- Format is presentation with live demos. No attendee laptops, no provisioned accounts, no breakout exercises.
- Weighting favors (a) fundamentals every student should know and (b) using AI in our own teaching.
- Advertising copy needed as a 200–300 word abstract.
- Decks are built with the shoji skill. This is a standing global instruction — use shoji unless cardstock is specifically requested, and do not ask.

---

## Current outline, 120 minutes

Spine is the instructor's own practice: what I teach, what I build, what works. Not a borrowed thesis.

| Segment | Min | Content |
|---|---|---|
| Open | 8 | Credit what Eccles has built, by name. Four-year timeline. Karpathy. The three questions the talk answers. |
| 1. Fundamentals every student should know | 35 | One capability — AI writes code and runs it — and everything downstream. Amortization workbook demo (model, not table), then into a deck. Chatbot / agent / API as three doors on one model. Persistent instructions. Prompting. Where errors come from, and why verification requires someone who understands the material. |
| 2. What a course can now cover | 20 | The 638 arc: valuation multiples → regression → machine learning → ninety-year backtests → a working app, in a six-week term. Then the 803 tier: skills, agents, connectors, security. The point is the raised analytical ceiling, not the plumbing. |
| Break | 5 | |
| 3. What this leaves our students | 15 | Where companies are. The expert–novice wall. Judgment as the thing that appreciates. |
| 4. Teaching tools that work | 32 | Slides as code, demoed live. Tutor skills (agency, binomial) — coach to the answer rather than hand it over. Course sites, reusable skills, problem sets, finance-data skill. Tutorbots get ~90 seconds at the end as frontier-not-deployed. |
| Close + Q&A | 5 | |

---

## Rejected approaches, and why

This is the most important section. Each of these was proposed, considered, and cut for a stated reason. Do not re-propose them.

Mollick's "overhang" as the organizing spine. Cut. The instructor likes the phrasing but it is not his material and he cannot advise an audience about it. Usable at most as a borrowed phrase in the open.

A tutorbot build demo as the centerpiece of Part 4. Cut. Heavy API cost per student and substantial build time; he is not prepared to recommend it to faculty yet. Demoted to a brief honest note on what he has not deployed and why. Note this is corroborated by the literature — the PNAS team hired two math teachers part-time to write per-problem guardrails.

Lab infrastructure as a section. Cut. He will not go into lab details. Background on why, recorded here only so it is not rediscovered: cost is high on Sonnet; GLM 4.7 is not strong enough; GLM is not a vision model, so it could not read the PNGs the Claude Code harness generates to check its own output; and web search was unavailable on the third-party endpoint. A fix was being researched when the thread was cut — switching to first-party models restores vision and the built-in WebSearch/WebFetch, and MCP search servers are the alternative if a third-party endpoint must stay. None of this belongs in the talk.

Assessment architecture as a section. Cut. Not his strong point, and he would be defending unfamiliar ground in front of people who have thought about it more. Keep it as a prepared ~90-second Q&A answer instead; it will be asked. The answer: detection does not work (Vanderbilt), the two frameworks worth knowing are Sydney's two-lane for security and the AIAS for design, his own course uses 60% random-draw group presentations and 40% participation with no exams, and he is not an expert on assessment policy. The closing disclaimer is what makes it credible.

A wake-up-call framing for Eccles. Cut. They are ahead of most schools and financed this three years ago. Open by crediting their work, then go deeper than their published plan.

---

## What Eccles has built

Needed for the open, and for not misrepresenting them in their own room.

Institutional: One-U Responsible AI Initiative, $100M, launched October 2023 by President Taylor Randall, led by Manish Parashar at the Scientific Computing and Imaging Institute; teaching and learning is one of three thematic areas. Parashar became the U's inaugural AI officer in February 2025. Centrally the U reports 36 AI-related academic programs or classes and 80 GPUs added in 2025, with NVIDIA and HPE partnerships. The Center for Teaching Excellence runs an AI 101 course for faculty and is piloting a tool that analyzes student course-feedback data.

School level: Dean Kurt Dirks set the vision — his phrase is "Eccles students will be AI-fluent and fundamentals-strong," worth using verbatim. Professor Himanshu Mishra leads implementation. The published roadmap (January 23, 2026) has four parts: faculty training; ethical and responsible use; hands-on student GenAI training; and AI guidance in advising and career services. Reported progress: GenAI integrated into courses reaching 1,100-plus students, up from a 900-plus figure cited earlier; faculty-to-faculty workshops; support for an AI4U student club; an online AI Foundations course in development for incoming freshmen.

The AI Faculty Workshop was built with the Responsible AI Initiative and the Center for Teaching Excellence. First session drew 95 faculty. Coverage dates it October 17 but the year could not be confirmed from cached text — say "their first faculty workshop" rather than name a date.

The Business AI minor is the flagship and went live this fall, so it is about six weeks old at delivery. Announced November 3, 2025. Sixteen credit hours: three required three-credit courses, a one-credit capstone, two three-credit electives. Open to every U undergraduate regardless of college. Minimal coding prerequisites by design. Named coursework includes Python programming, business strategy, machine learning and analytics, data visualization and communication, with an AI ethics elective. Tools are Python, Tableau, Retool, and generative AI; topics include machine learning, NLP, image recognition, predictive analytics, chatbot development. First AI-related academic program at the U approved by the Board of Trustees. Chong Oh (director of undergraduate information systems) championed it; Matt Pecsok took over leadership in July 2026. Oh's best line: "We want AI to help students learn, not for them to use it as a vending machine."

Also launched this fall: a 30-credit cohort MS in Financial Technology covering payments, digital lending, AI in finance, cybersecurity, algorithmic trading, and blockchain. This is the closest thing at Eccles to MGMT 638 and is probably the strongest point of contact in the room.

Two framing consequences. Their published roadmap does not address assessment architecture — but per the rejected-approaches section, that gap is a Q&A answer, not a section. And their minor is a tools-and-applications curriculum taught out of information systems; the 638/803 material is the layer above it (agents, skills, connectors, deployment, security), which is a complement rather than a correction and should be framed that way.

---

## Source material

Nothing in `~/repos/ai-lectures` is under version control. Dates below are file mtimes.

`2026-utah/` is an empty Quarto scaffold created July 11, 2026: `_quarto.yml` (output-dir `slides-html`, renders `slides-qmd/*.qmd`, post-render `flatten.py`), `slides-qmd/` with `revealjs-style.scss` and `images/`, empty `slides-html/` and `slides-pdf/`. Format is revealjs at 1920×1080, margin 0.05, linear navigation, fade transition, monokai highlighting, `slide-number: c/t`, centered, `auto-stretch: false`. `2026-zurich/` is an identical scaffold from the same afternoon.

Reusable by source:

- `2026-orientation/intro-to-ai.qmd` and `mba.qmd` — the fundamentals layer. One-capability framing, four-year timeline, Karpathy, prompting, sources of error in AI data analysis, skills, tutors, artifacts. Part 1 is mostly a harvest from these two.
- `mgmt638/slides/session01–12` — course arc and mechanics, prompting, agent anatomy, CLAUDE.md, the ML sequence (04, 05, 07), app build and deploy (07), skills and agents (08), prompt injection and containers (12). Part 2's first half comes from here.
- `mgmt803/slides/part1–8` — LLM internals, model landscape and cost per task, agents and harnesses, computer use, CLAUDE.md/skills/MCP/plugins, APIs and building chatbots and agents, git and deployment, RAG and local models, multi-agent and security, neural network internals and LoRA. Part 2's second half.
- `exec-ed-slides/1–8` — the HPE CFO quote on Alfred removing 90% of the work behind a 100-slide Monday review, the SaaSpocalypse ($285B in 48 hours), the 20-month capability timeline, the three-card Karpathy progression, the security sequence. Part 3 draws on these.
- `research/` — the teaching-with-AI literature base, described below.

Tooling: the shoji skill builds the deck; the deck skill exports PDFs via Decktape; a `slide-prose-editor` agent exists for trimming deck prose to a factual scaffold after drafting.

---

## The research folder

`research/` was built July 10–11, 2026 and set aside. Contents:

- `teaching-with-ai-research.md` (20KB) — the main artifact. HBS in depth, peer schools, the Mollick toolkit, the two randomized trials, assessment redesign, detection, accreditor signals, and a section 9 of local context on Rice, Utah, and Zurich. Header records the method: 29 sources, 144 claims, top 25 adversarially verified.
- `sources/` — 70 files. 60 markdown page captures plus 9 PDFs of the underlying studies (Bastani PNAS, Kestin physics RCT, BCG jagged frontier, P&G cybernetic teammate, ETH Ethel, PitchQuest, Mollick's Assigning AI). 29 Harvard Business Publishing Inspiring Minds articles in full text. `MANIFEST.md` documents retrieval and gaps.
- `hbs-reading-list.md` — the same material as a ranked reading list.
- `notes.md` — scrap. The Kaganer/IESE quote and four HBR citations.
- `Mollick - Instructors as Innovators.pdf` — loose at top level.
- `committee-memo.md` — written September 30, 2026 for a Rice curriculum committee. Separate deliverable, not Utah material. All figures in it verified.

Critical caveat on the research file: verified and useful are not the same sections. Sections 1–4 (HBS, peer schools, Mollick toolkit, the RCTs) were independently checked. Sections 5–9 were extracted but never verified. The corrections below have not yet been written back into the file.

---

## Verified facts, safe for slides

Checked against primary sources September 30, 2026.

The two randomized trials, read in full from the PDFs in `research/sources/`:

Bastani et al., PNAS. Large high school in Turkey, fall 2023–24, roughly 1,000 students across about 50 classes in grades 9–11, four 90-minute sessions covering ~15% of the semester's math curriculum. Preregistered, 2,848 observations, standard errors clustered at the classroom level. Three arms assigned by classroom: control (notes and textbook, no devices), GPT Base (plain ChatGPT-like interface), GPT Tutor (guardrailed). Session structure was teacher lecture → randomized assisted practice → closed-book exam on conceptually matched problems, with both practice and exam counting toward grades. Practice: +48% for GPT Base, +127% for GPT Tutor against a control mean of 0.284 out of 1. Exam: GPT Base −17%, statistically significant; GPT Tutor −0.4%, indistinguishable from control. Note carefully that GPT Tutor produced no positive exam effect — it erased harm, it did not help. Mechanism from message logs: GPT Base students asked for and copied solutions (the authors say "crutch"); GPT Tutor students asked for help and attempted answers. Students did not perceive any reduction in their learning. The guardrails were the correct worked solution per problem (to stop hallucination), a list of common mistakes with hints, an instruction never to give the full solution, and an instruction to require the student's work first; two math teachers were hired part-time to produce this. Outcome is same-session retention, not long-term learning.

Kestin et al., Scientific Reports 2025, 15:17458. N=194 in Harvard intro physics. Crossover design, two lessons in consecutive weeks (surface tension, then fluid flow), groups swapping conditions. The control was a well-designed in-class active-learning session, not a passive lecture; the AI group worked at home, alone. Median post-test 4.5 (AI) vs 3.5 (in-class) from a combined pre-test baseline of 2.75; median gains more than double; Mann-Whitney z = −5.6, p < 10⁻⁸. Regression effect 0.63 SD, understated by a ceiling effect; quantile regression 0.73–1.3. Time: 60 minutes of in-class instruction vs an AI median of 49 minutes, 70% under an hour, and no correlation between time on task and score. Engagement 4.1 vs 3.6, motivation 3.4 vs 3.1; enjoyment and growth mindset indistinguishable. 83% said the tutor's explanations were as good as or better than their in-class instructors'. Design detail worth keeping: a system prompt alone could not reliably scaffold a multi-part problem, so sequencing was built into the platform. The authors recommend AI for first exposure to new material, freeing class time for higher-order work assessed in person, and write explicitly that it should not replace in-person teaching. Limited to the understanding, applying, and analyzing levels of Bloom's taxonomy.

The synthesis both studies support: design determines the outcome, access alone determines nothing, and design means more than a prompt.

Other verified items:

- Vanderbilt disabled Turnitin's AI detector on August 16, 2023. Claimed 1% false-positive rate against the 75,000 papers Vanderbilt submitted in 2022 implies roughly 750 wrongly flagged. Detectors are more likely to flag writing by non-native English speakers.
- AACSB's October 2024 survey: 236 deans across 56 countries, 429 faculty from 321 institutions in 61 countries. 47% report an AI/GenAI policy, 45% report none, 8% unsure; 29% of faculty do not know. EMEA 62%, Americas 36%, Asia Pacific slightly over half.
- IESE's MBA, from September 2026: AI across 18 first-year courses and more than 40 AI-integrated sessions, organized as personal AI fluency, AI-enabled workflow and operating-model redesign, and strategic AI acumen. Deputy Dean Marc Badia: "We made a deliberate choice not to bolt AI onto a couple of electives and call it a transformation." Poets&Quants, June 2, 2026, framed the redesign as betting the MBA's future on judgment.
- Sydney's two-lane model: lane one is secure, supervised, in person, and placed strategically at the program level (viva voces, in-class assessment, tests, exams); lane two is open and unsecured, where AI use is assumed and coordinators cannot prohibit it, because restriction and detection in unsupervised assessment are neither reliable nor equitable. Lane one carries high workload, which is why it is placed strategically rather than everywhere.
- The AI Assessment Scale. Original: Perkins, Furze, Roe & MacVaugh, JUTLP 21(6), 2024 — the journal's paper of the year. Current: Perkins, Roe & Furze, "Reimagining the AIAS," JUTLP 22(7), 2025, doi 10.53761/rrm4y757. More than 300 institutions, 30 languages. Revised five levels are No AI; AI-Assisted Idea Generation and Structuring; AI-Assisted Editing; AI Task Completion with Human Evaluation; Full AI. The 2025 revision dropped the original Level 3 requirement that students submit a pre-AI draft, "acknowledging that the current detection methods cannot reliably verify such submissions," and replaced the traffic-light palette so no level reads as virtuous. TEQSA, Australia's tertiary regulator, recognized the original. Practitioner note 3: the scale is "to guide assessment redesign rather than to restrict students' use of GenAI through detection or prohibition." The authors position it as complementary to two-lane — the two "speak to different aspects of assessment design (AIAS) and assessment security (two-lane)." They accept Corbin, Dawson and Liu's (2025) warning about the "enforcement illusion" from labels applied without redesign.

### Corrections to `teaching-with-ai-research.md`

Not yet written back into the file. Four real errors:

1. The claim that Jones has no school-wide degree-program AI initiative reads as "we have nothing" and is wrong. Rice Business has Kathleen Perley as Faculty and AI Advisor to the Deans, a graduate elective in generative AI for business applications, undergraduate and executive teaching, and an online AI training program for faculty and staff. The defensible version is that there is no declared school-wide plan for where AI capability enters a degree program, who owns the fundamentals, and what happens to assessment — a governance gap, not an absence of activity.
2. The framework cited at 48 schools is the January 2026 edition. A July 28, 2026 update has 84, up from 26 at the inaugural July 2025 edition. It is produced by Inspire Higher Ed with AACSB, the Graduate Business Curriculum Roundtable, and GMAC — not AACSB alone.
3. The file says AI is reshaping accreditation expectations. The framework documents what participating schools report doing; it is not an accreditation standard. Do not tell an audience accreditation requires this.
4. AIAS details were off: first published 2023, authors as listed above, now maintained by Learning Innovation Practice Ltd, adoption 300-plus institutions, and the level names have changed.

Two smaller ones: Utah's dean is Kurt Dirks, and the Business AI minor the file dates to November 2025 is the announcement date — the program starts Fall 2026, and the January 2026 Eccles page does not mention it.

Held up as written: Vanderbilt in full; the AACSB deans survey including the regional split; IESE's course counts and the Badia quote; the Eccles four-part roadmap and 1,100-plus figure; both RCTs; and the TEQSA citation, which was briefly dropped and then confirmed from the 2025 AIAS paper.

HBS tutor-bot figures (930 students, 20,000-plus prompts, ~75% used it at least once, ~60% of use outside school hours peaking at 9pm, 6% for arithmetic) come from the research file's verified section and were not independently re-checked in this pass.

---

## Mollick's current material

Searched September 30, 2026. Important caveat: these came through a fetch-and-summarize pass, so every quote and figure below is second-hand and must be checked against the original before it reaches a slide.

- "The Overhang," September 18, 2026. The constraint is use, not capability — "the gap between what these models can do and what almost anyone is doing with them." Four human contributions: deep knowledge (his example is an experienced accountant glancing at a spreadsheet and knowing something is wrong), wide knowledge, taste ("the scarce resource is your ability to select among stuff using your own taste"), and agency. Rejected as the talk's spine but the accountant example is the single best answer to "then why still teach accounting."
- "The Twilight of the Chatbots," June 30, 2026. The placement material. A study of Claude Code users found expertise, not profession, predicted success — a lawyer with no coding background did about as well as a software engineer outside their home domain. "The walls between 'expert' and 'novice' get higher," because "knowing whether the output is right comes from ten years of doing the work by hand." Blunt that entry-level work is where disruption lands. Reported that a quarter of OpenAI staff run four or more agents simultaneously in a given week, across legal and HR as much as engineering.
- "Management as AI Superpower," January 27, 2026. Delegation is a management problem, not a technical one. Best line for Part 2 or 3: his students succeeded not because they understood AI but because they had years of training in scoping problems, defining deliverables, and recognizing good work — their frameworks from classes and jobs became their prompts. Cites GDPval with GPT-5.2 tying or beating human experts ~72% of the time on seven-hour professional tasks; verify that figure.
- "Co-Existence: The Next Phase of AI." Portfolio / Penguin Random House, October 20, 2026, ISBN 979-8-2171-8139-1. Publishes the day before delivery — worth naming from the podium. Argument: the co-intelligence model with the human at the center is obsolete because the labs always intended autonomous systems, and agents have arrived. His framing question: "what do you do when the AI is no longer just your assistant, but your reader, your critic, and the gatekeeper standing between your work and its audience?" Announcement post (June 4, 2026) cites roughly 17× more code, AI writing ~80% of Anthropic's code, and ~8× developer shipping — all three need verification.
- "Post-Apocalyptic Education," August 30, 2024. Still his sharpest statement on teaching: in education "the effort is the point," and two illusions block progress — teachers overestimate their ability to detect AI use, and students mistake the fluency of getting an answer for having learned. Pairs exactly with the PNAS result.
- "Making AI Work: Leadership, Lab, and Crowd," May 22, 2025. The framework the instructor already knows and likes.

One live tension worth knowing before Q&A: the AIAS authors ground their framework in social constructivism and explicitly reject "problematic understandings of GenAI chatbots as tutors for personalised learning, where students learn in isolation from their peers." That is a direct objection to what Harvard measured — and Harvard's winning condition was a student working alone at home. The reconcilable position is Harvard's own: tutors for first exposure, class time for synthesis and judgment, assessed in person.

---

## Open items

1. Build the deck. Nothing written yet. Suggested order: Part 1 and Part 4 first (the weighted halves, and the two needing working demos), then Parts 2 and 3 (largely harvested from 638/803), then open, close, and a timing pass. Rehearse both demos on the presentation machine.
2. Final ad copy. The last abstract draft has two stale sentences — one promising infrastructure guidance, one saying "we will build one" about a tutor. Both were cut from the talk. Needs a revision at 200–300 words.
3. Write the corrections above back into `teaching-with-ai-research.md` so stale figures do not resurface during the build.
4. PDF of `research/committee-memo.md` for handing out at Rice. Offered, not yet produced.
5. Confirm the year of the first Eccles AI Faculty Workshop before citing a date.
6. Verify Mollick's quotes and the GDPval and code-volume figures against the original posts before they go on slides.

## Demos to prepare

Three, all previously working:

- The amortization workbook as a model rather than a table, then dropped into a deck. Part 1, roughly 5 minutes. This is the strongest single demo — it reframes what faculty think AI is before anything has been argued.
- Slides as code. Ask for a new slide during the talk and show it appear; the deck they are watching is the artifact. Part 4, roughly 4 minutes.
- A tutor skill (agency or binomial) coaching rather than answering. Part 4, roughly 5 minutes. This replaced the tutorbot demo.
