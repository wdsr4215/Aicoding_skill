# 自进化项目治理文件集

## 文件职责

`PROJECT_MAP.md`

- 项目地图。
- 记录模块、入口、服务边界、关键文件、已迁移能力和残留风险。
- 新增正式文件必须在这里或项目级 skill 路由中可发现。

`TECH_STACK_DECISION.md`

- 唯一技术栈决策。
- 记录前端、后端、数据库、任务队列、包管理器、运行时版本。
- 禁止项目后期框架漂移。

`PROJECT_DEVELOPMENT_MANUAL.md`

- 唯一开发手册。
- 记录长期稳定规则：架构、服务边界、代码风格、目录约束、注释语言、重构方式。

`COMMERCIAL_ACCEPTANCE_CRITERIA.md`

- 验收标准。
- 每次开发完成前必须执行。
- 防止死文件、重复服务、数据库误改、临时文件污染、测试缺失。

`AI_CODING_MISTAKE_NOTEBOOK.md`

- 错题本。
- 记录 AI coding 反复犯的问题、触发信号、预防扫描、修正方式。

`COMMERCIAL_REFACTOR_LOG.md`

- 重构日志。
- 只记录阶段性变更、检查、结果和下一步。
- 超过可读规模后归档历史。

`DEPLOY_MANIFEST.md`

- 部署账本。
- 记录数据库 schema、migration、seed、后端服务、环境变量、部署脚本、CI/CD、重启动作和上线验证。
- 只记录需要部署或运维处理的变更，不写日常开发流水账。

`SKILL_PORTABILITY_GUIDE.md`

- skill 迁移指南。
- 说明哪些治理文件要随项目迁移。

`.codex/skills/project-governance/SKILL.md`

- 项目级 skill 路由。
- 只保留入口、必读文件、触发规则，不写长篇规范。

## 使用原则

- 通用规则沉淀到全局 `self-evolution-ai-coding`。
- 项目特定规则沉淀到项目级 skill 和项目控制文件。
- 不把项目私有业务规则写入全局 skill。
- 不把全局工程规范复制到每个项目的长文档中；项目只引用和补充。
- 技术栈由项目自己的 `TECH_STACK_DECISION.md` 决定，全局 skill 只提供选择方法。
- AI/Agent 运行时、提示词、记忆、评估和 skill 的边界优先写入项目开发手册；只有多项目通用规则才进入全局 reference。

## 全局参考文件

- `stack-selection.md`：技术栈选择方法。
- `commercial-engineering.md`：商业化工程质量标准。
- `self-evolution.md`：自我反思、错题本和规则吸收机制。
- `prompt-skill-boundary.md`：skill、prompt、memory、evaluator 和 AI/Agent 入口边界。
