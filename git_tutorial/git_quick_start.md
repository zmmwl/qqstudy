# Git版本控制速成教程

> 适合初中生的Git入门教程 - 30分钟学会版本控制！

---

## 目录

1. [为什么需要版本控制？](#第1节为什么需要版本控制)
2. [安装和配置](#第2节安装和配置)
3. [创建第一个仓库](#第3节创建第一个仓库)
4. [查看和回退](#第4节查看和回退)
5. [分支管理](#第5节分支管理)
6. [远程仓库 GitHub](#第6节远程仓库-github)
7. [协作开发](#第7节协作开发)
8. [最佳实践](#第8节最佳实践)

---

## 第1节：为什么需要版本控制？

### 故事：论文修改的噩梦

小明是一名初二学生，期末要交一篇研究报告。看看他的文件夹变成了什么样：

```
我的文档/
├── 研究报告.doc
├── 研究报告_修改.doc
├── 研究报告_最终版.doc
├── 研究报告_最终版_2.doc
├── 研究报告_老师改.doc
├── 研究报告_真的最终版.doc
├── 研究报告_打死不改了.doc
└── 研究报告_最终版_老师又改了_2024.doc
```

**问题来了：**
- 哪个是最新的？
- 老师上周说要改的那段在哪？
- 如果删错了怎么办？
- 两个人同时改怎么合并？

### Git就是解决方案

想象一下，如果有一个"时间机器"：

```
git_tutorial/
└── 研究报告.doc    # 只需要一个文件！
```

但这个文件有**超能力**：
- 可以随时回到过去任何一个版本
- 可以看到每次改了什么
- 可以多人同时修改，自动合并
- 永远不会丢失任何内容

这就是 **Git** - 程序员的时间机器！

### 什么是Git？

Git是一个**分布式版本控制系统**，就像给你的项目装了一个"时光机"：

| 功能 | 比喻 |
|------|------|
| 记录修改 | 游戏存档 |
| 查看历史 | 回放录像 |
| 回到过去 | 读取存档 |
| 多人协作 | 多人联机 |
| 分支开发 | 平行世界 |

---

## 第2节：安装和配置

### 2.1 安装Git

**Windows系统：**
1. 访问 https://git-scm.com/download/win
2. 下载安装包，一路"下一步"即可
3. 安装完成后，右键菜单会出现"Git Bash Here"

**Mac系统：**
```bash
# 打开终端，输入：
brew install git
```

**Linux系统（Ubuntu/Debian）：**
```bash
sudo apt-get install git
```

### 2.2 验证安装

打开终端（Windows用Git Bash），输入：

```bash
git --version
```

如果显示版本号，说明安装成功！
```
git version 2.43.0
```

### 2.3 配置你的身份

Git需要知道你是谁，这样才能记录是谁做的修改。

```bash
# 设置用户名（用你自己的名字）
git config --global user.name "小明"

# 设置邮箱（用你自己的邮箱）
git config --global user.email "xiaoming@example.com"

# 查看配置
git config --list
```

**说明：**
- `--global` 表示全局配置，对所有项目生效
- 只需要配置一次，以后就不用再配了

### 2.4 推荐配置

```bash
# 设置默认分支名为main
git config --global init.defaultBranch main

# 设置默认编辑器（可选）
git config --global core.editor "code --wait"  # VS Code
```

---

## 第3节：创建第一个仓库

### 3.1 什么是仓库？

**仓库（Repository）** = 被Git管理的文件夹

想象它是一个特殊的文件夹，里面有个隐形的小助手，记录着你的一举一动。

### 3.2 创建仓库

```bash
# 1. 创建一个新文件夹
mkdir my_project

# 2. 进入文件夹
cd my_project

# 3. 初始化Git仓库
git init
```

输出：
```
Initialized empty Git repository in /path/my_project/.git/
```

现在这个文件夹就变成了一个Git仓库！

**看看发生了什么：**
```bash
# 查看隐藏文件
ls -la
```

你会发现多了一个 `.git` 文件夹，这就是Git存储所有版本信息的地方。

### 3.3 Git的三个区域

在Git中，文件有三个状态：

```
┌─────────────┐    git add    ┌─────────────┐   git commit   ┌─────────────┐
│  工作区     │ ────────────> │   暂存区    │  ────────────> │   本地仓库  │
│ (Working)   │               │  (Staging)  │                │ (Repository)│
│  你编辑文件  │               │  准备提交   │                │  已保存版本  │
└─────────────┘               └─────────────┘                └─────────────┘
```

**比喻理解：**
- **工作区**：你的书桌，正在写作业
- **暂存区**：书包，把要交的作业放进去
- **本地仓库**：老师的档案柜，永久保存

### 3.4 添加和提交文件

让我们创建第一个文件：

```bash
# 创建一个文件
echo "# 我的项目" > README.md

# 再创建一个Python文件
echo 'print("Hello Git!")' > hello.py
```

**第一步：查看状态**
```bash
git status
```

输出：
```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md
        hello.py

nothing added to commit but untracked files present (use "git add" to track)
```

**第二步：添加到暂存区**
```bash
# 添加单个文件
git add README.md

# 或者添加所有文件
git add .

# 再次查看状态
git status
```

输出：
```
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hello.py
```

**第三步：提交到仓库**
```bash
# 提交，并写上说明
git commit -m "第一次提交：添加README文件"
```

输出：
```
[main (root-commit) a1b2c3d] 第一次提交：添加README文件
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
```

### 3.5 查看提交历史

```bash
# 查看历史记录
git log

# 简洁模式
git log --oneline

# 图形化显示
git log --oneline --graph --all
```

输出：
```
a1b2c3d (HEAD -> main) 第一次提交：添加README文件
```

### 3.6 完整流程总结

```bash
# 1. 初始化仓库
git init

# 2. 创建/修改文件
echo "内容" > 文件名

# 3. 查看状态
git status

# 4. 添加到暂存区
git add 文件名    # 或 git add .

# 5. 提交
git commit -m "提交说明"

# 6. 查看历史
git log
```

---

## 第4节：查看和回退

### 4.1 查看当前状态

```bash
# 查看工作区状态
git status

# 简洁模式
git status -s
```

**状态符号说明：**
| 符号 | 含义 |
|------|------|
| `??` | 未跟踪的新文件 |
| `A` | 已添加到暂存区 |
| `M` | 已修改 |
| `D` | 已删除 |

### 4.2 查看修改内容

```bash
# 查看工作区与暂存区的差异
git diff

# 查看暂存区与最新提交的差异
git diff --staged

# 查看两个版本之间的差异
git diff 版本号1 版本号2
```

**示例输出：**
```diff
diff --git a/README.md b/README.md
index abc1234..def5678 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,2 @@
 # 我的项目
+这是新增的一行
```

- 绿色（+）：新增内容
- 红色（-）：删除内容

### 4.3 回退操作

**场景1：撤销工作区的修改（还没add）**

```bash
# 撤销单个文件的修改
git checkout -- 文件名

# 或者用新命令
git restore 文件名
```

**场景2：取消暂存（已add，想撤销）**

```bash
# 取消暂存，但保留修改
git reset HEAD 文件名

# 或者用新命令
git restore --staged 文件名
```

**场景3：回退到上一个版本**

```bash
# 查看历史，找到要回退的版本
git log --oneline

# 回退到上一个版本
git reset --hard HEAD^

# 回退到上上个版本
git reset --hard HEAD^^

# 回退到指定版本
git reset --hard 版本号
```

**reset 参数说明：**
| 参数 | 效果 |
|------|------|
| `--soft` | 只回退commit，保留修改在暂存区 |
| `--mixed` | 回退commit和add，保留修改在工作区（默认）|
| `--hard` | 全部回退，修改全部丢失（危险！）|

### 4.4 撤销回退（后悔药）

```bash
# 查看所有操作记录
git reflog

# 找到要恢复的版本，然后reset回去
git reset --hard 版本号
```

### 4.5 删除文件

```bash
# 从Git和工作区都删除
git rm 文件名
git commit -m "删除文件"

# 只从Git删除，保留本地文件
git rm --cached 文件名
git commit -m "停止跟踪文件"
```

---

## 第5节：分支管理

### 5.1 什么是分支？

**分支**就像是平行宇宙！

想象你在写小说：
- **主线剧情**：主角正常发展（main分支）
- **支线剧情**：如果主角当初做了不同选择会怎样？（feature分支）

如果支线剧情写得好，可以合并到主线；如果不好，直接删掉，不影响主线。

```
        ┌─────────┐    ┌─────────┐
        │ feature │───>│ 合并    │
        └─────────┘    └─────────┘
             ↑              ↑
             │              │
main ───●────●────●────●────●────●
        │         │
        │         │
        └─────────┴──── 继续开发
```

### 5.2 分支基本操作

**查看分支：**
```bash
# 查看本地分支
git branch

# 查看所有分支（包括远程）
git branch -a
```

**创建分支：**
```bash
# 创建新分支
git branch 分支名

# 创建并切换到新分支
git checkout -b 分支名

# 或者用新命令
git switch -c 分支名
```

**切换分支：**
```bash
# 切换到已有分支
git checkout 分支名

# 或者用新命令
git switch 分支名
```

**删除分支：**
```bash
# 删除已合并的分支
git branch -d 分支名

# 强制删除（未合并也可以删）
git branch -D 分支名
```

### 5.3 分支实战示例

```bash
# 1. 创建一个新项目
mkdir game_project
cd game_project
git init

# 2. 创建主文件
echo "# 游戏项目" > README.md
git add .
git commit -m "初始化项目"

# 3. 创建新功能分支
git checkout -b feature/sound

# 4. 在新分支上开发
echo "添加音效功能" >> README.md
git add .
git commit -m "添加音效功能"

# 5. 切回主分支
git checkout main

# 6. 合并新功能
git merge feature/sound

# 7. 删除功能分支
git branch -d feature/sound
```

### 5.4 合并分支

**快速合并（Fast-forward）：**
当目标分支没有新提交时，直接移动指针。

```bash
git merge 分支名
```

**普通合并：**
当两个分支都有新提交时，会创建一个合并提交。

```bash
# 合并时保留分支信息
git merge --no-ff 分支名 -m "合并分支"
```

### 5.5 解决冲突

当两个分支修改了同一文件的同一位置，就会产生冲突。

**模拟冲突：**
```bash
# 创建测试分支
git checkout -b test

# 修改文件
echo "这是test分支的内容" > conflict.txt
git add .
git commit -m "test分支修改"

# 切回main分支
git checkout main

# 修改同一文件的同一位置
echo "这是main分支的内容" > conflict.txt
git add .
git commit -m "main分支修改"

# 尝试合并
git merge test
```

**冲突提示：**
```
CONFLICT (add/add): Merge conflict in conflict.txt
Automatic merge failed; fix conflicts and then commit the result.
```

**查看冲突文件：**
```bash
cat conflict.txt
```

```
<<<<<<< HEAD
这是main分支的内容
=======
这是test分支的内容
>>>>>>> test
```

**解决步骤：**
1. 手动编辑文件，保留想要的内容
2. 删除冲突标记（`<<<<<<<`, `=======`, `>>>>>>>`）
3. 添加并提交

```bash
# 手动解决冲突后
echo "这是合并后的内容" > conflict.txt
git add conflict.txt
git commit -m "解决合并冲突"
```

---

## 第6节：远程仓库 GitHub

### 6.1 什么是GitHub？

**GitHub** = Git仓库的云存储 + 程序员的社交网络

就像：
- Git是游戏机
- GitHub是游戏服务器（可以联机）

### 6.2 注册GitHub账号

1. 访问 https://github.com
2. 点击 "Sign up" 注册
3. 填写用户名、邮箱、密码
4. 验证邮箱

### 6.3 配置SSH密钥（推荐）

**生成SSH密钥：**
```bash
# 生成密钥（邮箱换成你的）
ssh-keygen -t ed25519 -C "your_email@example.com"

# 一路回车使用默认设置
# 查看公钥
cat ~/.ssh/id_ed25519.pub
```

**添加到GitHub：**
1. 复制公钥内容
2. GitHub → Settings → SSH and GPG keys → New SSH key
3. 粘贴保存

**测试连接：**
```bash
ssh -T git@github.com
```

### 6.4 创建远程仓库

1. GitHub首页点击 "New repository"
2. 填写仓库名（如：my_project）
3. 选择 Public（公开）或 Private（私有）
4. 不要勾选 "Initialize with README"（已有本地仓库时）
5. 点击 "Create repository"

### 6.5 关联远程仓库

```bash
# 添加远程仓库
git remote add origin git@github.com:用户名/仓库名.git

# 查看远程仓库
git remote -v

# 修改远程仓库地址
git remote set-url origin 新地址

# 删除远程仓库关联
git remote remove origin
```

### 6.6 推送和拉取

**推送（Push）：上传到远程**
```bash
# 第一次推送（设置上游分支）
git push -u origin main

# 以后推送
git push

# 推送所有分支
git push --all origin
```

**拉取（Pull）：从远程下载**
```bash
# 拉取并合并
git pull origin main

# 如果已设置上游，可直接
git pull
```

**获取（Fetch）：只下载不合并**
```bash
git fetch origin
git merge origin/main
```

### 6.7 克隆仓库

**克隆现有仓库：**
```bash
# HTTPS方式
git clone https://github.com/用户名/仓库名.git

# SSH方式（推荐）
git clone git@github.com:用户名/仓库名.git

# 克隆到指定文件夹
git clone 仓库地址 文件夹名
```

### 6.8 完整流程示例

```bash
# 场景：把本地项目上传到GitHub

# 1. 初始化本地仓库
cd my_project
git init
git add .
git commit -m "初始化项目"

# 2. 在GitHub创建仓库后，关联远程
git remote add origin git@github.com:用户名/my_project.git

# 3. 推送到GitHub
git push -u origin main

# 4. 以后每次更新
git add .
git commit -m "更新说明"
git push
```

---

## 第7节：协作开发

### 7.1 协作流程概述

团队协作的标准流程：

```
Fork → Clone → Branch → Commit → Push → Pull Request → Merge
```

### 7.2 Fork（复制别人的项目）

**Fork** = 把别人的仓库复制到自己账号下

1. 在GitHub上找到想参与的项目
2. 点击右上角 "Fork" 按钮
3. 选择自己的账号，确认Fork

### 7.3 Pull Request（PR）

**Pull Request** = 请求项目作者合并你的修改

**步骤：**
1. Fork项目
2. Clone到本地
3. 创建功能分支
4. 修改并提交
5. Push到自己的仓库
6. 在GitHub上创建Pull Request

**示例：**
```bash
# 1. Clone你Fork的仓库
git clone git@github.com:你的用户名/项目名.git
cd 项目名

# 2. 创建功能分支
git checkout -b fix-typo

# 3. 修改文件
echo "修正了一些错别字" >> README.md

# 4. 提交
git add .
git commit -m "修复README中的错别字"

# 5. 推送到你的仓库
git push origin fix-typo

# 6. 在GitHub上点击 "Compare & pull request" 创建PR
```

### 7.4 保持Fork同步

当原仓库更新后，你的Fork可能落后：

```bash
# 添加原仓库为上游
git remote add upstream 原仓库地址

# 获取原仓库更新
git fetch upstream

# 合并到本地
git checkout main
git merge upstream/main

# 推送到你的仓库
git push origin main
```

### 7.5 代码审查

Pull Request的流程：
1. 提交PR
2. 项目维护者审查代码
3. 可能提出修改建议
4. 你根据建议修改
5. 审查通过后合并

### 7.6 协作最佳实践

1. **每次PR只做一件事**
2. **写清楚PR的描述**
3. **保持代码风格一致**
4. **及时响应评论**
5. **尊重项目贡献指南**

---

## 第8节：最佳实践

### 8.1 Commit规范

**好的提交信息：**
```
feat: 添加用户登录功能
fix: 修复登录页面样式问题
docs: 更新API文档
style: 格式化代码
refactor: 重构用户模块
test: 添加登录测试用例
chore: 更新依赖版本
```

**提交信息格式：**
```
<类型>: <简短描述>

[可选的详细描述]

[可选的Issue关联]
```

**类型说明：**
| 类型 | 说明 |
|------|------|
| feat | 新功能 |
| fix | 修复bug |
| docs | 文档修改 |
| style | 代码格式（不影响功能）|
| refactor | 重构代码 |
| test | 测试相关 |
| chore | 构建/工具变动 |

**示例：**
```bash
git commit -m "feat: 添加用户注册功能

- 添加注册页面
- 实现表单验证
- 连接后端API

Closes #123"
```

### 8.2 .gitignore文件

**作用：** 告诉Git哪些文件不需要管理

**常用模板：**

```gitignore
# Python
__pycache__/
*.py[cod]
*.pyo
.env
venv/
.venv/

# Node.js
node_modules/
npm-debug.log

# IDE
.idea/
.vscode/
*.swp
*.swo

# 系统文件
.DS_Store
Thumbs.db

# 编译产物
dist/
build/
*.exe

# 敏感信息
.env
*.key
*.pem
config.local.json
```

**语法规则：**
```gitignore
# 注释
*.log        # 忽略所有.log文件
/TODO        # 只忽略根目录的TODO
build/       # 忽略build目录
!important.log # 不忽略这个文件（例外）
```

### 8.3 分支策略

**Git Flow模型：**

```
main（生产分支）
  │
  └── develop（开发分支）
        │
        ├── feature/xxx（功能分支）
        ├── feature/yyy
        │
        └── release/x.x（发布分支）
              │
              └── hotfix/xxx（热修复分支）
```

**简化版（适合小团队）：**

| 分支 | 用途 |
|------|------|
| main | 稳定的生产版本 |
| develop | 开发中的版本 |
| feature/* | 新功能开发 |
| hotfix/* | 紧急修复 |

**操作流程：**
```bash
# 开发新功能
git checkout -b feature/login develop
# ... 开发 ...
git commit -m "feat: 完成登录功能"
git checkout develop
git merge feature/login
git branch -d feature/login

# 发布
git checkout main
git merge develop
git tag -a v1.0.0 -m "版本1.0.0"
git push origin main --tags
```

### 8.4 其他好习惯

1. **频繁小提交**
   ```bash
   # 好：每个功能点一个提交
   git commit -m "添加用户名输入框"
   git commit -m "添加密码输入框"
   git commit -m "添加登录按钮"

   # 不好：一次提交太多
   git commit -m "完成了整个登录系统以及数据库和前端等等"
   ```

2. **推送前先拉取**
   ```bash
   git pull --rebase
   git push
   ```

3. **使用标签**
   ```bash
   # 创建标签
   git tag v1.0.0
   git tag -a v1.0.0 -m "发布1.0.0版本"

   # 推送标签
   git push origin v1.0.0
   git push origin --tags

   # 查看标签
   git tag -l
   ```

4. **使用别名简化命令**
   ```bash
   git config --global alias.st status
   git config --global alias.co checkout
   git config --global alias.br branch
   git config --global alias.ci commit
   git config --global alias.lg "log --oneline --graph --all"

   # 使用
   git st
   git lg
   ```

5. **使用README**
   ```markdown
   # 项目名称

   简短的项目描述

   ## 安装
   ## 使用方法
   ## 贡献指南
   ## 许可证
   ```

---

## 总结

恭喜你完成了Git速成教程！现在你已经掌握了：

- 基本的版本控制概念
- 创建和管理仓库
- 提交和回退操作
- 分支管理
- 远程仓库操作
- 团队协作流程
- 最佳实践

**记住这些核心命令：**

| 命令 | 作用 |
|------|------|
| `git init` | 初始化仓库 |
| `git add .` | 添加所有文件 |
| `git commit -m "msg"` | 提交 |
| `git status` | 查看状态 |
| `git log` | 查看历史 |
| `git branch` | 分支操作 |
| `git checkout` | 切换分支 |
| `git merge` | 合并分支 |
| `git clone` | 克隆仓库 |
| `git push` | 推送 |
| `git pull` | 拉取 |

**下一步：**
1. 完成练习题巩固知识
2. 创建自己的GitHub仓库
3. 参与开源项目
4. 学习更多Git高级功能

---

*教程作者：Claude*
*最后更新：2024年*
