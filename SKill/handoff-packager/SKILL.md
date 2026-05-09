# handoff-packager

## 1. 目标

用于给远程团队、本地部署、提示词协作或调试复现打包资料。目标是可用、可审计、分层清晰，不泄露到不该泄露的渠道。

## 2. 触发条件

- 用户要求打包提示词、配置、dev 环境、大模型配置。
- 用户要求交给远程团队、外包、同事、本地复现。
- 需要导出 SQL、配置 JSON、`.env`、模型供应商数据。
- 需要区分公开资料和敏感资料。

## 3. 核心原则

1. 默认生成 `public/` 和 `sensitive/` 两层。
2. 默认脱敏，除非用户明确要求可直接跑通。
3. 真实密钥只进入本地包，不在聊天中打印。
4. 包内必须有 `README.md` 和 `MANIFEST.json`。
5. 不包含数据库文件、上传素材、日志、node_modules、构建产物，除非用户明确要求。
6. 压缩包放入项目内 `handoff/` 或用户指定目录。

## 4. 推荐结构

```text
handoff/<project>_<purpose>_<timestamp>/
├── README.md
├── MANIFEST.json
├── public/
│   ├── prompts/
│   ├── config-data/
│   └── sanitized-sql/
└── sensitive/
    ├── env-files/
    ├── raw-sql/
    ├── model-config/
    └── runbooks/
```

## 5. 工作流

### Step 1：确认用途

判断是：

- 只评审提示词。
- 本地复现。
- 远程团队直接跑通。
- 生产迁移参考。

### Step 2：收集资料

常见资料：

- 提示词源文件。
- prompt template 导出。
- creative configs。
- genre configs。
- model providers/models。
- `.env.example` 或真实 `.env`。
- seed/sync/check 脚本。
- README/runbook。

### Step 3：敏感分层

- public：脱敏配置、提示词、说明文档。
- sensitive：真实 env、raw SQL、模型 key、服务器地址。

### Step 4：生成清单

`MANIFEST.json` 至少包含：

- 相对路径。
- 文件大小。
- 是否 sensitive。
- 生成时间。

### Step 5：校验

检查：

- zip 是否生成。
- 是否包含 README。
- 是否误包含 node_modules/build/log/uploads/db。
- sensitive 包是否明确标注。

## 6. 禁止行为

- 在聊天中直接输出真实 key。
- 把 sensitive 包提交到 Git。
- 混淆脱敏 SQL 和未脱敏 SQL。
- 只打提示词但漏掉模型和 env，导致队友无法运行。

## 7. 结束汇报

```text
交付包：
public：
sensitive：
验证：
风险：
```
