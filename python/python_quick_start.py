# ========================================
# Python 快速入门教程 (1小时学习计划)
# ========================================
# 建议学习时间分配：
# - 第1-5节：30分钟（基础语法和数据类型）
# - 第6-9节：20分钟（控制流和函数）
# - 第10-12节：10分钟（高级概念）

"""
使用方法：
1. 逐节阅读代码示例
2. 运行代码查看结果
3. 完成"练习"部分的题目
4. 阅读注释理解概念
"""

# ========================================
# 第1节：Hello World 和 注释 (2分钟)
# ========================================

# 这是单行注释

'''
这是多行注释
可以写多行
'''

"""
这也是多行注释
通常用于文档说明
"""

# 第一个程序
print("Hello, World!")  # print() 用于输出内容

# 练习1：打印你自己的名字
# _______________________________________


# ========================================
# 第2节：变量和数据类型 (5分钟)
# ========================================

# 变量赋值（Python不需要声明类型）
name = "小明"        # 字符串 str
age = 18            # 整数 int
height = 1.75       # 浮点数 float
is_student = True   # 布尔值 bool
nothing = None      # 空值 NoneType

# 查看变量类型
print(type(name))   # <class 'str'>
print(type(age))    # <class 'int'>

# 类型转换
num_str = "100"
num = int(num_str)      # 字符串转整数
price = float("19.99")  # 字符串转浮点数
text = str(123)         # 数字转字符串

# 练习2：创建变量存储你的信息（姓名、年龄、身高）
# 打印出所有信息
# _______________________________________


# ========================================
# 第3节：字符串操作 (5分钟)
# ========================================

# 字符串创建
text1 = '单引号字符串'
text2 = "双引号字符串"
text3 = """三引号可以
跨越多行"""

# 字符串拼接
greeting = "Hello" + " " + "World"
name = "小明"
message = f"你好，{name}！"  # f-string（推荐方式）

# 字符串方法
sentence = "  Hello Python World  "
print(sentence.upper())      # 转大写: "  HELLO PYTHON WORLD  "
print(sentence.lower())      # 转小写
print(sentence.strip())      # 去除首尾空格
print(sentence.split())      # 分割成列表: ['Hello', 'Python', 'World']
print(sentence.replace("Python", "编程"))  # 替换

# 字符串索引和切片
word = "Python"
print(word[0])       # 第一个字符: 'P'
print(word[-1])      # 最后一个字符: 'n'
print(word[0:3])     # 切片: 'Pyt'
print(word[3:])      # 切片: 'hon'
print(word[::-1])    # 反转: 'nohtyP'

print(word[5:0:-1])

# 练习3：创建一个字符串，使用至少3种字符串方法
# _______________________________________


# ========================================
# 第4节：数字和运算符 (3分钟)
# ========================================

# 基本运算
a = 10
b = 3

print(a + b)   # 加法: 13
print(a - b)   # 减法: 7
print(a * b)   # 乘法: 30
print(a / b)   # 除法: 3.333...
print(a // b)  # 整除: 3
print(a % b)   # 取余: 1
print(a ** b)  # 幂运算: 1000

# 比较运算符
print(a > b)   # True
print(a == b)  # False
print(a != b)  # True

# 逻辑运算符
x = True
y = False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False

# 练习4：计算圆的面积（半径为5，π=3.14159）
# _______________________________________


# ========================================
# 第5节：输入输出 (2分钟)
# ========================================

# 输出
print("一行输出")
print("多行", "输出", "用逗号分隔")  # 逗号会自动加空格

# 输入
# name = input("请输入你的名字：")  # 注意：input返回字符串
# age = int(input("请输入你的年龄："))  # 转换为整数

# 格式化输出（推荐f-string）
name = "小明"
age = 18
print(f"我叫{name}，今年{age}岁")
print(f"明年我就{age + 1}岁了")

# 练习5：编写程序询问用户姓名和年龄，然后打印问候
# _______________________________________


# ========================================
# 第6节：列表 List (5分钟)
# ========================================

# 创建列表
fruits = ["苹果", "香蕉", "橙子"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# 列表索引
print(fruits[0])      # 第一个元素: "苹果"
print(fruits[-1])     # 最后一个元素: "橙子"
print(fruits[1:3])    # 切片: ["香蕉", "橙子"]

# 列表方法
fruits.append("葡萄")      # 添加元素
fruits.insert(1, "草莓")   # 在指定位置插入
fruits.remove("苹果")      # 删除指定元素
popped = fruits.pop()      # 删除并返回最后一个元素
fruits.pop(0)              # 删除指定索引的元素

# 列表长度
print(len(fruits))

# 列表排序
nums = [3, 1, 4, 1, 5]
nums.sort()                # 升序排序: [1, 1, 3, 4, 5]
nums.sort(reverse=True)    # 降序排序: [5, 4, 3, 1, 1]

# 遍历列表
for fruit in fruits:
    print(fruit)

# 练习6：创建一个包含5个数字的列表，计算它们的和与平均值
# _______________________________________


# ========================================
# 第7节：字典 Dictionary (4分钟)
# ========================================

# 创建字典（键值对）
person = {
    "name": "小明",
    "age": 18,
    "city": "北京"
}

# 访问字典
print(person["name"])           # "小明"
print(person.get("age"))        # 18
print(person.get("job", "无"))  # "无"（键不存在时返回默认值）

# 修改字典
person["age"] = 19              # 修改值
person["job"] = "学生"          # 添加键值对
del person["city"]              # 删除键值对

# 字典方法
print(person.keys())            # 所有键
print(person.values())          # 所有值
print(person.items())           # 所有键值对

# 遍历字典
for key, value in person.items():
    print(f"{key}: {value}")

# 练习7：创建一个字典存储你的课程和成绩，计算平均分
# _______________________________________


# ========================================
# 第8节：条件语句 if (4分钟)
# ========================================

# if 语句
score = 85

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 逻辑条件
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("可以入场")
elif age < 18:
    print("未成年需要家长陪同")
else:
    print("需要购票")

# 三元表达式
status = "成年" if age >= 18 else "未成年"

# 练习8：编写程序判断一个数是正数、负数还是零
# _______________________________________


# ========================================
# 第9节：循环 Loops (5分钟)
# ========================================

# for 循环
for i in range(5):      # range(5) = 0, 1, 2, 3, 4
    print(f"第{i+1}次循环")

# 遍历列表
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(fruit)

# 使用 enumerate 获取索引
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# while 循环
count = 0
while count < 5:
    print(count)
    count += 1

# 循环控制
for i in range(10):
    if i == 3:
        continue    # 跳过本次循环
    if i == 7:
        break       # 退出循环
    print(i)        # 输出: 0, 1, 2, 4, 5, 6

# 练习9：使用循环打印1-100之间的所有偶数
# _______________________________________


# ========================================
# 第10节：函数 Functions (5分钟)
# ========================================

# 定义函数
def greet(name):
    """这是一个函数文档字符串"""
    return f"Hello, {name}!"

# 调用函数
message = greet("小明")
print(message)

# 带默认参数的函数
def introduce(name, age=18):
    return f"我叫{name}，今年{age}岁"

print(introduce("小红"))           # 使用默认年龄
print(introduce("小刚", 20))       # 指定年龄

# 多返回值
def calculate(a, b):
    return a + b, a - b

add, sub = calculate(10, 5)
print(f"和:{add}, 差:{sub}")

# 可变参数
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))  # 15

# 练习10：编写一个函数，判断一个数字是否为质数
# _______________________________________


# ========================================
# 第11节：文件操作 (3分钟)
# ========================================

# 写入文件
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Hello, Python!\n")
    f.write("这是第二行")

# 读取文件
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()      # 读取全部内容
    print(content)

# 逐行读取
with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())  # 去除换行符

# 追加内容
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("\n这是追加的内容")

# 练习11：创建一个文件，写入1-10的乘法表
# _______________________________________


# ========================================
# 第12节：异常处理 (2分钟)
# ========================================

# try-except 捕获异常
try:
    number = int(input("输入一个数字："))
    result = 10 / number
    print(f"结果：{result}")
except ValueError:
    print("请输入有效的数字！")
except ZeroDivisionError:
    print("不能除以零！")
except Exception as e:
    print(f"发生错误：{e}")

# 练习12：编写程序，处理除法运算中的各种错误
# _______________________________________


# ========================================
# 第13节：类和对象（面向对象基础，可选）
# ========================================

class Dog:
    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def bark(self):
        """方法"""
        return f"{self.name}说：汪汪！"

    def info(self):
        return f"名字：{self.name}，年龄：{self.age}岁"

# 创建对象
dog1 = Dog("旺财", 3)
dog2 = Dog("来福", 5)

print(dog1.bark())
print(dog2.info())


# ========================================
# 综合练习：猜数字游戏
# ========================================
"""
将以下代码保存为单独文件运行，
它是Python入门经典练习
"""

import random

def guess_number_game():
    """猜数字游戏"""
    secret = random.randint(1, 100)
    attempts = 0

    print("=== 猜数字游戏 ===")
    print("我想了一个1-100之间的数字，猜猜看？")

    while True:
        try:
            guess = int(input("输入你的猜测："))
            attempts += 1

            if guess == secret:
                print(f"恭喜你猜对了！答案就是{secret}")
                print(f"你用了{attempts}次")
                break
            elif guess < secret:
                print("太小了，再试一次")
            else:
                print("太大了，再试一次")

        except ValueError:
            print("请输入1-100之间的数字！")

# 取消注释运行游戏
# guess_number_game()


# ========================================
# 学习建议
# ========================================
"""
1. 每学完一节，先理解代码，自己写一遍
2. 完成每节后的练习题
3. 遇到问题使用 print() 调试
4. 进阶学习方向：
   - 虚拟环境（venv）
   - 第三方库（pip install）
   - 项目实战（爬虫、数据分析、Web开发）

推荐资源：
- 官方文档：https://docs.python.org/zh_CN/3/
- 在线练习：LeetCode、牛客网
- 项目练习：GitHub上的Python项目

下一步建议：
1. 完成100道Python基础题
2. 做一个小项目（如：待办事项应用）
3. 学习常用库：os, sys, datetime, json
4. 选择方向深入：Web/数据分析/Automation
"""

print("\n=== 教程结束 ===")
print("记住：最好的学习方式是多写代码！")
