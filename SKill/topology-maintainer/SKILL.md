

# topology-maintainer

## 1. 目标

维护当前项目根目录下的 `TOPOLOGY.md`，让它成为 AI 查找代码、理解架构、避免重复搜索的项目工程地图。

`TOPOLOGY.md` 是项目级文件，不是全局 Codex 文件。

它必须生成在当前项目根目录，例如：

```text
E:\2026\TOPOLOGY.md
```

禁止写入：

```text
C:\Users\wdsr4\.codex\TOPOLOGY.md
```

---

## 2. 核心原则

1. 先读地图，再搜文件。
2. 先合并旧信息，再写入新信息。
3. 只记录长期有价值的结构信息，不写流水账。
4. 自动更新，不频繁询问用户。
5. 地图服务于“下次更快定位”，不是为了好看。
6. 修复 AI 曾经犯过的错误后，必须沉淀到 `Known Pitfalls`。
7. 不允许因为维护 `TOPOLOGY.md` 阻塞正常开发流程。
8. 地图服务于下一次快速定位，不服务于仪式感。

---

## 3. 触发条件

当任务涉及以下内容时，必须激活本技能：

- 用户要求查找文件、定位模块、理解项目结构。
- 用户询问某个功能在哪里实现。
- 新增、删除、移动、重命名核心文件或目录。
- 新增或修改 API、router、service、model、controller。
- 新增或修改 store、context、hook、global state。
- 新增或修改部署入口、构建配置、核心脚本。
- 修复了一个可复用的历史踩坑。
- 发现 `TOPOLOGY.md` 中存在过期路径、重复模块、错误索引。
- 当前任务需要避免无脑全局搜索。

---

## 4. 不触发条件

以下情况通常不需要更新 `TOPOLOGY.md`：

- 纯文案修改。
- 局部样式微调。
- README 或注释修改。
- 小型组件内部逻辑修改，且不影响模块职责。
- 测试用例的小范围调整，且不影响项目结构。
- 临时日志、临时调试代码，且任务结束前已清理。

如果不更新，结束时只需要说明：

```text
TOPOLOGY.md：无结构变化
```

---

## 5. 项目根目录识别

执行前必须识别当前项目根目录。

向上查找以下标志：

- `TOPOLOGY.md`
- `DEPLOY_MANIFEST.md`
- `package.json`
- `pnpm-workspace.yaml`
- `pyproject.toml`
- `Cargo.toml`
- `go.mod`
- `.git`

规则：

1. `TOPOLOGY.md` 和 `DEPLOY_MANIFEST.md` 只能存在于项目根目录。
2. 不允许跨项目共享地图。
3. 如果存在多个候选根目录，并且会影响修改范围，才允许询问用户。
4. 如果不存在 `TOPOLOGY.md`，自动创建，不需要确认。

---

## 6. 工作流

### Step 1：读取地图

优先读取当前项目根目录下的：

```text
TOPOLOGY.md
```

目标：

- 快速定位模块。
- 避免全局搜索。
- 获取项目结构上下文。
- 获取历史 Known Pitfalls。
- 获取 Search Hints。

---

### Step 2：决定是否需要搜索

只有以下情况允许搜索项目：

- `TOPOLOGY.md` 缺失。
- `TOPOLOGY.md` 明显过期。
- 地图未覆盖目标模块。
- 地图路径不存在。
- 涉及跨模块链路。
- 用户明确要求全局搜索。

禁止：

```text
任务开始 → 无脑 rg 全项目
```

---

### Step 3：结构分析

分析以下变化：

- 新增目录
- 删除目录
- 模块移动
- API 链路变化
- Store 变化
- Hook 变化
- 配置变化
- 部署入口变化
- 前后端依赖变化

---

### Step 4：更新地图

必须更新：

- Directory Map
- Module Index
- API Index
- State Index
- Config Index
- Deployment Index
- Known Pitfalls
- Search Hints
- AI / Prompt Index（如果项目有提示词、模型或 AI 调用链路）

但只更新受影响区域。

禁止：

```text
整文件重写
```

---

### Step 5：压缩与合并

更新后必须：

1. 合并重复模块。
2. 删除过期路径。
3. 删除失效 Search Hints。
4. 压缩重复描述。
5. 避免流水账。
6. 保留已有有效信息。

---

## 7. TOPOLOGY.md 推荐结构

```md
# TOPOLOGY.md

Last Updated: YYYY-MM-DD HH:mm
Project Root: <project-root>

---

# 1. Tech Stack

- Frontend:
- Backend:
- Database:
- Package Manager:
- Deployment:

---

# 2. Directory Map

```text
/
├── src/
├── app/
├── components/
├── services/
└── ...
```

---

# 3. Module Index

| Module | Responsibility | Entry Files | Notes |
| ------ | -------------- | ----------- | ----- |

---

# 4. API Index

| API/Route | Router | Service | Model/DB | Frontend Caller |
| --------- | ------ | ------- | -------- | --------------- |

---

# 5. State Index

| State/Store/Hook | Path | Used By | Notes |
| ---------------- | ---- | ------- | ----- |

---

# 6. Config Index

| Config | Path | Purpose | Notes |
| ------ | ---- | ------- | ----- |

---

# 7. Deployment Index

| Item | Path | Purpose | Notes |
| ---- | ---- | ------- | ----- |

---

# 8. Known Pitfalls

| Pitfall | Cause | Prevention |
| ------- | ----- | ---------- |

---

# 9. Search Hints

- keyword:
- path:
- avoid:
  
  ```
  
  ```

---

## 8. Known Pitfalls 写入规则

以下情况必须写入：

- AI 曾重复犯错。
- API 字段错配。
- 环境变量遗漏。
- 部署漏项。
- 错误搜索路径。
- 前后端字段不一致。
- 同一个 Bug 原样重试。
- 不存在的路径或模块。
- 反复修改错误文件。

格式：

```md
| Pitfall | Cause | Prevention |
|---|---|---|
| UserStore 被重复创建 | 未先读取 State Index | 修改 Store 前先检查 TOPOLOGY.md |
```

禁止：

- 写情绪化描述。
- 写无复用价值的流水账。
- 写临时问题。

---

## 9. Search Hints 写入规则

目标：

减少未来搜索范围。

示例：

```md
- auth login flow: src/modules/auth/
- global modal store: src/stores/modal-store.ts
- deploy script: scripts/deploy-prod.ps1
- avoid searching dist/ and build/
```

规则：

1. 保持短小。
2. 保持可搜索。
3. 不写长篇解释。
4. 删除失效路径。
5. 删除重复关键词。

---

## 10. 禁止行为

禁止：

- 不读地图直接全局搜索。
- 每次任务都重建 TOPOLOGY.md。
- 把地图写成流水账。
- 记录 node_modules、dist、build、缓存目录。
- 写无意义目录树。
- 保留过期路径。
- 用情绪化语言描述架构。
- 把多个项目地图混在一起。
- 因为更新 TOPOLOGY.md 频繁打断用户。

---

## 11. 结束汇报

结束时只允许简短汇报：

```text
TOPOLOGY.md：已更新
```

或：

```text
TOPOLOGY.md：无结构变化
```

结束汇报保持简短，说明地图是否更新即可。
