# AI入门速成教程

适合初中生学习的AI入门教程，2小时掌握人工智能基础知识！

## 目录结构

```
ai_intro/
├── ai_quick_start.py              # 主教程（约2小时）
├── ai_exercises.py                # 练习题（带答案）
├── projects/                      # AI项目
│   ├── iris_classifier.py        # 鸢尾花分类
│   ├── house_price.py            # 房价预测
│   ├── digit_recognition.py      # 手写数字识别
│   └── sentiment_analysis.py     # 情感分析
├── data/                          # 示例数据
│   └── house_prices.csv          # 房价数据
└── README.md                      # 本文件
```

## 安装依赖

在运行教程前，请先安装必要的库：

```bash
pip install scikit-learn numpy pandas matplotlib joblib
```

如果安装太慢，可以使用国内镜像：

```bash
pip install scikit-learn numpy pandas matplotlib joblib -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 使用方法

### 1. 运行主教程

```bash
python ai_quick_start.py
```

这将运行8个章节的教程：
- 第1节：什么是人工智能？
- 第2节：机器学习基础
- 第3节：sklearn入门
- 第4节：分类问题 - 鸢尾花
- 第5节：回归问题 - 房价预测
- 第6节：模型评估
- 第7节：情感分析
- 第8节：AI的未来和伦理

### 2. 完成练习题

```bash
python ai_exercises.py
```

每道练习题都有提示和参考答案，建议先自己尝试！

### 3. 运行项目

```bash
# 鸢尾花分类
python projects/iris_classifier.py

# 房价预测
python projects/house_price.py

# 手写数字识别
python projects/digit_recognition.py

# 情感分析
python projects/sentiment_analysis.py
```

## 教程内容概览

### 第1节：什么是人工智能？
- AI的基本概念
- 日常生活中的AI应用
- AI的分类（弱AI vs 强AI）

### 第2节：机器学习基础
- 训练数据、特征、标签
- 机器学习工作流程
- 实现简单的水果分类器

### 第3节：sklearn入门
- sklearn库介绍
- 加载内置数据集
- 数据可视化

### 第4节：分类问题
- 分类概念
- KNN算法
- 鸢尾花分类实践

### 第5节：回归问题
- 回归概念
- 线性回归
- 房价预测实践

### 第6节：模型评估
- 准确率、精确率、召回率
- MSE、RMSE、R²
- 过拟合与欠拟合

### 第7节：情感分析
- 自然语言处理（NLP）
- 文本特征提取
- 情感分类实践

### 第8节：AI的未来和伦理
- AI发展趋势
- AI伦理问题
- 正确的AI观念

## 项目说明

### 1. 鸢尾花分类器 (iris_classifier.py)
- 使用KNN算法分类鸢尾花品种
- 完整的机器学习流程
- 寻找最佳K值
- 保存和加载模型

### 2. 房价预测 (house_price.py)
- 使用线性回归预测房价
- 数据探索和可视化
- 特征重要性分析
- 多种评估指标

### 3. 手写数字识别 (digit_recognition.py)
- 识别0-9的手写数字
- 图像数据处理
- 比较KNN和SVM
- 错误分析

### 4. 情感分析 (sentiment_analysis.py)
- 分析文本情感（正面/负面）
- 文本特征提取（Count, TF-IDF）
- 关键词重要性分析

## 学习建议

1. **按顺序学习**：先完成主教程，再做练习题
2. **动手实践**：运行每一行代码，理解其作用
3. **修改实验**：尝试修改参数，观察结果变化
4. **完成项目**：独立完成4个项目，巩固知识

## 核心概念速查

### 机器学习分类
- **分类**：预测离散类别（猫/狗、是/否）
- **回归**：预测连续数值（价格、温度）

### 常用算法
- **KNN**：找最近的K个邻居
- **线性回归**：找一条最合适的直线
- **朴素贝叶斯**：基于概率的分类

### 评估指标
- **准确率**：答对的比例
- **MSE**：均方误差
- **R²**：模型解释力（越接近1越好）

## 常见问题

### Q: 代码运行报错怎么办？
A: 确保已安装所有依赖库，检查Python版本（建议3.7+）

### Q: 中文显示乱码怎么办？
A: 代码中已设置中文字体，如果仍有问题，可能需要安装中文字体

### Q: 准确率不高怎么办？
A: 尝试调整参数（如KNN的K值），或使用不同的算法

## 下一步学习

完成本教程后，你可以继续学习：
1. 更多机器学习算法（决策树、随机森林、神经网络）
2. 深度学习入门（TensorFlow、PyTorch）
3. 计算机视觉（图像识别、目标检测）
4. 自然语言处理（文本生成、机器翻译）

---

祝学习愉快！有问题随时提问 🚀
