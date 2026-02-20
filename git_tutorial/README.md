# Git版本控制速成教程

> 30分钟学会Git版本控制 - 专为初中生设计

## 简介

这是一套适合初中生学习的Git入门教程，通过故事和比喻讲解概念，让你快速掌握版本控制的精髓。

## 教程文件

| 文件 | 说明 |
|------|------|
| [git_quick_start.md](git_quick_start.md) | 主教程 - 从入门到精通 |
| [git_exercises.md](git_exercises.md) | 练习题 - 边学边练 |
| [git_cheatsheet.md](git_cheatsheet.md) | 速查表 - 快速查阅命令 |

## 学习路径

```
第1天：阅读第1-4节，完成练习1-3
       └── 掌握基本操作：init、add、commit、status、log

第2天：阅读第5节，完成练习4-5
       └── 掌握分支操作：branch、checkout、merge

第3天：阅读第6-7节，完成练习6-8
       └── 掌握远程操作：clone、push、pull、PR

第4天：阅读第8节，完成练习9-10
       └── 掌握最佳实践，完成综合挑战
```

## 快速开始

### 1. 安装Git

**Windows:**
- 访问 https://git-scm.com/download/win 下载安装

**Mac:**
```bash
brew install git
```

**Linux:**
```bash
sudo apt-get install git
```

### 2. 配置身份

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

### 3. 创建第一个仓库

```bash
mkdir my_project
cd my_project
git init
echo "# 我的项目" > README.md
git add .
git commit -m "第一次提交"
```

## 核心命令速记

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

## 常见问题

**Q: Git和GitHub有什么区别？**
> Git是版本控制工具，GitHub是托管Git仓库的网站。就像：Git是游戏机，GitHub是游戏服务器。

**Q: 什么时候应该提交？**
> 完成一个小功能、修复一个bug、或者做出一个有意义的改动时就提交。不要积累太多改动。

**Q: commit信息怎么写？**
> 简短描述你做了什么，如："添加登录功能"、"修复计算错误"、"更新README"。

**Q: 遇到冲突怎么办？**
> Git会标记冲突的地方，手动编辑文件保留想要的内容，然后add和commit即可。

## 进阶学习

完成本教程后，可以继续学习：

1. **Git高级功能**
   - 交互式变基（rebase -i）
   - Git钩子（hooks）
   - 子模块（submodule）

2. **GitHub进阶**
   - GitHub Actions（CI/CD）
   - GitHub Pages（静态网站）
   - GitHub Projects（项目管理）

3. **团队协作**
   - Git Flow工作流
   - 代码审查（Code Review）
   - 持续集成/持续部署

## 资源链接

- [Git官方文档](https://git-scm.com/doc)
- [GitHub官方教程](https://docs.github.com)
- [Pro Git电子书](https://git-scm.com/book/zh/v2)（免费）

## 贡献

发现错误或有建议？欢迎提出Issue或Pull Request！

## 许可证

本教程采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 许可证。

---

*开始你的Git之旅吧！*
