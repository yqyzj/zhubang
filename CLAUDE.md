# CLAUDE.md

Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.

## 5. 项目硬约束（zbhugo）

**URL 与电话强制规则，违反即为缺陷：**

- **URL 不允许出现中文**：所有页面 URL、permalink、内链 `href`、canonical、og:url、sitemap、面包屑、分页链接等，必须使用纯英文/拼音/数字/连字符，不得包含任何中文字符。Markdown 文件名、`slug`、`[permalinks]` 配置均需保证生成的 URL 为纯 ASCII。
- **电话号码必须可以点击拨号**：站点内任意位置出现的电话号码（含页眉、页脚、CTA、浮动组件、正文、Markdown、JSON-LD 等）必须使用 `<a href="tel:号码">号码</a>` 形式包裹，禁止纯文本电话号码。电话号统一从 `hugo.toml` 的 `params.phone` 读取，避免硬编码不一致。

- **HTML 标签不得有前导空格**：Markdown 文件中的 HTML 代码（`<div>`、`</div>`、`<section>`、`<ul>` 等）必须顶格书写，前面不得有 4 个或更多空格。前导空格会导致 Hugo 将 HTML 标签解析为代码块（`<pre><code>`），破坏页面 DOM 结构，导致后续元素嵌套错误、CTA/页脚等版块宽度异常。

**自查清单（每次改动后必查）：**
1. 新增/修改的页面 URL 是否纯 ASCII？
2. 新增/修改的页面中电话号码是否可点击拨号？


