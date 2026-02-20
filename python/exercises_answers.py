# ========================================
# Python 快速入门 - 练习答案
# ========================================
# 建议先自己做练习，不会时再参考答案

# ========================================
# 练习1：打印你自己的名字
# ========================================
print("张三")
# 或者
name = "张三"
print(name)


# ========================================
# 练习2：创建变量存储你的信息
# ========================================
my_name = "张三"
my_age = 25
my_height = 1.75

print(f"姓名：{my_name}")
print(f"年龄：{my_age}")
print(f"身高：{my_height}")


# ========================================
# 练习3：字符串方法练习
# ========================================
text = "  Hello Python Programming  "
print(text.upper())        # "  HELLO PYTHON PROGRAMMING  "
print(text.lower())        # "  hello python programming  "
print(text.strip())        # "Hello Python Programming"
print(text.split())        # ['Hello', 'Python', 'Programming']
print(text.count("Python")) # 1
print(text.replace("Python", "世界"))  # "  Hello 世界 Programming  "


# ========================================
# 练习4：计算圆的面积
# ========================================
radius = 5
pi = 3.14159
area = pi * radius ** 2
print(f"半径为{radius}的圆面积是：{area}")


# ========================================
# 练习5：询问用户姓名和年龄
# ========================================
# 取消下面的注释来运行
"""
name = input("请输入你的名字：")
age = int(input("请输入你的年龄："))
print(f"你好，{name}！你今年{age}岁。")
"""


# ========================================
# 练习6：列表求和与平均值
# ========================================
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
average = total / len(numbers)
print(f"和：{total}")
print(f"平均值：{average}")

# 手动计算方式
total_manual = 0
for num in numbers:
    total_manual += num
print(f"手动计算的和：{total_manual}")


# ========================================
# 练习7：课程成绩字典
# ========================================
courses = {
    "语文": 85,
    "数学": 92,
    "英语": 88,
    "物理": 90,
    "化学": 87
}

# 计算平均分
average_score = sum(courses.values()) / len(courses)
print(f"平均分：{average_score}")

# 打印每门课的成绩
for course, score in courses.items():
    print(f"{course}：{score}分")


# ========================================
# 练习8：判断正负数
# ========================================
def check_number(num):
    if num > 0:
        print(f"{num}是正数")
    elif num < 0:
        print(f"{num}是负数")
    else:
        print(f"{num}是零")

# 测试
check_number(10)   # 正数
check_number(-5)   # 负数
check_number(0)    # 零


# ========================================
# 练习9：打印1-100的偶数
# ========================================
# 方法一：使用if判断
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

# 方法二：使用step（更优雅）
for i in range(2, 101, 2):
    print(i)

# 方法三：列表推导式（进阶）
evens = [i for i in range(1, 101) if i % 2 == 0]
print(evens)


# ========================================
# 练习10：判断质数
# ========================================
def is_prime(n):
    """判断一个数字是否为质数"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # 只需要检查到平方根
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# 测试
test_numbers = [2, 3, 4, 5, 7, 11, 15, 17, 20, 23]
for num in test_numbers:
    if is_prime(num):
        print(f"{num}是质数")
    else:
        print(f"{num}不是质数")


# ========================================
# 练习11：乘法表文件
# ========================================
def create_multiplication_table():
    """创建1-10乘法表文件"""
    with open("multiplication_table.txt", "w", encoding="utf-8") as f:
        for i in range(1, 11):
            for j in range(1, 11):
                f.write(f"{i}×{j}={i*j:2d}  ")
            f.write("\n")
    print("乘法表已创建！")

# 取消注释运行
# create_multiplication_table()


# ========================================
# 练习12：除法异常处理
# ========================================
def safe_division():
    """安全的除法计算器"""
    while True:
        try:
            num1 = float(input("输入第一个数字："))
            num2 = float(input("输入第二个数字："))

            if num2 == 0:
                print("错误：除数不能为零！")
                continue

            result = num1 / num2
            print(f"{num1} ÷ {num2} = {result}")
            break

        except ValueError:
            print("错误：请输入有效的数字！")
        except KeyboardInterrupt:
            print("\n程序已中断")
            break
        except Exception as e:
            print(f"未知错误：{e}")

# 取消注释运行
# safe_division()


# ========================================
# 额外练习：实用小程序集合
# ========================================

# 1. 温度转换器
def celsius_to_fahrenheit(celsius):
    """摄氏度转华氏度"""
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """华氏度转摄氏度"""
    return (fahrenheit - 32) * 5/9

print(f"25°C = {celsius_to_fahrenheit(25)}°F")
print(f"77°F = {fahrenheit_to_celsius(77)}°C")


# 2. 简单计算器
def calculator(a, b, operation):
    """简单计算器"""
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "错误：除数不能为零"
        return a / b
    else:
        return "未知操作"

print(calculator(10, 5, "+"))  # 15
print(calculator(10, 5, "/"))  # 2.0


# 3. 密码强度检查器
def check_password_strength(password):
    """检查密码强度"""
    if len(password) < 8:
        return "弱：密码长度至少8位"

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)

    if has_upper and has_lower and has_digit:
        return "强：密码包含大小写字母和数字"
    elif has_upper or has_lower or has_digit:
        return "中：建议混合使用大小写字母和数字"
    else:
        return "弱：密码过于简单"

print(check_password_strength("abc"))          # 弱
print(check_password_strength("abcdefg"))      # 弱
print(check_password_strength("Abc123"))       # 中
print(check_password_strength("Abcdefg123"))   # 强


# 4. 单词计数器
def word_counter(text):
    """统计文本中的单词数"""
    words = text.split()
    word_count = len(words)
    char_count = len(text.replace(" ", ""))
    return word_count, char_count

text = "Hello Python World"
words, chars = word_counter(text)
print(f"单词数：{words}")    # 3
print(f"字符数：{chars}")    # 15


# 5. 列表去重
def remove_duplicates(lst):
    """去除列表中的重复元素"""
    return list(set(lst))

numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
print(remove_duplicates(numbers))  # [1, 2, 3, 4, 5]
# 注意：set不保证顺序，如需保持顺序：
def remove_duplicates_ordered(lst):
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return seen

print(remove_duplicates_ordered(numbers))  # [1, 2, 3, 4, 5]


# ========================================
# 学习建议
# ========================================
"""
进阶练习方向：
1. 做LeetCode简单题（前50道）
2. 完成"Python 100题"练习
3. 尝试小项目：
   - 简易记事本
   - 单位转换器
   - 成绩管理系统
   - 文件批量重命名工具

推荐学习顺序：
1. 完成本教程所有练习 ✓
2. 学习Python标准库（os, sys, datetime, json, csv）
3. 选择方向：
   - 数据分析：学习pandas, numpy, matplotlib
   - Web开发：学习Flask或Django
   - 自动化：学习selenium, requests
   - 爬虫：学习beautifulsoup, scrapy
"""

print("\n=== 所有练习答案 ===")
print("建议先自己做，再对照答案修改")
print("每道题都有多种解法，尝试找到最优雅的方式")
