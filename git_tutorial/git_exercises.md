# Git练习题

> 边学边练，掌握Git核心技能！

---

## 练习说明

- 每个练习都有明确的目标和步骤
- 建议按顺序完成
- 遇到问题可以查看提示
- 完成后对照答案检查

---

## 练习1：创建你的第一个仓库

### 目标
学会初始化仓库、添加文件、提交更改

### 步骤

1. 在桌面创建一个名为 `git_practice` 的文件夹
2. 进入该文件夹并初始化Git仓库
3. 创建一个 `hello.txt` 文件，内容为 "Hello, Git!"
4. 将文件添加到暂存区
5. 提交更改，提交信息为 "第一次提交"

### 预期结果
- 能够用 `git log` 看到提交记录
- 仓库中有1个文件和1次提交

### 提示
<details>
<summary>点击查看提示</summary>

```bash
mkdir git_practice
cd git_practice
git init
echo "Hello, Git!" > hello.txt
git add hello.txt
git commit -m "第一次提交"
git log
```
</details>

---

## 练习2：修改和查看历史

### 目标
学会查看状态、修改文件、查看历史

### 步骤

1. 继续使用练习1的仓库
2. 修改 `hello.txt`，添加一行 "Welcome to Git!"
3. 查看当前状态
4. 查看具体修改内容（diff）
5. 提交这次修改
6. 再创建一个 `README.md` 文件并提交
7. 查看提交历史（简洁模式）

### 预期结果
- 有3次提交记录
- 能用 `git diff` 看到修改内容

### 提示
<details>
<summary>点击查看提示</summary>

```bash
# 修改文件
echo "Welcome to Git!" >> hello.txt

# 查看状态和差异
git status
git diff

# 提交
git add hello.txt
git commit -m "添加欢迎信息"

# 创建新文件
echo "# Git练习项目" > README.md
git add README.md
git commit -m "添加README文件"

# 查看历史
git log --oneline
```
</details>

---

## 练习3：回退操作

### 目标
学会撤销修改和回退版本

### 步骤

1. 继续使用之前的仓库
2. 修改 `hello.txt`，添加一行 "这是要撤销的内容"
3. **不要提交**，直接撤销这次修改
4. 再修改文件，添加 "这是要取消暂存的内容"
5. 这次先 `git add`，然后取消暂存（保留修改）
6. 再添加并提交
7. 回退到上一个版本
8. 用 `git reflog` 找回并恢复到最新版本

### 预期结果
- 理解三种回退的区别
- 能用 `reflog` 恢复误删的提交

### 提示
<details>
<summary>点击查看提示</summary>

```bash
# 撤销工作区修改
echo "这是要撤销的内容" >> hello.txt
git restore hello.txt  # 或 git checkout -- hello.txt

# 取消暂存
echo "这是要取消暂存的内容" >> hello.txt
git add hello.txt
git restore --staged hello.txt  # 或 git reset HEAD hello.txt

# 提交
git add hello.txt
git commit -m "添加新内容"

# 回退版本
git reset --hard HEAD^

# 恢复
git reflog  # 找到之前的版本号
git reset --hard 版本号
```
</details>

---

## 练习4：分支基础

### 目标
学会创建、切换、合并分支

### 步骤

1. 创建新分支 `feature`
2. 切换到 `feature` 分支
3. 创建文件 `feature.txt`，内容为 "这是新功能"
4. 提交更改
5. 切换回 `main` 分支
6. 合并 `feature` 分支
7. 删除 `feature` 分支
8. 查看分支列表确认删除

### 预期结果
- 理解分支的概念
- 能独立完成分支操作

### 提示
<details>
<summary>点击查看提示</summary>

```bash
# 创建并切换分支
git checkout -b feature
# 或
git switch -c feature

# 创建文件并提交
echo "这是新功能" > feature.txt
git add feature.txt
git commit -m "添加新功能"

# 切换回main并合并
git checkout main
# 或
git switch main
git merge feature

# 删除分支
git branch -d feature

# 确认
git branch
```
</details>

---

## 练习5：解决合并冲突

### 目标
学会处理分支合并时的冲突

### 步骤

1. 确保在 `main` 分支
2. 创建文件 `conflict.txt`，内容为 "Main分支内容"
3. 提交
4. 创建并切换到新分支 `test`
5. 修改 `conflict.txt` 为 "Test分支内容"
6. 提交
7. 切换回 `main` 分支
8. 修改 `conflict.txt` 为 "Main分支修改后内容"
9. 提交
10. 尝试合并 `test` 分支
11. 手动解决冲突（保留两边的内容）
12. 完成合并

### 预期结果
- 理解什么情况会产生冲突
- 能手动解决冲突

### 提示
<details>
<summary>点击查看提示</summary>

```bash
# main分支创建文件
echo "Main分支内容" > conflict.txt
git add conflict.txt
git commit -m "main分支创建文件"

# 创建test分支并修改
git checkout -b test
echo "Test分支内容" > conflict.txt
git add conflict.txt
git commit -m "test分支修改"

# 回main分支并修改同一位置
git checkout main
echo "Main分支修改后内容" > conflict.txt
git add conflict.txt
git commit -m "main分支修改"

# 尝试合并（会产生冲突）
git merge test

# 此时查看文件会有冲突标记
cat conflict.txt

# 手动解决冲突，编辑文件为想要的内容
echo "合并后的内容：包含main和test的修改" > conflict.txt

# 完成合并
git add conflict.txt
git commit -m "解决合并冲突"
```
</details>

---

## 练习6：.gitignore使用

### 目标
学会使用.gitignore排除不需要管理的文件

### 步骤

1. 创建一个新的测试仓库
2. 创建以下文件：
   - `app.py`（需要管理）
   - `config.py`（需要管理）
   - `secret.key`（不需要管理，包含敏感信息）
   - `debug.log`（不需要管理，日志文件）
   - `__pycache__/cache.pyc`（不需要管理，缓存文件）
3. 创建 `.gitignore` 文件，排除不需要管理的文件
4. 运行 `git status` 确认只有需要的文件被跟踪
5. 添加并提交

### 预期结果
- 只有 `app.py`、`config.py` 和 `.gitignore` 被提交

### 提示
<details>
<summary>点击查看提示</summary>

```bash
# 创建文件
mkdir -p __pycache__
touch app.py config.py secret.key debug.log
touch __pycache__/cache.pyc

# 创建.gitignore
cat > .gitignore << 'EOF'
# 敏感信息
secret.key

# 日志文件
*.log

# Python缓存
__pycache__/
*.pyc
EOF

# 查看状态
git status

# 应该只看到 app.py, config.py, .gitignore
git add .
git commit -m "初始化项目"
```
</details>

---

## 练习7：GitHub基础操作

### 目标
学会创建GitHub仓库并推送代码

### 步骤

1. 在GitHub上创建一个新仓库（先不要初始化README）
2. 在本地创建一个项目
3. 关联远程仓库
4. 推送代码到GitHub
5. 在GitHub上查看你的代码
6. 在本地修改文件并推送
7. 在GitHub上确认修改已同步

### 注意
- 需要先注册GitHub账号
- 建议配置SSH密钥

### 提示
<details>
<summary>点击查看提示</summary>

```bash
# 创建本地项目
mkdir github_practice
cd github_practice
git init
echo "# GitHub练习项目" > README.md
git add .
git commit -m "初始化项目"

# 关联远程仓库（替换为你的用户名）
git remote add origin git@github.com:你的用户名/github_practice.git

# 推送
git push -u origin main

# 修改并推送
echo "这是更新内容" >> README.md
git add .
git commit -m "更新README"
git push
```
</details>

---

## 练习8：克隆和协作

### 目标
学会克隆仓库和基本的协作流程

### 步骤

1. 找一个你想参与的开源项目，或者同学的项目
2. Fork到自己的账号
3. Clone到本地
4. 创建一个功能分支
5. 做一些小修改（如修复错别字）
6. 提交并推送到你的Fork
7. 创建Pull Request

### 预期结果
- 完成一次完整的协作流程

### 提示
<details>
<summary>点击查看提示</summary>

```bash
# Clone你Fork的仓库
git clone git@github.com:你的用户名/项目名.git
cd 项目名

# 创建功能分支
git checkout -b fix-typo

# 做修改
# ... 编辑文件 ...

# 提交
git add .
git commit -m "docs: 修复README中的错别字"

# 推送
git push origin fix-typo

# 在GitHub上点击 "Create Pull Request"
```
</details>

---

## 练习9：综合挑战

### 目标
综合运用所学知识

### 场景
你正在开发一个简单的Python计算器项目，需要完成以下任务：

### 步骤

1. 创建项目文件夹 `calculator`
2. 初始化Git仓库
3. 创建 `.gitignore`（排除Python缓存和虚拟环境）
4. 在 `main` 分支创建基础结构：
   - `README.md`：项目说明
   - `calculator.py`：主程序（只包含一个简单的加法函数）
5. 提交：`git commit -m "feat: 初始化计算器项目"`
6. 创建 `feature/subtract` 分支，添加减法功能
7. 创建 `feature/multiply` 分支，添加乘法功能
8. 切换回 `main`，依次合并两个功能分支
9. 给项目打标签 `v1.0.0`
10. （可选）推送到GitHub

### 预期结果
- 项目有清晰的提交历史
- 能看到分支合并的图形化记录

### 提示
<details>
<summary>点击查看提示</summary>

```bash
# 初始化
mkdir calculator && cd calculator
git init

# 创建.gitignore
cat > .gitignore << 'EOF'
__pycache__/
*.pyc
venv/
.env
EOF

# 创建基础文件
echo "# 计算器项目" > README.md
cat > calculator.py << 'EOF'
def add(a, b):
    """加法"""
    return a + b

if __name__ == "__main__":
    print(add(1, 2))
EOF

git add .
git commit -m "feat: 初始化计算器项目"

# 减法分支
git checkout -b feature/subtract
cat > calculator.py << 'EOF'
def add(a, b):
    """加法"""
    return a + b

def subtract(a, b):
    """减法"""
    return a - b

if __name__ == "__main__":
    print(add(1, 2))
    print(subtract(5, 3))
EOF
git add .
git commit -m "feat: 添加减法功能"

# 乘法分支（从main分出去）
git checkout main
git checkout -b feature/multiply
cat > calculator.py << 'EOF'
def add(a, b):
    """加法"""
    return a + b

def multiply(a, b):
    """乘法"""
    return a * b

if __name__ == "__main__":
    print(add(1, 2))
    print(multiply(3, 4))
EOF
git add .
git commit -m "feat: 添加乘法功能"

# 合并分支
git checkout main
git merge feature/subtract
# 可能需要解决冲突

git merge feature/multiply
# 可能需要解决冲突

# 打标签
git tag -a v1.0.0 -m "版本1.0.0"

# 查看结果
git log --oneline --graph --all
```
</details>

---

## 练习10：实战模拟 - 团队协作

### 目标
模拟真实的团队协作场景

### 场景
两个人（用两个文件夹模拟）协作开发一个项目

### 步骤

**准备阶段（作为项目创建者）：**

1. 创建一个项目并推送到GitHub
2. 邀请你的"队友"（可以是用另一个账号，或者让同学参与）

**作为开发者A（项目负责人）：**
1. 在 `main` 分支创建项目基础结构
2. 创建 `develop` 分支
3. 在GitHub上设置 `develop` 为默认分支
4. 审查并合并PR

**作为开发者B（贡献者）：**
1. Clone项目
2. 从 `develop` 创建功能分支
3. 开发新功能
4. 提交PR

**协作流程：**
1. 开发者B提交PR
2. 开发者A审查代码
3. 如有问题，开发者B修改
4. 最终合并到 `develop`
5. 测试通过后，合并 `develop` 到 `main`

### 预期结果
- 理解完整的团队协作流程
- 熟悉PR审查和合并

---

## 自我检测清单

完成以上练习后，检查你是否掌握了：

### 基础操作
- [ ] 能够初始化新仓库
- [ ] 能够添加和提交文件
- [ ] 能够查看提交历史
- [ ] 能够查看当前状态

### 回退操作
- [ ] 能够撤销未暂存的修改
- [ ] 能够取消已暂存的文件
- [ ] 能够回退到之前版本
- [ ] 能够恢复误删的提交

### 分支操作
- [ ] 能够创建和切换分支
- [ ] 能够合并分支
- [ ] 能够删除分支
- [ ] 能够解决合并冲突

### 远程操作
- [ ] 能够关联远程仓库
- [ ] 能够推送代码
- [ ] 能够拉取更新
- [ ] 能够克隆仓库

### 协作能力
- [ ] 能够Fork项目
- [ ] 能够创建Pull Request
- [ ] 理解协作流程
- [ ] 能够保持Fork同步

---

## 常见问题解答

### Q1: 提交后想修改提交信息怎么办？
```bash
# 修改最近一次提交的信息
git commit --amend -m "新的提交信息"
```

### Q2: 提交时漏了文件怎么办？
```bash
# 添加漏掉的文件
git add 漏掉的文件
# 追加到上一次提交
git commit --amend --no-edit
```

### Q3: 如何查看某个文件的修改历史？
```bash
git log -p 文件名
```

### Q4: 如何撤销已经推送的提交？
```bash
# 方法1：创建一个反向提交（推荐）
git revert 版本号
git push

# 方法2：回退后强制推送（危险！）
git reset --hard 版本号
git push --force
```

### Q5: 如何暂存当前工作切换分支？
```bash
# 暂存
git stash

# 切换分支做其他事
git checkout other-branch

# 回来后恢复
git checkout original-branch
git stash pop
```

---

*完成这些练习，你就是Git小能手了！*
