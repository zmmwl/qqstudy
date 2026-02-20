# 数据分析快速入门教程

适合初中生学习的数据分析教程，2-3小时快速上手！

## 目录结构

```
data_analysis/
├── data_analysis_quick_start.py   # 主教程
├── data_analysis_exercises.py     # 练习题（带答案）
├── data/                          # 示例数据
│   ├── students.csv              # 学生成绩数据（20条）
│   ├── movies.csv                # 电影评分数据（20条）
│   └── weather.csv               # 天气数据（25条）
└── README.md                      # 使用说明
```

## 环境准备

### 1. 安装Python
确保已安装Python 3.7或更高版本：
```bash
python --version
```

### 2. 安装依赖库
```bash
pip install pandas matplotlib numpy
```

## 使用方法

### 运行主教程
```bash
cd data_analysis
python data_analysis_quick_start.py
```

### 运行练习题
```bash
python data_analysis_exercises.py
```

## 教程内容

### 主教程章节（data_analysis_quick_start.py）

| 章节 | 内容 | 预计时间 |
|------|------|----------|
| 第1节 | 什么是数据分析？ | 10分钟 |
| 第2节 | 认识pandas和DataFrame | 15分钟 |
| 第3节 | 数据筛选 | 15分钟 |
| 第4节 | 数据统计 | 15分钟 |
| 第5节 | 数据可视化入门 | 20分钟 |
| 第6节 | 图表美化 | 15分钟 |
| 第7节 | 综合案例-学生成绩分析 | 20分钟 |
| 第8节 | 综合案例-电影数据分析 | 20分钟 |

### 练习题（data_analysis_exercises.py）

| 练习 | 难度 | 主题 |
|------|------|------|
| 练习1 | ★ | 数据查看 |
| 练习2 | ★ | 数据筛选 |
| 练习3 | ★★ | 多条件筛选 |
| 练习4 | ★ | 统计计算 |
| 练习5 | ★★ | 分组统计 |
| 练习6 | ★ | 排序 |
| 练习7 | ★★ | 数据可视化 |
| 练习8 | ★★★ | 综合分析 |
| 练习9 | ★★★ | 自定义分析 |
| 练习10 | ★★★ | 挑战题 |

## 示例数据说明

### students.csv - 学生成绩数据
- 20名学生的成绩数据
- 包含：姓名、班级、语文、数学、英语、科学、性别

### movies.csv - 电影数据
- 20部电影的评分数据
- 包含：电影名称、类型、评分、票房、年份、导演、时长

### weather.csv - 天气数据
- 25条天气记录
- 包含：日期、城市、最高温度、最低温度、天气、湿度、风力

## 输出文件

运行教程后，会生成以下图表文件：
- `output_line_chart.png` - 折线图示例
- `output_bar_chart.png` - 柱状图示例
- `output_pie_chart.png` - 饼图示例
- `output_scatter.png` - 散点图示例
- `output_subplots.png` - 子图示例
- `output_student_analysis.png` - 学生成绩分析报告
- `output_movie_analysis.png` - 电影数据分析报告
- 以及练习生成的图表文件

## 常用函数速查

### pandas常用函数
```python
# 读取数据
df = pd.read_csv('file.csv')

# 查看数据
df.head()        # 前5行
df.tail()        # 后5行
df.shape         # 形状
df.columns       # 列名
df.describe()    # 统计摘要
df.info()        # 信息

# 选择数据
df['列名']                    # 选择单列
df[['列1', '列2']]           # 选择多列
df.iloc[0]                   # 按位置选择行
df.loc[0, '列名']            # 按标签选择

# 筛选数据
df[df['列'] > 值]            # 条件筛选
df[df['列'].isin(['值1', '值2'])]  # 多值筛选

# 统计计算
df['列'].mean()   # 平均值
df['列'].sum()    # 总和
df['列'].max()    # 最大值
df['列'].min()    # 最小值
df['列'].count()  # 计数

# 分组统计
df.groupby('列')['值列'].mean()  # 分组求平均

# 排序
df.sort_values('列')                    # 升序
df.sort_values('列', ascending=False)  # 降序
```

### matplotlib常用函数
```python
# 创建图形
plt.figure(figsize=(宽, 高))

# 绑图
plt.plot(x, y)      # 折线图
plt.bar(x, y)       # 柱状图
plt.barh(x, y)      # 横向柱状图
plt.pie(data)       # 饼图
plt.scatter(x, y)   # 散点图
plt.hist(data)      # 直方图

# 设置
plt.title('标题')
plt.xlabel('x轴标签')
plt.ylabel('y轴标签')
plt.legend()        # 图例
plt.grid()          # 网格

# 保存和显示
plt.savefig('文件名.png')
plt.close()         # 关闭图形
```

## 学习建议

1. **边看边练**：不要只看代码，要动手运行
2. **理解概念**：理解每行代码的作用
3. **尝试修改**：修改参数看看效果变化
4. **举一反三**：用学到的知识分析自己的数据
5. **多做练习**：完成所有练习题

## 进阶学习

完成本教程后，可以继续学习：
- seaborn：更高级的统计图表
- plotly：交互式图表
- 数据清洗：处理缺失值、重复值
- 机器学习入门：scikit-learn

## 常见问题

### Q: 中文显示乱码怎么办？
A: 在代码开头添加：
```python
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
```

### Q: 提示找不到模块怎么办？
A: 确保已安装对应的库：
```bash
pip install pandas matplotlib numpy
```

### Q: 运行时提示文件不存在？
A: 确保在 `data_analysis` 目录下运行脚本，或使用绝对路径。

## 联系方式

如有问题，欢迎提Issue讨论！

---
祝你学习愉快！
