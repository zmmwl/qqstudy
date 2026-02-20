# -*- coding: utf-8 -*-
"""
项目2：房价预测
================
这是一个回归问题项目，使用线性回归预测房价。

项目目标：
- 加载房价数据
- 训练线性回归模型
- 评估模型性能
- 可视化结果

运行方式：
    python house_price.py
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler
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
    加载房价数据

    返回:
        tuple: (特征DataFrame, 标签Series)

    数据说明:
        使用本地CSV文件或生成模拟数据
    """
    print("=" * 50)
    print("🏠 房价预测项目")
    print("=" * 50)
    print()

    print("【步骤1：加载数据】")

    # 尝试加载本地数据
    data_path = '/mnt/c/dev/python/qqstudy/ai_intro/data/house_prices.csv'

    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
        print("  从本地文件加载数据")
    else:
        # 生成模拟数据
        print("  生成模拟房价数据...")
        df = generate_house_data()

    print(f"  样本数量：{len(df)}")
    print(f"  特征数量：{len(df.columns) - 1}")
    print()

    return df


def generate_house_data(n_samples=500):
    """
    生成模拟的房价数据

    参数:
        n_samples: 样本数量

    返回:
        DataFrame: 包含特征和价格的DataFrame

    特征说明:
        - area: 房屋面积（平方米）
        - bedrooms: 卧室数量
        - bathrooms: 卫生间数量
        - age: 房屋年龄（年）
        - distance: 距市中心距离（公里）
        - price: 房价（万元）
    """
    np.random.seed(42)

    # 生成特征
    area = np.random.uniform(50, 200, n_samples)           # 面积：50-200平米
    bedrooms = np.random.randint(1, 6, n_samples)          # 卧室：1-5间
    bathrooms = np.random.randint(1, 4, n_samples)         # 卫生间：1-3间
    age = np.random.uniform(0, 30, n_samples)              # 年龄：0-30年
    distance = np.random.uniform(1, 20, n_samples)         # 距离：1-20公里

    # 生成价格（基于特征的线性组合 + 噪声）
    # 基础价格 = 面积*2 + 卧室*10 + 卫生间*15 - 年龄*0.5 - 距离*3
    base_price = (area * 2 + bedrooms * 10 + bathrooms * 15
                  - age * 0.5 - distance * 3)
    noise = np.random.normal(0, 20, n_samples)  # 添加噪声
    price = base_price + noise

    # 确保价格为正
    price = np.maximum(price, 50)

    df = pd.DataFrame({
        'area': area,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'age': age,
        'distance': distance,
        'price': price
    })

    return df


def explore_data(df):
    """
    探索和可视化数据

    参数:
        df: 包含特征和价格的DataFrame

    功能:
        - 显示数据统计
        - 显示相关性
        - 生成可视化图表
    """
    print("【步骤2：探索数据】")

    # 显示前几行
    print("  数据预览：")
    print(df.head().round(2).to_string())
    print()

    # 统计信息
    print("  统计信息：")
    print(df.describe().round(2).to_string())
    print()

    # 相关性
    print("  与价格的相关性：")
    correlations = df.corr()['price'].drop('price').sort_values(ascending=False)
    for feature, corr in correlations.items():
        print(f"    {feature}: {corr:.3f}")
    print()

    # 可视化
    print("  正在生成可视化图表...")

    fig, axes = plt.subplots(2, 3, figsize=(15, 10))

    # 散点图：面积 vs 价格
    axes[0, 0].scatter(df['area'], df['price'], alpha=0.5)
    axes[0, 0].set_xlabel('面积 (平方米)')
    axes[0, 0].set_ylabel('价格 (万元)')
    axes[0, 0].set_title('面积 vs 价格')

    # 散点图：距离 vs 价格
    axes[0, 1].scatter(df['distance'], df['price'], alpha=0.5, c='orange')
    axes[0, 1].set_xlabel('距市中心 (公里)')
    axes[0, 1].set_ylabel('价格 (万元)')
    axes[0, 1].set_title('距离 vs 价格')

    # 散点图：年龄 vs 价格
    axes[0, 2].scatter(df['age'], df['price'], alpha=0.5, c='green')
    axes[0, 2].set_xlabel('房龄 (年)')
    axes[0, 2].set_ylabel('价格 (万元)')
    axes[0, 2].set_title('房龄 vs 价格')

    # 箱线图：卧室数量 vs 价格
    df.boxplot(column='price', by='bedrooms', ax=axes[1, 0])
    axes[1, 0].set_xlabel('卧室数量')
    axes[1, 0].set_ylabel('价格 (万元)')
    axes[1, 0].set_title('卧室数量 vs 价格')
    plt.suptitle('')  # 去掉自动生成的标题

    # 直方图：价格分布
    axes[1, 1].hist(df['price'], bins=30, edgecolor='black', alpha=0.7)
    axes[1, 1].set_xlabel('价格 (万元)')
    axes[1, 1].set_ylabel('频数')
    axes[1, 1].set_title('价格分布')

    # 相关性热力图（简化版）
    corr_matrix = df.corr()
    im = axes[1, 2].imshow(corr_matrix, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)
    axes[1, 2].set_xticks(range(len(corr_matrix.columns)))
    axes[1, 2].set_yticks(range(len(corr_matrix.columns)))
    axes[1, 2].set_xticklabels(corr_matrix.columns, rotation=45)
    axes[1, 2].set_yticklabels(corr_matrix.columns)
    axes[1, 2].set_title('相关性热力图')
    plt.colorbar(im, ax=axes[1, 2])

    plt.tight_layout()

    output_dir = '/mnt/c/dev/python/qqstudy/ai_intro'
    plt.savefig(os.path.join(output_dir, 'house_price_analysis.png'), dpi=100)
    print("  ✅ 图表已保存到：house_price_analysis.png")
    plt.close()
    print()


def train_model(df, test_size=0.2):
    """
    训练线性回归模型

    参数:
        df: 包含特征和价格的DataFrame
        test_size: 测试集比例

    返回:
        tuple: (模型, X_train, X_test, y_train, y_test, scaler)
    """
    print("【步骤3：训练模型】")

    # 准备特征和标签
    feature_cols = ['area', 'bedrooms', 'bathrooms', 'age', 'distance']
    X = df[feature_cols].values
    y = df['price'].values

    # 数据标准化（使特征在相同尺度）
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=test_size, random_state=42
    )

    print(f"  训练集大小：{len(X_train)}")
    print(f"  测试集大小：{len(X_test)}")
    print()

    # 创建并训练模型
    model = LinearRegression()
    model.fit(X_train, y_train)

    print("  ✅ 模型训练完成！")
    print()

    # 显示模型参数
    print("  模型参数：")
    print(f"    截距：{model.intercept_:.2f}")
    for feature, coef in zip(feature_cols, model.coef_):
        print(f"    {feature}: {coef:.2f}")
    print()

    return model, X_train, X_test, y_train, y_test, scaler, feature_cols


def evaluate_model(model, X_test, y_test, feature_cols, scaler):
    """
    评估模型性能

    参数:
        model: 训练好的模型
        X_test: 测试特征
        y_test: 测试标签
        feature_cols: 特征名称列表
        scaler: 标准化器

    功能:
        - 计算各种评估指标
        - 可视化预测结果
    """
    print("【步骤4：评估模型】")

    # 预测
    y_pred = model.predict(X_test)

    # 计算评估指标
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("  评估指标：")
    print(f"    均方误差 (MSE): {mse:.2f}")
    print(f"    均方根误差 (RMSE): {rmse:.2f}")
    print(f"    平均绝对误差 (MAE): {mae:.2f}")
    print(f"    R² 分数: {r2:.4f}")
    print()

    # 可视化预测结果
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # 真实值 vs 预测值
    axes[0].scatter(y_test, y_pred, alpha=0.5)
    axes[0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    axes[0].set_xlabel('真实价格 (万元)')
    axes[0].set_ylabel('预测价格 (万元)')
    axes[0].set_title(f'真实值 vs 预测值 (R²={r2:.3f})')

    # 残差分布
    residuals = y_test - y_pred
    axes[1].hist(residuals, bins=30, edgecolor='black', alpha=0.7)
    axes[1].set_xlabel('残差 (真实值 - 预测值)')
    axes[1].set_ylabel('频数')
    axes[1].set_title('残差分布')
    axes[1].axvline(x=0, color='r', linestyle='--')

    plt.tight_layout()

    output_dir = '/mnt/c/dev/python/qqstudy/ai_intro'
    plt.savefig(os.path.join(output_dir, 'house_price_evaluation.png'), dpi=100)
    print("  ✅ 评估图表已保存到：house_price_evaluation.png")
    plt.close()
    print()


def predict_new(model, scaler, feature_cols):
    """
    预测新房屋价格

    参数:
        model: 训练好的模型
        scaler: 标准化器
        feature_cols: 特征名称列表

    功能:
        - 对几个新房屋进行价格预测
    """
    print("【步骤5：预测新房价】")

    # 定义新房屋
    new_houses = pd.DataFrame({
        'area': [100, 150, 80],
        'bedrooms': [3, 4, 2],
        'bathrooms': [2, 2, 1],
        'age': [5, 10, 2],
        'distance': [5, 15, 3]
    })

    print("  新房屋信息：")
    print(new_houses.to_string())
    print()

    # 标准化
    X_new = scaler.transform(new_houses[feature_cols].values)

    # 预测
    predictions = model.predict(X_new)

    print("  预测价格：")
    for i, (features, price) in enumerate(zip(new_houses.values, predictions)):
        print(f"    房屋{i+1}: {features[0]:.0f}平米, {features[1]:.0f}室{features[2]:.0f}卫, {features[3]:.0f}年房龄, 距市中心{features[4]:.0f}公里")
        print(f"           → 预测价格: {price:.1f} 万元")
        print()


def feature_importance(model, feature_cols):
    """
    分析特征重要性

    参数:
        model: 训练好的模型
        feature_cols: 特征名称列表

    功能:
        - 显示每个特征对价格的影响程度
    """
    print("【步骤6：特征重要性分析】")

    # 获取系数绝对值
    importance = np.abs(model.coef_)

    # 排序
    indices = np.argsort(importance)[::-1]

    print("  特征重要性排序（从高到低）：")
    for i, idx in enumerate(indices):
        coef = model.coef_[idx]
        direction = "↑" if coef > 0 else "↓"
        print(f"    {i+1}. {feature_cols[idx]}: {importance[idx]:.2f} ({direction}影响价格)")
    print()

    # 可视化
    plt.figure(figsize=(10, 5))
    colors = ['green' if c > 0 else 'red' for c in model.coef_]
    plt.bar(feature_cols, model.coef_, color=colors)
    plt.xlabel('特征')
    plt.ylabel('系数')
    plt.title('特征对价格的影响')
    plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5)

    output_dir = '/mnt/c/dev/python/qqstudy/ai_intro'
    plt.savefig(os.path.join(output_dir, 'house_price_importance.png'), dpi=100)
    print("  ✅ 特征重要性图已保存到：house_price_importance.png")
    plt.close()
    print()


def main():
    """
    主程序入口

    执行完整的回归分析流程：
    1. 加载数据
    2. 探索数据
    3. 训练模型
    4. 评估模型
    5. 预测新数据
    6. 特征重要性分析
    """
    # 1. 加载数据
    df = load_data()

    # 2. 探索数据
    explore_data(df)

    # 3. 训练模型
    model, X_train, X_test, y_train, y_test, scaler, feature_cols = train_model(df)

    # 4. 评估模型
    evaluate_model(model, X_test, y_test, feature_cols, scaler)

    # 5. 预测新房价
    predict_new(model, scaler, feature_cols)

    # 6. 特征重要性
    feature_importance(model, feature_cols)

    print("=" * 50)
    print("🎉 项目完成！")
    print("=" * 50)
    print()
    print("你学会了：")
    print("  ✓ 加载和处理回归数据")
    print("  ✓ 数据标准化")
    print("  ✓ 训练线性回归模型")
    print("  ✓ 评估回归模型（MSE、RMSE、R²）")
    print("  ✓ 分析特征重要性")
    print()


if __name__ == "__main__":
    main()
