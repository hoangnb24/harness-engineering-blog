# Harness Engineering — A Student's Guide

Visible slide text: English. Speaker notes: Vietnamese.

---

<!-- Slide 1 -->

# Harness Engineering
a student's guide to the discipline behind coding agents
what it is, why it matters, and how to start thinking in harnesses
Hoang · kuckit.dev · 2026

::: notes
Mở đầu trong 30 giây. Hôm nay mình muốn trả lời ba câu hỏi: trong 18 tháng vừa rồi việc viết phần mềm đã thay đổi như thế nào; tại sao từ "harness" bắt đầu xuất hiện nhiều khi nói về coding agents; và với tư cách là sinh viên đang học cách ship phần mềm, các bạn nên làm gì. Câu trả lời ngắn là: học cách suy nghĩ theo harness. Phần còn lại của bài nói là cách chúng ta xây dựng mindset đó từng bước.
:::

---

<!-- Slide 2 -->

## The shift — 18 months that changed how we write code
"Humans steer. Agents execute." — Ryan Lopopolo, OpenAI, Feb 2026
LINES SHIPPED
1,000,000
in 5 months
MANUALLY WRITTEN
0
by humans
PRs / ENGINEER / DAY
3.5
throughput kept growing
Source: [openai.com/index/harness-engineering/](https://openai.com/index/harness-engineering/)

::: notes
Đặt bối cảnh cho cả bài. OpenAI kể một ví dụ rất mạnh: một sản phẩm nội bộ khoảng 1 triệu dòng code được ship trong 5 tháng, và con người không trực tiếp viết từng dòng code đó. Điều quan trọng không phải là khẩu hiệu "năng suất tăng 10 lần". Điều quan trọng là hình dạng công việc đã đổi: con người không còn chỉ gõ code, mà điều khiển agent, thiết kế môi trường, và kiểm soát chất lượng đầu ra.
:::

---

<!-- Slide 3 -->

## The word "harness" is 50 years old
The term has a genealogy. We didn't invent it for AI.
### 1970s
**Test harness** — a fixture that runs test code, captures output, compares to expected. A controlled environment for verifying behavior.
### 2010s
**ML eval harness** — a scaffold that runs a model against a fixed task suite, scores it, and produces a leaderboard. The benchmark infrastructure.
### 2024+
**Agent harness** — the system that wraps a language model and turns it into something that can act on the world. Tools, memory, state, feedback loops.
"If you're not the model, you're the harness." — Vivek Trivedy, LangChain, Mar 2026

::: notes
Giải thích từ "harness" bằng nghĩa gốc: nó là thứ giữ một năng lực mạnh mẽ trong một cấu trúc có thể điều khiển được. Test harness giữ code trong môi trường kiểm thử. ML eval harness giữ model trong bộ benchmark. Agent harness giữ language model trong môi trường có tool, memory, state và feedback loop. Model là phần mạnh; harness là phần làm cho sức mạnh đó dùng được và an toàn hơn.
:::

---

<!-- Slide 4 -->

## The externalization arc
Three waves, each moving capability *out* of the model and *into* the environment around it.
```text
2022–2023      prompt engineering     →  the right words in the chat
2024           context engineering     →  the right words + retrieved knowledge
2025–2026      harness engineering     →  the right words + the right environment
```
Each wave answered a question the previous one couldn't: "how do we make the model's capability actually usable in the real world?"
Source: arXiv [2604.08224](https://arxiv.org/abs/2604.08224) · "Externalization in LLM Agents"

::: notes
Đây là khung lịch sử. Prompt engineering hỏi: mình nên nói gì với model. Context engineering hỏi: model cần thấy thông tin nào. Harness engineering hỏi rộng hơn: model cần sống trong môi trường nào để có thể làm việc thật. Ba làn sóng này không thay thế nhau. Chúng chồng lên nhau: vẫn cần prompt tốt, vẫn cần context tốt, nhưng bây giờ còn cần thiết kế cả môi trường vận hành.
:::

---

<!-- Slide 5 -->

## What goes wrong without one
You've seen most of these. They are not model failures. They are environment failures.
### Edits before reading
The agent opens the file, makes a guess, writes the patch. The product intent was three layers up in `docs/`. The agent never read it.
### Conventions in someone's head
"We always use cursor pagination, never offset." That rule is in the team's chat history. The agent has no idea.
### No memory between sessions
Yesterday's decision: "use the new auth middleware." Today's agent: rewrites the old one because it has no record of yesterday.
### Validation discovered too late
The agent finishes a feature. Tests pass. Then a human notices: it didn't handle the empty case, didn't respect the role boundary, didn't update the audit log.
"Early progress was slower than we expected, not because Codex was incapable, but because the environment was underspecified." — OpenAI

::: notes
Đọc chậm từng failure mode và hỏi lớp: ai đã từng gặp những lỗi này. Điểm chung là model thường không "ngu" theo nghĩa đơn giản; nó làm điều có vẻ hợp lý dựa trên những gì nó thấy. Vấn đề nằm ở phần nó không thấy: convention nằm trong đầu team, quyết định cũ nằm trong Slack, validation command không được ghi lại. Harness là nơi những kiến thức đó phải được đưa ra ánh sáng.
:::

---

<!-- Slide 6 -->

## The new bottleneck
### Old bottleneck
writing code
### New bottleneck
designing the environment
"The primary job of our engineering team became enabling the agents to do useful work."
— Ryan Lopopolo, OpenAI
What an engineer spends time on now:
- Designing the environment the agent works in
- Specifying intent precisely enough that an agent can act on it
- Building feedback loops so the agent can verify its own work
- Asking, on every failure: *"what capability is missing, and how do I make it legible?"*

::: notes
Nhấn mạnh sự dịch chuyển bottleneck. Trước đây chúng ta bị giới hạn bởi tốc độ viết code, nhớ API, và tránh lỗi cú pháp. Bây giờ agent có thể làm rất nhiều phần đó. Bottleneck mới là: ý định có đủ rõ không, môi trường có đủ thông tin không, và agent có vòng phản hồi để tự kiểm chứng không. Tên nghề vẫn là software engineer, nhưng phần việc đang thay đổi.
:::

---

<!-- Slide 7 -->

_Act 2_
# The mental model
Concepts, vocabulary, anatomy

::: notes
Chuyển sang phần hai. Sau khi đã thấy bối cảnh thay đổi, bây giờ mình cần cho sinh viên một mental model rõ ràng. Đi từ từ: đầu tiên là định nghĩa, sau đó là các bộ phận của harness, cuối cùng là thói quen suy nghĩ như một harness engineer.
:::

---

<!-- Slide 8 -->

## The equation
```text
Agent = Model + Harness
```
### Model
The intelligence. A text-in, text-out function that knows a lot but can do nothing.
### Harness
The system around the model that turns text-in, text-out into work in the world. Tools, state, feedback, constraints.
"A harness is every piece of code, configuration, and execution logic that isn't the model itself." — LangChain

::: notes
Đây là định nghĩa gọn nhất. Hãy vẽ ranh giới: một bên là model, gồm weights, transformer, sampling, khả năng dự đoán text. Bên còn lại là harness: prompt, tools, scripts, vòng lặp gọi model, parser, permission gate, test runner. Khi model thông minh hơn, harness không kém quan trọng đi; ngược lại, càng cần harness tốt để trí thông minh đó biến thành công việc thật.
:::

---

<!-- Slide 9 -->

## What a raw model cannot do
Every one of these becomes a feature of the harness.
| Limitation | Harness feature |
| --- | --- |
| Cannot remember between sessions | memory & durable state |
| Cannot execute code | tool calls & bash sandbox |
| Cannot reach live data | retrieval & filesystem |
| Cannot install packages | environment setup scripts |
| Cannot enforce constraints | middleware & permission gates |
"The main idea is that we want to convert a desired agent behavior into an actual feature in the harness." — LangChain

::: notes
Đi từng dòng trong bảng. Một raw model thật sự không tự nhớ qua các session, không tự chạy command, không tự lấy live data, không tự cài package, và không tự enforce constraint. Mỗi giới hạn ở cột trái tương ứng với một phản ứng kỹ thuật ở cột phải. Bài học: mỗi lần mình ước "giá mà agent tự biết làm X", rất có thể X nên trở thành một feature của harness.
:::

---

<!-- Slide 10 -->

## Three ways of thinking about a harness
### 1. Externalize
Move cognitive burden *out* of the model and *into* the environment. The model doesn't have to remember; the harness stores. The model doesn't have to know the convention; the harness enforces it.
### 2. Legibilize
Make the system *legible* to the agent. Logs, metrics, UI, file structure — the agent can see what's happening. *"What capability is missing, and how do we make it legible?"*
### 3. Enforce
Make the system *enforceable*. Not just "the agent should do X" — but X is checked before the work is accepted. Lint, test, type-check, schema validation, approval gates.
Source: arXiv [2604.08224](https://arxiv.org/abs/2604.08224) (externalization) + OpenAI's "legibility" framing

::: notes
Ba động từ này là xương sống của bài. Externalize: đừng bắt model nhớ mọi thứ; đưa kiến thức ra file, database, docs, trace. Legibilize: agent không thể suy luận tốt về thứ nó không nhìn thấy, nên logs, file structure, status, và validation output phải dễ đọc. Enforce: "agent nên làm" chỉ là mong muốn; "agent phải pass check này" mới là cơ chế. Khi thiết kế harness, gần như luôn là một trong ba việc này.
:::

---

<!-- Slide 11 -->

## The 7 primitives
Every harness, no matter who built it, has these 7 pieces. The names may vary; the work is the same.

1. **Filesystem** — durable storage, offloaded context, working memory
2. **Tools** — the verbs the agent can call: read, write, run, search
3. **Orchestration** — the loop that calls the model, parses, dispatches
4. **Memory** — long-term state that survives a session
5. **Middleware** — compaction, lint checks, safety gates
6. **Sandbox** — the isolated place where agent code actually runs
7. **Verification** — the loop that proves the work is done

"Harness engineering is how we build systems around models to turn them into work engines." — LangChain

::: notes
Bảy primitive này không cần học thuộc lòng, nhưng cần nhận ra được. Khi nhìn một coding agent, một framework, hoặc setup của chính mình, hãy hỏi: nó có filesystem không, có tools không, có orchestration không, có memory không, có middleware không, sandbox ra sao, và verification nằm ở đâu. Nếu một agent hay thất bại, thường là một primitive trong số này đang yếu hoặc bị thiếu.
:::

---

<!-- Slide 12 -->

## Case study: how we mapped it
We built `repository-harness` — a meta-harness that lives at the repo level. Here's how it covers the 7 primitives.
| Primitive | In repository-harness |
| --- | --- |
| Filesystem + Git | `AGENTS.md`, `docs/`, story packets |
| Tools | `harness-cli`: intake, story, trace, audit, propose |
| Orchestration | intake → story → trace → backlog loop |
| Memory | `harness.db` (SQLite) + `docs/decisions/` |
| Middleware | score-context, audit, intervention, score-trace |
| Sandbox | per-project isolated `harness.db` + scoped `scripts/` |
| Verification | story verify, verify-all, test matrix |
github.com/hoangnb24/repository-harness

::: notes
Đây là ví dụ cụ thể từ repository-harness. Nhấn mạnh rằng đây không phải mapping duy nhất; mỗi team có thể thiết kế khác. Điểm quan trọng là sinh viên biết cách nhìn một artifact và hỏi: phần này đang phục vụ primitive nào. AGENTS.md là filesystem/context. CLI là tools. Trace là observability và memory. Verify command là verification. Nếu thấy primitive nào thiếu, đó là feature tiếp theo của harness.
:::

---

<!-- Slide 13 -->

## The maturity ladder
A vocabulary for talking about how mature a harness is. From a recent arXiv paper.

- **H0 · Bare environment.** The model sees only a prompt. No policy, no state.
- **H1 · Scaffolding & policy.** `AGENTS.md`, intake rules, templates exist. Static.
- **H2 · Durable state.** A database. Traces, decisions, stories are recorded. Queryable.
- **H3 · Active observability.** Traces are scored, friction is grouped, regressions are attributed.
- **H4 · Mechanical verification.** Stories have verify-commands. Pre-close gate warns when proof is missing.
- **H5 · Self-improving.** Friction becomes a proposal. The harness proposes changes to itself.

Source: arXiv [2605.13357](https://arxiv.org/abs/2605.13357); extended to H5 in our `docs/HARNESS_MATURITY.md`

::: notes
Đây là slide từ vựng, không phải slide khoe maturity. Phần lớn sinh viên hoặc team nhỏ sẽ bắt đầu ở H0 hoặc H1, và điều đó hoàn toàn ổn. Giá trị của ladder là nó cho mình ngôn ngữ để nói: hiện tại repo chỉ có policy tĩnh, bước tiếp theo là durable state; hoặc hiện tại có trace rồi, bước tiếp theo là scoring và audit. "Cần AI tốt hơn" quá mơ hồ; "từ H1 lên H2" thì đo được.
:::

---

<!-- Slide 14 -->

_Act 3_
# The mindset + how to start
Practical, concrete, your-first-week stuff

::: notes
Chuyển sang phần thực hành. Bây giờ sinh viên đã có lịch sử và mental model, câu hỏi là: thứ hai tuần tới làm gì. Phần này không còn là thuật ngữ nữa, mà là thói quen: hỏi câu nào khi agent fail, ghi lại gì sau mỗi run, và bắt đầu nhỏ như thế nào.
:::

---

<!-- Slide 15 -->

## 5 questions a harness engineer asks
These are the diagnostic questions. Ask them when something goes wrong. Ask them when something goes right.
1. *What did the agent see?* What files did it read? What context did it have? Where did its knowledge come from?
2. *What could the agent do?* Which tools? Which commands? What was it allowed to change?
3. *What did the agent actually do?* Trace it. Don't guess. Look at the diff, the log, the trace.
4. *What did the agent miss?* What should it have seen? What decision did it not know about? What convention did it violate?
5. *What should future agents inherit?* Write it down. The answer to #4 is the input to the next harness.
"The fix was almost never 'try harder.'" — OpenAI

::: notes
Đây là năm câu hỏi sinh viên nên nhớ. Không cần nhớ hết thuật ngữ, nhưng cần nhớ cách debug agent. Agent đã thấy gì. Agent được phép làm gì. Agent thực sự đã làm gì. Agent đã bỏ lỡ điều gì. Và điều gì nên được lưu lại cho agent lần sau. Mỗi lỗi của agent là một tín hiệu: có thứ gì đó trong harness chưa đủ rõ, chưa đủ thấy được, hoặc chưa được enforce.
:::

---

<!-- Slide 16 -->

## The harness thinking worksheet
Use this before, during, and after an agent run.
```text
BEFORE THE RUN
  What is the agent's job, in one sentence?
  What files should it read first?
  What decisions must it inherit?
  What is the proof that the work is done?
  What should it NOT touch?

DURING THE RUN
  Did the agent read what I expected it to read?
  Is it about to make a change outside the lane?
  Does its diff match the intent?

AFTER THE RUN
  Trace recorded? Friction captured?
  Anything that surprised me? Why?
  Anything I want the next agent to know?
  What feature of the harness was missing?
```
Adapted from the OpenAI "Ralph Wiggum Loop" + LangChain's "working backwards from desired agent behavior"

::: notes
Worksheet này biến năm câu hỏi thành thao tác. Trước khi chạy agent: làm rõ intent, file cần đọc, decision cần kế thừa, proof of done, và boundary. Trong lúc chạy: quan sát agent có đi lệch lane không. Sau khi chạy: ghi trace, ghi friction, ghi điều gây bất ngờ. Phần sau cùng là phần nhiều người bỏ qua, nhưng chính nó làm harness học được từ kinh nghiệm.
:::

---

<!-- Slide 17 -->

## Your first harness, this week
You don't need our project. You don't need codex. Five actions, in order.
1. **Write an `AGENTS.md` for your project.** One file. What should the agent read first? What conventions? What's off-limits?
2. **Classify one task as tiny / normal / high-risk.** Use the checklist. Get used to the vocabulary.
3. **Add a verify command to one story.** If the agent does X, what command proves X happened? Run it.
4. **Record one decision.** "We chose cursor pagination." One sentence. One file. That's the harness's memory.
5. **Capture one piece of friction.** "The agent forgot to update the audit log." That's a backlog item for your harness.
Templates: `docs/templates/` in the repository-harness repo

::: notes
Làm cho bước đầu thật nhỏ. Không cần framework lớn, không cần vendor, không cần viết hệ thống phức tạp. AGENTS.md chỉ là một file Markdown. Verify command chỉ là một command rõ ràng. Decision record có thể là vài dòng giải thích tại sao team chọn một pattern. Friction note là câu "agent quên cập nhật audit log". Mỗi thứ làm trong 15 phút này đều là một mảnh của harness.
:::

---

<!-- Slide 18 -->

## The proof: this isn't philosophy
Same agent. Same model. Same prompts. The only thing that changed was the harness.
```text
Baseline   Phase2   Phase3   Phase4   Phase5
Compliance    ████████ 80.6  →  ██████████ 96.7  →  ███████████ 100  →  100  →  100
Trace Q.      1.8         →        █████████ 2.6  →  2.5        →  2.1        →  2.1
Lane acc.     5/6  →  ██████ 6/6  →  6/6  →  6/6  →  6/6
Functional    100%  →  100%  →  100%  →  100%  →  100%
```
Harness compliance went from 80.6% to 100% across five phases. Same agent. Same model. Same prompts. Different environment.
Source: `harness-benchmark/benchmark/runs/`

::: notes
Đây là phần chứng minh rằng bài này không chỉ là triết lý. Cùng một agent, cùng model, cùng prompt, chỉ thay đổi môi trường. Benchmark chạy cùng 6 task qua các phase của harness. Compliance tăng từ 80.6% lên 100%. Lane accuracy từ 5/6 lên 6/6. Functional vẫn 100% vì khả năng code của agent không đổi. Điều đổi là môi trường: policy, trace, validation, và feedback loop.
:::

---

<!-- Slide 19 -->

## The bare-vs-harness difference
Same task. Two repos. Watch the agent behave differently.
#### BARE REPO · no harness
```text
$ codex exec "add /api/folders"

[codex] reading project state... 3 files, no AGENTS.md
[codex] looking for folders module... not found
[codex] assuming a standard structure. creating src/routes/folders.js
[codex] adding a SELECT * FROM folders query
[codex] committing. PR opened.

[review] discovered:
  - query has no auth check
  - schema mismatch with /api/bookmarks
  - no test coverage
  - 3 follow-up issues filed manually
```
#### HARNESS REPO · repository-harness
```text
$ codex exec "add /api/folders"

[intake]  type=change_request lane=normal
          verify: npm test
[story]   US-024 created
          linked: docs/product/folders.md
          linked: docs/decisions/0008-auth-boundary.md
[codex]   reading AGENTS.md → intake → story → docs
[codex]   matches /api/bookmarks envelope
[codex]   reuses requireAuth + WorkspaceId scope
[codex]   adds cursor pagination per 0008
[codex]   writes unit + integration tests
[verify]  story verify US-024 → npm test → PASS
[trace]   score=2.8/3, friction=0
```
Demo: `bare-vs-harness.sh` in the project repo

::: notes
Đây là slide nên đọc rất chậm. Cùng task, cùng prompt, cùng agent, nhưng repo bên trái không có harness nên agent đoán structure, quên auth, không viết test. Repo bên phải có intake, story, decision, docs và verify command, nên agent hành xử khác hẳn. Harness engineering không nhất thiết tạo ra agent thông minh hơn; nó tạo ra agent đáng tin hơn trong một môi trường cụ thể.
:::

---

<!-- Slide 20 -->

## Live demo — install + intake + trace
```text
# 1. Install into any project
$ curl -fsSL "https://raw.githubusercontent.com/hoangnb24/repository-harness/main/scripts/install-harness.sh" \
    | bash -s -- --yes

# 2. Classify the work
$ ./scripts/bin/harness-cli intake \
    --type change_request \
    --summary "add /api/folders with auth" \
    --lane normal

# 3. Run the agent
$ codex exec "implement US-024"

# 4. Record what happened
$ ./scripts/bin/harness-cli trace \
    --summary "implemented /api/folders" \
    --outcome completed

# 5. Look at the state
$ ./scripts/bin/harness-cli audit
$ ./scripts/bin/harness-cli propose
```
All commands documented in `docs/HARNESS.md` · repo: github.com/hoangnb24/repository-harness

::: notes
Đây là tour 5 command. Cài harness bằng một lệnh curl. Intake để phân loại công việc. Agent vẫn chạy như bình thường, không cần thay đổi cách nghĩ quá nhiều. Sau đó trace ghi lại chuyện gì đã xảy ra. Audit và propose giúp nhìn trạng thái hiện tại và đề xuất cải thiện. Mục tiêu của demo là cho thấy harness không phải khái niệm xa vời; nó có thể bắt đầu bằng một vòng lặp rất nhỏ.
:::

---

<!-- Slide 21 -->

## 3 things we learned the hard way
### 1. Documentation is not the harness
A 10,000-line AGENTS.md is not better than a 50-line one. The harness is the *system*: docs + state + commands + verification. Docs alone are noise.
### 2. The bottleneck is the trace, not the model
We spent 6 months on prompt tweaks. We spent 6 weeks on trace scoring and friction capture. The second 6 weeks gave us more than the first 6 months.
### 3. The harness is a product, not a wrapper
If you treat it as glue, it stays glue. If you treat it as a versioned, tested, evolving artifact, it becomes the thing that compounds.
Anecdotal evidence from building `repository-harness` across 5 phases

::: notes
Ba bài học thật từ quá trình build. Một: tài liệu không tự nó là harness; harness là hệ thống gồm docs, state, command, verification, trace. Hai: trace quan trọng sớm hơn mình tưởng, vì nếu không có trace thì không biết harness cần học gì. Ba: hãy đối xử với harness như một product có version, test, changelog, benchmark. Khi version hóa nó, mình bắt đầu cải thiện nó có chủ đích hơn.
:::

---

<!-- Slide 22 -->

## Where the field is heading
```text
2025  coding agents        Claude Code, Codex CLI, Aider, Cursor
2026  harness engineering  OpenAI, LangChain, the arXiv wave
      ↑
      you are here
2026+ self-evolving harnesses  harnesses that write themselves
2027? harness-as-a-product  a deployable unit, not a wrapper
```
See: arXiv [2604.25850](https://arxiv.org/abs/2604.25850) (AHE), [2603.28052](https://arxiv.org/abs/2603.28052) (Meta-Harness), [2606.13643](https://arxiv.org/abs/2606.13643) (Recursive Agent Harnesses)

::: notes
Nói về hướng phát triển của lĩnh vực. Self-evolving harness nghĩa là harness đọc trace của chính nó và đề xuất cách cải thiện. Meta-harness tìm hoặc tối ưu cách tổ chức harness. Recursive agent harness nghĩa là một agent có thể tạo ra các sub-harness hoặc subagent để chia việc. Với sinh viên, câu hỏi thú vị là: trong bảy primitive, mình muốn học sâu primitive nào trước.
:::

---

<!-- Slide 23 -->

## 5 papers to read after this
If you want to go deeper. Not required. But if you're going to cite this stuff in a paper, start here.

1. **arXiv 2605.13357** — AI Harness Engineering: A Runtime Substrate. 11 component responsibilities, H0-H3 maturity ladder. *The closest academic match to the practice.*
2. **arXiv 2604.08224** — Externalization in LLM Agents. The memory/skills/protocols/harness survey. The historical frame.
3. **arXiv 2605.18747** — Code as Agent Harness. "The repo IS the harness." A survey framing.
4. **arXiv 2603.28052** — Meta-Harness. End-to-end optimization of harness code from traces and scores.
5. **arXiv 2606.13643** — Recursive Agent Harnesses. Subagent harnesses as the recursive unit.

All abstracts: see the research notes for this talk.

::: notes
Nếu chỉ đọc một paper sau buổi này, hãy bắt đầu với 2605.13357 vì nó cho nhiều vocabulary gần nhất với practice. 2604.08224 giúp hiểu externalization. 2605.18747 giúp nhìn repo và code như một phần của harness. Hai paper cuối là hướng frontier: harness tự tối ưu và harness đệ quy. Không cần đọc hết ngay; mục tiêu là có bản đồ để đi sâu sau này.
:::

---

<!-- Slide 24 -->

## Vocabulary
Pin this slide. It will save you three Stack Overflow searches.

- **agent** — model + harness. A system that can act, not just answer.
- **harness** — everything around the model. Code, config, loop, tools, state, checks.
- **tool** — a function the model can call. Read, write, search, run, etc.
- **MCP** — Model Context Protocol. A standard way to expose tools to a model.
- **skill** — a reusable procedure the model can load on demand.
- **subagent** — an agent spawned by another agent, with isolated context.
- **middleware** — code that wraps the loop. Compaction, lint checks, gates.
- **trace** — a record of one agent run. Inputs, actions, output, friction.
- **friction** — anything that made the agent's job harder than it should have been.
- **legibility** — whether the agent can see what's happening in the system it's working on.

::: notes
Đây là slide tham chiếu. Nếu sinh viên bị ngợp, hãy nói rằng chỉ cần nhớ hai từ trước: harness và friction. Harness là môi trường quanh model. Friction là những gì làm agent làm việc khó hơn mức cần thiết. Trace ghi lại friction, backlog theo dõi friction, và proposal cố gắng loại bỏ friction. Đó là vòng lặp cải thiện.
:::

---

<!-- Slide 25 -->

## Try it tonight
### English
```text
curl -fsSL "https://raw.githubusercontent.com/hoangnb24/repository-harness/main/scripts/install-harness.sh" \
  | bash -s -- --yes

# then in your project:
# 1. write an AGENTS.md
# 2. classify one task
# 3. add a verify command
# 4. record one decision
# 5. capture one friction
```
### Tiếng Việt
```text
# Cài harness vào project bất kỳ:
curl -fsSL "https://raw.githubusercontent.com/hoangnb24/repository-harness/main/scripts/install-harness.sh" \
  | bash -s -- --yes

# Rồi trong project của bạn:
# 1. viết AGENTS.md
# 2. phân loại 1 task
# 3. thêm 1 verify command
# 4. ghi lại 1 decision
# 5. capture 1 friction
```
Start with one file. One decision. One friction note. The harness grows from there.

::: notes
Đây là khoảnh khắc song ngữ cho audience Việt Nam và quốc tế. Nhấn mạnh rằng hai cột nói cùng một điều: bắt đầu bằng 5 hành động nhỏ. Đây không phải project plan dài hạn, mà là kế hoạch cho tối nay hoặc sáng thứ hai. Không cần phải dùng đúng tool này; thứ quan trọng là discipline: ghi context, ghi decision, ghi validation, ghi friction.
:::

---

<!-- Slide 26 -->

## The harness mindset, in one sentence
Every time an agent fails,
ask: *what capability is missing,*
and *how do I make it legible and enforceable?*
Then build the smallest piece that fixes it.
Then write it down so the next agent inherits it.
That's the discipline.

::: notes
Đây là câu kết, đọc chậm. Mỗi khi agent fail, đừng chỉ nói "model chưa đủ tốt". Hỏi: capability nào bị thiếu, làm sao để capability đó trở nên thấy được và enforce được. Sau đó build phần nhỏ nhất để sửa, rồi ghi lại để agent lần sau kế thừa. Làm 20 lần thì có một harness. Làm 200 lần thì có một discipline.
:::

---

<!-- Slide 27 -->

# Q & A
github.com/hoangnb24/repository-harness
codeharness.kuckit.dev · @hoangmrb
"The app is what users touch. The harness is what agents touch."
— Thank you. —

::: notes
Giữ sân khấu ở phần Q&A. Nếu lớp im lặng, hỏi ngược lại: trong project của bạn, điều đầu tiên muốn làm cho agent thấy rõ hơn là gì. Hoặc: trong bảy primitive, primitive nào đang yếu nhất trong setup hiện tại của bạn. Những câu hỏi tốt nhất thường đến sau khi mọi người đã liên hệ bài nói với repo của chính họ.
:::
