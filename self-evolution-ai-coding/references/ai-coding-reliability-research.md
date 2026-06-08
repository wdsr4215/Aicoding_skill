# AI Coding 可靠性研究与工程化守卫

## 使用场景

当任务涉及大型重构、AI 生成代码、Agent 自主开发、旧系统迁移、AI 入口改造、模型输出解析、代码安全、技术债清理或“单次开发要尽量高置信度”时读取本文件。

本文件是泛用规则，不绑定具体项目。它把公开研究、大厂文档和本地踩坑转换成可执行的工程守卫。

## 关键结论

### 1. 任务必须小而清晰

GitHub Copilot 文档强调，AI agent 更适合清晰、范围明确、有验收标准和文件指向的任务。

落地规则：

- 复杂任务先拆成可验证切片。
- 每个切片必须有输入、输出、owner、验收标准。
- 不要让 agent 在没有边界时“一口气重构全系统”。

### 2. 先探索，再计划，再编码

Anthropic 的 Claude Code 最佳实践明确建议把探索、计划、实现、提交分开；如果任务跨多文件或不熟悉代码，直接编码容易解错问题。

落地规则：

- 修改前先读项目地图和关键文件。
- 不确定 owner 时先搜索入口和调用链。
- 计划不是长篇汇报，而是明确改哪、为什么、怎么验。

### 3. 必须给 AI 可运行的验证信号

Anthropic 文档把“给 Claude 一个可执行检查”视为闭环关键：测试、构建、lint、截图、fixture diff 都可以。

落地规则：

- 完成前至少跑一个真实信号。
- UI 改动优先截图或浏览器检查。
- 后端改动优先单测、接口 smoke、数据库读取或日志验证。
- 不能验证时说明阻断原因和下一个最小验证方式。

### 4. 上下文是稀缺资源

Anthropic 指出上下文窗口过满会让模型更容易忘记早期约束。GitHub 也建议用项目级自定义指令、路径级指令和 MCP 来提供稳定上下文。

落地规则：

- `SKILL.md` 只放入口和工作流，细节进 `references/`。
- 项目结构和长期规则写入项目地图和治理文件。
- 不把全部文档一次性读入上下文。
- 大文件只读相关片段，必要时先 `rg` 定位。

### 5. AI 代码有安全错觉

Perry 等人在 CCS 2023 论文中发现，使用 AI coding assistant 的参与者写出的代码可能更不安全，而且更容易相信自己写的是安全代码。

落地规则：

- 安全相关代码必须经过 `safety-gate` 或专门安全复核。
- AI 生成的鉴权、支付、SQL、文件操作、密钥处理、权限策略不能只靠“看起来对”。
- 使用参数化查询、权限边界、输入校验和日志审计作为硬门槛。

### 6. 真实软件工程远比单文件生成难

SWE-bench 显示，真实 issue 常需要跨函数、跨类、跨文件协调，并依赖执行环境、长上下文和复杂推理。

落地规则：

- 不把 benchmark 式单函数成功率等同于真实项目完成度。
- 涉及跨模块时必须画清 owner、数据流和副作用。
- 修复 bug 时优先复现失败，再修根因，再确认没有新增旁路。

### 7. 自我改进要有外部证据

Self-Refine 证明迭代反馈能提高输出质量，但工程里不能让同一个输出者只靠自评决定发布。

落地规则：

- 允许模型提出修正建议，但发布需要测试、规则、人工或独立 evaluator 证据。
- Skill 进化采用渐进 patch，不做整段覆盖。
- 每次进化要有证据、diff、影响范围、回滚点和回归结果。

### 8. 安全开发需要系统流程

NIST SSDF 把安全开发分成组织准备、软件保护、安全生产、漏洞响应四类实践，并强调风险驱动和持续改进。

落地规则：

- 高风险代码必须记录安全需求、风险和设计决策。
- 依赖、配置、构建产物和生产数据需要可追溯。
- 发现漏洞或重复错误后，要写入项目坑点和规则，不只修一次。

## AI Coding 高风险坑点清单

遇到以下情况必须触发质量守卫：

- 超大文件继续堆功能。
- 一个能力出现多个 service、多个 API owner、多个 prompt owner。
- 前后端、业务、数据、模型调用写成一坨。
- API route 直接写 SQL、拼 prompt、调模型 SDK 或扣费。
- 没有 source-of-truth，靠内存状态或前端假保存。
- 使用硬编码默认值替代数据库维护配置。
- 为了修 bug 加新兜底，但不删除旧错误路径。
- 只修 UI 文案，不查真实接口、日志或数据库。
- JSON 解析靠字符串切割，没有契约和失败处理。
- 生成成功但刷新丢失，没有持久化验证。
- AI 评估、Skill、Prompt、Memory、模型池各做一套。
- 技术栈漂移，一个项目混入多套框架和状态管理。
- 只跑 happy path，没有失败路径、权限、计费、并发和幂等检查。
- “已完成”只有壳，没有真实按钮、真实接口、真实数据。

## 高置信开发闭环

每个非小任务按这个顺序：

```text
任务理解
  -> 项目根与地图
  -> 技术栈和 owner
  -> 旧入口和行为基线
  -> 小切片实现
  -> 真实验证
  -> 残留扫描
  -> 地图/账本/坑点更新
```

### 任务理解

输出最短可执行判断：

- 这是什么能力。
- 谁是唯一 owner。
- 需要动哪些层。
- 哪些旧数据或旧入口要兼容。
- 验收信号是什么。

### 项目根与地图

优先读：

- `TOPOLOGY.md` / `PROJECT_MAP.md`
- `TECH_STACK_DECISION.md`
- `DEPLOY_MANIFEST.md`
- 直接相关文件

没有地图时创建最小地图，不要靠全局搜索长期工作。

### 技术栈和 owner

检查：

- 是否引入新框架。
- 是否复用已有 service / repository / provider。
- 是否把业务规则放到正确层。
- 是否有重复能力。

### 旧入口和行为基线

迁移前至少知道：

- 旧 API 和前端调用。
- 旧数据库读写。
- 旧 Prompt / AIService / provider。
- 计费、权限、幂等、副作用。
- 成功和失败响应。

### 小切片实现

规则：

- 先改最小可验证路径。
- 能覆盖就覆盖旧 owner，不新增平行 owner。
- 新兼容端口必须有清理计划和守卫测试。

### 真实验证

按风险选择：

- 单测、集成测试、类型检查、构建。
- API smoke、数据库查询、日志核对。
- 浏览器截图、交互点击、网络请求检查。
- 安全扫描、依赖扫描、权限测试。

### 残留扫描

完成后搜索：

- 旧 API 是否仍被公开调用。
- 旧 service 是否仍有运行入口。
- 旧 Prompt 是否仍是运行 owner。
- 是否有重复文件、死文件、临时文件。
- 是否有硬编码默认值或假保存。

### 地图和账本

结构变更写地图，部署/数据库/后端/环境变更写账本，重复错误写坑点。

## Skill 包落地建议

- 根路由只决定“用哪个 skill”。
- `self-evolution-ai-coding` 管长期工程治理和重构闭环。
- `code-quality-sentinel` 管质量和唯一 owner。
- `debug-investigator` 管证据优先排障。
- `verification-runner` 管验证选择和执行。
- `prompt-governor` 管 AI 入口、Prompt/Skill/Memory/Evaluator 收口。
- `deploy-ledger` 管部署、迁移、账本。
- `safety-gate` 管高风险确认。
- `repo-hygiene-auditor` 管死文件、脏目录和根目录清洁。

## 参考来源

- GitHub Docs, Best practices for using GitHub Copilot to work on tasks: https://docs.github.com/en/copilot/tutorials/cloud-agent/get-the-best-results
- Anthropic, Best practices for Claude Code: https://docs.anthropic.com/en/docs/claude-code/best-practices
- NIST Secure Software Development Framework: https://csrc.nist.gov/Projects/ssdf
- Perry et al., Do Users Write More Insecure Code with AI Assistants?: https://arxiv.org/abs/2211.03622
- Jimenez et al., SWE-bench: Can Language Models Resolve Real-World GitHub Issues?: https://arxiv.org/abs/2310.06770
- Madaan et al., Self-Refine: Iterative Refinement with Self-Feedback: https://arxiv.org/abs/2303.17651
- Fan et al., Large Language Models for Software Engineering: Survey and Open Problems: https://arxiv.org/abs/2310.03533
- Zhang et al., A Survey on Large Language Models for Software Engineering: https://arxiv.org/abs/2312.15223
