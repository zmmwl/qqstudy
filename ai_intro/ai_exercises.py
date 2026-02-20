# -*- coding: utf-8 -*-
"""
AI入门教程 - 练习题
====================
这里包含了每节课对应的练习题，帮助你巩固所学知识。

每个练习题都有：
- 题目描述
- 提示
- 参考答案

建议：先自己尝试，实在不会再看答案！
"""

import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score


# ============================================
# 第1节练习题
# ============================================
def exercise_1():
    """
    第1节练习：什么是人工智能？

    【练习1】
    写一个简单的规则匹配AI，能回答以下问题：
    - "你好" → "你好！"
    - "1+1等于几" → "等于2"
    - "今天星期几" → "我不知道"
    - "再见" → "再见！"

    提示：使用字典存储问答对
    """
    print("=" * 60)
    print("📝 第1节练习题")
    print("=" * 60)
    print()

    # ====== 在这里写你的代码 ======
    def my_chatbot(question):
        """
        简单问答机器人

        参数:
            question: 用户问题（字符串）

        返回:
            回答字符串
        """
        # TODO: 实现问答功能
        qa_dict = {
            "你好": "你好！",
            "1+1": "等于2",
            "星期": "我不知道",
            "再见": "再见！"
        }

        for key, answer in qa_dict.items():
            if key in question:
                return answer
        return "我不明白"

    # 测试你的机器人
    test_questions = ["你好呀", "1+1等于几？", "今天星期几", "拜拜，再见"]
    print("测试结果：")
    for q in test_questions:
        print(f"  问：{q} → 答：{my_chatbot(q)}")
    print()
    # ==============================

    print("【参考答案】见上方代码")
    print()


# ============================================
# 第2节练习题
# ============================================
def exercise_2():
    """
    第2节练习：机器学习基础

    【练习2】
    给定一些学生的数学成绩和语文成绩，以及他们是否及格，
    请使用KNN算法预测新学生是否能及格。

    数据：
    - 特征：[数学成绩, 语文成绩]
    - 标签：1=及格，0=不及格（两科平均分>=60为及格）
    """
    print("=" * 60)
    print("📝 第2节练习题")
    print("=" * 60)
    print()

    # 训练数据
    X_train = np.array([
        [80, 75],   # 及格
        [70, 65],   # 及格
        [90, 85],   # 及格
        [55, 50],   # 不及格
        [40, 45],   # 不及格
        [35, 40],   # 不及格
        [65, 70],   # 及格
        [50, 55],   # 不及格
    ])

    y_train = np.array([1, 1, 1, 0, 0, 0, 1, 0])

    print("训练数据：")
    print("  数学  语文  是否及格")
    for i, (features, label) in enumerate(zip(X_train, y_train)):
        status = "及格" if label == 1 else "不及格"
        print(f"  {features[0]:3d}   {features[1]:3d}   {status}")
    print()

    # ====== 在这里写你的代码 ======
    # 1. 创建KNN模型
    knn = KNeighborsClassifier(n_neighbors=3)

    # 2. 训练模型
    knn.fit(X_train, y_train)

    # 3. 预测新学生
    new_students = np.array([
        [60, 65],   # 预测：及格
        [45, 50],   # 预测：不及格
        [75, 80],   # 预测：及格
    ])

    predictions = knn.predict(new_students)
    # ==============================

    print("预测结果：")
    for features, pred in zip(new_students, predictions):
        status = "及格" if pred == 1 else "不及格"
        print(f"  数学{features[0]}分, 语文{features[1]}分 → {status}")
    print()

    print("【参考答案】")
    print("""
# 创建并训练KNN模型
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# 预测
new_students = np.array([[60, 65], [45, 50], [75, 80]])
predictions = knn.predict(new_students)
""")
    print()


# ============================================
# 第3节练习题
# ============================================
def exercise_3():
    """
    第3节练习：sklearn入门

    【练习3】
    加载sklearn的digits（手写数字）数据集，探索数据：
    1. 有多少个样本？
    2. 有多少个特征？
    3. 有哪些类别（数字0-9）？
    4. 显示第一个样本的图像
    """
    print("=" * 60)
    print("📝 第3节练习题")
    print("=" * 60)
    print()

    # 加载数据集
    digits = datasets.load_digits()

    # ====== 在这里写你的代码 ======
    # 1. 样本数量
    n_samples = len(digits.data)
    print(f"样本数量：{n_samples}")

    # 2. 特征数量
    n_features = digits.data.shape[1]
    print(f"特征数量：{n_features}")

    # 3. 类别
    print(f"类别：{digits.target_names}")
    # ==============================

    # 显示第一个数字
    import matplotlib.pyplot as plt
    plt.figure(figsize=(3, 3))
    plt.imshow(digits.images[0], cmap='gray')
    plt.title(f'第一个数字是: {digits.target[0]}')
    plt.axis('off')
    plt.savefig('/mnt/c/dev/python/qqstudy/ai_intro/digit_sample.png', dpi=100)
    print("✅ 第一个数字图像已保存到：digit_sample.png")
    plt.close()
    print()

    print("【参考答案】")
    print("""
# 加载数据
digits = datasets.load_digits()

# 探索数据
print(f"样本数量：{len(digits.data)}")
print(f"特征数量：{digits.data.shape[1]}")
print(f"类别：{digits.target_names}")

# 显示图像
plt.imshow(digits.images[0], cmap='gray')
""")
    print()


# ============================================
# 第4节练习题
# ============================================
def exercise_4():
    """
    第4节练习：分类问题

    【练习4】
    使用sklearn的wine（葡萄酒）数据集，训练一个KNN分类器，
    预测葡萄酒的类别。要求：
    1. 划分70%训练，30%测试
    2. 使用K=5的KNN
    3. 计算准确率
    """
    print("=" * 60)
    print("📝 第4节练习题")
    print("=" * 60)
    print()

    # 加载数据
    wine = datasets.load_wine()
    X = wine.data
    y = wine.target

    print(f"数据集：葡萄酒分类")
    print(f"样本数量：{len(X)}")
    print(f"类别数量：{len(wine.target_names)}")
    print()

    # ====== 在这里写你的代码 ======
    # 1. 划分数据
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # 2. 创建并训练模型
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)

    # 3. 预测
    y_pred = knn.predict(X_test)

    # 4. 计算准确率
    acc = accuracy_score(y_test, y_pred)
    # ==============================

    print(f"训练集大小：{len(X_train)}")
    print(f"测试集大小：{len(X_test)}")
    print(f"准确率：{acc:.2%}")
    print()

    print("【参考答案】")
    print("""
# 划分数据
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 训练模型
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# 预测和评估
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"准确率：{accuracy:.2%}")
""")
    print()


# ============================================
# 第5节练习题
# ============================================
def exercise_5():
    """
    第5节练习：回归问题

    【练习5】
    创建一个简单的线性回归模型，根据学习时间预测考试分数。
    数据如下：
    - 学习时间（小时）：[1, 2, 3, 4, 5, 6, 7, 8]
    - 考试分数：[45, 52, 60, 68, 75, 82, 88, 95]

    要求：
    1. 训练线性回归模型
    2. 预测学习9小时能得多少分
    3. 计算R²分数
    """
    print("=" * 60)
    print("📝 第5节练习题")
    print("=" * 60)
    print()

    # 数据
    study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
    exam_scores = np.array([45, 52, 60, 68, 75, 82, 88, 95])

    print("训练数据：")
    print("  学习时间(小时)  考试分数")
    for hours, score in zip(study_hours, exam_scores):
        print(f"       {hours[0]}           {score}")
    print()

    # ====== 在这里写你的代码 ======
    # 1. 创建并训练模型
    model = LinearRegression()
    model.fit(study_hours, exam_scores)

    # 2. 预测9小时
    predicted_score = model.predict([[9]])[0]
    print(f"学习9小时预测分数：{predicted_score:.1f}")

    # 3. 计算R²
    y_pred = model.predict(study_hours)
    r2 = r2_score(exam_scores, y_pred)
    print(f"R²分数：{r2:.4f}")
    # ==============================

    print()

    print("【参考答案】")
    print("""
# 创建并训练模型
model = LinearRegression()
model.fit(study_hours, exam_scores)

# 预测
predicted_score = model.predict([[9]])[0]
print(f"学习9小时预测分数：{predicted_score:.1f}")

# 评估
y_pred = model.predict(study_hours)
r2 = r2_score(exam_scores, y_pred)
print(f"R²分数：{r2:.4f}")
""")
    print()


# ============================================
# 第6节练习题
# ============================================
def exercise_6():
    """
    第6节练习：模型评估

    【练习6】
    使用iris数据集，比较K=1, 3, 5, 7, 9时KNN的准确率，
    找出最好的K值。
    """
    print("=" * 60)
    print("📝 第6节练习题")
    print("=" * 60)
    print()

    # 加载数据
    iris = datasets.load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.3, random_state=42
    )

    # ====== 在这里写你的代码 ======
    k_values = [1, 3, 5, 7, 9]
    accuracies = []

    print("K值比较：")
    for k in k_values:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        accuracies.append(acc)
        print(f"  K={k}: 准确率 {acc:.2%}")

    best_k = k_values[np.argmax(accuracies)]
    print(f"\n最好的K值：{best_k}")
    # ==============================

    print()

    print("【参考答案】")
    print("""
k_values = [1, 3, 5, 7, 9]
best_acc = 0
best_k = 1

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    if acc > best_acc:
        best_acc = acc
        best_k = k

    print(f"K={k}: {acc:.2%}")

print(f"最好的K值：{best_k}")
""")
    print()


# ============================================
# 第7节练习题
# ============================================
def exercise_7():
    """
    第7节练习：情感分析

    【练习7】
    创建一个简单的情感分析器，使用以下正面词和负面词：
    正面词：['好', '棒', '喜欢', '开心', '优秀']
    负面词：['差', '烂', '讨厌', '难过', '糟糕']

    判断这些句子的情感：
    - "这个产品质量很好"
    - "今天心情很差"
    - "这部电影棒极了"
    """
    print("=" * 60)
    print("📝 第7节练习题")
    print("=" * 60)
    print()

    # ====== 在这里写你的代码 ======
    positive_words = ['好', '棒', '喜欢', '开心', '优秀']
    negative_words = ['差', '烂', '讨厌', '难过', '糟糕']

    def analyze_sentiment(text):
        """分析文本情感"""
        pos_count = sum(1 for w in positive_words if w in text)
        neg_count = sum(1 for w in negative_words if w in text)

        if pos_count > neg_count:
            return "正面"
        elif neg_count > pos_count:
            return "负面"
        else:
            return "中性"

    test_sentences = [
        "这个产品质量很好",
        "今天心情很差",
        "这部电影棒极了"
    ]

    print("情感分析结果：")
    for sentence in test_sentences:
        result = analyze_sentiment(sentence)
        print(f"  '{sentence}' → {result}")
    # ==============================

    print()

    print("【参考答案】")
    print("""
positive_words = ['好', '棒', '喜欢', '开心', '优秀']
negative_words = ['差', '烂', '讨厌', '难过', '糟糕']

def analyze_sentiment(text):
    pos_count = sum(1 for w in positive_words if w in text)
    neg_count = sum(1 for w in negative_words if w in text)

    if pos_count > neg_count:
        return "正面"
    elif neg_count > pos_count:
        return "负面"
    else:
        return "中性"

# 测试
for sentence in test_sentences:
    print(f"'{sentence}' → {analyze_sentiment(sentence)}")
""")
    print()


# ============================================
# 第8节练习题
# ============================================
def exercise_8():
    """
    第8节练习：AI的未来和伦理

    【练习8】思考题（开放性，没有标准答案）

    思考并回答以下问题：
    1. 你认为AI会取代哪些工作？
    2. AI不能取代哪些工作？为什么？
    3. 如果让你设计一个AI，你想让它做什么？
    """
    print("=" * 60)
    print("📝 第8节练习题 - 思考题")
    print("=" * 60)
    print()

    print("请思考以下问题（没有标准答案）：")
    print()

    questions = [
        "1. 你认为AI会取代哪些工作？",
        "2. AI不能取代哪些工作？为什么？",
        "3. 如果让你设计一个AI，你想让它做什么？"
    ]

    for q in questions:
        print(f"  {q}")
        print("  你的思考：")
        print("  ...(请在这里写下你的想法)...")
        print()

    print("【一些思考方向】")
    print("""
1. AI可能取代的工作：
   - 重复性高的工作（如数据录入）
   - 规则明确的工作（如计算）
   - 危险的工作（如某些制造业）

2. AI难以取代的工作：
   - 需要创造力的工作（艺术家、作家）
   - 需要同理心的工作（心理咨询师、护士）
   - 需要复杂决策的工作（法官、企业家）

3. AI设计想法：
   - 每个人都可以有自己的创意！
   - 想想你平时有什么烦恼，AI能帮忙吗？
""")
    print()


# ============================================
# 练习题答案汇总
# ============================================
def show_all_answers():
    """显示所有练习题的答案"""
    print("=" * 60)
    print("📖 所有练习题答案汇总")
    print("=" * 60)
    print()

    print("""
【第1节答案】规则匹配机器人
----------------------------
def my_chatbot(question):
    qa_dict = {
        "你好": "你好！",
        "1+1": "等于2",
        "星期": "我不知道",
        "再见": "再见！"
    }
    for key, answer in qa_dict.items():
        if key in question:
            return answer
    return "我不明白"


【第2节答案】学生成绩预测
----------------------------
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
predictions = knn.predict(new_students)


【第3节答案】探索digits数据集
----------------------------
digits = datasets.load_digits()
print(f"样本数量：{len(digits.data)}")
print(f"特征数量：{digits.data.shape[1]}")
print(f"类别：{digits.target_names}")


【第4节答案】葡萄酒分类
----------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)


【第5节答案】学习时间与分数
----------------------------
model = LinearRegression()
model.fit(study_hours, exam_scores)
predicted_score = model.predict([[9]])[0]
r2 = r2_score(exam_scores, model.predict(study_hours))


【第6节答案】选择最佳K值
----------------------------
best_k = 1
best_acc = 0
for k in [1, 3, 5, 7, 9]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    acc = accuracy_score(y_test, knn.predict(X_test))
    if acc > best_acc:
        best_acc = acc
        best_k = k


【第7节答案】情感分析
----------------------------
def analyze_sentiment(text):
    pos = sum(1 for w in positive_words if w in text)
    neg = sum(1 for w in negative_words if w in text)
    return "正面" if pos > neg else "负面" if neg > pos else "中性"


【第8节答案】开放性思考题
----------------------------
思考AI对社会的影响，培养批判性思维
""")
    print()


# ============================================
# 主程序
# ============================================
def main():
    """运行所有练习题"""
    print("\n" + "🎯 AI入门教程 - 练习题" + "\n")
    print("提示：每道题都有提示和参考答案，先自己试试！")
    print()

    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
    exercise_7()
    exercise_8()

    print("=" * 60)
    print("🎉 恭喜你完成了所有练习题！")
    print("=" * 60)


if __name__ == "__main__":
    main()
