# ========================================
# 数据分析练习题（带答案）
# ========================================
# 建议先自己做，做不出来再看答案
# 每道题都有难度标识：★简单 ★★中等 ★★★困难

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 加载数据
df_students = pd.read_csv('data/students.csv')
df_movies = pd.read_csv('data/movies.csv')
df_weather = pd.read_csv('data/weather.csv')

# 计算学生总分
subjects = ['语文', '数学', '英语', '科学']
df_students['总分'] = df_students[subjects].sum(axis=1)
df_students['平均分'] = df_students[subjects].mean(axis=1)

print("数据加载完成！开始练习吧！")
print("=" * 60)


# ========================================
# 练习1：数据查看（难度：★）
# ========================================
print("\n【练习1】数据查看（难度：★）")
print("-" * 40)

"""
题目：
1. 查看天气数据的前5行
2. 查看天气数据有多少行、多少列
3. 查看天气数据的列名
4. 查看天气数据的统计摘要
"""

# 在这里写你的代码
# ...


# -------- 答案 --------
print("\n=== 答案 ===")
# 1
print("1. 天气数据前5行：")
print(df_weather.head())

# 2
print(f"\n2. 天气数据形状：{df_weather.shape[0]}行，{df_weather.shape[1]}列")

# 3
print(f"\n3. 列名：{list(df_weather.columns)}")

# 4
print("\n4. 统计摘要：")
print(df_weather.describe())


# ========================================
# 练习2：数据筛选（难度：★）
# ========================================
print("\n" + "=" * 60)
print("【练习2】数据筛选（难度：★）")
print("-" * 40)

"""
题目：
1. 筛选出所有女生的数据
2. 筛选出数学成绩大于85的学生
3. 筛选出北京的所有天气数据
4. 筛选出评分大于8.5的电影
"""

# 在这里写你的代码
# ...


# -------- 答案 --------
print("\n=== 答案 ===")
# 1
print("1. 所有女生：")
print(df_students[df_students['性别'] == '女'][['姓名', '性别']])

# 2
print("\n2. 数学>85的学生：")
print(df_students[df_students['数学'] > 85][['姓名', '数学']])

# 3
print("\n3. 北京的天气数据：")
print(df_weather[df_weather['城市'] == '北京'][['日期', '最高温度', '天气']].head())

# 4
print("\n4. 评分>8.5的电影：")
high_rating = df_movies[df_movies['评分'] > 8.5]
print(high_rating[['电影名称', '评分']])


# ========================================
# 练习3：多条件筛选（难度：★★）
# ========================================
print("\n" + "=" * 60)
print("【练习3】多条件筛选（难度：★★）")
print("-" * 40)

"""
题目：
1. 筛选出数学>85 且 英语>85 的学生
2. 筛选出1班或2班的学生
3. 筛选出北京在1月份的天气数据（日期包含'2024-01'）
4. 筛选出动画类型且评分>8的电影
"""

# 在这里写你的代码
# ...


# -------- 答案 --------
print("\n=== 答案 ===")
# 1
print("1. 数学>85且英语>85：")
good = df_students[(df_students['数学'] > 85) & (df_students['英语'] > 85)]
print(good[['姓名', '数学', '英语']])

# 2
print("\n2. 1班或2班的学生：")
class12 = df_students[df_students['班级'].isin(['1班', '2班'])]
print(class12[['姓名', '班级']])

# 3
print("\n3. 北京1月份天气：")
beijing_jan = df_weather[(df_weather['城市'] == '北京') & (df_weather['日期'].str.startswith('2024-01'))]
print(beijing_jan[['日期', '最高温度', '最低温度', '天气']])

# 4
print("\n4. 动画且评分>8：")
ani_good = df_movies[(df_movies['类型'] == '动画') & (df_movies['评分'] > 8)]
print(ani_good[['电影名称', '评分']])


# ========================================
# 练习4：统计计算（难度：★）
# ========================================
print("\n" + "=" * 60)
print("【练习4】统计计算（难度：★）")
print("-" * 40)

"""
题目：
1. 计算学生数学成绩的平均分、最高分、最低分
2. 计算电影的总票房
3. 计算北京的平均最高温度
4. 统计有多少部电影是动画类型
"""

# 在这里写你的代码
# ...


# -------- 答案 --------
print("\n=== 答案 ===")
# 1
print(f"1. 数学平均分：{df_students['数学'].mean():.2f}")
print(f"   数学最高分：{df_students['数学'].max()}")
print(f"   数学最低分：{df_students['数学'].min()}")

# 2
print(f"\n2. 电影总票房：{df_movies['票房(亿)'].sum():.2f}亿")

# 3
beijing = df_weather[df_weather['城市'] == '北京']
print(f"\n3. 北京平均最高温度：{beijing['最高温度'].mean():.1f}°C")

# 4
ani_count = len(df_movies[df_movies['类型'] == '动画'])
print(f"\n4. 动画电影数量：{ani_count}部")


# ========================================
# 练习5：分组统计（难度：★★）
# ========================================
print("\n" + "=" * 60)
print("【练习5】分组统计（难度：★★）")
print("-" * 40)

"""
题目：
1. 按班级分组，计算每个班的平均总分
2. 按性别分组，计算男女生的各科平均分
3. 按城市分组，计算每个城市的平均最高温度
4. 按电影类型分组，计算每种类型的数量和平均评分
"""

# 在这里写你的代码
# ...


# -------- 答案 --------
print("\n=== 答案 ===")
# 1
print("1. 各班级平均总分：")
print(df_students.groupby('班级')['总分'].mean().round(2))

# 2
print("\n2. 男女生各科平均分：")
print(df_students.groupby('性别')[subjects].mean().round(2))

# 3
print("\n3. 各城市平均最高温度：")
print(df_weather.groupby('城市')['最高温度'].mean().round(1))

# 4
print("\n4. 各类型电影统计：")
type_stats = df_movies.groupby('类型').agg({
    '电影名称': 'count',
    '评分': 'mean'
}).round(2)
type_stats.columns = ['数量', '平均评分']
print(type_stats)


# ========================================
# 练习6：排序（难度：★）
# ========================================
print("\n" + "=" * 60)
print("【练习6】排序（难度：★）")
print("-" * 40)

"""
题目：
1. 按总分降序排列学生，显示前5名
2. 按票房降序排列电影，显示前5名
3. 按评分升序排列电影，显示最后5名（评分最低的）
4. 先按班级升序，再按总分降序排列学生
"""

# 在这里写你的代码
# ...


# -------- 答案 --------
print("\n=== 答案 ===")
# 1
print("1. 总分前5名：")
print(df_students.sort_values('总分', ascending=False)[['姓名', '总分']].head())

# 2
print("\n2. 票房前5名：")
print(df_movies.sort_values('票房(亿)', ascending=False)[['电影名称', '票房(亿)']].head())

# 3
print("\n3. 评分最低5名：")
print(df_movies.sort_values('评分', ascending=True)[['电影名称', '评分']].head())

# 4
print("\n4. 按班级升序、总分降序：")
print(df_students.sort_values(['班级', '总分'], ascending=[True, False])[['姓名', '班级', '总分']].head(10))


# ========================================
# 练习7：数据可视化（难度：★★）
# ========================================
print("\n" + "=" * 60)
print("【练习7】数据可视化（难度：★★）")
print("-" * 40)

"""
题目：
1. 绑制学生数学成绩的柱状图
2. 绑制电影评分分布的直方图
3. 绑制学生性别分布的饼图
4. 绑制数学成绩和英语成绩的散点图
"""

# 在这里写你的代码
# ...


# -------- 答案 --------
print("\n=== 答案 ===")

# 1
plt.figure(figsize=(10, 6))
plt.bar(df_students['姓名'], df_students['数学'], color='steelblue')
plt.xlabel('学生')
plt.ylabel('数学成绩')
plt.title('学生数学成绩')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('exercise_7_1.png')
plt.close()
print("1. 数学成绩柱状图已保存为 exercise_7_1.png")

# 2
plt.figure(figsize=(8, 5))
plt.hist(df_movies['评分'], bins=8, color='coral', edgecolor='white')
plt.xlabel('评分')
plt.ylabel('数量')
plt.title('电影评分分布')
plt.savefig('exercise_7_2.png')
plt.close()
print("2. 评分分布直方图已保存为 exercise_7_2.png")

# 3
plt.figure(figsize=(6, 6))
gender_count = df_students['性别'].value_counts()
plt.pie(gender_count, labels=gender_count.index, autopct='%1.1f%%', colors=['#FF9999', '#66B2FF'])
plt.title('学生性别分布')
plt.savefig('exercise_7_3.png')
plt.close()
print("3. 性别分布饼图已保存为 exercise_7_3.png")

# 4
plt.figure(figsize=(8, 6))
plt.scatter(df_students['数学'], df_students['英语'], c='green', alpha=0.7, s=80)
plt.xlabel('数学成绩')
plt.ylabel('英语成绩')
plt.title('数学 vs 英语成绩')
plt.savefig('exercise_7_4.png')
plt.close()
print("4. 数学vs英语散点图已保存为 exercise_7_4.png")


# ========================================
# 练习8：综合分析（难度：★★★）
# ========================================
print("\n" + "=" * 60)
print("【练习8】综合分析（难度：★★★）")
print("-" * 40)

"""
题目：分析天气数据
1. 统计每个城市的平均最高温度和平均最低温度
2. 找出每个城市最热的一天（最高温度最高）
3. 统计每种天气出现的次数
4. 绑制各城市温度对比的柱状图
"""

# 在这里写你的代码
# ...


# -------- 答案 --------
print("\n=== 答案 ===")

# 1
print("1. 各城市平均温度：")
city_temp = df_weather.groupby('城市').agg({
    '最高温度': 'mean',
    '最低温度': 'mean'
}).round(1)
print(city_temp)

# 2
print("\n2. 各城市最热的一天：")
for city in df_weather['城市'].unique():
    city_data = df_weather[df_weather['城市'] == city]
    hottest = city_data.loc[city_data['最高温度'].idxmax()]
    print(f"   {city}：{hottest['日期']}，{hottest['最高温度']}°C")

# 3
print("\n3. 天气类型统计：")
print(df_weather['天气'].value_counts())

# 4
plt.figure(figsize=(10, 6))
x = range(len(city_temp.index))
width = 0.35
plt.bar([i - width/2 for i in x], city_temp['最高温度'], width, label='平均最高温', color='#FF6B6B')
plt.bar([i + width/2 for i in x], city_temp['最低温度'], width, label='平均最低温', color='#4ECDC4')
plt.xlabel('城市')
plt.ylabel('温度 (°C)')
plt.title('各城市平均温度对比')
plt.xticks(x, city_temp.index)
plt.legend()
plt.savefig('exercise_8_4.png')
plt.close()
print("\n4. 城市温度对比图已保存为 exercise_8_4.png")


# ========================================
# 练习9：自定义分析（难度：★★★）
# ========================================
print("\n" + "=" * 60)
print("【练习9】自定义分析（难度：★★★）")
print("-" * 40)

"""
题目：学生成绩深度分析

1. 添加一列"等级"，根据平均分划分：
   - 90分以上：优秀
   - 80-89分：良好
   - 70-79分：中等
   - 60-69分：及格
   - 60分以下：不及格

2. 统计每个等级的人数

3. 找出每个班的"学习之星"（班级总分第一名）

4. 分析每个学生的"优势科目"（得分最高的科目）

5. 生成一份可视化报告，包含：
   - 成绩等级分布饼图
   - 各班级平均分对比柱状图
   - 各科目成绩分布箱线图
"""

# 在这里写你的代码
# ...


# -------- 答案 --------
print("\n=== 答案 ===")

# 1
def get_grade(avg):
    if avg >= 90:
        return '优秀'
    elif avg >= 80:
        return '良好'
    elif avg >= 70:
        return '中等'
    elif avg >= 60:
        return '及格'
    else:
        return '不及格'

df_students['等级'] = df_students['平均分'].apply(get_grade)
print("1. 添加等级列完成")
print(df_students[['姓名', '平均分', '等级']].head(10))

# 2
print("\n2. 各等级人数：")
print(df_students['等级'].value_counts())

# 3
print("\n3. 各班学习之星：")
for cls in df_students['班级'].unique():
    class_data = df_students[df_students['班级'] == cls]
    star = class_data.loc[class_data['总分'].idxmax()]
    print(f"   {cls}：{star['姓名']}，总分{star['总分']}")

# 4
print("\n4. 各学生优势科目：")
def get_best_subject(row):
    scores = {sub: row[sub] for sub in subjects}
    return max(scores, key=scores.get)

df_students['优势科目'] = df_students.apply(get_best_subject, axis=1)
print(df_students[['姓名', '优势科目']].head(10))

# 优势科目统计
print("\n优势科目分布：")
print(df_students['优势科目'].value_counts())

# 5
print("\n5. 生成可视化报告...")
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# 等级分布饼图
grade_count = df_students['等级'].value_counts()
axes[0, 0].pie(grade_count, labels=grade_count.index, autopct='%1.1f%%',
               colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'])
axes[0, 0].set_title('成绩等级分布')

# 各班平均分柱状图
class_avg = df_students.groupby('班级')['总分'].mean()
axes[0, 1].bar(class_avg.index, class_avg.values, color='steelblue')
axes[0, 1].set_xlabel('班级')
axes[0, 1].set_ylabel('平均总分')
axes[0, 1].set_title('各班级平均总分')

# 各科成绩箱线图
df_students[subjects].boxplot(ax=axes[1, 0])
axes[1, 0].set_ylabel('分数')
axes[1, 0].set_title('各科成绩分布')

# 优势科目柱状图
advantage_count = df_students['优势科目'].value_counts()
axes[1, 1].bar(advantage_count.index, advantage_count.values, color='coral')
axes[1, 1].set_xlabel('科目')
axes[1, 1].set_ylabel('人数')
axes[1, 1].set_title('学生优势科目分布')

plt.suptitle('学生成绩深度分析报告', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('exercise_9_report.png', dpi=150)
plt.close()
print("可视化报告已保存为 exercise_9_report.png")


# ========================================
# 练习10：挑战题（难度：★★★）
# ========================================
print("\n" + "=" * 60)
print("【练习10】挑战题（难度：★★★）")
print("-" * 40)

"""
题目：电影数据分析挑战

1. 计算每部电影的"性价比"（评分/票房，单位：分/亿）
   并找出性价比最高的3部电影

2. 按年份分组，统计每年的：
   - 电影数量
   - 平均评分
   - 总票房
   然后绑制"年份-总票房"的折线图

3. 分析导演的票房号召力：
   - 统计每位导演的电影数量和总票房
   - 找出总票房最高的导演

4. 创建一个评分等级（9分以上为神作，8-9分为佳作，
   6-8分为普通，6分以下为烂片），统计各等级数量

5. 绑制一个综合分析图，包含：
   - 左上：票房TOP10横向柱状图
   - 右上：评分分布直方图
   - 左下：类型占比饼图
   - 右下：评分vs票房散点图
"""

# 在这里写你的代码
# ...


# -------- 答案 --------
print("\n=== 答案 ===")

# 去重
df_m = df_movies.drop_duplicates(subset=['电影名称'])

# 1
print("1. 性价比最高的3部电影：")
df_m['性价比'] = df_m['评分'] / df_m['票房(亿)']
best_value = df_m.nlargest(3, '性价比')
print(best_value[['电影名称', '评分', '票房(亿)', '性价比']])

# 2
print("\n2. 各年份统计：")
year_stats = df_m.groupby('年份').agg({
    '电影名称': 'count',
    '评分': 'mean',
    '票房(亿)': 'sum'
}).round(2)
year_stats.columns = ['数量', '平均评分', '总票房']
print(year_stats)

plt.figure(figsize=(10, 5))
plt.plot(year_stats.index, year_stats['总票房'], marker='o', linewidth=2)
plt.xlabel('年份')
plt.ylabel('总票房（亿）')
plt.title('各年份总票房趋势')
plt.grid(alpha=0.3)
plt.savefig('exercise_10_2.png')
plt.close()
print("年份-票房折线图已保存")

# 3
print("\n3. 导演票房统计：")
director_stats = df_m.groupby('导演').agg({
    '电影名称': 'count',
    '票房(亿)': 'sum'
}).round(2)
director_stats.columns = ['电影数', '总票房']
director_stats = director_stats.sort_values('总票房', ascending=False)
print(director_stats.head())
print(f"\n票房最高导演：{director_stats.index[0]}，总票房{director_stats.iloc[0]['总票房']}亿")

# 4
print("\n4. 评分等级分布：")
def get_rating_grade(rating):
    if rating >= 9:
        return '神作'
    elif rating >= 8:
        return '佳作'
    elif rating >= 6:
        return '普通'
    else:
        return '烂片'

df_m['等级'] = df_m['评分'].apply(get_rating_grade)
print(df_m['等级'].value_counts())

# 5
print("\n5. 综合分析图...")
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# 票房TOP10
top10 = df_m.nlargest(10, '票房(亿)')
axes[0, 0].barh(top10['电影名称'], top10['票房(亿)'], color='steelblue')
axes[0, 0].set_xlabel('票房（亿）')
axes[0, 0].set_title('票房TOP10')
axes[0, 0].invert_yaxis()

# 评分分布
axes[0, 1].hist(df_m['评分'], bins=10, color='coral', edgecolor='white')
axes[0, 1].set_xlabel('评分')
axes[0, 1].set_ylabel('数量')
axes[0, 1].set_title('评分分布')

# 类型饼图
type_count = df_m['类型'].value_counts()
axes[1, 0].pie(type_count, labels=type_count.index, autopct='%1.1f%%')
axes[1, 0].set_title('类型分布')

# 评分vs票房
axes[1, 1].scatter(df_m['评分'], df_m['票房(亿)'], c=df_m['年份'], cmap='viridis', s=100, alpha=0.7)
axes[1, 1].set_xlabel('评分')
axes[1, 1].set_ylabel('票房（亿）')
axes[1, 1].set_title('评分vs票房')

plt.suptitle('电影数据综合分析', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('exercise_10_report.png', dpi=150)
plt.close()
print("综合分析图已保存为 exercise_10_report.png")


# ========================================
# 练习完成！
# ========================================
print("\n" + "=" * 60)
print("恭喜！所有练习完成！")
print("=" * 60)
print("""
你已完成的练习：
- 练习1：数据查看 ★
- 练习2：数据筛选 ★
- 练习3：多条件筛选 ★★
- 练习4：统计计算 ★
- 练习5：分组统计 ★★
- 练习6：排序 ★
- 练习7：数据可视化 ★★
- 练习8：综合分析 ★★★
- 练习9：自定义分析 ★★★
- 练习10：挑战题 ★★★

下一步建议：
1. 找自己感兴趣的数据进行分析
2. 尝试回答自己提出的问题
3. 学习更高级的可视化（seaborn, plotly）
4. 学习数据清洗技巧
""")
