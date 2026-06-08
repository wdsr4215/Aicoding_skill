from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def write_file(path: Path, content: str, overwrite: bool) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        return f"SKIP {path}"
    path.write_text(content.strip() + "\n", encoding="utf-8")
    return f"WRITE {path}"


def project_map(project_name: str, today: str) -> str:
    return f"""
# {project_name} Project Map

Status: active project map
Last updated: {today}

## Project Purpose

写清楚项目长期目标、核心用户、商业化目标和不可破坏的约束。

## Current Architecture

```text
待盘点：前端、后端、数据库、任务队列、外部服务、部署入口。
```

## Control Files

- `PROJECT_MAP.md`
- `TECH_STACK_DECISION.md`
- `PROJECT_DEVELOPMENT_MANUAL.md`
- `COMMERCIAL_ACCEPTANCE_CRITERIA.md`
- `AI_CODING_MISTAKE_NOTEBOOK.md`
- `COMMERCIAL_REFACTOR_LOG.md`
- `SKILL_PORTABILITY_GUIDE.md`
- `.codex/skills/project-governance/SKILL.md`

## Module Map

| Module | Owner File/Directory | Responsibility | Status |
| --- | --- | --- | --- |
| TBD | TBD | TBD | inventory-needed |

## Service Boundaries

- 一个服务只负责一个业务能力。
- API 路由只做协议适配。
- Repository 负责数据访问。
- Policy / Validator 负责拒绝规则。
- Provider Adapter 负责第三方 SDK。

## Temporary Artifacts

临时页面、一次性脚本、截图、验证产物必须放在项目外部或明确的 scratch 目录，不进入正式源码结构。
"""


def tech_stack(project_name: str, today: str) -> str:
    return f"""
# {project_name} Technology Stack Decision

Status: active governance
Last updated: {today}

## Rule

本文件是技术栈唯一事实源。新增框架、数据库、队列、状态管理、UI 库、包管理器或运行时版本前，必须先更新本文件并说明原因。

技术栈不是由全局 skill 写死，而是根据项目类型、团队能力、端类型、商业化风险、部署环境和长期维护成本选择。选择时可参考全局 skill 的 `references/stack-selection.md`。

## Current Stack

| Layer | Decision | Version | Notes |
| --- | --- | --- | --- |
| Frontend | TBD | TBD | |
| Backend | TBD | TBD | |
| Database | TBD | TBD | |
| Cache/Queue | TBD | TBD | |
| Package Manager | TBD | TBD | |
| Runtime | TBD | TBD | |

## Anti-Drift Rules

- 不为临时功能单独引入新框架。
- 不为单个页面单独建立 UI 体系。
- 不在多个模块重复实现同一业务能力。
- 大版本升级必须单独切片并验证。

## Decision Record

| Decision | Reason | Alternatives Rejected | Review Date |
| --- | --- | --- | --- |
| TBD | TBD | TBD | TBD |
"""


def development_manual(project_name: str, today: str) -> str:
    return f"""
# {project_name} Development Manual

Status: mandatory guide
Last updated: {today}

## Required Reading

日常改动先读：

1. `PROJECT_MAP.md`
2. `TECH_STACK_DECISION.md`
3. `COMMERCIAL_ACCEPTANCE_CRITERIA.md`
4. 直接触碰的代码文件

架构、支付、身份、数据库、AI 调度、跨端技术栈或大型重构时，再读：

1. `PROJECT_DEVELOPMENT_MANUAL.md`
2. `AI_CODING_MISTAKE_NOTEBOOK.md`
3. `COMMERCIAL_REFACTOR_LOG.md`

## Architecture Rules

- 模块化单体优先，微服务是清晰边界后的部署形态。
- 一个业务能力只有一个 owner。
- API route / controller 不写业务决策。
- Service / Use Case 只协调一个清晰业务动作。
- Repository 负责数据库查询。
- Policy / Validator 负责规则判断和拒绝。
- Adapter 负责第三方服务。

## Refactor Rules

闭环渐进重构：

```text
能力盘点 -> 行为基线 -> 小切片抽取 -> 回测 -> 残留扫描 -> 删除旧实现 -> 更新地图
```

禁止长期保留新旧双轨。

## File Rules

- 新增正式文件必须在项目地图或项目级 skill 路由中体现。
- 临时文件不能进入正式项目结构。
- 超大文件继续加功能前，先评估抽取。
- 注释、docstring、开发说明默认使用团队主要语言。

## Skill / Prompt / Memory Rules

- skill 负责稳定流程、工程约束、验收规则和工具路由。
- prompt 负责本次任务目标、输出格式、当前素材和临时约束。
- memory 负责长期稳定偏好、关系、状态和会影响未来决策的事实。
- 不允许把所有 skill、所有记忆和所有项目文档一次性塞入上下文。
- 涉及 AI 员工、Agent 或内容生成时，先明确数字员工角色、任务权限、可用 skill、可用记忆和本次 prompt。

## Self-Evolution Rules

- 出现构建失败、需求误判、重复服务、脏代码、隐藏耦合或用户指出维护性问题时，必须反思。
- 项目私有问题写入 `AI_CODING_MISTAKE_NOTEBOOK.md`。
- 多项目通用问题沉淀到全局 `self-evolution-ai-coding`。
- 只有稳定、可复用、可验收的经验才能上升为规则。

## Governance Size Rule

- skill 只做路由，不写长篇手册。
- 能写入已有治理文件的规则，不新增文件。
- 日志过大时归档历史，活动文件只保留当前阶段。
"""


def acceptance(project_name: str, today: str) -> str:
    return f"""
# {project_name} Commercial Acceptance Criteria

Status: mandatory acceptance gate
Last updated: {today}

## Universal Checklist

每次完成前必须回答：

- 技术栈是否符合 `TECH_STACK_DECISION.md`。
- 服务 owner 是否唯一。
- 新文件是否可路由、可访问、可验收。
- API route 是否只做协议适配。
- 是否误改数据库 schema。
- 是否有旧实现和新实现重复承载同一能力。
- 是否有临时文件、测试页面、构建产物污染项目。
- 是否跑了构建、测试、静态扫描或合理回测。
- 是否更新 `PROJECT_MAP.md` 和 `COMMERCIAL_REFACTOR_LOG.md`。
- 是否主动评估用户未明确提出但会影响商业化上线的风险。
- 是否发现可沉淀的错误模式，并更新 `AI_CODING_MISTAKE_NOTEBOOK.md`。
- 如果涉及 AI 生成，是否明确 skill、prompt、memory 和数字员工职责边界。

## Required Scans

按项目技术栈补充实际命令：

```text
rg -n "TODO|FIXME|console.log|print\\(" .
rg -n "ALTER TABLE|CREATE TABLE|DROP TABLE|add_column|drop_column" .
```
"""


def mistake_notebook(project_name: str, today: str) -> str:
    return f"""
# {project_name} AI Coding Mistake Notebook

Status: active mistake memory
Last updated: {today}

## Purpose

记录本项目中 AI coding 反复犯的问题，形成下次开发前的预防检查。

## Entries

### 001. 未盘点能力就开始重构

触发信号：

- 只看局部文件就移动代码。
- 没找调用方、路由、返回结构和副作用。

预防：

- 重构前先列能力范围、调用方、数据读写、外部依赖和回测方式。

### 002. 只完成代码，不沉淀经验

触发信号：

- 同类问题反复出现。
- 用户重复强调同一规范。
- 修复完成但没有新增预防扫描。

预防：

- 完成后判断是否需要更新错题本。
- 稳定通用规则再上升到全局 skill reference。
"""


def refactor_log(project_name: str, today: str) -> str:
    return f"""
# {project_name} Refactor Log

Status: active log
Last updated: {today}

## {today} Governance Bootstrap

Scope:

- `PROJECT_MAP.md`
- `TECH_STACK_DECISION.md`
- `PROJECT_DEVELOPMENT_MANUAL.md`
- `COMMERCIAL_ACCEPTANCE_CRITERIA.md`
- `AI_CODING_MISTAKE_NOTEBOOK.md`
- `SKILL_PORTABILITY_GUIDE.md`
- `.codex/skills/project-governance/SKILL.md`

Result:

- Project governance files initialized.
"""


def portability(project_name: str, today: str) -> str:
    return f"""
# {project_name} Skill Portability Guide

Status: active portability guide
Last updated: {today}

## Files To Carry

- `.codex/skills/project-governance/SKILL.md`
- `PROJECT_MAP.md`
- `TECH_STACK_DECISION.md`
- `PROJECT_DEVELOPMENT_MANUAL.md`
- `COMMERCIAL_ACCEPTANCE_CRITERIA.md`
- `AI_CODING_MISTAKE_NOTEBOOK.md`
- `COMMERCIAL_REFACTOR_LOG.md`

## Export

```powershell
Compress-Archive -Force `
  -Path ".codex\\skills\\project-governance", `
        "PROJECT_MAP.md", `
        "TECH_STACK_DECISION.md", `
        "PROJECT_DEVELOPMENT_MANUAL.md", `
        "COMMERCIAL_ACCEPTANCE_CRITERIA.md", `
        "AI_CODING_MISTAKE_NOTEBOOK.md", `
        "COMMERCIAL_REFACTOR_LOG.md", `
        "SKILL_PORTABILITY_GUIDE.md" `
  -DestinationPath "{project_name}-governance.zip"
```
"""


def project_skill(project_name: str) -> str:
    return f"""
---
name: project-governance
description: {project_name} 项目级治理 skill。用于本项目开发、重构、技术栈约束、项目地图维护、验收、错题本和交接。处理本项目代码、架构、数据库、前后端、部署、测试、项目文件或长期维护时使用。
---

# {project_name} Project Governance

## Required Reading

日常改动：

1. `PROJECT_MAP.md`
2. `TECH_STACK_DECISION.md`
3. `COMMERCIAL_ACCEPTANCE_CRITERIA.md`
4. 直接触碰的代码文件

架构或高风险改动：

1. `PROJECT_DEVELOPMENT_MANUAL.md`
2. `AI_CODING_MISTAKE_NOTEBOOK.md`
3. `COMMERCIAL_REFACTOR_LOG.md`

## Rules

- 遵循全局 `self-evolution-ai-coding`。
- 项目私有规则写入项目控制文件，不写入全局 skill。
- 新增正式文件必须更新 `PROJECT_MAP.md` 或本 skill 路由。
- 完成前执行 `COMMERCIAL_ACCEPTANCE_CRITERIA.md`。
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--project-name", default=None)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    project_name = args.project_name or root.name
    today = date.today().isoformat()

    files = {
        root / "PROJECT_MAP.md": project_map(project_name, today),
        root / "TECH_STACK_DECISION.md": tech_stack(project_name, today),
        root / "PROJECT_DEVELOPMENT_MANUAL.md": development_manual(project_name, today),
        root / "COMMERCIAL_ACCEPTANCE_CRITERIA.md": acceptance(project_name, today),
        root / "AI_CODING_MISTAKE_NOTEBOOK.md": mistake_notebook(project_name, today),
        root / "COMMERCIAL_REFACTOR_LOG.md": refactor_log(project_name, today),
        root / "SKILL_PORTABILITY_GUIDE.md": portability(project_name, today),
        root / ".codex" / "skills" / "project-governance" / "SKILL.md": project_skill(project_name),
    }

    for path, content in files.items():
        print(write_file(path, content, args.overwrite))


if __name__ == "__main__":
    main()
