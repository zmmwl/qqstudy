# ========================================
# 数据分析快速入门教程 (2-3小时学习计划)
# ========================================
# 适合：初中生及以上
# 前置知识：Python基础（变量、列表、字典、循环）
# 学习目标：学会用Python分析数据、画图表

"""
使用方法：
1. 确保安装了必要的库：pip install pandas matplotlib
2. 逐节阅读代码示例
3. 运行代码查看结果
4. 完成"动手练习"部分的题目

学习时间分配：
- 第1-2节：20分钟（认识数据分析）
- 第3-4节：30分钟（数据筛选和统计）
- 第5-6节：40分钟（数据可视化）
- 第7-8节：40分钟（综合案例）
"""

# ========================================
# 准备工作：导入库
# ========================================

# 【什么是"库"？】
# 库就像是一个"工具箱"，里面装着别人写好的代码
# 我们导入库，就可以直接使用里面的工具，不用自己从头写
# 比如：pandas库里有人写好的读取Excel的功能，我们直接调用就行

# pandas 是数据分析的核心库，提供 DataFrame 数据结构
# 就像 Excel 一样强大，但可以处理更多数据、做更复杂的操作
import pandas as pd  # as pd 表示给它起个简短的别名，以后用 pd 就行

# matplotlib 是绑图库，用于数据可视化
# 可以画出各种漂亮的图表：折线图、柱状图、饼图等
import matplotlib.pyplot as plt  # 同样起个简短别名 plt

# 设置中文显示（解决中文乱码问题）
# 如果不设置，图表中的中文会显示成方框
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

print("库导入成功！让我们开始数据分析之旅吧！")
print("=" * 50)


# ========================================
# 第1节：什么是数据分析？
# ========================================
"""
【生活中的数据分析】

想象一下这些场景：
1. 老师统计全班成绩，算出平均分、最高分、最低分
2. 你记录一个月的零花钱，看看都花在哪里了
3. 分析你最爱的篮球队，谁的得分最高

这些都是"数据分析"！简单来说：
- 数据分析 = 收集数据 + 整理数据 + 发现规律 + 做出决策

【数据分析的步骤】
1. 收集数据（比如：问卷调查、网络爬取、已有文件）
2. 清洗数据（比如：删除错误数据、填补缺失值）
3. 分析数据（比如：计算平均数、找最大最小值）
4. 可视化展示（比如：画图表让别人看懂）
5. 得出结论（比如：发现男生数学成绩更好）

【我们用什么工具？】
- pandas：处理表格数据（就像Excel，但更强大）
- matplotlib：绑各种漂亮的图表

让我们开始吧！
"""
print("\n第1节：什么是数据分析？ - 完成！")


# ========================================
# 第2节：认识 pandas 和 DataFrame
# ========================================
print("\n" + "=" * 50)
print("第2节：认识 pandas 和 DataFrame")
print("=" * 50)

# 【什么是 DataFrame？】
# DataFrame 就像一个Excel表格，有行有列
# 每一列可以存储不同类型的数据
#
# 【更形象的比喻】
# 把 DataFrame 想象成一个"成绩单"：
# - 每一行是一个学生的信息（张三、李四、王五...）
# - 每一列是一种信息（姓名、年龄、语文成绩、数学成绩...）
# - 表头就是列名，告诉我们每列是什么意思

# 2.1 创建一个简单的 DataFrame
print("\n--- 2.1 创建DataFrame ---")

# 方法一：用字典创建
student_data = {
    '姓名': ['小明', '小红', '小刚', '小芳'],
    '年龄': [13, 14, 13, 14],
    '数学成绩': [88, 92, 76, 85],
    '英语成绩': [90, 88, 82, 95]
}

df_simple = pd.DataFrame(student_data)
print("简单学生表：")
print(df_simple)

# 【代码解释】
# pd.DataFrame(字典) 把字典转成表格
# 字典的 key 变成列名，value 变成列数据

# 2.2 读取CSV文件
print("\n--- 2.2 读取CSV文件 ---")

# 读取学生成绩数据（CSV是一种常用的表格文件格式）
df_students = pd.read_csv('data/students.csv')
print("学生成绩数据：")
print(df_students)

# 【pd.read_csv 参数说明】
# pd.read_csv(filepath, encoding='utf-8', sep=',')
# - filepath: 文件路径
# - encoding: 编码方式（中文用 utf-8 或 gbk）
# - sep: 分隔符（默认逗号，也可以是 \t 制表符）

# 2.3 查看数据的基本信息
print("\n--- 2.3 查看数据基本信息 ---")

print("前5行数据：")
print(df_students.head())      # 查看前5行

print("\n后3行数据：")
print(df_students.tail(3))     # 查看后3行

print("\n数据形状（行数，列数）：")
print(df_students.shape)       # (20, 7) 表示20行7列

print("\n列名：")
print(df_students.columns)     # 所有列名

print("\n数据类型：")
print(df_students.dtypes)      # 每列的数据类型

print("\n数据统计摘要：")
print(df_students.describe())  # 数值列的统计信息

# 【describe() 输出解释 - 用成绩来理解】
# count: 有多少个学生（非空值数量）
# mean: 平均分（所有成绩加起来除以人数）
# std: 标准差（想象成"成绩波动大小"）
#      - 标准差大：成绩高低差距大，有人考100有人考60
#      - 标准差小：成绩都差不多，都在80分左右
# min: 最低分
# 25%: 把成绩从小到大排，排到25%位置的那个分数
#      例如20人，第5个人的分数（比这低的有25%的人）
# 50%: 中位数（排正中间那个人的分数）
#      例如20人，第10个人的分数
# 75%: 排到75%位置的那个分数
# max: 最高分

# 2.4 查看数据信息
print("\n--- 2.4 数据详细信息 ---")
print(df_students.info())

# 【动手练习 2】
# 1. 读取电影数据 movies.csv，查看前5行
# 2. 查看电影数据的形状和列名
# 3. 使用 describe() 查看电影评分的统计信息

# 练习答案在本节末尾

print("\n--- 练习2答案 ---")
# 答案1
df_movies = pd.read_csv('data/movies.csv')
print("电影数据前5行：")
print(df_movies.head())

# 答案2
print(f"\n电影数据形状：{df_movies.shape}")
print(f"列名：{list(df_movies.columns)}")

# 答案3
print("\n评分统计：")
print(df_movies['评分'].describe())


# ========================================
# 第3节：数据筛选
# ========================================
print("\n" + "=" * 50)
print("第3节：数据筛选")
print("=" * 50)

# 3.1 选择列
print("\n--- 3.1 选择列 ---")

# 选择单列（返回Series）
# 【什么是Series？】
# Series 就是一列数据，像一排排队的同学
# 它只有一个维度（只有一列），不像 DataFrame 有多列
names = df_students['姓名']
print("所有学生姓名：")
print(names)

# 选择多列（注意是双中括号！）
# 【为什么是双中括号？】
# 单括号 ['列名'] = 选择一列，返回 Series
# 双括号 [['列名1', '列名2']] = 选择多列，返回 DataFrame
# 记忆：外面的大括号表示"我要选列"，里面的小括号是"列名列表"
scores = df_students[['姓名', '数学', '英语']]
print("\n姓名和成绩：")
print(scores)

# 【选择列的语法】
# df['列名'] - 选择单列，返回Series
# df[['列名1', '列名2']] - 选择多列，返回DataFrame

# 3.2 选择行
print("\n--- 3.2 选择行 ---")

# 使用 iloc 按位置选择（iloc = integer location）
print("第1行数据：")
print(df_students.iloc[0])

print("\n第2-4行数据：")
print(df_students.iloc[1:4])

print("\n第1行第2列的数据：")
print(df_students.iloc[0, 1])

# 使用 loc 按标签选择
print("\n第1-3行，指定列：")
print(df_students.loc[0:2, ['姓名', '班级', '数学']])

# 【iloc vs loc】
# iloc: 用数字位置选择，如 df.iloc[0, 1]
# loc: 用标签选择，如 df.loc[0, '姓名']

# 3.3 条件筛选
print("\n--- 3.3 条件筛选 ---")

# 筛选数学成绩大于90的学生
high_math = df_students[df_students['数学'] > 90]
print("数学成绩>90的学生：")
print(high_math)

# 【条件筛选语法】
# df[df['列名'] > 值] - 大于
# df[df['列名'] < 值] - 小于
# df[df['列名'] == 值] - 等于
# df[df['列名'] != 值] - 不等于

# 多条件筛选
print("\n数学>85 且 英语>85 的学生：")
good_students = df_students[(df_students['数学'] > 85) & (df_students['英语'] > 85)]
print(good_students[['姓名', '数学', '英语']])

# 【多条件语法】
# & 表示"且"（and）
# | 表示"或"（or）
# 注意：每个条件要用括号括起来！

# 筛选特定值
print("\n1班的学生：")
class1 = df_students[df_students['班级'] == '1班']
print(class1[['姓名', '班级']])

# 筛选包含特定值的行
print("\n名字里带'明'的学生：")
ming_students = df_students[df_students['姓名'].str.contains('明')]
print(ming_students[['姓名']])

# 使用 isin 筛选多个值
print("\n1班和2班的学生：")
class12 = df_students[df_students['班级'].isin(['1班', '2班'])]
print(class12[['姓名', '班级']])

# 【动手练习 3】
# 1. 从电影数据中筛选评分大于8的电影
# 2. 从电影数据中筛选"动画"类型的电影
# 3. 从学生数据中筛选总分大于340的学生（语文+数学+英语+科学）

print("\n--- 练习3答案 ---")
# 答案1
high_rating = df_movies[df_movies['评分'] > 8]
print(f"评分>8的电影有{len(high_rating)}部：")
print(high_rating[['电影名称', '评分']])

# 答案2
animations = df_movies[df_movies['类型'] == '动画']
print(f"\n动画电影有{len(animations)}部：")
print(animations[['电影名称', '评分']])

# 答案3
df_students['总分'] = df_students['语文'] + df_students['数学'] + df_students['英语'] + df_students['科学']
top_students = df_students[df_students['总分'] > 340]
print(f"\n总分>340的学生有{len(top_students)}人：")
print(top_students[['姓名', '总分']])


# ========================================
# 第4节：数据统计
# ========================================
print("\n" + "=" * 50)
print("第4节：数据统计")
print("=" * 50)

# 4.1 基本统计函数
print("\n--- 4.1 基本统计函数 ---")

# 常用统计函数
print(f"数学平均分：{df_students['数学'].mean():.2f}")      # 平均值
print(f"数学最高分：{df_students['数学'].max()}")          # 最大值
print(f"数学最低分：{df_students['数学'].min()}")          # 最小值
print(f"数学成绩总和：{df_students['数学'].sum()}")        # 总和
print(f"学生总数：{df_students['数学'].count()}")          # 计数
print(f"数学成绩标准差：{df_students['数学'].std():.2f}")  # 标准差
print(f"数学成绩中位数：{df_students['数学'].median()}")   # 中位数

# 【统计函数列表】
# mean() - 平均值
# sum() - 总和
# max() - 最大值
# min() - 最小值
# count() - 计数
# std() - 标准差
# median() - 中位数
# var() - 方差
# quantile(0.25) - 25%分位数

# 4.2 一次计算多列统计
print("\n--- 4.2 多列统计 ---")

# 计算各科平均分
subjects = ['语文', '数学', '英语', '科学']
print("各科平均分：")
print(df_students[subjects].mean())

# 计算每个学生的总分和平均分
df_students['总分'] = df_students[subjects].sum(axis=1)  # axis=1 表示横向计算
df_students['平均分'] = df_students[subjects].mean(axis=1)
print("\n学生成绩（含总分和平均分）：")
print(df_students[['姓名', '总分', '平均分']].head())

# 【axis参数说明 - 用成绩表来理解】
# 想象一张成绩表，学生姓名在左边，各科成绩在右边
#
# axis=0（纵向，默认值）：
#   - 从上往下看，对"每一列"进行操作
#   - 例如：计算"数学"这列的平均分（把所有学生的数学成绩加起来求平均）
#   - 口诀：axis=0，往下走，每列算一个结果
#
# axis=1（横向）：
#   - 从左往右看，对"每一行"进行操作
#   - 例如：计算"张三"的总分（把张三的语数英科都加起来）
#   - 口诀：axis=1，往右走，每行算一个结果

# 4.3 分组统计 groupby
print("\n--- 4.3 分组统计 ---")

# 按班级分组，计算各科平均分
print("各班级各科平均分：")
class_avg = df_students.groupby('班级')[subjects].mean()
print(class_avg.round(2))  # round(2) 保留2位小数

# 【groupby语法 - 用"分组站队"来理解】
# 想象体育课分组：老师喊"按班级集合！"
# - 1班的学生站到一起
# - 2班的学生站到一起
# - 3班的学生站到一起
# 然后每个小组分别做统计（比如数人数、量身高）
#
# df.groupby('分组列')['统计列'].统计函数()
# 例如：按班级分组，计算数学成绩的平均值
#
# 代码执行过程：
# 1. groupby('班级') -> 把相同班级的行放在一起
# 2. ['数学'] -> 从每组中取出数学成绩
# 3. .mean() -> 计算每组的平均分

# 按性别分组统计
print("\n按性别统计：")
gender_stats = df_students.groupby('性别').agg({
    '语文': 'mean',
    '数学': 'mean',
    '总分': ['mean', 'max', 'min']
})
print(gender_stats.round(2))

# 【agg函数】同时计算多个统计量
# df.groupby('列').agg({'列1': 'mean', '列2': 'max'})

# 按班级统计人数
print("\n各班级人数：")
print(df_students['班级'].value_counts())

# 【value_counts()】统计每个值出现的次数

# 4.4 排序
print("\n--- 4.4 排序 ---")

# 按总分降序排列
print("成绩排行榜（按总分降序）：")
ranking = df_students.sort_values('总分', ascending=False)
print(ranking[['姓名', '班级', '总分']].head(10))

# 按班级和总分排序
print("\n按班级和总分排序：")
ranking2 = df_students.sort_values(['班级', '总分'], ascending=[True, False])
print(ranking2[['姓名', '班级', '总分']].head(10))

# 【sort_values语法】
# df.sort_values('列名') - 升序排列
# df.sort_values('列名', ascending=False) - 降序排列
# df.sort_values(['列1', '列2'], ascending=[True, False]) - 多列排序

# 【动手练习 4】
# 1. 计算电影数据的平均评分、最高评分、最低评分
# 2. 按电影类型分组，计算每种类型的平均评分
# 3. 按票房降序排列电影，显示前10名

print("\n--- 练习4答案 ---")
# 答案1
print(f"电影平均评分：{df_movies['评分'].mean():.2f}")
print(f"电影最高评分：{df_movies['评分'].max()}")
print(f"电影最低评分：{df_movies['评分'].min()}")

# 答案2
type_rating = df_movies.groupby('类型')['评分'].mean().sort_values(ascending=False)
print("\n各类型电影平均评分：")
print(type_rating.round(2))

# 答案3
top_movies = df_movies.sort_values('票房(亿)', ascending=False)
print("\n票房前10名：")
print(top_movies[['电影名称', '类型', '票房(亿)']].head(10))


# ========================================
# 第5节：数据可视化入门
# ========================================
print("\n" + "=" * 50)
print("第5节：数据可视化入门")
print("=" * 50)

# 5.1 折线图
print("\n--- 5.1 折线图 ---")

# 准备数据：某学生各科成绩
student_name = '张明'
# 下面的代码一步步拆解：
# 1. df_students['姓名'] == student_name -> 找出姓名是"张明"的行（返回True/False）
# 2. df_students[...] -> 用上面的条件筛选出"张明"的那一行
# 3. [subjects] -> 只取出科目这几列
# 4. .values -> 把数据转成纯数字数组（去掉行列标签）
# 5. [0] -> 取第一个元素（因为结果是一个二维数组，我们要的是第一行）
student_scores = df_students[df_students['姓名'] == student_name][subjects].values[0]

# 【绑折线图前的准备】
# plt.figure() 就像拿出一张白纸准备画画
# figsize=(8, 5) 表示这张纸宽8单位、高5单位
plt.figure(figsize=(8, 5))  # 创建画布，设置大小
plt.plot(subjects, student_scores, marker='o', linewidth=2, markersize=8)
# marker: 数据点样式，linewidth: 线宽，markersize: 点大小

plt.title(f'{student_name}各科成绩')  # 标题
plt.xlabel('科目')                     # x轴标签
plt.ylabel('分数')                     # y轴标签
plt.grid(True, alpha=0.3)              # 显示网格，alpha设置透明度
plt.savefig('output_line_chart.png')   # 保存图片
plt.close()                            # 关闭图形（释放内存）
print("折线图已保存为 output_line_chart.png")

# 【plt.plot 参数说明】
# plt.plot(x数据, y数据, 参数...)
# - color: 线条颜色（'red', 'blue', '#FF5733'）
# - linestyle: 线条样式（'-'实线, '--'虚线, ':'点线）
# - marker: 数据点样式（'o'圆点, 's'方块, '^'三角）
# - linewidth: 线宽
# - markersize: 点大小

# 5.2 柱状图
print("\n--- 5.2 柱状图 ---")

# 各科平均分柱状图
avg_scores = df_students[subjects].mean()

plt.figure(figsize=(8, 5))
bars = plt.bar(subjects, avg_scores, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])

# 在柱子上显示数值
for bar, score in zip(bars, avg_scores):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             f'{score:.1f}', ha='center', va='bottom')

plt.title('各科目平均分')
plt.xlabel('科目')
plt.ylabel('平均分')
plt.ylim(0, 100)  # 设置y轴范围
plt.savefig('output_bar_chart.png')
plt.close()
print("柱状图已保存为 output_bar_chart.png")

# 【plt.bar 参数说明】
# plt.bar(x数据, y数据, 参数...)
# - color: 柱子颜色（可以是列表，每个柱子不同颜色）
# - width: 柱子宽度
# - edgecolor: 边框颜色
# - alpha: 透明度（0-1）

# 5.3 饼图
print("\n--- 5.3 饼图 ---")

# 学生性别分布
gender_count = df_students['性别'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(gender_count, labels=gender_count.index, autopct='%1.1f%%',
        colors=['#FF9999', '#66B2FF'], startangle=90, explode=(0.05, 0))
# autopct: 显示百分比格式
# startangle: 起始角度
# explode: 突出显示（数值表示偏移量）

plt.title('学生性别分布')
plt.savefig('output_pie_chart.png')
plt.close()
print("饼图已保存为 output_pie_chart.png")

# 【plt.pie 参数说明】
# plt.pie(数据, 参数...)
# - labels: 各部分标签
# - autopct: 百分比格式（'%1.1f%%'表示保留1位小数）
# - colors: 颜色列表
# - explode: 突出显示
# - shadow: 是否显示阴影

# 5.4 散点图
print("\n--- 5.4 散点图 ---")

# 数学成绩 vs 英语成绩
plt.figure(figsize=(8, 6))
plt.scatter(df_students['数学'], df_students['英语'],
            c=df_students['总分'], cmap='RdYlGn', s=100, alpha=0.7)
# c: 颜色根据什么变化
# cmap: 颜色映射
# s: 点的大小

plt.colorbar(label='总分')  # 显示颜色条
plt.title('数学成绩 vs 英语成绩')
plt.xlabel('数学成绩')
plt.ylabel('英语成绩')
plt.savefig('output_scatter.png')
plt.close()
print("散点图已保存为 output_scatter.png")

# 【动手练习 5】
# 1. 绑制电影评分的柱状图（显示前10部电影）
# 2. 绘制电影类型分布的饼图

print("\n--- 练习5答案 ---")
# 答案1：电影评分柱状图
top10_movies = df_movies.head(10)
plt.figure(figsize=(12, 6))
plt.barh(top10_movies['电影名称'], top10_movies['评分'], color='skyblue')
plt.xlabel('评分')
plt.title('电影评分（前10部）')
plt.tight_layout()  # 自动调整布局
plt.savefig('output_exercise5_1.png')
plt.close()
print("练习5-1图表已保存")

# 答案2：电影类型饼图
type_count = df_movies['类型'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(type_count, labels=type_count.index, autopct='%1.1f%%')
plt.title('电影类型分布')
plt.savefig('output_exercise5_2.png')
plt.close()
print("练习5-2图表已保存")


# ========================================
# 第6节：图表美化
# ========================================
print("\n" + "=" * 50)
print("第6节：图表美化")
print("=" * 50)

# 6.1 添加标题、标签、图例
print("\n--- 6.1 基本美化 ---")

# 班级平均分对比图
class_avg = df_students.groupby('班级')[subjects].mean()

plt.figure(figsize=(12, 6))

# 【分组柱状图的原理 - 用"排队站好"来理解】
# 想象有4个班级站成一排，每个班级有4个科目的柱子
# 如果所有柱子都挤在同一位置，就会重叠看不清
# 所以我们要让它们"错开站"：
#
# x = [0, 1, 2, 3] 表示4个班级的位置（中心点）
# width = 0.2 是每个柱子的宽度
#
# 柱子位置计算：
# - 语文柱子：中心往左偏 1.5*width（最左边）
# - 数学柱子：中心往左偏 0.5*width
# - 英语柱子：中心往右偏 0.5*width
# - 科学柱子：中心往右偏 1.5*width（最右边）
#
# 这样4个柱子就整整齐齐并排站在每个班级位置上了！
x = range(len(class_avg.index))  # [0, 1, 2, 3] 每个数字代表一个班级
width = 0.2  # 每个柱子的宽度

# 绘制4组柱子，每组偏移不同位置
plt.bar([i - 1.5*width for i in x], class_avg['语文'], width, label='语文', color='#FF6B6B')
plt.bar([i - 0.5*width for i in x], class_avg['数学'], width, label='数学', color='#4ECDC4')
plt.bar([i + 0.5*width for i in x], class_avg['英语'], width, label='英语', color='#45B7D1')
plt.bar([i + 1.5*width for i in x], class_avg['科学'], width, label='科学', color='#96CEB4')

plt.xlabel('班级', fontsize=12)
plt.ylabel('平均分', fontsize=12)
plt.title('各班级各科平均分对比', fontsize=14, fontweight='bold')
plt.xticks(x, class_avg.index)  # 设置x轴刻度标签
plt.legend(loc='upper right')   # 显示图例
plt.grid(axis='y', alpha=0.3)   # 只显示y轴网格
plt.tight_layout()
plt.savefig('output_beautified_1.png')
plt.close()
print("美化图表1已保存")

# 6.2 设置样式
# 【过渡说明】学会了绑图，接下来让图表更好看！
# 就像写作文，先学会写，再学会写得漂亮
print("\n--- 6.2 设置样式 ---")

# 使用内置样式（就像给图表换"皮肤"）
# plt.style.available 可以查看所有可用样式
plt.style.use('seaborn-v0_8')  # 可选：ggplot, seaborn, dark_background 等

# 绑制成绩分布直方图
# 【什么是直方图？】
# 把成绩分成几个区间，看每个区间有多少人
# 比如：60-70分3人，70-80分8人，80-90分6人...
# 就像把全班按成绩"分桶装"
plt.figure(figsize=(10, 6))
plt.hist(df_students['总分'], bins=10, color='skyblue', edgecolor='black', alpha=0.7)
# bins=10: 把成绩分成10个区间（桶）
# 比如满分400分，分成10个桶，每个桶就是40分的范围

plt.xlabel('总分')
plt.ylabel('人数')
plt.title('学生总分分布')
plt.axvline(df_students['总分'].mean(), color='red', linestyle='--', label=f'平均分: {df_students["总分"].mean():.1f}')
plt.legend()
plt.savefig('output_beautified_2.png')
plt.close()
print("美化图表2已保存")

# 恢复默认样式
plt.style.use('default')

# 【常用样式】
# plt.style.available  # 查看所有可用样式
# 常用：'ggplot', 'seaborn-v0_8', 'dark_background', 'fivethirtyeight'

# 6.3 子图（多图画在一起）
print("\n--- 6.3 子图 ---")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 子图1：语文成绩分布
axes[0, 0].hist(df_students['语文'], bins=8, color='#FF6B6B', edgecolor='white')
axes[0, 0].set_title('语文成绩分布')
axes[0, 0].set_xlabel('分数')
axes[0, 0].set_ylabel('人数')

# 子图2：数学成绩分布
axes[0, 1].hist(df_students['数学'], bins=8, color='#4ECDC4', edgecolor='white')
axes[0, 1].set_title('数学成绩分布')
axes[0, 1].set_xlabel('分数')

# 子图3：各科平均分
avg_scores = df_students[subjects].mean()
axes[1, 0].bar(subjects, avg_scores, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
axes[1, 0].set_title('各科平均分')
axes[1, 0].set_ylabel('平均分')

# 子图4：性别分布饼图
gender_count = df_students['性别'].value_counts()
axes[1, 1].pie(gender_count, labels=gender_count.index, autopct='%1.1f%%',
               colors=['#FF9999', '#66B2FF'])
axes[1, 1].set_title('性别分布')

plt.suptitle('学生成绩分析报告', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('output_subplots.png')
plt.close()
print("子图已保存为 output_subplots.png")

# 【subplots 参数说明】
# plt.subplots(行数, 列数, figsize=(宽, 高))
# 返回 fig（整个图形）和 axes（子图数组）
# axes[0, 0] 表示第1行第1列的子图

# 【动手练习 6】
# 1. 绘制电影票房前10的横向柱状图，添加标题、标签、网格
# 2. 绘制一个包含2个子图的图表：左图是评分分布直方图，右图是类型饼图

print("\n--- 练习6答案 ---")
# 答案1
top10_box = df_movies.nlargest(10, '票房(亿)')
plt.figure(figsize=(10, 6))
plt.barh(top10_box['电影名称'], top10_box['票房(亿)'], color='coral')
plt.xlabel('票房（亿）')
plt.ylabel('电影')
plt.title('电影票房排行榜 TOP10', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('output_exercise6_1.png')
plt.close()
print("练习6-1已保存")

# 答案2
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# 评分分布
axes[0].hist(df_movies['评分'], bins=10, color='steelblue', edgecolor='white')
axes[0].set_title('电影评分分布')
axes[0].set_xlabel('评分')
axes[0].set_ylabel('数量')

# 类型饼图
type_count = df_movies['类型'].value_counts()
axes[1].pie(type_count, labels=type_count.index, autopct='%1.1f%%')
axes[1].set_title('电影类型分布')

plt.tight_layout()
plt.savefig('output_exercise6_2.png')
plt.close()
print("练习6-2已保存")


# ========================================
# 第7节：综合案例 - 学生成绩分析
# ========================================
print("\n" + "=" * 50)
print("第7节：综合案例 - 学生成绩分析")
print("=" * 50)

# 7.1 数据准备
# 【为什么要有综合案例？】
# 前面我们学习了各种零散的知识点（筛选、统计、画图）
# 现在通过一个完整的案例，把所有知识点串起来
# 就像学做菜，学了切菜、炒菜、调味，现在要做一整桌菜！
print("\n--- 7.1 数据加载和预处理 ---")

# 重新加载数据
df = pd.read_csv('data/students.csv')

# 计算总分和平均分
subjects = ['语文', '数学', '英语', '科学']
df['总分'] = df[subjects].sum(axis=1)
df['平均分'] = df[subjects].mean(axis=1).round(2)

print("数据预处理完成！")
print(df.head())

# 7.2 成绩概览
print("\n--- 7.2 成绩概览 ---")

print("=== 全班成绩统计 ===")
print(f"学生总数：{len(df)}人")
print(f"总分平均：{df['总分'].mean():.2f}分")
print(f"总分最高：{df['总分'].max()}分 ({df.loc[df['总分'].idxmax(), '姓名']})")
print(f"总分最低：{df['总分'].min()}分 ({df.loc[df['总分'].idxmin(), '姓名']})")

print("\n=== 各科成绩统计 ===")
for subject in subjects:
    print(f"{subject}：平均{df[subject].mean():.1f}分，"
          f"最高{df[subject].max()}分，最低{df[subject].min()}分")

# 7.3 排名分析
print("\n--- 7.3 排名分析 ---")

# 按总分排名
# sort_values(): 按总分排序，ascending=False 表示从高到低
# reset_index(drop=True): 重置索引（行号），丢弃旧的索引
#   - 排序后行号是乱的（比如原来第3行可能变成第1行）
#   - reset_index 让行号重新变成 0,1,2,3...
df_ranked = df.sort_values('总分', ascending=False).reset_index(drop=True)

# 让索引从1开始（因为排名没有第0名）
# df_ranked.index 是行的标签，我们把它改成 1,2,3,4...
df_ranked.index = df_ranked.index + 1  # 排名从1开始

print("=== 成绩排行榜 TOP10 ===")
print(df_ranked[['姓名', '班级', '总分', '平均分']].head(10))

# 7.4 班级对比
print("\n--- 7.4 班级对比 ---")

class_stats = df.groupby('班级').agg({
    '总分': ['mean', 'max', 'min', 'count'],
    '数学': 'mean',
    '语文': 'mean'
}).round(2)

print("=== 各班级成绩统计 ===")
print(class_stats)

# 找出最强班级
best_class = df.groupby('班级')['总分'].mean().idxmax()
print(f"\n平均分最高的班级：{best_class}")

# 7.5 可视化报告
print("\n--- 7.5 生成可视化报告 ---")

fig = plt.figure(figsize=(16, 12))

# 1. 成绩排行榜 TOP10
ax1 = fig.add_subplot(2, 2, 1)
top10 = df_ranked.head(10)
colors = ['gold' if i < 3 else 'steelblue' for i in range(10)]
ax1.barh(top10['姓名'], top10['总分'], color=colors)
ax1.set_xlabel('总分')
ax1.set_title('成绩排行榜 TOP10', fontweight='bold')
ax1.invert_yaxis()  # 从上到下排列

# 2. 各科成绩分布（箱线图）
# 【什么是箱线图？- 用"打包行李"来理解】
# 箱线图用一个"箱子"展示数据的分布情况：
#
#      ┌───┐  <- 上边缘（最高分附近，不包括极端值）
#      │   │
#   ┌──┴───┴──┐ <- 上四分位数（75%的人低于这个分）
#   │    ●    │ <- 中位数线（正中间那个人的分数）
#   └──┬───┬──┘ <- 下四分位数（25%的人低于这个分）
#      │   │
#      └───┘  <- 下边缘（最低分附近，不包括极端值）
#        ○      <- 圆点是异常值（特别低或特别高的分数）
#
# 箱子越"扁"：成绩集中在中间，波动小
# 箱子越"长"：成绩分散，高低差距大
ax2 = fig.add_subplot(2, 2, 2)
df[subjects].boxplot(ax=ax2)
ax2.set_ylabel('分数')
ax2.set_title('各科成绩分布（箱线图）', fontweight='bold')

# 3. 班级平均分对比
ax3 = fig.add_subplot(2, 2, 3)
class_avg = df.groupby('班级')[subjects].mean()
class_avg.plot(kind='bar', ax=ax3, width=0.8)
ax3.set_xlabel('班级')
ax3.set_ylabel('平均分')
ax3.set_title('各班级各科平均分', fontweight='bold')
ax3.legend(loc='upper right')
ax3.set_xticklabels(class_avg.index, rotation=0)

# 4. 性别成绩对比
ax4 = fig.add_subplot(2, 2, 4)
gender_avg = df.groupby('性别')[subjects].mean()
gender_avg.plot(kind='bar', ax=ax4, width=0.7)
ax4.set_xlabel('性别')
ax4.set_ylabel('平均分')
ax4.set_title('男女生各科平均分对比', fontweight='bold')
ax4.legend(loc='upper right')
ax4.set_xticklabels(gender_avg.index, rotation=0)

plt.suptitle('学生成绩分析报告', fontsize=18, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('output_student_analysis.png', bbox_inches='tight', dpi=150)
plt.close()
print("学生成绩分析报告已保存为 output_student_analysis.png")

# 7.6 成绩等级分析
print("\n--- 7.6 成绩等级分析 ---")

# 定义成绩等级函数
def get_grade(score):
    """
    根据分数返回对应的等级

    参数:
        score: 分数值（整数或浮点数，范围0-100）
               例如: 95, 85.5, 72

    返回:
        等级字符串: '优秀'(>=90), '良好'(>=80), '中等'(>=70), '及格'(>=60), '不及格'(<60)

    调用示例:
        get_grade(95)    # 返回 '优秀'
        get_grade(85.5)  # 返回 '良好'
        get_grade(55)    # 返回 '不及格'
    """
    if score >= 90:
        return '优秀'
    elif score >= 80:
        return '良好'
    elif score >= 70:
        return '中等'
    elif score >= 60:
        return '及格'
    else:
        return '不及格'

# 调用示例1：直接调用
print("调用示例：")
print(f"  get_grade(95) = {get_grade(95)}")      # 优秀
print(f"  get_grade(85.5) = {get_grade(85.5)}")  # 良好
print(f"  get_grade(55) = {get_grade(55)}")      # 不及格

# 调用示例2：在DataFrame中使用apply批量处理
# 【apply 是什么？- 用"流水线"来理解】
# 想象工厂流水线：
# - 传送带把每个产品（每行数据）送到工人面前
# - 工人对每个产品执行同样的操作（调用 get_grade 函数）
# - 处理完放回传送带继续
#
# df['平均分'].apply(get_grade) 的意思是：
# "对平均分这一列的每个数字，都调用 get_grade 函数"
# 就像对全班每个人的平均分都判断一次等级
df['等级'] = df['平均分'].apply(get_grade)
grade_count = df['等级'].value_counts()

print("=== 成绩等级分布 ===")
print(grade_count)

# 绘制等级分布饼图
plt.figure(figsize=(8, 8))
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
plt.pie(grade_count, labels=grade_count.index, autopct='%1.1f%%',
        colors=colors[:len(grade_count)], startangle=90, explode=[0.05]*len(grade_count))
plt.title('学生成绩等级分布', fontsize=14, fontweight='bold')
plt.savefig('output_grade_distribution.png')
plt.close()
print("等级分布图已保存")

print("\n=== 学生成绩分析完成！===")


# ========================================
# 第8节：综合案例 - 电影数据分析
# ========================================
print("\n" + "=" * 50)
print("第8节：综合案例 - 电影数据分析")
print("=" * 50)

# 8.1 数据加载和预处理
print("\n--- 8.1 数据加载 ---")

df_movies = pd.read_csv('data/movies.csv')

# 去除重复数据
df_movies = df_movies.drop_duplicates(subset=['电影名称'])
print(f"共加载 {len(df_movies)} 部电影")
print(df_movies.head())

# 8.2 基础统计
print("\n--- 8.2 基础统计 ---")

print("=== 电影数据统计 ===")
print(f"平均评分：{df_movies['评分'].mean():.2f}")
print(f"最高评分：{df_movies['评分'].max()} ({df_movies.loc[df_movies['评分'].idxmax(), '电影名称']})")
print(f"最低评分：{df_movies['评分'].min()} ({df_movies.loc[df_movies['评分'].idxmin(), '电影名称']})")
print(f"总票房：{df_movies['票房(亿)'].sum():.2f}亿")
print(f"平均时长：{df_movies['时长(分钟)'].mean():.1f}分钟")

# 8.3 类型分析
print("\n--- 8.3 类型分析 ---")

type_stats = df_movies.groupby('类型').agg({
    '电影名称': 'count',
    '评分': 'mean',
    '票房(亿)': ['sum', 'mean']
}).round(2)

type_stats.columns = ['数量', '平均评分', '总票房', '平均票房']
type_stats = type_stats.sort_values('数量', ascending=False)

print("=== 电影类型统计 ===")
print(type_stats)

# 8.4 评分与票房关系
print("\n--- 8.4 评分与票房关系 ---")

# 计算相关系数
# 【什么是相关系数？- 用"朋友关系"来理解】
# 相关系数告诉我们两个事物是否有"关联"：
#
# 正相关（接近+1）：一个增加，另一个也增加
#   例如：学习时间越长，成绩越高
#
# 负相关（接近-1）：一个增加，另一个减少
#   例如：玩游戏时间越长，成绩越低
#
# 无相关（接近0）：两个事物没关系
#   例如：鞋码和成绩没关系
#
# 这里算的是：评分高，票房是否也高？
correlation = df_movies['评分'].corr(df_movies['票房(亿)'])
print(f"评分与票房的相关系数：{correlation:.2f}")

# 8.5 年份分析
print("\n--- 8.5 年份分析 ---")

year_stats = df_movies.groupby('年份').agg({
    '电影名称': 'count',
    '评分': 'mean',
    '票房(亿)': 'sum'
}).round(2)

year_stats.columns = ['数量', '平均评分', '总票房']
print("=== 各年份电影统计 ===")
print(year_stats)

# 8.6 生成可视化报告
print("\n--- 8.6 生成可视化报告 ---")

fig = plt.figure(figsize=(16, 12))

# 1. 票房TOP10
ax1 = fig.add_subplot(2, 2, 1)
top10_box = df_movies.nlargest(10, '票房(亿)')

# 【渐变色的原理】
# plt.cm.Reds 是一个颜色地图，从浅红到深红
# np.linspace(0.4, 0.8, 10) 生成10个数字，从0.4到0.8等间隔
# 这些数字对应颜色地图上的位置，越大的数字颜色越深
# 结果：10个柱子颜色从浅红渐变到深红
import numpy as np  # numpy 是数值计算库，用于生成数字序列
colors = plt.cm.Reds(np.linspace(0.4, 0.8, 10))  # 生成10个渐变红色

ax1.barh(top10_box['电影名称'], top10_box['票房(亿)'], color=colors)
ax1.set_xlabel('票房（亿）')
ax1.set_title('票房排行榜 TOP10', fontweight='bold')
ax1.invert_yaxis()

# 2. 评分TOP10
ax2 = fig.add_subplot(2, 2, 2)
top10_rating = df_movies.nlargest(10, '评分')
colors = plt.cm.Greens(np.linspace(0.4, 0.8, 10))
ax2.barh(top10_rating['电影名称'], top10_rating['评分'], color=colors)
ax2.set_xlabel('评分')
ax2.set_title('评分排行榜 TOP10', fontweight='bold')
ax2.invert_yaxis()

# 3. 类型分布
ax3 = fig.add_subplot(2, 2, 3)
type_count = df_movies['类型'].value_counts()
ax3.pie(type_count, labels=type_count.index, autopct='%1.1f%%',
        colors=plt.cm.Set3.colors[:len(type_count)])
ax3.set_title('电影类型分布', fontweight='bold')

# 4. 评分与票房散点图
ax4 = fig.add_subplot(2, 2, 4)
scatter = ax4.scatter(df_movies['评分'], df_movies['票房(亿)'],
                      c=df_movies['年份'], cmap='viridis', s=100, alpha=0.7)
ax4.set_xlabel('评分')
ax4.set_ylabel('票房（亿）')
ax4.set_title('评分与票房关系（颜色表示年份）', fontweight='bold')
plt.colorbar(scatter, ax=ax4, label='年份')

plt.suptitle('电影数据分析报告', fontsize=18, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('output_movie_analysis.png', bbox_inches='tight', dpi=150)
plt.close()
print("电影数据分析报告已保存为 output_movie_analysis.png")

print("\n=== 电影数据分析完成！===")


# ========================================
# 总结
# ========================================
print("\n" + "=" * 50)
print("教程总结")
print("=" * 50)

print("""
恭喜你完成了数据分析快速入门教程！

【你学到了什么】
1. 什么是数据分析及其步骤
2. 使用 pandas 读取和处理数据
3. 数据筛选、排序、分组统计
4. 使用 matplotlib 绑制各种图表
5. 图表美化技巧
6. 两个完整的综合案例

【常用函数速查表】
- pd.read_csv() - 读取CSV文件
- df.head()/tail() - 查看前/后几行
- df.shape - 数据形状
- df.describe() - 统计摘要
- df['列名'] - 选择列
- df[df['列'] > 值] - 条件筛选
- df.groupby('列') - 分组
- df.sort_values('列') - 排序
- df.mean()/sum()/max()/min() - 统计计算
- plt.plot() - 折线图
- plt.bar()/barh() - 柱状图
- plt.pie() - 饼图
- plt.scatter() - 散点图
- plt.hist() - 直方图
- plt.subplot() - 子图

【下一步学习建议】
1. 完成 data_analysis_exercises.py 中的练习题
2. 找自己感兴趣的数据进行分析
3. 学习更多可视化库：seaborn, plotly
4. 学习数据清洗技巧：处理缺失值、重复值
5. 学习更高级的统计分析方法

【实用资源】
- pandas官方文档：https://pandas.pydata.org/
- matplotlib官方文档：https://matplotlib.org/
- 数据来源：Kaggle、天池、政府开放数据
""")

print("\n=== 教程结束 ===")
print("记住：数据分析最重要的是多练多思考！")
