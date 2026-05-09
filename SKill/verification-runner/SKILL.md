# verification-runner

## 1. 目标

为每次修改选择合适的验证方式，避免“改完就说好了”。验证不追求形式齐全，而追求能证明本次改动闭环。

## 2. 触发条件

- 完成代码修改。
- 用户要求测试、检查、验证。
- 修复 bug、部署、数据库、AI 调用、UI 交互。
- 修改影响核心页面、API、状态、构建入口。

## 3. 验证分层

| 层级 | 目标 | 示例 |
|---|---|---|
| Static | 代码静态正确 | lint, typecheck, py_compile |
| Unit | 小单元逻辑 | pytest, vitest |
| Build | 构建可用 | npm run build, vite build |
| Smoke | 核心入口能跑 | curl API, open page |
| UI | 交互和布局 | 浏览器截图、移动端视口 |
| Data | 数据迁移/写入 | migration dry-run, schema check |
| Deploy | 线上可用 | service status, URL 200, logs |

## 4. 工作流

1. 根据变更识别验证最小集合。
2. 优先运行项目已有 scripts，不发明新验证体系。
3. 验证失败时进入 `debug-investigator`。
4. 无法验证时说明原因和替代检查。
5. 长耗时验证可先跑最小 smoke，再说明未覆盖范围。

## 5. 推荐选择

### 前端

- TypeScript 项目：`npm run typecheck` 或现有等价脚本。
- UI 改动：构建 + 关键页面截图或浏览器检查。
- 移动端/iOS 样式：至少检查窄屏视口、安全区、底部固定层、弹窗层级。

### 后端

- Python：`python -m py_compile` 或 pytest。
- API：curl/http smoke。
- FastAPI：检查路由导入、服务启动日志。

### 数据库

- migration：检查顺序、回滚说明、备份要求。
- 生产写入：必须进入 `safety-gate`。

### AI 调用

- 检查 JSON 解析。
- 检查输入长度限制。
- 检查余额/扣费/失败补偿。
- 如不真实调用模型，至少用 mock 或解析样例验证。

## 6. 禁止行为

- 没有验证就宣称完成。
- 失败命令原样重复。
- 为了通过测试删除测试。
- 把验证失败归因于环境但不说明证据。

## 7. 结束汇报

```text
验证：
通过：
未覆盖：
原因：
```
