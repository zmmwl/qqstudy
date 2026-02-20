# -*- coding: utf-8 -*-
"""
项目1：鸢尾花分类器
====================
这是一个完整的机器学习项目，使用KNN算法对鸢尾花进行分类。

项目目标：
- 加载鸢尾花数据集
- 训练KNN分类模型
- 评估模型性能
- 可视化结果
- 保存模型供后续使用

运行方式：
    python iris_classifier.py
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import os

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
    加载鸢尾花数据集

    返回:
        tuple: (特征数据X, 标签数据y, 特征名称, 类别名称)

    数据说明:
        - 150个样本
        - 4个特征：花萼长度、花萼宽度、花瓣长度、花瓣宽度
        - 3个类别：山鸢尾、变色鸢尾、维吉尼亚鸢尾
    """
    print("=" * 50)
    print("🌺 鸢尾花分类器")
    print("=" * 50)
    print()

    print("【步骤1：加载数据】")

    # 从sklearn加载内置数据集
    iris = datasets.load_iris()

    X = iris.data          # 特征数据
    y = iris.target        # 标签
    feature_names = iris.feature_names    # 特征名称
    target_names = iris.target_names      # 类别名称

    print(f"  样本数量：{len(X)}")
    print(f"  特征数量：{len(feature_names)}")
    print(f"  特征名称：{feature_names}")
    print(f"  类别数量：{len(target_names)}")
    print(f"  类别名称：{target_names}")
    print()

    return X, y, feature_names, target_names


def explore_data(X, y, feature_names, target_names):
    """
    探索和可视化数据

    参数:
        X: 特征数据（numpy数组）
        y: 标签数据（numpy数组）
        feature_names: 特征名称列表
        target_names: 类别名称列表

    功能:
        - 显示数据统计
        - 生成可视化图表
    """
    print("【步骤2：探索数据】")

    # 转换为DataFrame方便分析
    df = pd.DataFrame(X, columns=feature_names)
    df['species'] = [target_names[i] for i in y]

    # 显示统计信息
    print("  数据统计：")
    print(df.describe().round(2).to_string())
    print()

    # 可视化
    print("  正在生成可视化图表...")

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # 图1：花瓣长度 vs 花瓣宽度
    colors = ['red', 'green', 'blue']
    for i, name in enumerate(target_names):
        mask = df['species'] == name
        axes[0, 0].scatter(
            df.loc[mask, 'petal length (cm)'],
            df.loc[mask, 'petal width (cm)'],
            c=colors[i], label=name, alpha=0.7, s=50
        )
    axes[0, 0].set_xlabel('花瓣长度 (cm)')
    axes[0, 0].set_ylabel('花瓣宽度 (cm)')
    axes[0, 0].set_title('花瓣特征分布')
    axes[0, 0].legend()

    # 图2：花萼长度 vs 花萼宽度
    for i, name in enumerate(target_names):
        mask = df['species'] == name
        axes[0, 1].scatter(
            df.loc[mask, 'sepal length (cm)'],
            df.loc[mask, 'sepal width (cm)'],
            c=colors[i], label=name, alpha=0.7, s=50
        )
    axes[0, 1].set_xlabel('花萼长度 (cm)')
    axes[0, 1].set_ylabel('花萼宽度 (cm)')
    axes[0, 1].set_title('花萼特征分布')
    axes[0, 1].legend()

    # 图3：各类别花瓣长度箱线图
    data_by_species = [df.loc[df['species'] == name, 'petal length (cm)'].values
                       for name in target_names]
    axes[1, 0].boxplot(data_by_species, labels=target_names)
    axes[1, 0].set_ylabel('花瓣长度 (cm)')
    axes[1, 0].set_title('各类别花瓣长度分布')

    # 图4：各类别数量
    df['species'].value_counts().plot(kind='bar', ax=axes[1, 1],
                                       color=['red', 'green', 'blue'])
    axes[1, 1].set_xlabel('品种')
    axes[1, 1].set_ylabel('数量')
    axes[1, 1].set_title('各类别样本数量')
    axes[1, 1].tick_params(axis='x', rotation=0)

    plt.tight_layout()

    # 保存图表
    output_dir = '/mnt/c/dev/python/qqstudy/ai_intro'
    plt.savefig(os.path.join(output_dir, 'iris_analysis.png'), dpi=100)
    print(f"  ✅ 图表已保存到：iris_analysis.png")
    plt.close()
    print()


def train_model(X, y, test_size=0.3, random_state=42, n_neighbors=5):
    """
    训练KNN分类模型

    参数:
        X: 特征数据（numpy数组）
        y: 标签数据（numpy数组）
        test_size: 测试集比例（默认0.3）
        random_state: 随机种子（默认42）
        n_neighbors: KNN的K值（默认5）

    返回:
        tuple: (模型, X_train, X_test, y_train, y_test)
    """
    print("【步骤3：训练模型】")

    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    print(f"  训练集大小：{len(X_train)}")
    print(f"  测试集大小：{len(X_test)}")
    print(f"  使用算法：KNN (K={n_neighbors})")
    print()

    # 创建并训练模型
    model = KNeighborsClassifier(n_neighbors=n_neighbors)
    model.fit(X_train, y_train)

    print("  ✅ 模型训练完成！")
    print()

    return model, X_train, X_test, y_train, y_test


def evaluate_model(model, X_test, y_test, target_names):
    """
    评估模型性能

    参数:
        model: 训练好的模型
        X_test: 测试特征
        y_test: 测试标签
        target_names: 类别名称

    功能:
        - 计算准确率
        - 显示分类报告
        - 绘制混淆矩阵
    """
    print("【步骤4：评估模型】")

    # 预测
    y_pred = model.predict(X_test)

    # 准确率
    accuracy = accuracy_score(y_test, y_pred)
    print(f"  准确率：{accuracy:.2%}")
    print()

    # 分类报告
    print("  分类报告：")
    print(classification_report(y_test, y_pred, target_names=target_names))

    # 混淆矩阵可视化
    cm = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(8, 6))
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('混淆矩阵')
    plt.colorbar()
    tick_marks = np.arange(len(target_names))
    plt.xticks(tick_marks, target_names)
    plt.yticks(tick_marks, target_names)

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
    plt.savefig(os.path.join(output_dir, 'iris_confusion_matrix.png'), dpi=100)
    print("  ✅ 混淆矩阵已保存到：iris_confusion_matrix.png")
    plt.close()
    print()


def predict_new(model, target_names):
    """
    使用模型预测新数据

    参数:
        model: 训练好的模型
        target_names: 类别名称

    功能:
        - 对几个新样本进行预测
        - 显示预测结果和概率
    """
    print("【步骤5：预测新数据】")

    # 定义一些新的鸢尾花样本
    # [花萼长度, 花萼宽度, 花瓣长度, 花瓣宽度]
    new_samples = np.array([
        [5.1, 3.5, 1.4, 0.2],  # 可能是山鸢尾
        [6.7, 3.0, 5.2, 2.3],  # 可能是维吉尼亚鸢尾
        [5.9, 3.0, 4.2, 1.5],  # 可能是变色鸢尾
    ])

    print("  新样本预测：")
    print("  花萼长度  花萼宽度  花瓣长度  花瓣宽度  →  预测品种")
    print("  --------  --------  --------  --------     --------")

    predictions = model.predict(new_samples)
    probabilities = model.predict_proba(new_samples)

    for i, (sample, pred, prob) in enumerate(zip(new_samples, predictions, probabilities)):
        print(f"    {sample[0]:.1f}      {sample[1]:.1f}      {sample[2]:.1f}      {sample[3]:.1f}    →  {target_names[pred]}")
        print(f"                                              概率：{prob}")
        print()

    print()


def find_best_k(X, y, k_range=range(1, 21)):
    """
    寻找最佳的K值

    参数:
        X: 特征数据
        y: 标签数据
        k_range: K值范围

    功能:
        - 测试不同K值
        - 绘制准确率曲线
        - 找出最佳K值
    """
    print("【步骤6：寻找最佳K值】")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    k_scores = []

    for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        score = knn.score(X_test, y_test)
        k_scores.append(score)

    best_k = k_range[np.argmax(k_scores)]
    best_score = max(k_scores)

    print(f"  最佳K值：{best_k}")
    print(f"  最佳准确率：{best_score:.2%}")
    print()

    # 可视化
    plt.figure(figsize=(10, 6))
    plt.plot(k_range, k_scores, 'bo-')
    plt.xlabel('K值')
    plt.ylabel('准确率')
    plt.title('不同K值的准确率')
    plt.grid(True)

    output_dir = '/mnt/c/dev/python/qqstudy/ai_intro'
    plt.savefig(os.path.join(output_dir, 'iris_k_comparison.png'), dpi=100)
    print("  ✅ K值比较图已保存到：iris_k_comparison.png")
    plt.close()
    print()


def save_model(model, filename='iris_model.pkl'):
    """
    保存模型到文件

    参数:
        model: 要保存的模型
        filename: 保存的文件名

    功能:
        将模型序列化保存，方便后续加载使用
    """
    output_dir = '/mnt/c/dev/python/qqstudy/ai_intro'
    filepath = os.path.join(output_dir, filename)
    joblib.dump(model, filepath)
    print(f"  ✅ 模型已保存到：{filename}")
    print()


def main():
    """
    主程序入口

    执行完整的机器学习流程：
    1. 加载数据
    2. 探索数据
    3. 训练模型
    4. 评估模型
    5. 预测新数据
    6. 优化参数
    7. 保存模型
    """
    # 1. 加载数据
    X, y, feature_names, target_names = load_data()

    # 2. 探索数据
    explore_data(X, y, feature_names, target_names)

    # 3. 训练模型
    model, X_train, X_test, y_train, y_test = train_model(X, y)

    # 4. 评估模型
    evaluate_model(model, X_test, y_test, target_names)

    # 5. 预测新数据
    predict_new(model, target_names)

    # 6. 寻找最佳K值
    find_best_k(X, y)

    # 7. 保存模型
    print("【步骤7：保存模型】")
    save_model(model)

    print("=" * 50)
    print("🎉 项目完成！")
    print("=" * 50)
    print()
    print("你学会了：")
    print("  ✓ 加载和探索数据")
    print("  ✓ 训练KNN分类器")
    print("  ✓ 评估模型性能")
    print("  ✓ 预测新数据")
    print("  ✓ 优化模型参数")
    print("  ✓ 保存和加载模型")
    print()


if __name__ == "__main__":
    main()
