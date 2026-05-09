# skills/ui-guardian/SKILL.md

# ui-guardian

## 1. 目标

用于处理：

- 页面
- 组件
- Dashboard
- 表单
- 弹窗
- 列表
- loading/error/empty
- 交互逻辑
- 响应式布局
- 移动端 / iOS 规范
- 安全区 / 底部固定操作区
- 弹窗 / 抽屉层级
- 图标
- UI 一致性

目标：

1. 防止反人类交互。
2. 防止 Emoji 充当正式图标。
3. 防止 UI / 逻辑 / 请求揉成巨石文件。
4. 防止 loading/error/empty 缺失。
5. 防止出现大量重复组件。
6. 保持项目 UI 风格一致。
7. 保持合理拆分，但不过度架构。

---

## 2. 核心原则

1. UI 必须低认知负担。
2. loading / error / empty 必须闭环。
3. 优先复用已有组件。
4. 优先复用已有设计系统。
5. 不做视觉孤岛。
6. 不为小页面过度拆分。
7. 不允许巨石组件。
8. UI 与业务逻辑尽量分离。
9. 不允许 Emoji 当正式图标。
10. 移动端高频按钮必须靠近手指路径，底部固定操作必须处理安全区。
11. 弹窗、抽屉、资产库、选择器必须有全局层级约定，当前交互层永远在最上方。

---

## 3. 触发条件

以下情况必须激活：

- 页面开发
- UI 重构
- Dashboard
- 表单
- 弹窗
- Table
- Card
- Tabs
- Loading
- Error Boundary
- Empty State
- 响应式布局
- iOS 安全区
- 触控热区
- 弹窗层级
- 样式调整
- 图标调整
- Design System
- 前端组件优化

---

## 4. 不触发条件

以下情况通常不需要：

- 后端逻辑
- migration
- Docker
- CI/CD
- 数据库
- 非 UI 类工具函数
- 纯部署问题

---

## 5. UI 原则

### A. 图标规则

禁止：

```text
❌ Emoji 充当正式图标
```

优先：

- lucide
- heroicons
- svg assets
- 项目已有 icon system

规则：

1. 图标必须语义化。
2. 图标必须与主色调一致。
3. 不引入新的图标体系，除非必要。
4. 不允许多个风格混用。

---

### B. Loading / Error / Empty

必须考虑：

- loading
- skeleton
- error
- retry
- empty state

禁止：

```text
接口请求中页面完全空白
```

或：

```text
报错无反馈
```

---

### C. 表单

必须：

- 有校验
- 有错误提示
- 有提交状态
- 有 disabled 状态

禁止：

```text
疯狂点击提交
```

---

### D. Dashboard / Table

必须：

- 有 empty state
- 有 loading
- 有分页或性能考虑
- 有错误反馈

禁止：

```text
一次性渲染巨大数据
```

---

### E. Modal / Drawer

必须：

- 支持关闭
- 支持 ESC
- 支持 loading
- 支持错误反馈
- 支持焦点/滚动隔离
- 支持底部高频操作固定展示
- 不被页面底部蒙版、目录、资产浮层遮挡

禁止：

```text
点击无响应
```

### F. iOS / 移动端

必须检查：

- 顶部导航是否避开状态栏。
- 底部按钮是否处理 safe-area-inset-bottom。
- 可点击区域是否至少接近 44px。
- 固定/悬浮层是否遮挡主要内容。
- 弹窗内部滚动是否可用，背景滚动是否被正确锁定。
- 文案是否在窄屏换行失控。
- PC 与移动端是否存在功能缺失。

禁止：

```text
PC 能用、移动端入口丢失
```

---

## 6. 拆分规则

当组件同时包含：

- 视图
- API 请求
- 大量状态
- 数据转换
- 表单逻辑
- 样式逻辑

时：

应该考虑拆分：

```text
components/
hooks/
services/
utils/
types/
```

但：

禁止为了拆分而拆分。

---

## 7. 巨石组件防御

以下情况视为高风险巨石组件：

- 超过 400 行
- 多个业务域
- 多个 API
- 多个复杂 useEffect
- 大量 inline logic
- 大量 inline style
- 多个 modal
- 多个 table
- 多个 form

建议：

- 提取 hook
- 提取 service
- 提取 section component
- 提取 types

禁止：

```text
所有逻辑塞一个 tsx
```

---

## 8. 状态管理规则

优先：

- 复用已有 store/context
- 复用已有 hook

禁止：

```text
重复创建全局状态
```

修改前必须：

读取：

```text
TOPOLOGY.md -> State Index
```

---

## 9. 样式规则

遵循项目已有体系：

- Tailwind
- CSS Modules
- styled-components
- emotion
- SCSS

禁止：

- 混用多个体系
- 局部引入完全不同设计语言
- 大量 !important
- inline style 泛滥

---

## 10. 响应式规则

必须考虑：

- 手机
- 平板
- 桌面

至少：

```text
核心布局不能崩
```

禁止：

```text
只在自己屏幕尺寸能用
```

---

## 11. 性能规则

必须注意：

- memo
- virtualization
- debounce
- lazy loading
- image optimization

但：

禁止：

```text
为了性能做过度复杂优化
```

---

## 12. DEPLOY_MANIFEST 联动规则

以下情况必须更新：

```text
DEPLOY_MANIFEST.md
```

- 核心页面
- 路由
- layout
- build config
- global state
- 前后端字段联动
- SSR/CSR 切换
- hydration 风险

以下情况通常不需要：

- 文案
- 小样式
- icon 替换
- 局部 spacing

---

## 13. TOPOLOGY 联动规则

以下情况必须更新：

```text
TOPOLOGY.md
```

- 新增页面
- 新增模块
- 新增 global state
- 新增 design system
- 新增 shared component
- 新增 layout system
- 目录结构变化

---

## 14. 常见问题防御

### A. React / Next.js

检查：

- hydration mismatch
- stale closure
- dependency array
- async race
- server/client boundary

### E. UniApp / H5

检查：

- tabBar 页面跳转必须使用 `switchTab`。
- H5 构建期开关是否正确注入。
- fixed 元素在移动端是否越过安全区。
- scroll-view / 页面滚动是否被弹层锁死。

---

### B. Loading 问题

检查：

- 是否有 pending state
- 是否有 retry
- 是否阻塞主线程

---

### C. 表单问题

检查：

- disabled state
- duplicate submit
- validation
- optimistic update

---

### D. UI 一致性

检查：

- spacing
- typography
- color
- icon style
- border radius
- shadow

---

## 15. 禁止行为

禁止：

- Emoji 充当正式图标。
- 页面没有 loading/error。
- 所有逻辑塞一个文件。
- 重复创建 store。
- 大量复制粘贴组件。
- 不复用 design system。
- 不读 TOPOLOGY.md。
- 样式体系混乱。
- 不考虑响应式。
- 不考虑错误反馈。
- 不考虑 empty state。
- 不考虑提交状态。
- 移动端功能比 PC 少。
- 弹层 z-index 无全局约定。

---

## 16. 结束汇报

结束时只允许：

```text
UI：
状态闭环：
TOPOLOGY.md：已更新 / 无结构变化
DEPLOY_MANIFEST.md：已更新 / 无需记录
```

结束汇报保持简短，只保留 UI 结果、状态闭环、验证和风险。
