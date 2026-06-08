---
name: self-evolution-ai-coding
description: 通用 AI coding 自进化工程治理技能。用于新项目初始化、长期重构、复杂功能开发、能力迁移、旧库兼容、数字生命/Agent 底座接入、代码质量治理、技术栈固化、项目地图维护、验收标准执行、错题本沉淀、交接打包和防止 AI coding 产生高耦合、超大文件、死文件、重复服务、脏代码。用户提到自进化、self-evolution、通用开发规范、项目治理、重构模式、能力迁移、数字生命、Agent 运行时、多层记忆、Prompt/Skill/Memory/Evaluator 收口、旧数据库兼容、项目地图、技术栈固化、验收、长期一致性、避免屎山代码时使用。
---

# 自进化 AI Coding

## 核心目标

把每个项目当作长期商业化工程处理，而不是一次性代码生成。

默认目标：

- 先固化技术栈和项目地图，再开发。
- 先识别边界和业务事实，再重构。
- 一个服务只做一件事。
- 新文件必须可路由、可访问、可验收。
- 临时文件、测试页面、一次性脚本不能混入正式项目。
- 每次完成都要回测、扫描和记录。

## 快速启动

新项目或空项目启动时，先运行脚手架：

```powershell
python "$env:USERPROFILE\.codex\skills\self-evolution-ai-coding\scripts\scaffold_governance.py" --project-root .
```

如果项目有名称：

```powershell
python "$env:USERPROFILE\.codex\skills\self-evolution-ai-coding\scripts\scaffold_governance.py" --project-root . --project-name "项目名"
```

脚手架会生成：

- `PROJECT_MAP.md`
- `TECH_STACK_DECISION.md`
- `PROJECT_DEVELOPMENT_MANUAL.md`
- `COMMERCIAL_ACCEPTANCE_CRITERIA.md`
- `AI_CODING_MISTAKE_NOTEBOOK.md`
- `COMMERCIAL_REFACTOR_LOG.md`
- `SKILL_PORTABILITY_GUIDE.md`
- `.codex/skills/project-governance/SKILL.md`

已有文件默认不会覆盖。需要重建模板时显式传 `--overwrite`。

## 工作流

### 1. 新项目初始化

先生成治理文件，再读项目结构。

检查：

- 是否有项目地图。
- 是否有唯一技术栈决策。
- 是否有验收标准。
- 是否有项目级 skill 路由。
- 临时产物目录是否独立。

如果缺失，运行 `scripts/scaffold_governance.py`。

技术栈不要在 skill 中写死。先读取 `references/stack-selection.md`，结合项目类型、团队能力、端类型、商业化风险、部署环境和长期维护成本，生成项目自己的 `TECH_STACK_DECISION.md`。

### 2. 日常开发

每次改动前读取：

- `PROJECT_MAP.md`
- `TECH_STACK_DECISION.md`
- `COMMERCIAL_ACCEPTANCE_CRITERIA.md`
- 直接触碰的代码文件

架构、高风险商业化、支付、身份、数据库、AI 调度、跨端技术栈变更时，再读取：

- `PROJECT_DEVELOPMENT_MANUAL.md`
- `AI_CODING_MISTAKE_NOTEBOOK.md`
- `COMMERCIAL_REFACTOR_LOG.md`
- `references/commercial-engineering.md`
- `references/ai-coding-reliability-research.md`

### 3. 重构模式

必须闭环渐进：

```text
能力盘点 -> 行为基线 -> 小切片抽取 -> 回测 -> 残留扫描 -> 删除旧实现 -> 更新地图
```

禁止：

- 一次性大爆炸重写。
- 新旧同能力长期双轨。
- 在超大文件里继续堆功能。
- 页面、路由或 controller 直接承载业务规则。
- API route 直接写 SQL。
- 前端直接拼复杂 prompt 或直接调用模型 SDK。

### 4. 能力迁移可靠性

涉及旧项目能力迁移、AI 入口、数字生命/Agent 运行时、多层记忆、Prompt 到 Skill、模型池、工具、评估、进化、扣费、旧数据库兼容时，先读取：

- `references/capability-migration-reliability.md`

迁移前必须先回答：

- 当前能力的唯一 owner 是谁。
- 旧入口、旧 Prompt、旧 AIService、旧数据库写入和副作用在哪里。
- 哪些旧表语义必须完全兼容。
- 新链路如何留下 Trace、source facts、memory、Skill、model、tool、evaluation、evolution 和 billing 证据。
- 清旧入口前有哪些守卫测试能防止双轨复活。

原则：

- API 只做适配，业务算法留业务层，通用运行底座只接收结构化算法结果和证据。
- 旧 Prompt 只能作为 Skill seed / Policy seed / 兼容数据，不能继续作为公开运行入口。
- 不新增第二套 Memory、Skill、Prompt、Evaluator、模型池或扣费体系。
- 旧库保护优先，只新增旁路表和索引；生产迁移必须单独确认。

### 5. 高置信 AI 编码闭环

当用户提到 AI 编码坑点、超大文件、重复实现、脏代码、硬编码兜底、缺少架构、技术栈漂移、壳子功能、没有闭环验证或希望单次开发更可靠时，读取：

- `references/ai-coding-reliability-research.md`

该 reference 将公开研究和工程踩坑转成可执行守卫：任务拆分、上下文裁剪、唯一 owner、真实验证、安全复核、残留扫描和进化回滚。

### 6. 验收模式

完成前必须检查：

- 技术栈是否符合 `TECH_STACK_DECISION.md`。
- 新文件是否在地图或 skill 路由中体现。
- 数据库 schema 是否被改动。
- 旧入口是否仍重复承载业务逻辑。
- 是否有临时文件污染项目。
- 是否跑了构建、测试或合理的替代回测。
- 是否更新 `COMMERCIAL_REFACTOR_LOG.md`。

如果发现重复错误、隐藏耦合、需求误判、测试缺口或用户未意识到的商业风险，必须更新错题本。读取 `references/self-evolution.md` 后再沉淀规则。

## 数字员工、Agent 底座与提示词

如果项目涉及 AI 员工、数字生命、Agent、提示词编排、记忆、技能路由或内容生产，读取：

- `references/digital-employee-runtime.md`
- `references/prompt-skill-boundary.md`
- `references/capability-migration-reliability.md`

原则：

- skill 负责稳定方法、流程、约束、验收和工具路由。
- prompt 负责一次性任务上下文、角色目标、产物格式和生成策略。
- 数字员工共享同一套 skill 架构，但拥有不同的角色记忆、领域知识、任务权限和提示词模板。
- 灵感扩展、文旅导览、商业短片等能力应建模为数字员工或场景专家，而不是散落的固定提示词。
- 按需加载：先识别场景和任务，再读取对应 reference，不允许一次性加载全部治理材料。

## 文件膨胀规则

不要无限新增治理文件。

规则：

- 能写入已有治理文件的规则，不新增文件。
- `SKILL.md` 只做入口和工作流，不堆长规范。
- 大规则进入项目控制文件。
- 历史日志变大后归档为 `docs/archive/`，活动日志只保留最近阶段和索引。
- 项目地图只保留当前结构、入口、边界和路由，不记录长篇过程。

## 资源

- `scripts/scaffold_governance.py`：生成项目治理文件和项目级 skill 路由。
- `references/governance-file-set.md`：治理文件职责说明。
- `references/stack-selection.md`：技术栈推荐与稳定策略。
- `references/commercial-engineering.md`：商业化编码质量、低耦合和可维护性标准。
- `references/capability-migration-reliability.md`：旧能力迁移到数字生命/Agent 底座时的唯一 owner、旧库兼容、运行 Trace、清旧和守卫测试标准。
- `references/ai-coding-reliability-research.md`：AI 编码常见失败模式、研究依据、大厂实践和高置信闭环守卫。
- `references/self-evolution.md`：自我反思、错题本和规则吸收机制。
- `references/digital-employee-runtime.md`：数字生命底座和数字员工架构。
- `references/prompt-skill-boundary.md`：skill、提示词、记忆和场景专家的边界。
