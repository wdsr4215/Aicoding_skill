# requirements-architect

## 1. 目标

用于需求澄清、技术规格锁定和架构一致性维护。目标是在写代码前确认“要做什么、用什么做、跑在哪里、怎么验证、怎么部署”，避免后续开发过程中语言版本、框架、数据库、服务器和接口契约漂移。

## 2. 触发条件

必须激活：

- 新项目初始化。
- 新增跨端功能：前端 + 后端、API + DB、UI + AI 调用。
- 修改核心业务链路。
- 涉及后端 service/model/router/controller/middleware。
- 涉及数据库、migration、seed、db_scripts。
- 涉及部署、服务器、Docker、Nginx、PM2、systemd、CI/CD。
- 涉及模型供应商、AI 调用、扣费、权限、会员体系。
- 用户明确要求方案、框架、技术规格、架构文档。

通常不需要激活：

- 纯文案。
- 局部样式微调。
- 单个小 bug 且技术栈明确。
- 不影响架构和部署的小组件内部调整。

## 3. 核心原则

1. 规格基于事实，不凭记忆猜。
2. 先读项目现有规格，再补缺口。
3. 需求清楚时直接推进，需求会影响架构或数据安全时才确认。
4. 技术规格要短、准、可执行，不写空泛口号。
5. 同一项目的技术规格必须可复用，避免每次重新发明。
6. 规格变化必须同步地图和部署账本。

## 4. 事实来源优先级

按顺序查：

1. `TOPOLOGY.md`
2. `TECH_SPEC.md`
3. `DEPLOY_MANIFEST.md`
4. `package.json` / lockfile / workspace file
5. `pyproject.toml` / `requirements.txt` / `.python-version`
6. `Dockerfile` / `docker-compose.yml`
7. `.env.example` / 配置模板
8. 后端入口和数据库配置
9. CI/CD、Nginx、PM2、systemd、部署脚本

不要从真实 `.env` 里复制密钥到规格文档。

## 5. 写代码前输出规格

满足触发条件时，在动手前输出一份短规格摘要：

```text
需求边界：
技术栈：
运行环境：
数据层：
接口契约：
验证方式：
待确认：
```

要求：

- 每项 1-3 行。
- 以项目事实为准。
- 对不确定但低风险的内容写“当前假设”并继续。
- 对会影响数据库、生产、权限、真实费用、用户数据的疑点，列为“待确认”并等待用户。

## 6. TECH_SPEC.md 规则

`TECH_SPEC.md` 是项目级技术规格文档，不是每个项目都强制存在。

应创建或更新：

- 新项目初始化。
- 技术栈或运行环境首次明确。
- 切换框架、数据库、服务器、部署方式。
- 新增关键外部服务：支付、AI provider、对象存储、消息队列。
- 团队协作需要统一开发/部署规格。

可以不创建或不更新：

- 局部 bug 修复。
- 小 UI 调整。
- 文案修改。
- 已有 `TOPOLOGY.md` 和 `DEPLOY_MANIFEST.md` 已足够表达本次规格。

推荐结构：

```md
# TECH_SPEC.md

## Runtime
- Frontend:
- Backend:
- Package Manager:
- Python/Node Version:

## Frameworks
- Web:
- API:
- ORM:
- UI:

## Data
- Database:
- Migration:
- Cache:
- Storage:

## Services
- API Server:
- Admin:
- H5/Web:
- Worker/Scheduler:

## Build & Run
- Local:
- Test:
- Production:

## Environment Variables
- VARIABLE_NAME: purpose, no secret value

## Verification
- Build:
- Test:
- Smoke:
- Deploy Check:
```

## 7. 澄清规则

需要确认：

- 需求目标存在互斥解释。
- 技术选型会改变长期架构。
- 数据库 schema 或生产数据会受影响。
- 涉及真实费用、扣费、会员、权限。
- 涉及真实密钥或生产环境。
- 有多个项目根目录且修改范围不确定。

不需要确认：

- 能从现有代码、地图、配置确定的技术事实。
- 低风险实现细节。
- 项目已有明确模式的组件拆分、接口封装、样式复用。

确认问题格式：

```text
待确认：
1. <具体分歧>；推荐 <方案>，原因 <一句话>。
```

不要提出开放式大问题。

## 8. 输出质量

规格摘要必须覆盖：

- Python/Node 或主要运行时版本。
- 前端框架和构建方式。
- 后端框架和服务入口。
- 数据库和 migration 方式。
- 服务器/容器/进程管理方式。
- API 契约和权限边界。
- 验证和部署检查。

如果某项当前项目不存在，写“不涉及”。

## 9. 联动规则

必须更新 `TOPOLOGY.md`：

- 新增 `TECH_SPEC.md`。
- 技术栈、运行入口、架构边界变化。
- 新增核心服务、数据库、队列、调度器。

必须更新 `DEPLOY_MANIFEST.md`：

- 技术规格变化需要部署同步。
- 运行时版本、环境变量、服务器路径、构建命令变化。
- 数据库或服务入口变化。

涉及生产、数据库、真实密钥时进入 `safety-gate`。

## 10. 结束汇报

```text
技术规格：
待确认：
已记录：
验证：
```
