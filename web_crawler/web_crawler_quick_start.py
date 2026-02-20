# -*- coding: utf-8 -*-
"""
网络爬虫速成教程 - 适合初中生学习
=====================================

作者: Python学习教程
适合人群: 初中生及编程初学者
学习时间: 约2-3小时

什么是网络爬虫？
----------------
网络爬虫（Web Crawler）是一种自动浏览网页的程序。
它像一只小蜘蛛，在互联网的"网"上爬行，自动访问网页并提取你需要的信息。

⚠️ 重要提醒：爬虫要合法合规！
---------------------------
1. 遵守网站的 robots.txt 规则
2. 不要频繁请求，给服务器造成压力
3. 不要爬取隐私信息和付费内容
4. 学习目的使用，不要用于商业

让我们开始吧！
"""

print("=" * 60)
print("🚀 欢迎来到网络爬虫速成教程！")
print("=" * 60)


# ============================================================
# 第1节：什么是网络爬虫？
# ============================================================
"""
📖 第1节：什么是网络爬虫？

【概念】
网络爬虫（也叫网络蜘蛛、网络机器人）是一种自动获取网页内容的程序。

【工作原理】
1. 发送请求：向网站服务器发送HTTP请求
2. 获取响应：服务器返回网页内容（HTML代码）
3. 解析内容：从HTML中提取需要的数据
4. 保存数据：把数据存到文件或数据库

【类比理解】
想象你在图书馆找资料：
- 你 = 爬虫程序
- 图书馆 = 互联网
- 书架上的书 = 网页
- 翻书找信息 = 解析HTML
- 抄写笔记 = 保存数据

【法律与道德】
✅ 可以做的：
   - 爬取公开的、允许爬取的数据
   - 遵守网站的使用条款
   - 用于学习研究

❌ 不能做的：
   - 爬取个人隐私信息
   - 绕过付费墙爬取付费内容
   - 频繁请求导致服务器瘫痪
   - 出售爬取的数据

【robots.txt 是什么？】
robots.txt 是网站告诉爬虫哪些页面可以爬、哪些不能爬的文件。
例如：https://www.baidu.com/robots.txt
"""

def section_1_what_is_crawler():
    """
    第1节演示：了解爬虫的基本概念

    这个函数展示了爬虫的基本工作流程

    参数说明：
        无参数

    调用示例：
        section_1_what_is_crawler()
    """
    print("\n" + "=" * 60)
    print("📖 第1节：什么是网络爬虫？")
    print("=" * 60)

    print("""
【爬虫的工作流程】

    ┌─────────────┐
    │  1. 发送请求  │  → 向网站服务器发送HTTP请求
    └──────┬──────┘
           ↓
    ┌─────────────┐
    │  2. 获取响应  │  → 服务器返回HTML代码
    └──────┬──────┘
           ↓
    ┌─────────────┐
    │  3. 解析内容  │  → 从HTML中提取数据
    └──────┬──────┘
           ↓
    ┌─────────────┐
    │  4. 保存数据  │  → 存入文件或数据库
    └─────────────┘

【重要提醒】
- 爬虫前先看看网站的 robots.txt
- 设置请求间隔，不要给服务器造成压力
- 尊重版权，不要滥用爬取的数据
    """)


# ============================================================
# 第1节调用示例
# ============================================================
def example_section_1():
    """
    第1节调用示例：演示如何调用 section_1_what_is_crawler()

    这个示例展示了如何运行第1节的内容
    """
    # 直接调用函数即可
    section_1_what_is_crawler()

    # 也可以这样理解：
    # section_1_what_is_crawler  # 这是函数名（不要加括号）
    # section_1_what_is_crawler()  # 这是调用函数（要加括号）
    print("\n提示：section_1 不需要传参数，直接调用即可！")


# ============================================================
# 第2节：HTTP 请求基础
# ============================================================
"""
📖 第2节：HTTP 请求基础

【什么是HTTP？】
HTTP（超文本传输协议）是浏览器和服务器之间通信的"语言"。

【requests 库】
requests 是 Python 最流行的 HTTP 请求库，非常简单易用。

安装方法：
pip install requests

【常用方法】
- requests.get(url)       # 获取网页
- requests.post(url)      # 提交表单
- response.status_code    # 状态码
- response.text           # 网页内容（字符串）
- response.content        # 网页内容（字节）

【常见状态码】
- 200: 成功
- 404: 页面不存在
- 403: 禁止访问
- 500: 服务器错误
"""

def section_2_http_basics():
    """
    第2节演示：学习HTTP请求基础

    这个函数演示如何使用 requests 库发送HTTP请求

    参数说明：
        无参数

    调用示例：
        section_2_http_basics()
    """
    print("\n" + "=" * 60)
    print("📖 第2节：HTTP 请求基础")
    print("=" * 60)

    # 导入 requests 库
    import requests

    # 示例网站：httpbin.org 是一个专门用于测试HTTP请求的网站
    print("\n【示例1】发送GET请求")
    print("-" * 40)

    # 发送GET请求
    url = "https://httpbin.org/get"
    print(f"正在请求: {url}")

    response = requests.get(url)

    # 查看状态码
    print(f"状态码: {response.status_code}")

    # 状态码含义
    status_meanings = {
        200: "成功！请求已完成",
        404: "页面不存在",
        403: "禁止访问",
        500: "服务器内部错误"
    }
    print(f"状态码含义: {status_meanings.get(response.status_code, '未知状态')}")

    # 查看响应内容（前200个字符）
    print(f"响应内容（前200字符）: {response.text[:200]}...")

    print("\n【示例2】带参数的GET请求")
    print("-" * 40)

    # 很多网站需要传递参数，比如搜索
    # 例如：https://example.com/search?q=python
    params = {
        "q": "python爬虫",
        "page": 1
    }

    response = requests.get("https://httpbin.org/get", params=params)
    print(f"实际请求URL: {response.url}")

    print("\n【示例3】添加请求头")
    print("-" * 40)

    # 请求头可以告诉服务器你是谁
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    response = requests.get("https://httpbin.org/get", headers=headers)
    print(f"状态码: {response.status_code}")

    # 解析JSON响应
    data = response.json()
    print(f"服务器收到的User-Agent: {data['headers']['User-Agent']}")


def send_request(url, params=None, headers=None, timeout=10):
    """
    发送HTTP请求的通用函数

    这是一个封装好的请求函数，带有错误处理

    参数说明：
        url (str): 要请求的网址
        params (dict): URL参数，如 {"q": "python", "page": 1}
        headers (dict): 请求头，如 {"User-Agent": "..."}
        timeout (int): 超时时间（秒），默认10秒

    返回值：
        Response对象，如果失败返回None

    调用示例：
        # 简单请求
        response = send_request("https://httpbin.org/get")

        # 带参数请求
        response = send_request(
            "https://httpbin.org/get",
            params={"q": "python"},
            headers={"User-Agent": "MyCrawler/1.0"}
        )
    """
    import requests

    try:
        response = requests.get(url, params=params, headers=headers, timeout=timeout)

        # 检查状态码
        if response.status_code == 200:
            return response
        elif response.status_code == 404:
            print(f"❌ 错误：页面不存在 (404)")
        elif response.status_code == 403:
            print(f"❌ 错误：禁止访问 (403)，可能需要设置User-Agent")
        else:
            print(f"❌ 错误：状态码 {response.status_code}")
        return None

    except requests.exceptions.Timeout:
        print(f"❌ 错误：请求超时（超过{timeout}秒）")
        return None
    except requests.exceptions.ConnectionError:
        print(f"❌ 错误：网络连接失败，请检查网络")
        return None
    except Exception as e:
        print(f"❌ 错误：{e}")
        return None


# ============================================================
# 第3节：解析 HTML
# ============================================================
"""
📖 第3节：解析 HTML

【什么是HTML？】
HTML（超文本标记语言）是网页的"骨架"，用来定义网页的结构。

【HTML基本结构】
<html>
    <head>
        <title>网页标题</title>
    </head>
    <body>
        <h1>这是一级标题</h1>
        <p>这是一个段落</p>
        <a href="https://example.com">这是一个链接</a>
        <div class="container">
            <span id="price">99元</span>
        </div>
    </body>
</html>

【BeautifulSoup 库】
BeautifulSoup 是最流行的HTML解析库，可以轻松提取网页内容。

安装方法：
pip install beautifulsoup4

【常用方法】
- soup.find('tag')          # 找第一个标签
- soup.find_all('tag')      # 找所有标签
- soup.select('selector')   # CSS选择器
- element.text              # 获取文本内容
- element['attr']           # 获取属性值
"""

def section_3_parse_html():
    """
    第3节演示：学习HTML解析

    这个函数演示如何使用 BeautifulSoup 解析HTML

    参数说明：
        无参数

    调用示例：
        section_3_parse_html()
    """
    print("\n" + "=" * 60)
    print("📖 第3节：解析 HTML")
    print("=" * 60)

    from bs4 import BeautifulSoup

    # 示例HTML代码（模拟一个简单的网页）
    html = """
    <html>
        <head>
            <title>我的第一个网页</title>
        </head>
        <body>
            <h1 class="main-title">欢迎学习爬虫</h1>
            <div class="content">
                <p class="intro">这是一个用于学习的示例网页。</p>
                <p class="description">爬虫很有趣！</p>
            </div>
            <ul class="book-list">
                <li class="book">
                    <span class="title">Python入门</span>
                    <span class="price">59元</span>
                </li>
                <li class="book">
                    <span class="title">爬虫实战</span>
                    <span class="price">79元</span>
                </li>
                <li class="book">
                    <span class="title">数据分析</span>
                    <span class="price">89元</span>
                </li>
            </ul>
            <a href="https://example.com/page1">第1页</a>
            <a href="https://example.com/page2">第2页</a>
        </body>
    </html>
    """

    print("\n【示例1】创建BeautifulSoup对象")
    print("-" * 40)

    # 创建BeautifulSoup对象
    # 'html.parser' 是Python内置的解析器
    soup = BeautifulSoup(html, 'html.parser')

    print(f"网页标题: {soup.title.text}")

    print("\n【示例2】find() - 查找第一个匹配的标签")
    print("-" * 40)

    # find() 只返回第一个匹配的元素
    first_p = soup.find('p')
    print(f"第一个<p>标签: {first_p.text}")

    # 可以按class查找
    intro = soup.find('p', class_='intro')
    print(f"class为intro的<p>: {intro.text}")

    # 可以按id查找
    # element = soup.find('tag', id='my-id')

    print("\n【示例3】find_all() - 查找所有匹配的标签")
    print("-" * 40)

    # find_all() 返回所有匹配的元素（列表）
    all_p = soup.find_all('p')
    print(f"找到{len(all_p)}个<p>标签:")
    for i, p in enumerate(all_p, 1):
        print(f"  {i}. {p.text}")

    # 查找所有书籍
    books = soup.find_all('li', class_='book')
    print(f"\n找到{len(books)}本书:")
    for book in books:
        title = book.find('span', class_='title').text
        price = book.find('span', class_='price').text
        print(f"  - {title}: {price}")

    print("\n【示例4】CSS选择器 - select() 和 select_one()")
    print("-" * 40)

    # select_one() 返回第一个匹配的元素
    first_link = soup.select_one('a')
    print(f"第一个链接: {first_link.text} -> {first_link['href']}")

    # select() 返回所有匹配的元素
    all_links = soup.select('a')
    print(f"\n所有链接:")
    for link in all_links:
        print(f"  - {link.text}: {link['href']}")

    # 更复杂的选择器
    book_titles = soup.select('.book-list .book .title')
    print(f"\n所有书名（CSS选择器）:")
    for title in book_titles:
        print(f"  - {title.text}")


def parse_html(html_content, parser='html.parser'):
    """
    解析HTML内容的通用函数

    参数说明：
        html_content (str): HTML字符串
        parser (str): 解析器，默认 'html.parser'

    返回值：
        BeautifulSoup对象

    调用示例：
        soup = parse_html("<html><body>Hello</body></html>")
        print(soup.body.text)
    """
    from bs4 import BeautifulSoup
    return BeautifulSoup(html_content, parser)


# ============================================================
# 第4节：提取数据
# ============================================================
"""
📖 第4节：提取数据

【提取文本】
element.text          # 获取标签内的纯文本
element.string        # 获取唯一字符串（如果只有一个字符串）
element.get_text()    # 获取所有文本，可设置分隔符

【提取属性】
element['href']       # 获取href属性
element['class']      # 获取class属性（返回列表）
element.get('href')   # 安全获取，不存在返回None

【导航】
element.parent        # 父元素
element.children      # 所有子元素
element.next_sibling  # 下一个兄弟元素
element.prev_sibling  # 上一个兄弟元素
"""

def section_4_extract_data():
    """
    第4节演示：学习数据提取

    这个函数演示如何从HTML中提取各种数据

    参数说明：
        无参数

    调用示例：
        section_4_extract_data()
    """
    print("\n" + "=" * 60)
    print("📖 第4节：提取数据")
    print("=" * 60)

    from bs4 import BeautifulSoup

    # 更复杂的HTML示例
    html = """
    <div class="product-card">
        <h2 class="name">Python编程书</h2>
        <p class="description">适合初学者的Python教程</p>
        <div class="price-info">
            <span class="original-price">¥99.00</span>
            <span class="sale-price">¥59.00</span>
        </div>
        <a href="/product/123" class="buy-link" data-id="123">立即购买</a>
        <img src="/images/book.jpg" alt="Python编程书封面">
        <ul class="tags">
            <li>编程</li>
            <li>Python</li>
            <li>入门</li>
        </ul>
    </div>
    """

    soup = BeautifulSoup(html, 'html.parser')

    print("\n【示例1】提取文本内容")
    print("-" * 40)

    # 找到商品卡片
    card = soup.find('div', class_='product-card')

    # 提取商品名
    name = card.find('h2', class_='name').text
    print(f"商品名: {name}")

    # 提取描述
    desc = card.find('p', class_='description').text
    print(f"描述: {desc}")

    # 提取所有标签
    tags = card.find('ul', class_='tags').find_all('li')
    print(f"标签: {', '.join([tag.text for tag in tags])}")

    print("\n【示例2】提取属性值")
    print("-" * 40)

    # 提取链接地址
    link = card.find('a', class_='buy-link')
    href = link['href']
    data_id = link['data-id']
    print(f"链接地址: {href}")
    print(f"数据ID: {data_id}")

    # 提取图片地址
    img = card.find('img')
    img_src = img['src']
    img_alt = img['alt']
    print(f"图片地址: {img_src}")
    print(f"图片描述: {img_alt}")

    print("\n【示例3】安全提取（避免报错）")
    print("-" * 40)

    # 使用 get() 方法，如果属性不存在不会报错
    link = card.find('a')
    href = link.get('href', '无')  # 如果没有href，返回'无'
    target = link.get('target', '_self')  # 如果没有target，返回'_self'
    print(f"href: {href}")
    print(f"target: {target}")

    # 安全提取文本
    price_element = card.find('span', class_='sale-price')
    price = price_element.text if price_element else "价格未知"
    print(f"售价: {price}")

    print("\n【示例4】提取嵌套数据")
    print("-" * 40)

    # 提取价格信息
    price_info = card.find('div', class_='price-info')
    original_price = price_info.find('span', class_='original-price').text
    sale_price = price_info.find('span', class_='sale-price').text
    print(f"原价: {original_price}")
    print(f"售价: {sale_price}")

    # 计算折扣
    import re
    orig = float(re.search(r'[\d.]+', original_price).group())
    sale = float(re.search(r'[\d.]+', sale_price).group())
    discount = sale / orig * 10
    print(f"折扣: {discount:.1f}折")


def extract_text(element, default='无'):
    """
    安全提取元素的文本内容

    参数说明：
        element: BeautifulSoup元素
        default (str): 如果元素不存在，返回的默认值

    返回值：
        str: 文本内容或默认值

    调用示例：
        text = extract_text(soup.find('h1'))
        text = extract_text(soup.find('h1'), default='未找到')
    """
    if element:
        return element.get_text(strip=True)
    return default


def extract_attribute(element, attr, default=None):
    """
    安全提取元素的属性值

    参数说明：
        element: BeautifulSoup元素
        attr (str): 属性名
        default: 如果属性不存在，返回的默认值

    返回值：
        属性值或默认值

    调用示例：
        href = extract_attribute(link, 'href')
        href = extract_attribute(link, 'href', default='#')
    """
    if element:
        return element.get(attr, default)
    return default


# ============================================================
# 第5节：保存数据
# ============================================================
"""
📖 第5节：保存数据

【常见的保存方式】
1. CSV文件 - 表格数据，可用Excel打开
2. JSON文件 - 结构化数据，易于交换
3. TXT文件 - 简单文本
4. 数据库 - 大量数据，如SQLite

【CSV格式】
逗号分隔值，例如：
姓名,年龄,城市
张三,18,北京
李四,20,上海

【JSON格式】
JavaScript对象表示法，例如：
{
    "name": "张三",
    "age": 18,
    "city": "北京"
}
"""

def section_5_save_data():
    """
    第5节演示：学习保存数据

    这个函数演示如何将爬取的数据保存到文件

    参数说明：
        无参数

    调用示例：
        section_5_save_data()
    """
    print("\n" + "=" * 60)
    print("📖 第5节：保存数据")
    print("=" * 60)

    import csv
    import json
    import os

    # 模拟爬取的数据
    books = [
        {"title": "Python入门", "author": "张三", "price": 59},
        {"title": "爬虫实战", "author": "李四", "price": 79},
        {"title": "数据分析", "author": "王五", "price": 89},
    ]

    # 创建保存目录
    save_dir = "/mnt/c/dev/python/qqstudy/web_crawler/data"
    os.makedirs(save_dir, exist_ok=True)

    print("\n【示例1】保存为CSV文件")
    print("-" * 40)

    csv_file = os.path.join(save_dir, "books.csv")

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        # 创建写入器
        writer = csv.writer(f)

        # 写入表头
        writer.writerow(['书名', '作者', '价格'])

        # 写入数据
        for book in books:
            writer.writerow([book['title'], book['author'], book['price']])

    print(f"✅ 已保存到: {csv_file}")

    # 使用DictWriter（更方便）
    csv_file2 = os.path.join(save_dir, "books_dict.csv")

    with open(csv_file2, 'w', newline='', encoding='utf-8') as f:
        # 创建字典写入器
        writer = csv.DictWriter(f, fieldnames=['title', 'author', 'price'])

        # 写入表头
        writer.writeheader()

        # 写入数据
        writer.writerows(books)

    print(f"✅ 已保存到: {csv_file2}")

    print("\n【示例2】保存为JSON文件")
    print("-" * 40)

    json_file = os.path.join(save_dir, "books.json")

    with open(json_file, 'w', encoding='utf-8') as f:
        # ensure_ascii=False 保证中文正常显示
        # indent=4 格式化输出，便于阅读
        json.dump(books, f, ensure_ascii=False, indent=4)

    print(f"✅ 已保存到: {json_file}")

    # 读取JSON文件
    with open(json_file, 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)

    print(f"读取到的数据: {loaded_data[0]}")

    print("\n【示例3】保存为TXT文件")
    print("-" * 40)

    txt_file = os.path.join(save_dir, "books.txt")

    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write("=" * 40 + "\n")
        f.write("书籍列表\n")
        f.write("=" * 40 + "\n\n")

        for i, book in enumerate(books, 1):
            f.write(f"{i}. {book['title']}\n")
            f.write(f"   作者: {book['author']}\n")
            f.write(f"   价格: ¥{book['price']}\n\n")

    print(f"✅ 已保存到: {txt_file}")

    print("\n【示例4】保存到SQLite数据库")
    print("-" * 40)

    import sqlite3

    db_file = os.path.join(save_dir, "books.db")

    # 连接数据库（不存在则创建）
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # 创建表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT,
            price REAL
        )
    ''')

    # 插入数据
    for book in books:
        cursor.execute(
            'INSERT INTO books (title, author, price) VALUES (?, ?, ?)',
            (book['title'], book['author'], book['price'])
        )

    # 提交事务
    conn.commit()

    # 查询数据
    cursor.execute('SELECT * FROM books')
    all_books = cursor.fetchall()
    print(f"数据库中的书籍:")
    for book in all_books:
        print(f"  {book}")

    # 关闭连接
    conn.close()

    print(f"✅ 已保存到: {db_file}")


def save_to_csv(data, filepath, fieldnames=None):
    """
    保存数据到CSV文件

    参数说明：
        data (list): 数据列表，每个元素是字典
        filepath (str): 保存路径
        fieldnames (list): 字段名列表，如果为None则使用第一个字典的键

    返回值：
        bool: 是否成功

    调用示例：
        data = [
            {"name": "张三", "age": 18},
            {"name": "李四", "age": 20}
        ]
        save_to_csv(data, "output.csv")
    """
    import csv

    if not data:
        print("❌ 数据为空，无法保存")
        return False

    try:
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            if fieldnames is None:
                fieldnames = list(data[0].keys())

            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        print(f"✅ 已保存 {len(data)} 条数据到: {filepath}")
        return True
    except Exception as e:
        print(f"❌ 保存失败: {e}")
        return False


def save_to_json(data, filepath, indent=4):
    """
    保存数据到JSON文件

    参数说明：
        data: 要保存的数据（列表或字典）
        filepath (str): 保存路径
        indent (int): 缩进空格数，None表示压缩

    返回值：
        bool: 是否成功

    调用示例：
        data = {"name": "张三", "age": 18}
        save_to_json(data, "output.json")
    """
    import json

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=indent)

        print(f"✅ 已保存数据到: {filepath}")
        return True
    except Exception as e:
        print(f"❌ 保存失败: {e}")
        return False


# ============================================================
# 第6节：处理反爬虫
# ============================================================
"""
📖 第6节：处理反爬虫

【为什么有反爬虫？】
网站为了保护服务器和防止数据被滥用，会采取一些措施阻止爬虫。

【常见的反爬虫措施】
1. 检查User-Agent - 识别是否是浏览器
2. 检查Referer - 判断请求来源
3. IP限制 - 同一IP请求次数过多
4. 验证码 - 需要人工验证
5. 登录验证 - 需要登录才能访问

【应对方法】
1. 设置User-Agent - 模拟浏览器
2. 添加Referer - 模拟从网站内部访问
3. 设置请求延迟 - 避免请求过于频繁
4. 使用代理IP - 更换IP地址
5. 处理Cookie - 保持登录状态

【重要提醒】
⚠️ 这些方法仅用于学习，请勿用于恶意爬取！
"""

def section_6_anti_crawler():
    """
    第6节演示：学习处理反爬虫

    这个函数演示如何设置请求头来模拟浏览器

    参数说明：
        无参数

    调用示例：
        section_6_anti_crawler()
    """
    print("\n" + "=" * 60)
    print("📖 第6节：处理反爬虫")
    print("=" * 60)

    import requests
    import time
    import random

    print("\n【示例1】设置User-Agent")
    print("-" * 40)

    # 常用的User-Agent
    user_agents = [
        # Chrome浏览器
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        # Firefox浏览器
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
        # Safari浏览器
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
        # Edge浏览器
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    ]

    # 随机选择一个User-Agent
    headers = {
        "User-Agent": random.choice(user_agents)
    }

    print(f"User-Agent: {headers['User-Agent'][:50]}...")

    response = requests.get("https://httpbin.org/get", headers=headers)
    print(f"状态码: {response.status_code}")

    print("\n【示例2】完整的请求头设置")
    print("-" * 40)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.google.com/",  # 模拟从Google搜索过来
        "Connection": "keep-alive",
    }

    print("请求头设置:")
    for key, value in headers.items():
        print(f"  {key}: {value[:40]}..." if len(value) > 40 else f"  {key}: {value}")

    print("\n【示例3】设置请求延迟")
    print("-" * 40)

    # 模拟爬取多个页面
    urls = [
        "https://httpbin.org/get?page=1",
        "https://httpbin.org/get?page=2",
        "https://httpbin.org/get?page=3",
    ]

    for i, url in enumerate(urls, 1):
        print(f"正在请求第{i}页: {url}")

        # 模拟请求
        # response = requests.get(url, headers=headers)

        # 设置随机延迟（1-3秒）
        delay = random.uniform(1, 3)
        print(f"  等待 {delay:.1f} 秒...")
        # time.sleep(delay)  # 实际使用时取消注释

        print(f"  ✅ 完成")
        print()

    print("⚠️ 提示：设置延迟可以避免给服务器造成压力")

    print("\n【示例4】Session保持会话")
    print("-" * 40)

    # 使用Session可以保持Cookie
    session = requests.Session()

    # 设置Session的默认headers
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    })

    # 所有请求都会带上Cookie
    # response1 = session.get("https://example.com/login")
    # response2 = session.get("https://example.com/profile")

    print("Session可以保持Cookie，适合需要登录的网站")


def get_random_headers():
    """
    获取随机请求头

    返回值：
        dict: 包含随机User-Agent的请求头字典

    调用示例：
        headers = get_random_headers()
        response = requests.get(url, headers=headers)
    """
    import random

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    ]

    return {
        "User-Agent": random.choice(user_agents),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    }


def crawl_with_delay(url, delay_range=(1, 3), max_retries=3):
    """
    带延迟和重试的爬取函数

    参数说明：
        url (str): 要爬取的URL
        delay_range (tuple): 延迟范围（秒），如 (1, 3) 表示1-3秒
        max_retries (int): 最大重试次数

    返回值：
        Response对象或None

    调用示例：
        response = crawl_with_delay("https://example.com", delay_range=(2, 5))
    """
    import requests
    import time
    import random

    headers = get_random_headers()

    for attempt in range(max_retries):
        try:
            # 添加随机延迟
            delay = random.uniform(*delay_range)
            time.sleep(delay)

            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code == 200:
                return response
            elif response.status_code == 429:
                # 请求过于频繁，等待更长时间
                wait_time = (attempt + 1) * 5
                print(f"请求过于频繁，等待{wait_time}秒后重试...")
                time.sleep(wait_time)
            else:
                print(f"状态码 {response.status_code}，尝试 {attempt + 1}/{max_retries}")

        except Exception as e:
            print(f"请求失败: {e}，尝试 {attempt + 1}/{max_retries}")

    return None


# ============================================================
# 第7节：翻页爬取
# ============================================================
"""
📖 第7节：翻页爬取

【为什么要翻页？】
很多网站的内容分布在多个页面，需要翻页才能获取全部数据。

【翻页的两种方式】
1. URL规律翻页 - 页码直接体现在URL中
   例如：/page/1, /page/2, /page/3...

2. 参数翻页 - 通过URL参数控制页码
   例如：?page=1, ?page=2, ?page=3...

【翻页爬取的步骤】
1. 分析翻页规律
2. 构造每一页的URL
3. 循环请求每一页
4. 提取数据并保存
5. 判断是否到达最后一页
"""

def section_7_pagination():
    """
    第7节演示：学习翻页爬取

    这个函数演示如何爬取多页数据

    参数说明：
        无参数

    调用示例：
        section_7_pagination()
    """
    print("\n" + "=" * 60)
    print("📖 第7节：翻页爬取")
    print("=" * 60)

    print("\n【示例1】分析翻页规律")
    print("-" * 40)

    # 以 quotes.toscrape.com 为例
    # 第1页: https://quotes.toscrape.com/page/1/
    # 第2页: https://quotes.toscrape.com/page/2/
    # 第3页: https://quotes.toscrape.com/page/3/
    # ...

    base_url = "https://quotes.toscrape.com/page/{}/"

    print("URL规律分析:")
    for page in range(1, 4):
        url = base_url.format(page)
        print(f"  第{page}页: {url}")

    print("\n【示例2】参数翻页")
    print("-" * 40)

    # 有些网站使用参数翻页
    # 第1页: https://example.com/articles?page=1
    # 第2页: https://example.com/articles?page=2

    import requests

    base_url = "https://httpbin.org/get"

    print("参数翻页示例:")
    for page in range(1, 4):
        params = {"page": page, "size": 10}
        # 实际请求
        # response = requests.get(base_url, params=params)

        # 构造的URL示例
        print(f"  第{page}页参数: {params}")

    print("\n【示例3】完整的翻页爬取流程")
    print("-" * 40)

    # 翻页爬取的伪代码
    print("""
翻页爬取的一般流程:

1. 设置起始页码和最大页数
2. while 循环:
   a. 构造当前页URL
   b. 发送请求
   c. 解析页面提取数据
   d. 保存数据
   e. 检查是否还有下一页
   f. 如果没有下一页，退出循环
   g. 页码 + 1
   h. 添加延迟，避免请求过快
    """)


def crawl_multiple_pages(base_url, max_pages=5, delay=(1, 2)):
    """
    翻页爬取通用函数

    参数说明：
        base_url (str): 基础URL，使用 {} 作为页码占位符
                        例如："https://example.com/page/{}"
        max_pages (int): 最大爬取页数
        delay (tuple): 请求延迟范围（秒）

    返回值：
        list: 所有页面提取的数据列表

    调用示例：
        # 爬取前5页
        data = crawl_multiple_pages("https://quotes.toscrape.com/page/{}/", max_pages=5)

        # 带自定义延迟
        data = crawl_multiple_pages("https://example.com/page/{}/", max_pages=10, delay=(2, 4))
    """
    import requests
    from bs4 import BeautifulSoup
    import time
    import random

    all_data = []

    for page in range(1, max_pages + 1):
        url = base_url.format(page)
        print(f"正在爬取第 {page} 页: {url}")

        try:
            # 添加随机延迟
            time.sleep(random.uniform(*delay))

            # 发送请求
            headers = get_random_headers()
            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                # 这里返回soup，具体提取逻辑由调用者实现
                all_data.append({
                    'page': page,
                    'url': url,
                    'soup': soup
                })
                print(f"  ✅ 第 {page} 页爬取成功")
            else:
                print(f"  ❌ 第 {page} 页状态码: {response.status_code}")
                break

        except Exception as e:
            print(f"  ❌ 第 {page} 页爬取失败: {e}")
            break

    print(f"\n共爬取 {len(all_data)} 页")
    return all_data


# ============================================================
# 第8节：综合案例
# ============================================================
"""
📖 第8节：综合案例

现在我们来实现一个完整的爬虫项目！

【目标】
爬取 http://quotes.toscrape.com 网站的名言警句

【数据】
- 名言内容
- 作者
- 标签

【步骤】
1. 发送HTTP请求获取网页
2. 解析HTML提取数据
3. 翻页获取更多数据
4. 保存到CSV文件
"""

def section_8_complete_example():
    """
    第8节：综合案例 - 爬取名言网站

    这是一个完整的爬虫示例，展示了所有前面学到的知识

    参数说明：
        无参数

    调用示例：
        section_8_complete_example()
    """
    print("\n" + "=" * 60)
    print("📖 第8节：综合案例 - 爬取名言网站")
    print("=" * 60)

    import requests
    from bs4 import BeautifulSoup
    import csv
    import time
    import random
    import os

    # 目标网站
    base_url = "https://quotes.toscrape.com/page/{}/"

    # 存储所有名言
    all_quotes = []

    # 爬取前3页作为示例
    max_pages = 3

    print(f"\n开始爬取 {base_url} 前 {max_pages} 页的名言...")
    print("-" * 40)

    for page in range(1, max_pages + 1):
        url = base_url.format(page)
        print(f"\n正在爬取第 {page} 页: {url}")

        try:
            # 1. 添加延迟
            delay = random.uniform(1, 2)
            time.sleep(delay)

            # 2. 发送请求
            headers = get_random_headers()
            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code != 200:
                print(f"  ❌ 状态码: {response.status_code}")
                continue

            # 3. 解析HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            # 4. 提取数据
            quotes = soup.find_all('div', class_='quote')

            print(f"  找到 {len(quotes)} 条名言")

            for quote in quotes:
                # 提取名言内容
                text = quote.find('span', class_='text').text

                # 提取作者
                author = quote.find('small', class_='author').text

                # 提取标签
                tags = quote.find_all('a', class_='tag')
                tag_list = [tag.text for tag in tags]

                # 保存数据
                quote_data = {
                    'text': text,
                    'author': author,
                    'tags': ', '.join(tag_list)
                }
                all_quotes.append(quote_data)

                # 显示
                print(f"  - {author}: {text[:30]}...")

            # 5. 检查是否还有下一页
            next_btn = soup.find('li', class_='next')
            if not next_btn:
                print("  已到达最后一页")
                break

        except Exception as e:
            print(f"  ❌ 爬取失败: {e}")
            continue

    # 6. 保存数据
    print(f"\n共爬取 {len(all_quotes)} 条名言")

    if all_quotes:
        save_dir = "/mnt/c/dev/python/qqstudy/web_crawler/data"
        os.makedirs(save_dir, exist_ok=True)
        csv_file = os.path.join(save_dir, "quotes.csv")

        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['text', 'author', 'tags'])
            writer.writeheader()
            writer.writerows(all_quotes)

        print(f"✅ 数据已保存到: {csv_file}")

    return all_quotes


# ============================================================
# 练习题
# ============================================================
"""
📝 练习题

请完成 /mnt/c/dev/python/qqstudy/web_crawler/web_crawler_exercises.py 中的练习

练习内容包括：
1. 发送HTTP请求
2. 解析HTML
3. 提取数据
4. 保存数据
5. 翻页爬取
6. 综合练习

每道题都有参考答案，建议先自己尝试，再看答案。
"""


# ============================================================
# 运行所有示例
# ============================================================
def run_all_sections():
    """
    运行所有章节的示例

    参数说明：
        无参数

    调用示例：
        run_all_sections()
    """
    print("\n" + "🚀" * 30)
    print("开始运行所有章节示例...")
    print("🚀" * 30)

    section_1_what_is_crawler()  # 概念介绍
    section_2_http_basics()      # HTTP请求
    section_3_parse_html()       # HTML解析
    section_4_extract_data()     # 数据提取
    section_5_save_data()        # 保存数据
    section_6_anti_crawler()     # 反爬虫
    section_7_pagination()       # 翻页爬取
    # section_8_complete_example() # 综合案例（需要网络）

    print("\n" + "=" * 60)
    print("🎉 所有章节演示完成！")
    print("=" * 60)

    print("""
📚 接下来你可以：

1. 运行练习题：
   python web_crawler_exercises.py

2. 查看示例代码：
   - examples/crawl_quotes.py    # 爬取名言
   - examples/crawl_weather.py   # 爬取天气
   - examples/crawl_books.py     # 爬取书籍

3. 开始自己的爬虫项目！

⚠️ 记住：爬虫要合法合规！
    """)


# ============================================================
# 主程序入口
# ============================================================
if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║           🕷️  网络爬虫速成教程  🕷️                      ║
║                                                          ║
║           适合初中生及编程初学者                          ║
║           学习时间：约2-3小时                             ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

【目录】
第1节：什么是网络爬虫？（概念、原理、法律道德）
第2节：HTTP 请求基础（requests库、GET请求、状态码）
第3节：解析 HTML（BeautifulSoup、find/find_all）
第4节：提取数据（获取文本、属性、CSS选择器）
第5节：保存数据（CSV、JSON、数据库）
第6节：处理反爬虫（User-Agent、请求头、延迟）
第7节：翻页爬取（分析分页、循环爬取）
第8节：综合案例

【使用方法】
1. 运行所有示例：
   run_all_sections()

2. 运行单个章节：
   section_1_what_is_crawler()  # 第1节
   section_2_http_basics()      # 第2节
   ...

3. 运行综合案例（需要网络）：
   section_8_complete_example()

【依赖安装】
pip install requests beautifulsoup4

⚠️ 重要提醒：爬虫要合法合规！
- 遵守网站的 robots.txt 规则
- 不要频繁请求，给服务器造成压力
- 不要爬取隐私信息和付费内容
    """)

    # 提示用户输入
    print("\n请选择操作：")
    print("1. 运行所有示例（不需要网络的部分）")
    print("2. 只运行综合案例（需要网络）")
    print("3. 退出")

    choice = input("\n请输入选项 (1/2/3): ").strip()

    if choice == '1':
        run_all_sections()
    elif choice == '2':
        section_8_complete_example()
    else:
        print("再见！继续加油学习！")
