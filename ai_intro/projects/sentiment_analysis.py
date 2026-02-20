# -*- coding: utf-8 -*-
"""
项目4：情感分析
================
这是一个自然语言处理项目，分析文本的情感倾向（正面/负面）。

项目目标：
- 理解文本数据预处理
- 学习文本特征提取
- 训练情感分类模型
- 分析新文本情感

运行方式：
    python sentiment_analysis.py
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import os
import re

# 设置中文显示（兼容不同系统）
import platform
if platform.system() == 'Windows':
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'SimSun']
elif platform.system() == 'Darwin':  # Mac
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'PingFang SC']
else:  # Linux
    plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei', 'Noto Sans CJK SC', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False


def load_data():
    """
    加载情感分析数据

    返回:
        tuple: (文本列表, 标签列表)

    数据说明:
        使用模拟的中文评论数据
        标签：1=正面，0=负面
    """
    print("=" * 50)
    print("😊 情感分析项目")
    print("=" * 50)
    print()

    print("【步骤1：加载数据】")

    # 创建模拟的中文评论数据
    positive_comments = [
        "这个产品非常好，我很喜欢",
        "服务态度很好，非常满意",
        "质量优秀，值得推荐",
        "物美价廉，超级棒",
        "非常开心，下次还会来",
        "体验非常好，五星好评",
        "太棒了，超出预期",
        "完美，没有任何问题",
        "客服很有耐心，好评",
        "物流很快，包装很好",
        "颜色很好看，很喜欢",
        "性价比很高，推荐购买",
        "用起来很舒服，质量好",
        "味道很好，很新鲜",
        "效果明显，非常满意",
        "这个真的很不错",
        "比想象中更好",
        "非常满意这次购物",
        "值得购买，推荐给大家",
        "太喜欢了，爱不释手",
    ]

    negative_comments = [
        "质量太差了，很失望",
        "服务态度恶劣，不满意",
        "完全不值这个价格",
        "很糟糕的一次体验",
        "退货了，非常不满意",
        "差评，不会再来了",
        "质量有问题，不推荐",
        "收到的商品有损坏",
        "客服态度很差",
        "物流太慢了，差评",
        "颜色和图片不符",
        "性价比很低，不划算",
        "用起来不舒服，质量差",
        "味道不好，不新鲜",
        "没有效果，很失望",
        "这个真的很差劲",
        "比想象中差很多",
        "非常不满意这次购物",
        "不值得购买",
        "很失望，不推荐",
    ]

    # 合并数据
    texts = positive_comments + negative_comments
    labels = [1] * len(positive_comments) + [0] * len(negative_comments)

    # 打乱数据
    np.random.seed(42)
    indices = np.random.permutation(len(texts))
    texts = [texts[i] for i in indices]
    labels = [labels[i] for i in indices]

    print(f"  样本数量：{len(texts)}")
    print(f"  正面评论：{sum(labels)}")
    print(f"  负面评论：{len(labels) - sum(labels)}")
    print()

    return texts, labels


def explore_data(texts, labels):
    """
    探索文本数据

    参数:
        texts: 文本列表
        labels: 标签列表

    功能:
        - 显示数据示例
        - 统计文本长度
        - 分析词频
    """
    print("【步骤2：探索数据】")

    # 显示部分数据
    print("  数据示例：")
    print("  ---------- 正面评论 ----------")
    for text in texts[:3]:
        if labels[texts.index(text)] == 1:
            print(f"    {text}")

    print("  ---------- 负面评论 ----------")
    for i in range(len(texts)):
        if labels[i] == 0:
            print(f"    {texts[i]}")
            if i >= 22:  # 只显示3条
                break
    print()

    # 统计文本长度
    lengths = [len(text) for text in texts]
    print(f"  文本长度统计：")
    print(f"    最短：{min(lengths)} 字符")
    print(f"    最长：{max(lengths)} 字符")
    print(f"    平均：{np.mean(lengths):.1f} 字符")
    print()

    # 可视化
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    # 文本长度分布
    axes[0].hist([l for l, y in zip(lengths, labels) if y == 1],
                 alpha=0.7, label='正面', bins=10)
    axes[0].hist([l for l, y in zip(lengths, labels) if y == 0],
                 alpha=0.7, label='负面', bins=10)
    axes[0].set_xlabel('文本长度')
    axes[0].set_ylabel('数量')
    axes[0].set_title('文本长度分布')
    axes[0].legend()

    # 类别分布
    counts = [sum(labels), len(labels) - sum(labels)]
    axes[1].bar(['正面', '负面'], counts, color=['green', 'red'])
    axes[1].set_ylabel('数量')
    axes[1].set_title('类别分布')

    plt.tight_layout()

    output_dir = '/mnt/c/dev/python/qqstudy/ai_intro'
    plt.savefig(os.path.join(output_dir, 'sentiment_data.png'), dpi=100)
    print("  ✅ 数据可视化已保存到：sentiment_data.png")
    plt.close()
    print()


def preprocess_text(text):
    """
    预处理文本

    参数:
        text: 原始文本

    返回:
        处理后的文本

    功能:
        - 去除标点符号
        - 去除多余空格
    """
    # 去除标点
    text = re.sub(r'[^\w\s]', '', text)
    # 去除多余空格
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def extract_features(texts, method='count'):
    """
    提取文本特征

    参数:
        texts: 文本列表
        method: 特征提取方法（'count' 或 'tfidf'）

    返回:
        tuple: (特征矩阵, 向量化器)

    特征提取说明:
        - Count: 词频统计（每个词出现的次数）
        - TF-IDF: 考虑词的重要性
    """
    print("【步骤3：特征提取】")

    # 预处理
    processed_texts = [preprocess_text(text) for text in texts]

    # 选择向量化方法
    if method == 'count':
        print("  使用方法：词频统计 (Count Vectorizer)")
        vectorizer = CountVectorizer()
    else:
        print("  使用方法：TF-IDF")
        vectorizer = TfidfVectorizer()

    # 转换文本为特征矩阵
    X = vectorizer.fit_transform(processed_texts)

    print(f"  特征数量：{X.shape[1]}")
    print(f"  特征矩阵形状：{X.shape}")
    print()

    return X, vectorizer


def train_model(X, labels, test_size=0.3, model_type='nb'):
    """
    训练情感分类模型

    参数:
        X: 特征矩阵
        labels: 标签列表
        test_size: 测试集比例
        model_type: 模型类型（'nb'=朴素贝叶斯, 'lr'=逻辑回归）

    返回:
        tuple: (模型, X_train, X_test, y_train, y_test)
    """
    print("【步骤4：训练模型】")

    # 转换标签为数组
    y = np.array(labels)

    # 划分数据集
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )

    print(f"  训练集大小：{X_train.shape[0]}")
    print(f"  测试集大小：{X_test.shape[0]}")
    print()

    # 选择模型
    if model_type == 'nb':
        print("  使用算法：朴素贝叶斯")
        model = MultinomialNB()
    else:
        print("  使用算法：逻辑回归")
        model = LogisticRegression(max_iter=1000)

    # 训练
    model.fit(X_train, y_train)

    print("  ✅ 模型训练完成！")
    print()

    return model, X_train, X_test, y_train, y_test


def evaluate_model(model, X_test, y_test):
    """
    评估模型性能

    参数:
        model: 训练好的模型
        X_test: 测试特征
        y_test: 测试标签
    """
    print("【步骤5：评估模型】")

    # 预测
    y_pred = model.predict(X_test)

    # 准确率
    accuracy = accuracy_score(y_test, y_pred)
    print(f"  准确率：{accuracy:.2%}")
    print()

    # 分类报告
    print("  分类报告：")
    print(classification_report(y_test, y_pred, target_names=['负面', '正面']))
    print()

    # 混淆矩阵
    cm = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(6, 5))
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('混淆矩阵')
    plt.colorbar()
    tick_marks = ['负面', '正面']
    plt.xticks([0, 1], tick_marks)
    plt.yticks([0, 1], tick_marks)

    # 在格子中显示数字
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, format(cm[i, j], 'd'),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('真实标签')
    plt.xlabel('预测标签')
    plt.tight_layout()

    output_dir = '/mnt/c/dev/python/qqstudy/ai_intro'
    plt.savefig(os.path.join(output_dir, 'sentiment_confusion_matrix.png'), dpi=100)
    print("  ✅ 混淆矩阵已保存到：sentiment_confusion_matrix.png")
    plt.close()
    print()


def predict_new(model, vectorizer, new_texts):
    """
    预测新文本的情感

    参数:
        model: 训练好的模型
        vectorizer: 向量化器
        new_texts: 新文本列表

    返回:
        预测结果列表
    """
    print("【步骤6：预测新文本】")

    # 预处理
    processed = [preprocess_text(text) for text in new_texts]

    # 向量化
    X_new = vectorizer.transform(processed)

    # 预测
    predictions = model.predict(X_new)
    probabilities = model.predict_proba(X_new)

    print("  预测结果：")
    for text, pred, prob in zip(new_texts, predictions, probabilities):
        sentiment = "正面 😊" if pred == 1 else "负面 😞"
        confidence = prob[pred]
        print(f"    '{text}'")
        print(f"      → {sentiment} (置信度: {confidence:.2%})")
        print()

    return predictions


def analyze_keywords(vectorizer, model, top_n=10):
    """
    分析关键词的重要性

    参数:
        vectorizer: 向量化器
        model: 训练好的模型
        top_n: 显示的关键词数量
    """
    print("【步骤7：关键词分析】")

    # 获取特征词
    feature_names = vectorizer.get_feature_names_out()

    # 获取模型系数（逻辑回归）
    if hasattr(model, 'coef_'):
        coef = model.coef_[0]

        # 正面词（系数最大）
        positive_indices = np.argsort(coef)[-top_n:][::-1]
        print(f"  最能代表正面情感的词：")
        for idx in positive_indices:
            print(f"    {feature_names[idx]}: {coef[idx]:.3f}")

        print()

        # 负面词（系数最小）
        negative_indices = np.argsort(coef)[:top_n]
        print(f"  最能代表负面情感的词：")
        for idx in negative_indices:
            print(f"    {feature_names[idx]}: {coef[idx]:.3f}")
    else:
        print("  注：朴素贝叶斯模型的关键词分析较复杂，建议使用逻辑回归模型")

    print()


def simple_sentiment_dict():
    """
    基于情感词典的简单情感分析

    展示最基础的情感分析方法
    """
    print("【附加：情感词典方法】")

    # 定义情感词典
    positive_words = ['好', '棒', '喜欢', '开心', '满意', '优秀', '推荐', '完美', '好评', '喜欢']
    negative_words = ['差', '烂', '讨厌', '难过', '失望', '糟糕', '差评', '问题', '损坏', '不满']

    def analyze(text):
        """
        分析文本情感

        参数:
            text: 输入文本

        返回:
            情感类别和得分
        """
        pos_count = sum(1 for w in positive_words if w in text)
        neg_count = sum(1 for w in negative_words if w in text)

        score = pos_count - neg_count
        if score > 0:
            return "正面", score
        elif score < 0:
            return "负面", score
        else:
            return "中性", score

    print("  基于情感词典的简单分析：")

    test_texts = [
        "这个产品非常好，我很满意",
        "质量太差了，很失望",
        "普通的产品，没什么特别的"
    ]

    for text in test_texts:
        sentiment, score = analyze(text)
        print(f"    '{text}' → {sentiment} (得分: {score})")

    print()
    print("  注：情感词典方法简单但不够精确，机器学习方法更准确")
    print()


def main():
    """
    主程序入口

    执行完整的情感分析流程：
    1. 加载数据
    2. 探索数据
    3. 特征提取
    4. 训练模型
    5. 评估模型
    6. 预测新文本
    7. 分析关键词
    """
    # 1. 加载数据
    texts, labels = load_data()

    # 2. 探索数据
    explore_data(texts, labels)

    # 3. 特征提取
    X, vectorizer = extract_features(texts, method='count')

    # 4. 训练模型
    model, X_train, X_test, y_train, y_test = train_model(X, labels, model_type='nb')

    # 5. 评估模型
    evaluate_model(model, X_test, y_test)

    # 6. 预测新文本
    new_texts = [
        "这个产品真的很棒，非常推荐",
        "质量太差了，完全不值得一买",
        "服务态度很好，物流也很快"
    ]
    predict_new(model, vectorizer, new_texts)

    # 7. 分析关键词（使用逻辑回归模型）
    print("  使用逻辑回归模型分析关键词...")
    X_lr, vectorizer_lr = extract_features(texts, method='tfidf')
    model_lr, _, _, _, _ = train_model(X_lr, labels, model_type='lr')
    analyze_keywords(vectorizer_lr, model_lr)

    # 8. 展示情感词典方法
    simple_sentiment_dict()

    print("=" * 50)
    print("🎉 项目完成！")
    print("=" * 50)
    print()
    print("你学会了：")
    print("  ✓ 文本数据预处理")
    print("  ✓ 文本特征提取（Count, TF-IDF）")
    print("  ✓ 训练文本分类模型")
    print("  ✓ 情感分析基本方法")
    print("  ✓ 关键词重要性分析")
    print()


if __name__ == "__main__":
    main()
