# -*- coding: utf-8 -*-
"""
网络爬虫练习题 - 带答案
========================

使用说明：
1. 每道练习题都有一个练习函数和一个答案函数
2. 建议先自己完成练习函数中的 TODO 部分
3. 完成后可以查看答案函数验证

运行方法：
python web_crawler_exercises.py
"""

print("=" * 60)
print("📝 网络爬虫练习题")
print("=" * 60)


# ============================================================
# 练习1：发送HTTP请求
# ============================================================
"""
练习1：发送HTTP请求

目标：学会使用 requests 库发送HTTP请求

任务：
1. 发送GET请求到 https://httpbin.org/get
2. 打印状态码
3. 打印响应内容的前100个字符
"""

def exercise_1_request():
    """
    练习1：发送HTTP请求

    TODO: 完成下面的代码
    """
    import requests

    print("\n" + "=" * 40)
    print("练习1：发送HTTP请求")
    print("=" * 40)

    # TODO: 设置URL
    url = "https://httpbin.org/get"

    # TODO: 发送GET请求
    response = requests.get(url)

    # TODO: 打印状态码
    print(f"状态码: {response.status_code}")

    # TODO: 打印响应内容的前100个字符
    print(f"响应内容: {response.text[:100]}...")


def answer_1_request():
    """
    练习1答案
    """
    import requests

    print("\n" + "=" * 40)
    print("练习1答案")
    print("=" * 40)

    # 设置URL
    url = "https://httpbin.org/get"

    # 发送GET请求
    response = requests.get(url)

    # 打印状态码
    print(f"状态码: {response.status_code}")

    # 打印响应内容的前100个字符
    print(f"响应内容: {response.text[:100]}...")

    print("\n✅ 答案说明：")
    print("1. 使用 requests.get(url) 发送GET请求")
    print("2. response.status_code 获取状态码（200表示成功）")
    print("3. response.text 获取响应内容（字符串格式）")


# ============================================================
# 练习2：带参数的请求
# ============================================================
"""
练习2：带参数的请求

目标：学会在请求中传递参数

任务：
1. 发送带参数的GET请求
2. 参数：search="python", page=1
3. 打印实际请求的URL
"""

def exercise_2_params():
    """
    练习2：带参数的请求

    TODO: 完成下面的代码
    """
    import requests

    print("\n" + "=" * 40)
    print("练习2：带参数的请求")
    print("=" * 40)

    # TODO: 设置URL和参数
    url = "https://httpbin.org/get"
    params = {"search": "python", "page": 1}

    # TODO: 发送带参数的请求
    response = requests.get(url, params=params)

    # TODO: 打印实际请求的URL
    print(f"实际请求URL: {response.url}")


def answer_2_params():
    """
    练习2答案
    """
    import requests

    print("\n" + "=" * 40)
    print("练习2答案")
    print("=" * 40)

    url = "https://httpbin.org/get"
    params = {"search": "python", "page": 1}

    # 发送带参数的请求
    response = requests.get(url, params=params)

    # 打印实际请求的URL
    print(f"实际请求URL: {response.url}")

    print("\n✅ 答案说明：")
    print("1. 使用 params 参数传递URL参数")
    print("2. requests 会自动将参数拼接到URL中")
    print("3. response.url 可以查看实际请求的完整URL")


# ============================================================
# 练习3：解析HTML
# ============================================================
"""
练习3：解析HTML

目标：学会使用 BeautifulSoup 解析HTML

任务：
给定HTML代码，提取：
1. 网页标题
2. 所有段落内容
3. 第一个链接的地址
"""

def exercise_3_parse():
    """
    练习3：解析HTML

    TODO: 完成下面的代码
    """
    from bs4 import BeautifulSoup

    print("\n" + "=" * 40)
    print("练习3：解析HTML")
    print("=" * 40)

    html = """
    <html>
        <head><title>我的网页</title></head>
        <body>
            <h1>欢迎</h1>
            <p>这是第一段。</p>
            <p>这是第二段。</p>
            <a href="https://example.com">示例链接</a>
            <a href="https://python.org">Python官网</a>
        </body>
    </html>
    """

    # TODO: 创建BeautifulSoup对象
    soup = BeautifulSoup(html, 'html.parser')

    # TODO: 提取并打印网页标题
    title = soup.title.text
    print(f"网页标题: {title}")

    # TODO: 提取并打印所有段落
    paragraphs = soup.find_all('p')
    print(f"段落内容:")
    for p in paragraphs:
        print(f"  - {p.text}")

    # TODO: 提取并打印第一个链接的地址
    first_link = soup.find('a')
    print(f"第一个链接地址: {first_link['href']}")


def answer_3_parse():
    """
    练习3答案
    """
    from bs4 import BeautifulSoup

    print("\n" + "=" * 40)
    print("练习3答案")
    print("=" * 40)

    html = """
    <html>
        <head><title>我的网页</title></head>
        <body>
            <h1>欢迎</h1>
            <p>这是第一段。</p>
            <p>这是第二段。</p>
            <a href="https://example.com">示例链接</a>
            <a href="https://python.org">Python官网</a>
        </body>
    </html>
    """

    soup = BeautifulSoup(html, 'html.parser')

    # 提取网页标题
    title = soup.title.text
    print(f"网页标题: {title}")

    # 提取所有段落
    paragraphs = soup.find_all('p')
    print(f"段落内容:")
    for p in paragraphs:
        print(f"  - {p.text}")

    # 提取第一个链接的地址
    first_link = soup.find('a')
    print(f"第一个链接地址: {first_link['href']}")

    print("\n✅ 答案说明：")
    print("1. BeautifulSoup(html, 'html.parser') 创建解析对象")
    print("2. soup.title.text 获取标题文本")
    print("3. soup.find_all('p') 获取所有<p>标签")
    print("4. soup.find('a') 获取第一个<a>标签")
    print("5. element['attr'] 获取属性值")


# ============================================================
# 练习4：CSS选择器
# ============================================================
"""
练习4：CSS选择器

目标：学会使用CSS选择器提取数据

任务：
给定HTML代码，使用CSS选择器提取：
1. class为"highlight"的元素内容
2. id为"main"的元素内的所有列表项
3. 所有链接的href属性
"""

def exercise_4_selector():
    """
    练习4：CSS选择器

    TODO: 完成下面的代码
    """
    from bs4 import BeautifulSoup

    print("\n" + "=" * 40)
    print("练习4：CSS选择器")
    print("=" * 40)

    html = """
    <div id="main">
        <h1 class="highlight">重要标题</h1>
        <p class="highlight">重要内容</p>
        <ul>
            <li>项目1</li>
            <li>项目2</li>
            <li>项目3</li>
        </ul>
        <nav>
            <a href="/home">首页</a>
            <a href="/about">关于</a>
        </nav>
    </div>
    """

    # TODO: 创建BeautifulSoup对象
    soup = BeautifulSoup(html, 'html.parser')

    # TODO: 使用CSS选择器提取class为"highlight"的元素
    highlights = soup.select('.highlight')
    print("class为highlight的元素:")
    for el in highlights:
        print(f"  - {el.text}")

    # TODO: 使用CSS选择器提取id为"main"内的所有li
    items = soup.select('#main li')
    print("\nid为main内的列表项:")
    for item in items:
        print(f"  - {item.text}")

    # TODO: 使用CSS选择器提取所有链接的href
    links = soup.select('a')
    print("\n所有链接:")
    for link in links:
        print(f"  - {link.text}: {link['href']}")


def answer_4_selector():
    """
    练习4答案
    """
    from bs4 import BeautifulSoup

    print("\n" + "=" * 40)
    print("练习4答案")
    print("=" * 40)

    html = """
    <div id="main">
        <h1 class="highlight">重要标题</h1>
        <p class="highlight">重要内容</p>
        <ul>
            <li>项目1</li>
            <li>项目2</li>
            <li>项目3</li>
        </ul>
        <nav>
            <a href="/home">首页</a>
            <a href="/about">关于</a>
        </nav>
    </div>
    """

    soup = BeautifulSoup(html, 'html.parser')

    # 使用CSS选择器提取class为"highlight"的元素
    highlights = soup.select('.highlight')
    print("class为highlight的元素:")
    for el in highlights:
        print(f"  - {el.text}")

    # 使用CSS选择器提取id为"main"内的所有li
    items = soup.select('#main li')
    print("\nid为main内的列表项:")
    for item in items:
        print(f"  - {item.text}")

    # 使用CSS选择器提取所有链接的href
    links = soup.select('a')
    print("\n所有链接:")
    for link in links:
        print(f"  - {link.text}: {link['href']}")

    print("\n✅ 答案说明：")
    print("1. soup.select('.class') - 按class选择")
    print("2. soup.select('#id') - 按id选择")
    print("3. soup.select('#id li') - 选择id内所有li")
    print("4. CSS选择器更灵活，支持组合选择")


# ============================================================
# 练习5：保存数据到CSV
# ============================================================
"""
练习5：保存数据到CSV

目标：学会将数据保存为CSV文件

任务：
将以下学生数据保存到CSV文件：
- 表头：姓名, 年龄, 班级
- 数据：张三, 14, 初二1班
        李四, 15, 初二2班
        王五, 14, 初二1班
"""

def exercise_5_csv():
    """
    练习5：保存数据到CSV

    TODO: 完成下面的代码
    """
    import csv
    import os

    print("\n" + "=" * 40)
    print("练习5：保存数据到CSV")
    print("=" * 40)

    # 数据
    students = [
        {"name": "张三", "age": 14, "class": "初二1班"},
        {"name": "李四", "age": 15, "class": "初二2班"},
        {"name": "王五", "age": 14, "class": "初二1班"},
    ]

    # 保存路径
    save_dir = "/mnt/c/dev/python/qqstudy/web_crawler/data"
    os.makedirs(save_dir, exist_ok=True)
    filepath = os.path.join(save_dir, "students.csv")

    # TODO: 将数据写入CSV文件
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'age', 'class'])
        writer.writeheader()
        writer.writerows(students)

    print(f"✅ 数据已保存到: {filepath}")


def answer_5_csv():
    """
    练习5答案
    """
    import csv
    import os

    print("\n" + "=" * 40)
    print("练习5答案")
    print("=" * 40)

    students = [
        {"name": "张三", "age": 14, "class": "初二1班"},
        {"name": "李四", "age": 15, "class": "初二2班"},
        {"name": "王五", "age": 14, "class": "初二1班"},
    ]

    save_dir = "/mnt/c/dev/python/qqstudy/web_crawler/data"
    os.makedirs(save_dir, exist_ok=True)
    filepath = os.path.join(save_dir, "students_answer.csv")

    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        # 创建字典写入器
        writer = csv.DictWriter(f, fieldnames=['name', 'age', 'class'])

        # 写入表头
        writer.writeheader()

        # 写入数据
        writer.writerows(students)

    print(f"✅ 数据已保存到: {filepath}")

    # 读取并显示内容
    with open(filepath, 'r', encoding='utf-8') as f:
        print("\n文件内容:")
        print(f.read())

    print("✅ 答案说明：")
    print("1. csv.DictWriter 可以直接写入字典列表")
    print("2. fieldnames 指定字段顺序")
    print("3. writeheader() 写入表头")
    print("4. writerows() 写入多行数据")


# ============================================================
# 练习6：保存数据到JSON
# ============================================================
"""
练习6：保存数据到JSON

目标：学会将数据保存为JSON文件

任务：
将书籍数据保存到JSON文件，要求：
1. 格式化输出（缩进4空格）
2. 中文正常显示
"""

def exercise_6_json():
    """
    练习6：保存数据到JSON

    TODO: 完成下面的代码
    """
    import json
    import os

    print("\n" + "=" * 40)
    print("练习6：保存数据到JSON")
    print("=" * 40)

    # 数据
    books = {
        "category": "编程",
        "books": [
            {"title": "Python入门", "price": 59},
            {"title": "爬虫实战", "price": 79},
        ]
    }

    # 保存路径
    save_dir = "/mnt/c/dev/python/qqstudy/web_crawler/data"
    os.makedirs(save_dir, exist_ok=True)
    filepath = os.path.join(save_dir, "books.json")

    # TODO: 将数据写入JSON文件
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

    print(f"✅ 数据已保存到: {filepath}")


def answer_6_json():
    """
    练习6答案
    """
    import json
    import os

    print("\n" + "=" * 40)
    print("练习6答案")
    print("=" * 40)

    books = {
        "category": "编程",
        "books": [
            {"title": "Python入门", "price": 59},
            {"title": "爬虫实战", "price": 79},
        ]
    }

    save_dir = "/mnt/c/dev/python/qqstudy/web_crawler/data"
    os.makedirs(save_dir, exist_ok=True)
    filepath = os.path.join(save_dir, "books_answer.json")

    # 写入JSON文件
    with open(filepath, 'w', encoding='utf-8') as f:
        # ensure_ascii=False 保证中文正常显示
        # indent=4 格式化输出
        json.dump(books, f, ensure_ascii=False, indent=4)

    print(f"✅ 数据已保存到: {filepath}")

    # 读取并显示内容
    with open(filepath, 'r', encoding='utf-8') as f:
        print("\n文件内容:")
        print(f.read())

    print("\n✅ 答案说明：")
    print("1. json.dump(data, file) 将数据写入JSON文件")
    print("2. ensure_ascii=False 保证中文正常显示")
    print("3. indent=4 格式化输出，便于阅读")


# ============================================================
# 练习7：完整爬虫
# ============================================================
"""
练习7：完整爬虫

目标：综合运用所学知识完成一个简单爬虫

任务：
爬取模拟的HTML页面，提取商品信息并保存
"""

def exercise_7_complete():
    """
    练习7：完整爬虫

    TODO: 完成下面的代码
    """
    from bs4 import BeautifulSoup
    import json
    import os

    print("\n" + "=" * 40)
    print("练习7：完整爬虫")
    print("=" * 40)

    # 模拟的网页HTML
    html = """
    <div class="products">
        <div class="product">
            <h2 class="title">Python编程书</h2>
            <span class="price">59.00</span>
            <p class="desc">适合初学者</p>
        </div>
        <div class="product">
            <h2 class="title">数据结构</h2>
            <span class="price">49.00</span>
            <p class="desc">计算机基础</p>
        </div>
        <div class="product">
            <h2 class="title">网络爬虫实战</h2>
            <span class="price">69.00</span>
            <p class="desc">进阶教程</p>
        </div>
    </div>
    """

    # TODO: 1. 创建BeautifulSoup对象
    soup = BeautifulSoup(html, 'html.parser')

    # TODO: 2. 找到所有商品
    products = soup.find_all('div', class_='product')

    # TODO: 3. 提取每个商品的信息
    all_products = []
    for product in products:
        title = product.find('h2', class_='title').text
        price = product.find('span', class_='price').text
        desc = product.find('p', class_='desc').text

        product_data = {
            'title': title,
            'price': price,
            'desc': desc
        }
        all_products.append(product_data)

        print(f"提取: {title} - {price}元")

    # TODO: 4. 保存到JSON文件
    save_dir = "/mnt/c/dev/python/qqstudy/web_crawler/data"
    os.makedirs(save_dir, exist_ok=True)
    filepath = os.path.join(save_dir, "products.json")

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(all_products, f, ensure_ascii=False, indent=4)

    print(f"\n✅ 共提取 {len(all_products)} 个商品")
    print(f"✅ 数据已保存到: {filepath}")


def answer_7_complete():
    """
    练习7答案
    """
    from bs4 import BeautifulSoup
    import json
    import os

    print("\n" + "=" * 40)
    print("练习7答案")
    print("=" * 40)

    html = """
    <div class="products">
        <div class="product">
            <h2 class="title">Python编程书</h2>
            <span class="price">59.00</span>
            <p class="desc">适合初学者</p>
        </div>
        <div class="product">
            <h2 class="title">数据结构</h2>
            <span class="price">49.00</span>
            <p class="desc">计算机基础</p>
        </div>
        <div class="product">
            <h2 class="title">网络爬虫实战</h2>
            <span class="price">69.00</span>
            <p class="desc">进阶教程</p>
        </div>
    </div>
    """

    # 1. 创建BeautifulSoup对象
    soup = BeautifulSoup(html, 'html.parser')

    # 2. 找到所有商品
    products = soup.find_all('div', class_='product')

    # 3. 提取每个商品的信息
    all_products = []
    for product in products:
        # 提取标题
        title = product.find('h2', class_='title').text
        # 提取价格
        price = product.find('span', class_='price').text
        # 提取描述
        desc = product.find('p', class_='desc').text

        product_data = {
            'title': title,
            'price': price,
            'desc': desc
        }
        all_products.append(product_data)

        print(f"提取: {title} - {price}元")

    # 4. 保存到JSON文件
    save_dir = "/mnt/c/dev/python/qqstudy/web_crawler/data"
    os.makedirs(save_dir, exist_ok=True)
    filepath = os.path.join(save_dir, "products_answer.json")

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(all_products, f, ensure_ascii=False, indent=4)

    print(f"\n✅ 共提取 {len(all_products)} 个商品")
    print(f"✅ 数据已保存到: {filepath}")

    print("\n✅ 答案说明：")
    print("1. 创建BeautifulSoup对象解析HTML")
    print("2. find_all() 找到所有商品容器")
    print("3. 循环每个商品，用find()提取具体信息")
    print("4. json.dump() 保存数据到文件")


# ============================================================
# 练习8：翻页爬取（模拟）
# ============================================================
"""
练习8：翻页爬取

目标：学会处理多页数据

任务：
模拟爬取多页数据，提取所有页面的信息
"""

def exercise_8_pagination():
    """
    练习8：翻页爬取（模拟）

    TODO: 完成下面的代码
    """
    from bs4 import BeautifulSoup
    import json
    import os
    import time
    import random

    print("\n" + "=" * 40)
    print("练习8：翻页爬取（模拟）")
    print("=" * 40)

    # 模拟3页数据
    pages = [
        """<div class="items"><span class="item">第1页-项目A</span></div>""",
        """<div class="items"><span class="item">第2页-项目B</span></div>""",
        """<div class="items"><span class="item">第3页-项目C</span></div>""",
    ]

    all_items = []

    # TODO: 循环处理每一页
    for i, page_html in enumerate(pages, 1):
        print(f"处理第 {i} 页...")

        # TODO: 解析当前页
        soup = BeautifulSoup(page_html, 'html.parser')
        items = soup.find_all('span', class_='item')

        # TODO: 提取数据
        for item in items:
            all_items.append(item.text)
            print(f"  提取: {item.text}")

        # 模拟延迟（实际爬虫需要）
        # time.sleep(random.uniform(1, 2))

    print(f"\n✅ 共提取 {len(all_items)} 条数据")
    print(f"所有数据: {all_items}")


def answer_8_pagination():
    """
    练习8答案
    """
    from bs4 import BeautifulSoup
    import json
    import os
    import time
    import random

    print("\n" + "=" * 40)
    print("练习8答案")
    print("=" * 40)

    # 模拟3页数据（实际中是通过请求不同URL获取的）
    pages = [
        """<div class="items"><span class="item">第1页-项目A</span></div>""",
        """<div class="items"><span class="item">第2页-项目B</span></div>""",
        """<div class="items"><span class="item">第3页-项目C</span></div>""",
    ]

    all_items = []

    # 循环处理每一页
    for i, page_html in enumerate(pages, 1):
        print(f"处理第 {i} 页...")

        # 解析当前页
        soup = BeautifulSoup(page_html, 'html.parser')

        # 提取数据
        items = soup.find_all('span', class_='item')
        for item in items:
            all_items.append(item.text)
            print(f"  提取: {item.text}")

        # 模拟延迟（实际爬虫中必须有）
        delay = random.uniform(0.1, 0.3)  # 演示用较短延迟
        time.sleep(delay)

    print(f"\n✅ 共提取 {len(all_items)} 条数据")
    print(f"所有数据: {all_items}")

    print("\n✅ 答案说明：")
    print("1. 使用循环处理多页")
    print("2. 每页都要解析和提取数据")
    print("3. 将所有数据合并到一起")
    print("4. 实际爬虫中要添加延迟，避免请求过快")


# ============================================================
# 运行所有练习
# ============================================================
def run_all_exercises():
    """运行所有练习题"""
    print("\n" + "📝" * 20)
    print("运行所有练习题...")
    print("📝" * 20)

    exercise_1_request()
    exercise_2_params()
    exercise_3_parse()
    exercise_4_selector()
    exercise_5_csv()
    exercise_6_json()
    exercise_7_complete()
    exercise_8_pagination()

    print("\n" + "=" * 60)
    print("🎉 所有练习完成！")
    print("=" * 60)


def run_all_answers():
    """运行所有答案"""
    print("\n" + "📖" * 20)
    print("运行所有答案...")
    print("📖" * 20)

    answer_1_request()
    answer_2_params()
    answer_3_parse()
    answer_4_selector()
    answer_5_csv()
    answer_6_json()
    answer_7_complete()
    answer_8_pagination()

    print("\n" + "=" * 60)
    print("🎉 所有答案展示完成！")
    print("=" * 60)


# ============================================================
# 主程序入口
# ============================================================
if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║              📝 网络爬虫练习题  📝                       ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

【练习列表】
1. 发送HTTP请求
2. 带参数的请求
3. 解析HTML
4. CSS选择器
5. 保存数据到CSV
6. 保存数据到JSON
7. 完整爬虫
8. 翻页爬取

【使用方法】
1. 运行练习题：exercise_1_request()
2. 查看答案：answer_1_request()
3. 运行所有练习：run_all_exercises()
4. 查看所有答案：run_all_answers()

【建议】
- 先自己完成练习，再看答案
- 每个练习都有详细说明
    """)

    # 提示用户输入
    print("\n请选择操作：")
    print("1. 运行所有练习")
    print("2. 查看所有答案")
    print("3. 运行单个练习（输入练习编号1-8）")
    print("4. 查看单个答案（输入答案编号1-8）")
    print("5. 退出")

    choice = input("\n请输入选项: ").strip()

    if choice == '1':
        run_all_exercises()
    elif choice == '2':
        run_all_answers()
    elif choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
        # 运行单个练习或答案
        num = choice
        if input("查看答案？(y/n): ").lower() == 'y':
            exec(f"answer_{num}_*" + "{" + "*"[0] + "}" + "()")
        else:
            exec(f"exercise_{num}_*" + "{" + "*"[0] + "}" + "()")
    else:
        print("再见！继续加油学习！")
