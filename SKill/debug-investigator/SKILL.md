# debug-investigator

## 1. 目标

用于处理：

- Bug
- 报错
- 异常行为
- 失败命令
- 构建失败
- 线上问题
- 日志异常
- API 不一致
- 环境问题

目标：

1. 防止 AI 盲猜修复。
2. 防止同错原样重试。
3. 防止不看日志直接改代码。
4. 防止小问题大重构。
5. 防止错误定位到错误模块。
6. 将可复用问题沉淀到 `TOPOLOGY.md -> Known Pitfalls`。

---

## 2. 核心原则

1. 先定位，再修改。
2. 先缩小范围，再修复。
3. 日志优先于猜测。
4. 调用链优先于直觉。
5. 不允许“试试看”式随机修复。
6. 修复后必须验证。
7. 同一个错误禁止原样重试。
8. Bug 修复必须可复盘。
9. 能通过日志、代码和配置推断的默认自动推进，不把排查变成频繁提问。

---

## 3. 触发条件

以下情况必须激活本技能：

- 用户提供错误日志。
- 用户提供异常截图。
- 用户说：
  - 报错了
  - 没生效
  - 运行失败
  - build failed
  - deploy failed
  - 页面白屏
  - 接口 500
  - 请求失败
  - 无限 loading
  - hydration error
  - 类型错误
  - migration 失败
  - docker 起不来
- 命令执行失败。
- 修改后行为异常。
- CI/CD 失败。
- 测试失败。
- 线上与本地不一致。

---

## 4. 不触发条件

以下情况通常不需要激活：

- 普通功能开发。
- 文案修改。
- 纯样式调整。
- 无错误信息的产品讨论。

---

## 5. 工作流

### Step 1：复述问题

先明确：

- 错误现象。
- 触发条件。
- 报错位置。
- 是否可复现。
- 本地还是线上。
- 是否最近改动导致。

禁止：

```text
还没理解问题就直接改代码
```

---

### Step 2：读取 TOPOLOGY.md

优先读取：

```text
TOPOLOGY.md
```

目标：

- 获取模块入口。
- 获取 API 链路。
- 获取状态链路。
- 获取 Known Pitfalls。
- 避免搜索错误目录。

---

### Step 3：定位调用链

必须分析：

- 调用入口。
- 参数来源。
- API 请求。
- Store / State。
- Hook。
- Router。
- Middleware。
- 环境变量。
- 数据库。
- Docker / Nginx / PM2。
- 构建链路。

目标：

```text
缩小问题范围
```

禁止：

```text
全项目乱搜 + 随机修改
```

---

### Step 4：检查日志与上下文

优先：

- 日志
- stack trace
- console
- network
- server output
- build output
- test output

如果日志不足：

允许：

- 增加最小必要日志
- 增加断点
- 增加临时 debug 输出

但任务结束前必须清理。

如果是线上问题：

- 先区分代码版本、构建产物、环境变量、服务状态、缓存和数据状态。
- 不把“本地正常”当作线上正常的证据。
- 涉及生产执行时进入 `safety-gate`。

---

### Step 5：决定修复路径

修复前必须判断：

- 根因是什么？
- 是否只是症状？
- 是否影响其他模块？
- 是否会破坏现有接口？
- 是否涉及部署？
- 是否需要 migration？
- 是否需要 build？
- 是否需要 env sync？

禁止：

```text
用大重构解决小问题
```

---

### Step 6：验证

修复后必须验证：

- build
- lint
- typecheck
- test
- API
- 页面行为
- Docker
- migration
- CI/CD

至少验证：

```text
最小可行路径
```

禁止：

```text
改完直接宣布修复成功
```

---

### Step 7：沉淀 Pitfall

如果属于：

- AI 容易重复犯错
- 环境坑
- API 坑
- 搜索路径坑
- 部署坑
- 类型坑
- hydration 坑
- 前后端字段不一致

必须写入：

```text
TOPOLOGY.md -> Known Pitfalls
```

---

## 6. Known Pitfalls 写入规则

格式：

```md
| Pitfall | Cause | Prevention |
|---|---|---|
```

示例：

```md
| Pitfall | Cause | Prevention |
|---|---|---|
| API 返回 snake_case 导致前端字段 undefined | frontend 使用 camelCase 假设 | 修改接口前先检查 API Index |
```

---

## 7. 高优先级排查顺序

优先排查：

1. 最近改动。
2. 环境变量。
3. API 字段变化。
4. 路由变化。
5. build 配置。
6. store/state。
7. async race。
8. hydration。
9. migration。
10. Docker/Nginx/PM2。
11. 缓存和旧构建产物。
12. 生产环境变量。

禁止：

```text
一上来全局重构
```

---

## 8. 常见错误防御

### A. API 错误

检查：

- 请求路径
- 请求方法
- headers
- token
- response shape
- 字段命名
- 类型

---

### B. 前后端字段不一致

检查：

- snake_case
- camelCase
- nullable
- optional
- enum

---

### C. 环境变量问题

检查：

- 是否存在
- 是否 reload
- 是否同步线上
- 是否 build 时注入
- 是否 server/client 混用

---

### D. React / Next.js

检查：

- hydration mismatch
- server/client component
- useEffect race
- stale closure
- dependency array

---

### E. Docker / 部署

检查：

- compose 文件
- volume
- cache
- restart
- build context
- env injection

---

### F. TypeScript

检查：

- any
- unknown
- nullable
- undefined
- type narrowing
- generic mismatch

---

## 9. 禁止行为

禁止：

- 不读日志直接修复。
- 同一个失败命令原样重复执行。
- 随机尝试不同代码。
- 不验证直接宣布成功。
- 删除大段代码掩盖问题。
- 为小问题做大重构。
- 猜测不存在的 API。
- 猜测不存在的环境变量。
- 猜测不存在的文件。
- 不清理临时 debug 代码。
- 不更新 Known Pitfalls。

---

## 10. DEPLOY_MANIFEST 联动规则

如果修复涉及：

- migration
- env
- Docker
- backend
- build
- CI/CD
- deploy script

必须更新：

```text
DEPLOY_MANIFEST.md
```

---

## 11. 结束汇报

结束时只允许：

```text
根因：
修改：
验证：
Known Pitfalls：已更新 / 无需更新
```

结束汇报保持简短，聚焦根因、修改、验证和可复用教训。
