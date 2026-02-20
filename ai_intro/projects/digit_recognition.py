# -*- coding: utf-8 -*-
"""
项目3：手写数字识别
====================
这是一个图像分类项目，识别0-9的手写数字。

项目目标：
- 加载手写数字数据集
- 训练分类模型
- 可视化数字图像
- 测试识别效果

运行方式：
    python digit_recognition.py
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
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
    加载手写数字数据集

    返回:
        tuple: (图像数据, 标签, 图像数组形式)

    数据说明:
        - 1797个手写数字样本
        - 每个数字是8x8像素的灰度图像
        - 标签是0-9的数字
    """
    print("=" * 50)
    print("🔢 手写数字识别项目")
    print("=" * 50)
    print()

    print("【步骤1：加载数据】")

    # 加载sklearn内置的手写数字数据集
    digits = datasets.load_digits()

    X = digits.data          # 特征数据（64个像素值）
    y = digits.target        # 标签（0-9）
    images = digits.images   # 图像形式（8x8矩阵）

    print(f"  样本数量：{len(X)}")
    print(f"  图像尺寸：{images[0].shape}（8x8像素）")
    print(f"  特征数量：{X.shape[1]}（64个像素值）")
    print(f"  类别数量：{len(np.unique(y))}（数字0-9）")
    print()

    return X, y, images


def explore_data(X, y, images):
    """
    探索和可视化数据

    参数:
        X: 特征数据
        y: 标签
        images: 图像数组

    功能:
        - 显示数字图像示例
        - 统计各类别数量
    """
    print("【步骤2：探索数据】")

    # 显示数字图像示例
    print("  数字图像示例：")

    fig, axes = plt.subplots(2, 5, figsize=(12, 5))

    for i, ax in enumerate(axes.flat):
        # 找到当前数字的第一个样本
        idx = np.where(y == i)[0][0]
        ax.imshow(images[idx], cmap='gray')
        ax.set_title(f'数字 {i}')
        ax.axis('off')

    plt.tight_layout()

    output_dir = '/mnt/c/dev/python/qqstudy/ai_intro'
    plt.savefig(os.path.join(output_dir, 'digit_samples.png'), dpi=100)
    print("  ✅ 样本图像已保存到：digit_samples.png")
    plt.close()
    print()

    # 显示更多样本
    print("  显示前20个训练样本：")

    fig, axes = plt.subplots(2, 10, figsize=(15, 3))

    for i in range(20):
        ax = axes[i // 10, i % 10]
        ax.imshow(images[i], cmap='gray')
        ax.set_title(f'{y[i]}')
        ax.axis('off')

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'digit_first20.png'), dpi=100)
    print("  ✅ 前20个样本已保存到：digit_first20.png")
    plt.close()
    print()

    # 统计各类别数量
    print("  各数字数量：")
    unique, counts = np.unique(y, return_counts=True)
    for digit, count in zip(unique, counts):
        bar = '█' * (count // 5)
        print(f"    数字 {digit}: {count:3d} {bar}")
    print()


def train_model(X, y, test_size=0.3, model_type='knn'):
    """
    训练数字识别模型

    参数:
        X: 特征数据
        y: 标签
        test_size: 测试集比例
        model_type: 模型类型（'knn' 或 'svm'）

    返回:
        tuple: (模型, X_train, X_test, y_train, y_test)
    """
    print("【步骤3：训练模型】")

    # 划分数据集
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )

    print(f"  训练集大小：{len(X_train)}")
    print(f"  测试集大小：{len(X_test)}")
    print()

    # 选择模型
    if model_type == 'knn':
        print("  使用算法：K近邻 (KNN, K=5)")
        model = KNeighborsClassifier(n_neighbors=5)
    else:
        print("  使用算法：支持向量机 (SVM)")
        model = SVC(kernel='rbf', gamma=0.001)

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

    功能:
        - 计算准确率
        - 显示混淆矩阵
        - 分析错误分类
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
    print(classification_report(y_test, y_pred))
    print()

    # 混淆矩阵
    cm = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(10, 8))
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('混淆矩阵')
    plt.colorbar()
    tick_marks = np.arange(10)
    plt.xticks(tick_marks, range(10))
    plt.yticks(tick_marks, range(10))

    # 在格子中显示数字
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, format(cm[i, j], 'd'),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('真实数字')
    plt.xlabel('预测数字')
    plt.tight_layout()

    output_dir = '/mnt/c/dev/python/qqstudy/ai_intro'
    plt.savefig(os.path.join(output_dir, 'digit_confusion_matrix.png'), dpi=100)
    print("  ✅ 混淆矩阵已保存到：digit_confusion_matrix.png")
    plt.close()
    print()

    # 分析错误分类
    errors = np.where(y_pred != y_test)[0]
    print(f"  错误分类数量：{len(errors)} / {len(y_test)}")

    if len(errors) > 0:
        print("  部分错误示例：")
        # 重塑测试集图像
        test_images = X_test.reshape(-1, 8, 8)

        fig, axes = plt.subplots(2, 5, figsize=(12, 5))

        for i, ax in enumerate(axes.flat):
            if i < len(errors):
                idx = errors[i]
                ax.imshow(test_images[idx], cmap='gray')
                ax.set_title(f'真实:{y_test[idx]}, 预测:{y_pred[idx]}')
            ax.axis('off')

        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'digit_errors.png'), dpi=100)
        print("  ✅ 错误分类示例已保存到：digit_errors.png")
        plt.close()
    print()


def predict_samples(model, X_test, y_test, n_samples=10):
    """
    预测并可视化样本

    参数:
        model: 训练好的模型
        X_test: 测试特征
        y_test: 测试标签
        n_samples: 显示的样本数量
    """
    print("【步骤5：预测样本】")

    # 随机选择一些样本
    np.random.seed(42)
    indices = np.random.choice(len(X_test), n_samples, replace=False)

    # 预测
    predictions = model.predict(X_test[indices])
    actuals = y_test[indices]

    # 可视化
    fig, axes = plt.subplots(2, 5, figsize=(12, 5))

    for i, ax in enumerate(axes.flat):
        if i < n_samples:
            img = X_test[indices[i]].reshape(8, 8)
            ax.imshow(img, cmap='gray')

            correct = '✓' if predictions[i] == actuals[i] else '✗'
            ax.set_title(f'预测:{predictions[i]} 实际:{actuals[i]} {correct}')
        ax.axis('off')

    plt.tight_layout()

    output_dir = '/mnt/c/dev/python/qqstudy/ai_intro'
    plt.savefig(os.path.join(output_dir, 'digit_predictions.png'), dpi=100)
    print("  ✅ 预测结果已保存到：digit_predictions.png")
    plt.close()
    print()

    # 打印结果
    print("  预测结果：")
    correct_count = 0
    for i in range(n_samples):
        match = "✓ 正确" if predictions[i] == actuals[i] else "✗ 错误"
        print(f"    样本{i+1}: 预测={predictions[i]}, 实际={actuals[i]} → {match}")
        if predictions[i] == actuals[i]:
            correct_count += 1
    print(f"\n  正确率：{correct_count}/{n_samples}")
    print()


def compare_models(X, y):
    """
    比较不同模型的性能

    参数:
        X: 特征数据
        y: 标签

    功能:
        - 训练KNN和SVM
        - 比较准确率
    """
    print("【步骤6：比较不同模型】")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    models = {
        'KNN (K=1)': KNeighborsClassifier(n_neighbors=1),
        'KNN (K=3)': KNeighborsClassifier(n_neighbors=3),
        'KNN (K=5)': KNeighborsClassifier(n_neighbors=5),
        'KNN (K=7)': KNeighborsClassifier(n_neighbors=7),
        'SVM': SVC(kernel='rbf', gamma=0.001),
    }

    results = {}

    print("  训练和评估各模型...")
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        results[name] = accuracy
        print(f"    {name}: {accuracy:.2%}")
    print()

    # 可视化比较
    plt.figure(figsize=(10, 5))
    names = list(results.keys())
    accuracies = list(results.values())
    colors = ['blue', 'blue', 'blue', 'blue', 'green']

    bars = plt.bar(names, accuracies, color=colors)
    plt.ylim(0.9, 1.0)
    plt.ylabel('准确率')
    plt.title('不同模型准确率比较')

    # 在柱子上显示数值
    for bar, acc in zip(bars, accuracies):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.002,
                f'{acc:.2%}', ha='center', va='bottom')

    plt.tight_layout()

    output_dir = '/mnt/c/dev/python/qqstudy/ai_intro'
    plt.savefig(os.path.join(output_dir, 'digit_model_comparison.png'), dpi=100)
    print("  ✅ 模型比较图已保存到：digit_model_comparison.png")
    plt.close()
    print()


def main():
    """
    主程序入口

    执行完整的数字识别流程：
    1. 加载数据
    2. 探索数据
    3. 训练模型
    4. 评估模型
    5. 预测样本
    6. 比较不同模型
    """
    # 1. 加载数据
    X, y, images = load_data()

    # 2. 探索数据
    explore_data(X, y, images)

    # 3. 训练模型
    model, X_train, X_test, y_train, y_test = train_model(X, y)

    # 4. 评估模型
    evaluate_model(model, X_test, y_test)

    # 5. 预测样本
    predict_samples(model, X_test, y_test)

    # 6. 比较模型
    compare_models(X, y)

    print("=" * 50)
    print("🎉 项目完成！")
    print("=" * 50)
    print()
    print("你学会了：")
    print("  ✓ 加载和可视化图像数据")
    print("  ✓ 训练数字识别模型")
    print("  ✓ 分析混淆矩阵")
    print("  ✓ 比较不同模型性能")
    print()


if __name__ == "__main__":
    main()
