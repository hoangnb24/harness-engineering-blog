# Harness Engineering — A Student's Guide

Visible slide text: English. Speaker notes: Vietnamese.

This v2 deck is structured as a connected teaching path: why the field changed, what a harness is, how to practice the skill, and how `repository-harness` applies it.

---

<!-- Slide 1 -->

# Harness Engineering

## A student's guide to building reliable coding-agent workflows

What changed. What a harness is. How to practice it this week.

Hoang · kuckit.dev · 2026

::: notes
Chào các bạn. Hôm nay mình muốn nói về Harness Engineering, nhưng không phải như một buzzword mới trong AI. Mình muốn nói về nó như một kỹ năng thực hành. Nếu các bạn dùng coding agent như Codex, Claude Code, Cursor, hay Aider, câu hỏi không chỉ là "model nào thông minh hơn", mà là "mình tạo môi trường như thế nào để agent làm việc đáng tin hơn". Cuối buổi này, mình muốn các bạn có thể mang về một framework rất cụ thể để áp dụng vào repo của mình.
:::

---

<!-- Slide 2 -->

## What you should take away

By the end, you should be able to:

1. Explain why `Agent = Model + Harness`
2. Diagnose an agent failure without blaming the model first
3. Turn a vague task into a small, verifiable story packet
4. Add one useful harness artifact to your own repo
5. Practice the loop until it becomes muscle memory

::: notes
Trước khi đi vào chi tiết, mình muốn các bạn biết mình sẽ lấy gì từ buổi này. Không phải chỉ là hiểu một định nghĩa. Sau buổi này, các bạn nên giải thích được vì sao agent không chỉ là model, mà là model cộng với harness. Các bạn cũng nên biết cách nhìn một agent failure và hỏi: lỗi này do model thật sự yếu, hay do repo chưa cho agent đủ context, tool, boundary, hoặc validation. Và quan trọng nhất: các bạn sẽ có một bài tập nhỏ để luyện trong tuần này.
:::

---

<!-- Slide 3 -->

## The practice loop

```text
Observe failure
  → name the missing capability
  → make it visible
  → make it enforceable
  → record it for the next agent
```

That loop is the muscle memory.

::: notes
Các bạn hãy giữ loop này trong đầu, vì gần như toàn bộ bài nói hôm nay sẽ quay lại đây. Khi agent fail, phản xạ đầu tiên của mình không nên là "model dở quá". Phản xạ nên là: agent đang thiếu capability nào. Nó thiếu context? Thiếu quyền gọi tool? Thiếu boundary? Thiếu command để chứng minh done? Khi tìm ra capability thiếu, mình làm nó visible, làm nó enforceable, rồi ghi lại để agent sau được kế thừa. Đây chính là muscle memory của harness engineering.
:::

---

<!-- Slide 4 -->

## The shift

> "Humans steer. Agents execute."  
> — Ryan Lopopolo, OpenAI

OpenAI's framing:

- The human specifies intent
- The agent does more of the mechanical work
- The engineer designs the environment that makes the work reliable

Source: [openai.com/index/harness-engineering/](https://openai.com/index/harness-engineering/)

::: notes
Để hiểu vì sao chuyện này quan trọng, mình muốn bắt đầu bằng một câu của OpenAI: "Humans steer. Agents execute." Nghĩa là con người vẫn là người định hướng. Nhưng agent bắt đầu làm nhiều phần công việc cơ học hơn: sửa file, chạy test, mở PR, lặp lại. Khi agent bắt đầu execute thật, mình không thể chỉ viết prompt rồi hy vọng. Mình cần lane cho agent đi, signal để agent biết đúng sai, guardrail để agent không vượt biên, và feedback để agent học từ lần trước.
:::

---

<!-- Slide 5 -->

## The old bottleneck vs the new bottleneck

| Before coding agents | With coding agents |
|---|---|
| Writing every line | Specifying the work clearly |
| Remembering every convention | Making conventions visible |
| Manually checking everything | Designing verification gates |
| Fixing one failure at a time | Turning failures into reusable context |

::: notes
Các bạn nhìn bảng này như một sự dịch chuyển kỹ năng. Trước đây, bottleneck lớn là tự viết từng dòng code và tự nhớ mọi convention. Bây giờ, khi có agent, bottleneck chuyển sang việc mình mô tả công việc rõ đến đâu, convention có nằm trong repo hay chỉ nằm trong đầu người, và correctness có được kiểm chứng bằng command hay chỉ bằng cảm giác. Vì vậy software engineering không biến mất. Nó mở rộng thêm một lớp mới: thiết kế môi trường làm việc cho agent.
:::

---

<!-- Slide 6 -->

## A small failure story

```text
Task: "Add /api/folders for the current user"

Agent creates:
  src/routes/folders.js
  SELECT * FROM folders
  no auth check
  no pagination
  no tests
```

The code may run. The workflow failed.

::: notes
Bây giờ mình đưa một ví dụ nhỏ. Mình bảo agent: thêm `/api/folders` cho current user. Agent tạo file mới, viết `SELECT * FROM folders`, không auth check, không pagination, không test. Code có thể chạy. Nhưng workflow đã fail. Tại sao? Vì agent không biết pattern endpoint hiện có nằm ở đâu, không biết boundary về auth, không biết response shape cần reuse, và không có validation bắt buộc. Đây là loại failure mà harness engineering muốn xử lý.
:::

---

<!-- Slide 7 -->

## Failure is a signal

When an agent fails, ask:

| Symptom | Likely missing harness capability |
|---|---|
| Wrong files edited | Repo map or task boundary |
| Old decision reopened | Decision record |
| No tests written | Validation matrix |
| Unsafe query added | Safety boundary |
| Same mistake repeated | Trace + feedback loop |

::: notes
Điểm mình muốn các bạn nhớ là: failure không chỉ là một bug cần fix. Failure là một tín hiệu. Nếu agent sửa sai file, có thể repo thiếu map hoặc task thiếu boundary. Nếu agent bỏ test, có thể thiếu validation matrix. Nếu agent tạo query không an toàn, có thể thiếu safety boundary. Nếu cùng một lỗi lặp lại nhiều lần, có thể chúng ta không ghi trace và không đưa bài học đó ngược lại vào repo. Nói cách khác, mỗi failure đang chỉ cho mình biết harness thiếu mảnh nào.
:::

---

<!-- Slide 8 -->

## The simplest definition

```text
Agent = Model + Harness
```

The model predicts.

The harness lets prediction become action:

- tools
- files
- memory
- permissions
- feedback
- verification

::: notes
Đây là định nghĩa đơn giản nhất của cả buổi: Agent bằng Model cộng Harness. Model là phần dự đoán, suy luận, viết kế hoạch, viết code. Nhưng model một mình không sửa file, không chạy test, không nhớ quyết định của team, và không tự enforce rule. Harness là mọi thứ xung quanh model giúp prediction trở thành action: tool, file, memory, permission, feedback, verification. Từ đây về sau, mỗi khi thấy agent hành xử sai, các bạn hãy hỏi: vấn đề nằm ở model, hay nằm ở harness?
:::

---

<!-- Slide 9 -->

## View 1 — Model vs Harness

| Model | Harness |
|---|---|
| Knows patterns | Provides local context |
| Generates plans/code | Gives tools to act |
| Can be inconsistent | Adds checks and gates |
| Has limited session memory | Stores durable state |
| Needs prompts | Provides operating environment |

Student question: *Which side of the line is the problem on?*

::: notes
View đầu tiên là ranh giới giữa model và harness. Model biết nhiều pattern chung, nhưng harness mới cung cấp context local của repo. Model có thể sinh code, nhưng harness mới cho nó tool để hành động. Model có thể không ổn định, nhưng harness thêm check và gate. Vì vậy khi debug, đừng bắt đầu bằng câu "đổi model nào đây". Hãy bắt đầu bằng câu trên slide: vấn đề đang nằm ở phía nào của đường ranh này?
:::

---

<!-- Slide 10 -->

## View 2 — Context

Agents need five layers of context:

1. Task: what to do now
2. Session: what happened in this run
3. Repo instructions: how this repo works
4. Decision history: why things are this way
5. Model knowledge: what the model already learned elsewhere

Reliable work depends most on layers 3 and 4.

::: notes
View thứ hai là context. Khi mới dùng agent, chúng ta thường tập trung vào task prompt: "hãy làm việc này". Nhưng agent trong repo cần nhiều hơn vậy. Nó cần biết chuyện gì xảy ra trong session này, repo này có rule gì, và vì sao team đã chọn những decision hiện tại. Layer 3 và layer 4 đặc biệt quan trọng: repo instructions và decision history. Nếu hai layer này thiếu, agent sẽ dựa vào kiến thức chung từ model, và kiến thức chung thường không đủ cho repo cụ thể của các bạn.
:::

---

<!-- Slide 11 -->

## View 3 — Workflow

A harness is not just documentation.

It is a path:

```text
intake
  → story packet
  → agent execution
  → verification gate
  → human review
  → decision / trace record
```

::: notes
View thứ ba là workflow. Mình muốn sửa một hiểu lầm: harness không phải là một file tài liệu thật dài. Một file `AGENTS.md` dài 10.000 dòng không tự động làm agent tốt hơn. Harness là con đường mà công việc đi qua. Task đi vào bằng intake. Nó được đóng gói thành story packet. Agent execute trong boundary. Sau đó có verification gate, human review, rồi decision hoặc trace được ghi lại. Tài liệu là một phần của harness, nhưng harness thật sự là workflow.
:::

---

<!-- Slide 12 -->

## View 4 — Evidence

Do not ask, "Did the agent seem right?"

Ask:

1. What did it read?
2. What did it change?
3. What command proved it?
4. What did review discover?
5. What should the next agent inherit?

Evidence turns vibes into engineering.

::: notes
View thứ tư là evidence. Khi review output của agent, đừng chỉ hỏi "nhìn có ổn không". Hãy hỏi: agent đã đọc gì, đã đổi gì, command nào chứng minh đúng, review phát hiện điều gì, và lần sau agent nên kế thừa bài học nào. Nếu không có evidence, chúng ta chỉ review bằng cảm giác. Harness engineering muốn biến cảm giác thành dữ liệu: diff, command, result, trace, friction. Evidence là thứ làm cho workflow trở thành engineering.
:::

---

<!-- Slide 13 -->

## View 5 — Repository Harness

At the repo level, the harness becomes files and commands:

| Need | Repo artifact |
|---|---|
| Operating rules | `AGENTS.md` |
| System map | `docs/architecture.md` |
| Proof of correctness | validation matrix |
| Bounded task | story packet |
| Durable memory | decision records |
| Learning loop | traces + friction log |

::: notes
View thứ năm là repo-level harness. Đây là lúc khái niệm biến thành file và command. Nếu cần operating rules, dùng `AGENTS.md`. Nếu cần system map, viết architecture doc. Nếu cần proof of correctness, tạo validation matrix. Nếu task quá mơ hồ, dùng story packet. Nếu agent cứ mở lại decision cũ, viết decision record. Nếu muốn hệ thống học từ lỗi, ghi trace và friction. Các artifact này nhỏ, nhưng mỗi cái thêm một capability cụ thể cho agent.
:::

---

<!-- Slide 14 -->

## The externalization arc

```text
Prompt engineering   → put better words in the prompt
Context engineering  → put better knowledge around the task
Harness engineering  → put better environment around the model
```

Each wave moves work out of the model and into the system.

Source: [arXiv 2604.08224](https://arxiv.org/abs/2604.08224)

::: notes
Nếu nhìn rộng hơn, chúng ta đang đi qua một quá trình externalization. Prompt engineering nói: chọn từ ngữ tốt hơn trong prompt. Context engineering nói: đưa knowledge tốt hơn vào quanh task. Harness engineering nói: thiết kế cả môi trường quanh model. Ba thứ này không cạnh tranh với nhau. Các bạn vẫn cần prompt tốt. Vẫn cần context tốt. Nhưng khi agent bắt đầu hành động trong repo thật, các bạn còn cần environment tốt.
:::

---

<!-- Slide 15 -->

## Three harness moves

When something fails, choose one move:

| Move | Meaning | Example |
|---|---|---|
| Externalize | Move knowledge out of heads | write a decision record |
| Legibilize | Make state visible to the agent | add repo map or trace |
| Enforce | Make correctness checkable | add verify command |

::: notes
Bây giờ mình muốn các bạn có ba động tác thực hành. Một là externalize: đưa kiến thức ra khỏi đầu người và đặt nó vào repo. Hai là legibilize: làm cho trạng thái hệ thống nhìn thấy được với agent. Ba là enforce: biến một điều "nên làm" thành một check bắt buộc. Khi gặp failure, hãy thử hỏi: lỗi này cần externalize, legibilize, hay enforce?
:::

---

<!-- Slide 16 -->

## Exercise 1 — Diagnose the failure

Given this review comment:

> "The endpoint works, but it returns data from other users."

Diagnose it:

1. What did the agent miss?
2. Which harness capability was missing?
3. What artifact would prevent this next time?

Expected answer: safety boundary + decision record + integration test.

::: notes
Mình muốn các bạn thử luyện ngay. Review comment nói: endpoint chạy được, nhưng trả data của user khác. Đừng vội sửa code trong đầu. Hãy diagnose như một harness engineer. Agent đã miss gì? Có thể nó miss auth boundary. Harness thiếu capability nào? Có thể thiếu safety boundary hoặc decision record về workspace scope. Artifact nào giúp lần sau? Có thể là integration test và decision record. Bài tập này không nhằm tìm một đáp án duy nhất; nó luyện thói quen map symptom sang missing capability.
:::

---

<!-- Slide 17 -->

## The story packet

The story packet turns a vague ask into a bounded unit of work.

```md
Problem:
User outcome:
Relevant files:
Constraints:
Acceptance criteria:
Validation commands:
Out of scope:
```

It answers: *what does done mean?*

::: notes
Artifact đầu tiên mình muốn các bạn luyện là story packet. Story packet biến một yêu cầu mơ hồ thành một đơn vị công việc có boundary. Nó trả lời những câu rất thực tế: user problem là gì, file nào liên quan, constraint nào không được vi phạm, acceptance criteria là gì, command nào chứng minh done, và cái gì nằm ngoài scope. `AGENTS.md` nói repo hoạt động như thế nào; story packet nói task lần này phải làm gì.
:::

---

<!-- Slide 18 -->

## From vague prompt to story packet

Vague:

> "Add a profile page."

Harnessed:

```md
What to build: Profile page with editable display name
Where to work: src/pages/profile.tsx, src/api/profile.ts
Constraints: do not change auth middleware
Acceptance: load, edit, save, error state
Validate: npm test -- profile && npm run typecheck
Out of scope: avatar upload, billing settings
```

::: notes
Các bạn nhìn sự khác biệt ở đây. "Add a profile page" nghe đơn giản, nhưng agent phải đoán rất nhiều: profile nào, file nào, có auth không, save flow ra sao, có avatar không, validate thế nào. Bản harnessed không dài hơn quá nhiều, nhưng nó giảm số thứ agent phải đoán. Đây là cách các bạn giao việc cho agent giống như giao việc cho một bạn junior mới vào team: không cần viết tiểu thuyết, nhưng phải nói rõ lane và definition of done.
:::

---

<!-- Slide 19 -->

## Exercise 2 — Rewrite the task

Rewrite this into a story packet:

> "Fix checkout bugs."

Minimum fields:

- user-facing problem
- likely files to inspect
- constraints
- acceptance criteria
- validation command

::: notes
Bây giờ đến lượt các bạn. Prompt là "Fix checkout bugs". Nếu đưa nguyên câu này cho agent, agent sẽ phải đoán gần như mọi thứ. Trong 2 phút, hãy thử viết lại thành story packet tối thiểu: user-facing problem là gì, agent nên inspect file nào, constraint nào quan trọng, acceptance criteria là gì, và command nào chứng minh fix. Khi làm bài này, điều mình muốn các bạn cảm nhận là: specification rõ không phải để làm chậm agent; nó làm agent ít đi sai hơn.
:::

---

<!-- Slide 20 -->

## The validation matrix

Validation should not be invented at the end.

| Change type | Required checks |
|---|---|
| Docs only | lint / link check |
| UI component | unit tests + build |
| API change | unit + integration + typecheck |
| Database migration | migration validation + human approval |
| Auth or billing | full suite + security review |

::: notes
Sau story packet, phần tiếp theo là validation. Một lỗi rất phổ biến là đến cuối mới hỏi: "À, phải chạy test nào nhỉ?" Validation matrix đưa câu trả lời đó lên trước. Nếu là docs, check nhẹ. Nếu là UI, unit test và build. Nếu là API, thêm integration và typecheck. Nếu là auth hoặc billing, phải có full suite và review kỹ hơn. Đây là enforcement: done không còn là "trông có vẻ được", mà là "đã pass đúng check cho loại thay đổi này".
:::

---

<!-- Slide 21 -->

## Decision records

Decision records prevent agents from reopening old debates.

```md
# Decision: Use cursor pagination

Context:
Offset pagination caused slow queries on large workspaces.

Decision:
All list endpoints use cursor pagination.

What would reopen this:
A measured product requirement for random page jumps.
```

::: notes
Validation giúp chứng minh hiện tại. Decision record giúp kế thừa quá khứ. Ví dụ team đã quyết định dùng cursor pagination vì offset pagination chậm. Nếu quyết định này chỉ nằm trong đầu một người, agent có thể "cải tiến" bằng cách quay lại offset. Decision record nói rõ context, decision, và khi nào được reopen. Nó không cần dài. Chỉ cần đủ để agent lần sau không mở lại cùng một tranh luận.
:::

---

<!-- Slide 22 -->

## Trace and friction

After a run, capture:

```text
Task:
Files read:
Files changed:
Commands run:
Result:
Friction:
What future agents should know:
```

The trace is how the harness learns.

::: notes
Sau một run, đừng chỉ nhìn final diff rồi đóng tab. Hãy ghi lại trace. Task là gì, agent đọc file nào, đổi file nào, chạy command nào, kết quả ra sao. Và đặc biệt: friction là gì. Agent thiếu thông tin ở đâu? Nó hỏi lại điều gì? Nó đi sai lane chỗ nào? Nếu không ghi friction, session tiếp theo sẽ lặp lại lỗi cũ. Nếu ghi friction, các bạn có nguyên liệu để cải thiện harness.
:::

---

<!-- Slide 23 -->

## The harness worksheet

Before the run:

- What is the job?
- What should the agent read first?
- What must it not touch?
- What proves done?

After the run:

- What surprised us?
- What friction should become repo context?
- What check should become mandatory?

::: notes
Nếu các bạn chỉ nhớ một slide thực hành, hãy nhớ slide này. Trước khi chạy agent, hỏi bốn câu: job là gì, agent nên đọc gì trước, không được đụng gì, và done được chứng minh bằng gì. Sau khi chạy, hỏi tiếp: điều gì làm mình bất ngờ, friction nào nên trở thành repo context, và check nào nên bắt buộc từ lần sau. Worksheet này là cách biến harness engineering thành thói quen hằng ngày.
:::

---

<!-- Slide 24 -->

## Repository-harness: applying the model

`repository-harness` packages the practice loop into repo artifacts:

```text
intake      → classify the work
story       → bound the task
verify      → prove completion
trace       → record what happened
audit       → find harness gaps
propose     → suggest improvements
```

::: notes
Bây giờ mình quay lại `repository-harness`. Sau tất cả những gì vừa học, các bạn sẽ thấy tool này không phải magic. Nó chỉ đóng gói practice loop thành command và artifact. `intake` để classify work. `story` để bound task. `verify` để chứng minh done. `trace` để ghi lại chuyện gì đã xảy ra. `audit` để tìm gap trong harness. `propose` để biến friction thành cải tiến. Tool chỉ là hình dạng cụ thể của discipline.
:::

---

<!-- Slide 25 -->

## Bare repo vs harnessed repo

Same task. Same model. Different environment.

| Behavior | Bare repo | Harnessed repo |
|---|---|---|
| Reads policy first | no | yes |
| Reuses API pattern | no | yes |
| Respects auth boundary | no | yes |
| Writes tests | no | yes |
| Runs verify command | no | yes |
| Records trace | no | yes |

::: notes
Các bạn nhìn bảng này như một thí nghiệm tư duy. Cùng task, cùng model, nhưng environment khác nhau. Bare repo không nói rõ policy, pattern, auth boundary, test, verify, trace. Harnessed repo có những thứ đó. Kết quả là agent hành xử khác. Đây là ý chính: harness không thay đổi weights của model, nhưng thay đổi môi trường mà model hành động trong đó. Và môi trường đó có thể làm output đáng tin hơn rất nhiều.
:::

---

<!-- Slide 26 -->

## The five-minute demo

```bash
# 1. Install
curl -fsSL "https://raw.githubusercontent.com/hoangnb24/repository-harness/main/scripts/install-harness.sh" \
  | bash -s -- --yes

# 2. Classify
./scripts/bin/harness-cli intake --type change_request --lane normal

# 3. Create story
./scripts/bin/harness-cli story add

# 4. Verify
./scripts/bin/harness-cli story verify

# 5. Trace
./scripts/bin/harness-cli trace --outcome completed
```

::: notes
Nếu mình demo live, mình sẽ không trình bày đây như một list command khô khan. Mình muốn các bạn nhìn nó như một vòng lặp. Đầu tiên cài harness. Sau đó classify work. Tiếp theo tạo story. Khi agent làm xong, verify. Cuối cùng trace. Nếu các bạn không dùng đúng tool này cũng không sao. Điều mình muốn các bạn copy là sequence: classify, bound, verify, record.
:::

---

<!-- Slide 27 -->

## What to practice this week

Pick one small repo and do five reps:

1. Write a one-screen `AGENTS.md`
2. Convert one vague task into a story packet
3. Add one validation matrix row
4. Record one decision
5. Capture one trace after an agent run

Five reps build the first muscle memory.

::: notes
Đây là homework của buổi này. Đừng cố build một harness hoàn chỉnh ngay. Hãy chọn một repo nhỏ và làm năm rep. Viết một `AGENTS.md` ngắn. Chuyển một task mơ hồ thành story packet. Thêm một dòng vào validation matrix. Ghi một decision. Capture một trace sau khi chạy agent. Một lần thì các bạn hiểu concept. Năm lần thì tay bắt đầu quen. Đó là muscle memory.
:::

---

<!-- Slide 28 -->

## How to know it is working

Measure behavior, not vibes:

- fewer clarification loops
- smaller diffs
- fewer boundary violations
- validation runs before review
- repeated mistakes become repo updates
- future agents inherit past decisions

::: notes
Làm sao biết mình đang tiến bộ? Đừng đo bằng cảm giác "repo có vẻ xịn hơn". Hãy đo behavior. Agent có hỏi lại ít hơn không? Diff có nhỏ và dễ review hơn không? Có ít boundary violation hơn không? Validation có chạy trước khi human review không? Lỗi lặp lại có trở thành update trong repo không? Nếu những hành vi này thay đổi, harness của các bạn đang thật sự tốt hơn.
:::

---

<!-- Slide 29 -->

## The research map

Where the ideas show up:

- OpenAI: engineers steer agents by designing the environment
- LangChain: the harness is everything around the model
- Externalization papers: move capability out of the model into infrastructure
- Harness papers: tools, memory, state, verification, trace, and self-improvement

The practice is new. The pattern is becoming clear.

::: notes
Nếu các bạn muốn đọc sâu hơn, đây là bản đồ nghiên cứu. OpenAI nói về engineer steer agent bằng cách thiết kế environment. LangChain nói harness là mọi thứ xung quanh model. Các paper về externalization nói về việc đưa capability ra khỏi model và vào infrastructure. Các paper về harness nói về tools, memory, state, verification, trace, và self-improvement. Các nguồn này dùng từ khác nhau, nhưng đang hội tụ vào cùng một pattern.
:::

---

<!-- Slide 30 -->

## Read next

Start here:

1. OpenAI — Harness Engineering
2. LangChain — The Anatomy of an Agent Harness
3. arXiv 2604.08224 — Externalization in LLM Agents
4. arXiv 2605.13357 — AI Harness Engineering
5. repository-harness docs and templates

Read with one question: *what should I add to my repo?*

::: notes
Khi đọc những nguồn này, đừng đọc như một literature survey thuần túy. Hãy đọc với một câu hỏi thực hành: sau khi đọc xong, mình nên thêm gì vào repo của mình. Một decision record? Một validation gate? Một trace format? Một story template? Cách đọc đó biến research thành practice. Và với chủ đề này, practice mới là thứ làm các bạn giỏi hơn.
:::

---

<!-- Slide 31 -->

## The closing sentence

Every time an agent fails:

1. Find the missing capability
2. Make it visible
3. Make it enforceable
4. Record it
5. Let the next agent inherit it

That is harness engineering.

::: notes
Mình muốn kết thúc bằng đúng loop ban đầu. Mỗi khi agent fail, hãy tìm capability thiếu. Làm nó visible. Làm nó enforceable. Ghi lại. Và để agent tiếp theo được kế thừa. Nếu các bạn nhớ năm bước này, các bạn có thể dùng nó với bất kỳ coding agent nào: Codex, Claude Code, Cursor, Aider, hay tool mới trong tương lai. Đó là Harness Engineering.
:::

---

<!-- Slide 32 -->

# Q & A

github.com/hoangnb24/repository-harness

codeharness.kuckit.dev · @hoangmrb

> The app is what users touch.  
> The harness is what agents touch.

::: notes
Cảm ơn các bạn. Nếu có câu hỏi, mình rất muốn nghe từ repo thật của các bạn. Agent của bạn thường fail ở đâu? Nó thiếu context, thiếu boundary, thiếu validation, hay thiếu memory? Và nếu tuần này chỉ được thêm một artifact vào repo, các bạn sẽ thêm gì: `AGENTS.md`, validation matrix, story packet, decision record, hay trace? Mình nghĩ câu trả lời cho câu hỏi đó chính là điểm bắt đầu của harness đầu tiên của các bạn.
:::
