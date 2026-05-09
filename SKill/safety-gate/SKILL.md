# safety-gate

## 1. 目标

用于控制：

- 高风险操作
- 不可逆操作
- 生产环境操作
- 数据库操作
- 权限与密钥操作
- 大范围删除
- Git 推送
- 线上部署

目标：

1. 防止 AI 自动执行危险操作。
2. 防止误删、误部署、误迁移。
3. 防止真实密钥泄漏。
4. 防止 AI 在高风险情况下自动推进。
5. 保持低打扰，仅在真正危险时确认。

---

## 2. 核心原则

1. 默认自动执行。
2. 只有真正高风险才中断确认。
3. 不允许“所有事情都确认”。
4. 不允许“高风险也不确认”。
5. 必须给出影响范围。
6. 必须给出回滚建议。
7. 必须说明为什么危险。

---

## 3. 必须确认的操作

以下操作必须暂停并等待用户确认：

### A. Git

- git push
- git push --force
- git reset --hard
- git clean -fd
- git rebase
- git branch -D

---

### B. 文件删除

- rm -rf
- del /s
- rmdir /s
- 删除大量目录
- 清空目录
- 覆盖重要配置文件

---

### C. 数据库

- migration
- drop table
- truncate
- delete all
- schema change
- production db write

---

### D. 部署

- production deploy
- kubectl apply
- docker compose down
- pm2 restart
- nginx reload
- systemctl restart

---

### E. 环境变量 / 权限

- 修改 .env
- 修改 secret
- 修改 token
- 修改权限策略
- 修改认证逻辑
- 打包或分发包含真实 secret 的 sensitive 交付包

---

### F. 不可逆脚本

- cleanup script
- destructive script
- batch delete
- overwrite script

---

## 4. 不需要确认的操作

以下操作默认自动执行：

- 搜索文件
- 读取文件
- 修改普通代码
- 新增普通组件
- 新增普通 hook
- 新增普通 service
- lint
- build
- typecheck
- test
- 更新 TOPOLOGY.md
- 更新 DEPLOY_MANIFEST.md
- 合并部署记录
- 归档已完成部署记录

---

## 5. 确认前必须说明

执行高风险操作前，必须说明：

```text
操作：
影响范围：
涉及环境：
风险：
回滚方式：
建议命令：
```

确认问题必须带上上下文，不能只给一个空泛的执行请求。

---

## 6. 高风险识别规则

以下情况自动提升风险等级：

- 当前环境是 production
- 涉及真实数据库
- 涉及真实用户数据
- 涉及权限系统
- 涉及支付
- 涉及鉴权
- 涉及 CI/CD
- 涉及 secrets
- 涉及基础设施

---

## 7. 部署安全规则

生产部署前必须：

1. 检查 DEPLOY_MANIFEST.md
2. 检查 Pending Deployment
3. 检查 migration 顺序
4. 检查 env sync
5. 检查 rollback
6. 检查 build
7. 检查 verification checklist

禁止：

```text
不看 DEPLOY_MANIFEST.md 直接部署
```

---

## 8. 数据库安全规则

migration 前必须：

- 确认环境
- 确认 rollback
- 确认顺序
- 确认依赖

禁止：

- 自动 drop table
- 自动 truncate
- 自动 delete all

除非用户明确确认。

---

## 9. Secret 安全规则

禁止：

- 输出真实 secret
- 输出 token
- 输出 production password
- 写入真实密钥到 TOPOLOGY.md
- 写入真实密钥到 DEPLOY_MANIFEST.md

允许：

```text
只记录变量名
```

例如：

```text
OPENAI_API_KEY
DATABASE_URL
```

禁止记录真实值。

敏感交付包规则：

- 可以在本地生成包含真实配置的压缩包，但必须明确标注 sensitive。
- 不在聊天中展示真实值。
- 不提交到 Git。
- 不上传公开平台。
- 交付包必须包含 README，说明适用范围和风险。

---

## 10. 多项目保护

如果存在：

- 多个 package.json
- 多个 git root
- 多个 deploy target

且可能误操作：

必须确认当前项目根目录。

---

## 11. 自动推进规则

如果不属于高风险：

```text
默认自动推进
```

禁止：

```text
每一步都请求确认
```

---

## 12. 常见危险防御

### A. Git

检查：

- 当前 branch
- uncommitted changes
- remote target

---

### B. Deploy

检查：

- environment
- rollback
- build
- migration
- env sync

---

### C. 删除

检查：

- 路径
- glob
- scope
- 是否可恢复

---

### D. Database

检查：

- target db
- rollback
- backup
- migration dependency

---

## 13. 禁止行为

禁止：

- 高频确认低风险任务。
- 高风险不确认。
- 不说明影响范围。
- 不说明回滚方式。
- 输出真实 secret。
- 自动 destructive migration。
- 自动 force push。
- 自动生产部署。
- 自动清空数据库。
- 自动清空目录。

---

## 14. 结束汇报

结束时只允许：

```text
风险：
确认状态：
是否已执行：
回滚：
```

结束汇报保持简短，说明风险、确认状态、执行状态和回滚方式。
