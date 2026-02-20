# Python 自动化脚本教程

> 适合初中生学习的自动化脚本入门教程，约2小时可完成基础学习。

## 目录结构

```
automation/
├── automation_quick_start.py      # 主教程（8节课程）
├── automation_exercises.py        # 练习题（带答案）
├── scripts/                       # 实用脚本
│   ├── file_organizer.py         # 文件整理器
│   ├── batch_rename.py           # 批量重命名
│   ├── excel_processor.py        # Excel处理
│   └── text_replacer.py          # 文本替换
├── test_files/                    # 测试文件（运行教程时自动创建）
└── README.md                      # 本文件
```

## 快速开始

### 1. 运行主教程

```bash
cd /mnt/c/dev/python/qqstudy/automation
python automation_quick_start.py
```

### 2. 运行练习题

```bash
python automation_exercises.py
```

### 3. 使用实用脚本

```bash
# 文件整理器
python scripts/file_organizer.py

# 批量重命名
python scripts/batch_rename.py

# Excel处理
python scripts/excel_processor.py

# 文本替换
python scripts/text_replacer.py
```

## 教程内容

### 第1节：什么是自动化？
- 自动化的概念和应用场景
- Python自动化的优势

### 第2节：文件操作自动化
- 创建、复制、移动、删除文件
- os 和 shutil 模块的使用

### 第3节：批量重命名
- 添加前缀/后缀
- 修改扩展名
- 序号编号

### 第4节：文件整理器
- 按文件类型分类
- 字典的使用

### 第5节：Excel自动化
- openpyxl 库的使用
- 读写Excel文件
- 设置样式

### 第6节：文本处理
- 批量文本替换
- 日志分析
- 数据提取

### 第7节：定时任务
- schedule 库的使用
- 定时提醒

### 第8节：综合案例
- 智能作业文件整理器

## 依赖安装

```bash
# Excel处理需要
pip install openpyxl

# 定时任务需要
pip install schedule
```

## 学习建议

1. **按顺序学习**：教程是循序渐进的，建议从第1节开始
2. **动手实践**：边学边改代码，尝试不同的效果
3. **完成练习**：每节后的练习题能巩固所学知识
4. **实际应用**：用实用脚本解决真实问题

## 实用脚本功能

### file_organizer.py - 文件整理器
- 自动按类型分类文件
- 支持自定义分类规则
- 生成整理报告

### batch_rename.py - 批量重命名
- 添加前缀/后缀
- 修改扩展名
- 序号重命名
- 查找替换文件名

### excel_processor.py - Excel处理
- 创建Excel文件
- 读写数据
- 计算统计信息
- 设置样式

### text_replacer.py - 文本替换
- 单文件/批量替换
- 正则表达式支持
- 日志分析
- 预览模式

## 常见问题

**Q: 提示缺少模块怎么办？**
A: 使用 `pip install 模块名` 安装，如 `pip install openpyxl`

**Q: 路径有中文报错？**
A: 确保文件开头有 `# -*- coding: utf-8 -*-`

**Q: 权限不足？**
A: 以管理员身份运行，或选择有权限的文件夹

## 作者

Python学习小组

## 更新日志

- v1.0 (2024): 初始版本，包含8节教程和4个实用脚本
