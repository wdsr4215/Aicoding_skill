# skills/deploy-ledger/SKILL.md

# deploy-ledger

## 1. 目标

维护当前项目根目录下的 `DEPLOY_MANIFEST.md`，让它成为唯一可信的部署账本。

目标：

1. 防止部署遗漏。
2. 防止前后端只部署一侧。
3. 防止数据库 migration 顺序错误。
4. 防止环境变量漏同步。
5. 防止 AI 修改代码后忘记记录部署动作。
6. 防止 Pending Deployment 无限堆积。
7. 部署完成后自动归档并压缩历史。

`DEPLOY_MANIFEST.md` 是项目级文件，不是全局 Codex 文件。

它必须位于：

```text
<project-root>/DEPLOY_MANIFEST.md
```

禁止写入：

```text
C:\Users\wdsr4\.codex\DEPLOY_MANIFEST.md
```

---

## 2. 核心原则

1. 所有需要部署的改动必须可追踪。
2. 同一变更链路必须自动合并。
3. 部署完成后必须清空 Pending。
4. Archive 只保留压缩摘要，不写流水账。
5. 自动维护，不频繁询问用户。
6. 不允许 AI 修改后忘记记录部署动作。
7. 不允许 DEPLOY_MANIFEST.md 无限膨胀。

---

## 3. 触发条件

以下情况必须激活本技能：

- 数据库 schema 修改。
- migration。
- seed。
- db_scripts。
- 后端 service。
- model。
- router。
- controller。
- middleware。
- API 协议变化。
- 前端核心页面。
- 路由。
- 全局状态。
- 构建入口。
- Docker。
- Nginx。
- PM2。
- systemd。
- CI/CD。
- 部署脚本。
- `.env`。
- 环境变量。
- 服务器路径。
- 任何需要：
  - build
  - restart
  - deploy
  - migrate
  - sync env
  - restart service
    的修改。
- 提示词模板、模型配置、AI 调用扣费逻辑需要同步到数据库或生产配置。

---

## 4. 不触发条件

以下情况通常不需要更新：

- 纯文案修改。
- 局部样式微调。
- README 修改。
- 注释修改。
- 小型组件内部逻辑调整。
- 不影响构建和部署的测试调整。

如果不更新，结束时只需要：

```text
DEPLOY_MANIFEST.md：无需记录
```

---

## 5. 项目根目录识别

执行前必须识别当前项目根目录。

向上查找：

- `DEPLOY_MANIFEST.md`
- `TOPOLOGY.md`
- `package.json`
- `.git`
- `pnpm-workspace.yaml`
- `pyproject.toml`
- `Cargo.toml`
- `go.mod`

规则：

1. `DEPLOY_MANIFEST.md` 只能属于当前项目。
2. 不允许多个项目共用一个部署账本。
3. 如果不存在：
   - 自动创建。
   - 不需要确认。
4. 如果存在多个候选根目录，并影响部署范围，才允许询问用户。

---

## 6. 工作流（开发阶段）

### Step 1：读取账本

读取：

```text
DEPLOY_MANIFEST.md
```

目标：

- 获取 Pending Deployment。
- 获取历史 Deployment Pitfalls。
- 获取部署链路。
- 获取 migration 顺序。
- 获取环境同步要求。

---

### Step 2：分析本次改动

分析：

- 是否涉及 build。
- 是否涉及 restart。
- 是否涉及 migration。
- 是否涉及 env sync。
- 是否涉及前后端联动。
- 是否涉及数据库。
- 是否涉及 Docker/Nginx/PM2/systemd。
- 是否涉及 CI/CD。

---

### Step 3：决定是否需要记录

如果满足部署触发条件：

必须写入：

```text
Pending Deployment
```

否则：

```text
无需记录
```

---

### Step 4：自动合并

更新时必须：

1. 合并同一文件的多次变更。
2. 合并同一 migration 链路。
3. 合并同一部署批次。
4. 合并同一环境变量链路。
5. 删除重复 Pending。
6. 保持 Pending 精简。
7. 记录提示词/模型配置同步时，只写 template key、脚本路径、变量名，不写真实密钥值。

禁止：

```text
每次修改都新增一大段流水账
```

---

## 7. 工作流（部署完成阶段）

当用户表达：

- 已部署
- 部署完成
- 发版完成
- 线上已更新
- 已上线

必须执行：

---

### Step 1：读取 Pending Deployment

分析哪些项已完成。

---

### Step 2：归档

将已完成项移动到：

```text
Deployment Archive
```

Archive 只保留：

- 日期
- 范围
- 文件
- 执行命令
- 验证结果
- 剩余风险

禁止复制完整 Pending。

---

### Step 3：清空 Pending

已完成项必须从：

```text
Pending Deployment
```

移除。

禁止：

```text
部署完成后 Pending 还堆积旧记录
```

---

### Step 4：记录踩坑

如果部署中出现：

- 漏部署
- migration 顺序错误
- env 漏同步
- 前后端版本不一致
- Docker 配置错误
- Nginx 路径错误
- PM2 重启错误

必须写入：

```text
Deployment Pitfalls
```

---

## 8. DEPLOY_MANIFEST.md 推荐结构

```md
# DEPLOY_MANIFEST.md

Last Updated: YYYY-MM-DD HH:mm
Project Root: <project-root>

---

# 1. Pending Deployment

| ID | Scope | Files | Required Action | Status | Notes |
|---|---|---|---|---|---|

---

# 2. Environment Changes

| Variable | Scope | Server Path | Action | Notes |
|---|---|---|---|---|

---

# 3. Database Changes

| Order | Script/Change | Action | Rollback | Notes |
|---|---|---|---|---|

---

# 4. Backend Changes

| Files | Change Summary | Deploy Action | Notes |
|---|---|---|---|

---

# 5. Frontend Changes

| Files | Change Summary | Build Required | Notes |
|---|---|---|---|

---

# 6. Script / Infra Changes

| Files | Change Summary | Execute Order | Notes |
|---|---|---|---|

---

# 7. Verification Checklist

- [ ] Build
- [ ] Test
- [ ] Migration
- [ ] Smoke Test
- [ ] Rollback Plan

---

# 8. Deployment Archive

## YYYY-MM-DD

- Scope:
- Files:
- Commands:
- Verification:
- Remaining Risks:

---

# 9. Deployment Pitfalls

| Pitfall | Cause | Prevention |
|---|---|---|
```

---

## 9. Deployment Pitfalls 写入规则

以下情况必须写入：

- AI 修改后忘记部署。
- migration 顺序错误。
- 环境变量未同步。
- 前端 build 未执行。
- API 已部署但前端未更新。
- Docker compose 未重启。
- PM2 reload 漏执行。
- CI/CD pipeline 未同步。
- 使用错误服务器路径。
- 线上缓存未清理。

示例：

```md
| Pitfall | Cause | Prevention |
|---|---|---|
| API 字段已改但前端未重新 build | 只部署 backend | 前后端联动改动必须同时写入 Pending |
```

禁止：

- 写情绪化描述。
- 写临时问题。
- 写无复用价值流水账。

---

## 10. 禁止行为

禁止：

- 修改后不更新部署账本。
- migration 不记录执行顺序。
- 记录真实密钥值。
- Pending 无限堆积。
- 部署完成不归档。
- Archive 记录完整流水账。
- 前后端联动只记录一侧。
- 不验证 build/migration。
- 因维护 DEPLOY_MANIFEST.md 频繁打断用户。

---

## 11. 结束汇报

结束时只允许简短汇报：

```text
DEPLOY_MANIFEST.md：已更新
```

或：

```text
DEPLOY_MANIFEST.md：已归档并清空已完成项
```

或：

```text
DEPLOY_MANIFEST.md：无需记录
```

结束汇报保持简短，说明账本状态即可。
