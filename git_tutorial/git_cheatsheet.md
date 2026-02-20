# Git命令速查表

> 快速查找你需要的Git命令

---

## 配置相关

```bash
# 设置用户名
git config --global user.name "你的名字"

# 设置邮箱
git config --global user.email "你的邮箱"

# 查看所有配置
git config --list

# 设置默认分支名
git config --global init.defaultBranch main

# 设置命令别名
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.lg "log --oneline --graph --all"
```

---

## 仓库操作

```bash
# 初始化仓库
git init

# 克隆仓库
git clone <仓库地址>

# 克隆到指定文件夹
git clone <仓库地址> <文件夹名>

# 克隆指定分支
git clone -b <分支名> <仓库地址>
```

---

## 基本操作

```bash
# 查看状态
git status
git status -s                    # 简洁模式

# 添加文件到暂存区
git add <文件名>                  # 添加单个文件
git add .                        # 添加所有文件
git add -A                       # 添加所有文件（包括删除）
git add -u                       # 只添加已跟踪文件的修改

# 提交
git commit -m "提交信息"          # 提交
git commit -am "提交信息"         # 添加并提交（已跟踪文件）
git commit --amend -m "新信息"    # 修改上次提交信息
git commit --amend --no-edit     # 追加文件到上次提交

# 查看差异
git diff                         # 工作区 vs 暂存区
git diff --staged               # 暂存区 vs 最新提交
git diff HEAD                   # 工作区 vs 最新提交
git diff <版本1> <版本2>         # 两个版本间的差异
git diff <分支1> <分支2>         # 两个分支间的差异
```

---

## 历史查看

```bash
# 查看提交历史
git log
git log --oneline               # 简洁模式
git log --oneline --graph       # 图形化显示
git log --oneline --graph --all # 显示所有分支
git log -n 5                    # 只看最近5条
git log -p                      # 显示每次提交的差异
git log --stat                  # 显示文件变更统计

# 查看操作记录（后悔药）
git reflog

# 搜索提交
git log --grep="关键词"          # 按提交信息搜索
git log -S "代码内容"           # 按代码内容搜索

# 查看文件历史
git log -p <文件名>             # 查看某文件的修改历史
git log --follow <文件名>       # 跟踪文件重命名
```

---

## 撤销操作

```bash
# 撤销工作区修改
git checkout -- <文件名>
git restore <文件名>            # 新命令

# 取消暂存
git reset HEAD <文件名>
git restore --staged <文件名>   # 新命令

# 回退版本
git reset --soft HEAD^          # 回退commit，保留暂存区
git reset --mixed HEAD^         # 回退commit和暂存区（默认）
git reset --hard HEAD^          # 全部回退（危险！）
git reset --hard <版本号>       # 回退到指定版本

# 撤销提交（创建反向提交）
git revert <版本号>             # 安全，不会丢失历史

# 删除文件
git rm <文件名>                 # 删除文件并暂存
git rm --cached <文件名>        # 只从Git删除，保留本地
```

---

## 分支操作

```bash
# 查看分支
git branch                      # 本地分支
git branch -a                   # 所有分支（含远程）
git branch -r                   # 只看远程分支
git branch -v                   # 显示最后一次提交

# 创建分支
git branch <分支名>             # 创建分支
git checkout -b <分支名>        # 创建并切换
git switch -c <分支名>          # 新命令：创建并切换

# 切换分支
git checkout <分支名>
git switch <分支名>             # 新命令

# 合并分支
git merge <分支名>              # 合并到当前分支
git merge --no-ff <分支名>      # 禁用快进合并

# 删除分支
git branch -d <分支名>          # 删除已合并分支
git branch -D <分支名>          # 强制删除

# 重命名分支
git branch -m <旧名> <新名>
git branch -m <新名>            # 重命名当前分支

# 查看已合并/未合并的分支
git branch --merged
git branch --no-merged
```

---

## 远程操作

```bash
# 查看远程仓库
git remote
git remote -v                   # 显示地址

# 添加远程仓库
git remote add origin <地址>

# 修改远程仓库地址
git remote set-url origin <新地址>

# 删除远程仓库
git remote remove origin

# 推送
git push origin main            # 推送到main分支
git push -u origin main         # 第一次推送（设置上游）
git push                        # 之后简写
git push --all origin           # 推送所有分支
git push origin --tags          # 推送所有标签
git push -f                     # 强制推送（危险！）

# 拉取
git pull origin main            # 拉取并合并
git pull --rebase origin main   # 拉取并变基

# 获取（不合并）
git fetch origin
git fetch --all

# 查看远程分支信息
git remote show origin
```

---

## 标签操作

```bash
# 创建标签
git tag v1.0.0                  # 轻量标签
git tag -a v1.0.0 -m "说明"     # 附注标签
git tag v1.0.0 <版本号>         # 给历史版本打标签

# 查看标签
git tag
git tag -l "v1.*"               # 筛选标签
git show v1.0.0                 # 查看标签详情

# 推送标签
git push origin v1.0.0          # 推送单个标签
git push origin --tags          # 推送所有标签

# 删除标签
git tag -d v1.0.0               # 删除本地标签
git push origin --delete v1.0.0 # 删除远程标签

# 检出标签
git checkout v1.0.0             # 查看标签版本
git checkout -b version1 v1.0.0 # 从标签创建分支
```

---

## 暂存操作（Stash）

```bash
# 暂存当前工作
git stash
git stash save "说明"           # 带说明的暂存

# 查看暂存列表
git stash list

# 恢复暂存
git stash pop                   # 恢复并删除暂存
git stash apply                 # 恢复但保留暂存
git stash apply stash@{2}       # 恢复指定暂存

# 删除暂存
git stash drop                  # 删除最近暂存
git stash drop stash@{2}        # 删除指定暂存
git stash clear                 # 删除所有暂存

# 查看暂存内容
git stash show                  # 简要信息
git stash show -p               # 详细差异
```

---

## 变基操作（Rebase）

```bash
# 变基
git rebase main                 # 将当前分支变基到main

# 继续变基（解决冲突后）
git rebase --continue

# 跳过当前提交
git rebase --skip

# 放弃变基
git rebase --abort

# 交互式变基（可压缩、编辑、删除提交）
git rebase -i HEAD~3
```

---

## 其他实用命令

```bash
# 查看某行代码的修改历史
git blame <文件名>
git blame -L 10,20 <文件名>     # 只看10-20行

# 查找引入bug的提交
git bisect start
git bisect bad                  # 当前版本有bug
git bisect good v1.0.0          # 这个版本没问题
# Git会自动二分查找，直到找到问题提交
git bisect reset                # 结束查找

# 清理未跟踪文件
git clean -n                    # 预览要删除的文件
git clean -f                    # 删除未跟踪文件
git clean -fd                   # 删除未跟踪文件和目录

# 归档
git archive -o project.zip HEAD # 导出最新版本

# 统计
git shortlog -s                 # 查看贡献者统计
git log --author="名字" --oneline | wc -l  # 某人提交数
```

---

## 常用场景速查

### 场景1：新项目初始化
```bash
git init
git add .
git commit -m "初始化项目"
git remote add origin <地址>
git push -u origin main
```

### 场景2：日常开发流程
```bash
git pull                        # 先拉取最新代码
# ... 编写代码 ...
git status                      # 查看修改
git diff                        # 查看详细修改
git add .                       # 添加修改
git commit -m "提交信息"        # 提交
git push                        # 推送
```

### 场景3：创建新功能分支
```bash
git checkout -b feature/新功能
# ... 开发 ...
git add .
git commit -m "feat: 添加新功能"
git checkout main
git merge feature/新功能
git branch -d feature/新功能
git push
```

### 场景4：撤销最近一次提交（保留修改）
```bash
git reset --soft HEAD^
```

### 场景5：撤销已推送的提交
```bash
git revert <版本号>
git push
```

### 场景6：临时切换分支
```bash
git stash                       # 暂存当前工作
git checkout other-branch       # 切换分支做其他事
git checkout original-branch    # 回来
git stash pop                   # 恢复工作
```

### 场景7：同步Fork的仓库
```bash
git remote add upstream <原仓库地址>
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

### 场景8：解决合并冲突
```bash
# 冲突发生时
git status                      # 查看冲突文件
# ... 手动编辑冲突文件 ...
git add <冲突文件>
git commit -m "解决冲突"
```

---

## 状态符号速查

| 符号 | 含义 |
|------|------|
| `??` | 未跟踪的新文件 |
| `A ` | 新添加到暂存区 |
| `M ` | 已修改（在暂存区）|
| ` M` | 已修改（不在暂存区）|
| `MM` | 暂存区有修改，工作区也有修改 |
| `D ` | 已删除（在暂存区）|
| ` D` | 已删除（不在暂存区）|
| `R ` | 已重命名 |
| `C ` | 已复制 |

---

## Commit类型速查

| 类型 | 说明 | 示例 |
|------|------|------|
| `feat` | 新功能 | feat: 添加用户登录 |
| `fix` | 修复bug | fix: 修复登录验证 |
| `docs` | 文档 | docs: 更新README |
| `style` | 格式 | style: 格式化代码 |
| `refactor` | 重构 | refactor: 重构登录模块 |
| `test` | 测试 | test: 添加登录测试 |
| `chore` | 杂项 | chore: 更新依赖 |
| `perf` | 性能 | perf: 优化查询速度 |
| `ci` | CI/CD | ci: 添加GitHub Actions |
| `revert` | 回退 | revert: 回退xxx提交 |

---

## .gitignore常用模板

```gitignore
# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
.Python
venv/
.env

# Node.js
node_modules/
npm-debug.log
yarn-error.log

# Java
*.class
*.jar
*.war
target/

# IDE
.idea/
.vscode/
*.sublime-*

# 系统
.DS_Store
Thumbs.db

# 敏感信息
.env
*.key
*.pem
secrets/
```

---

*收藏这份速查表，随时查阅！*
