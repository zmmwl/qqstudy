# -*- coding: utf-8 -*-
"""
示例3：爬取书籍信息
====================

目标网站：http://books.toscrape.com
这是一个专门用于学习爬虫的在线书店

爬取内容：
- 书名
- 价格
- 评分
- 是否有库存
- 封面图片链接

运行方法：
python crawl_books.py
"""

import requests
from bs4 import BeautifulSoup
import csv
import json
import time
import random
import os
import re


def get_headers():
    """
    获取随机请求头

    返回值：
        dict: 请求头字典
    """
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    ]
    return {
        "User-Agent": random.choice(user_agents),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    }


def parse_price(price_str):
    """
    解析价格字符串

    参数说明：
        price_str (str): 价格字符串，如 "£25.99"

    返回值：
        float: 价格数值
    """
    # 提取数字部分
    match = re.search(r'[\d.]+', price_str)
    if match:
        return float(match.group())
    return 0.0


def parse_rating(rating_class):
    """
    解析评分

    参数说明：
        rating_class (str): 评分class名，如 "Three"

    返回值：
        int: 评分数值（1-5）
    """
    rating_map = {
        "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5
    }
    for key, value in rating_map.items():
        if key in rating_class:
            return value
    return 0


def parse_availability(availability_str):
    """
    解析库存状态

    参数说明：
        availability_str (str): 库存字符串

    返回值：
        bool: 是否有库存
    """
    return "In stock" in availability_str


def crawl_books(max_pages=2):
    """
    爬取书籍信息

    参数说明：
        max_pages (int): 最大爬取页数，默认2页

    返回值：
        list: 书籍列表

    调用示例：
        books = crawl_books(5)  # 爬取5页
        books = crawl_books()   # 爬取2页（默认）
    """
    print("=" * 60)
    print("📚 开始爬取书籍信息")
    print("=" * 60)
    print(f"目标: http://books.toscrape.com")
    print(f"计划爬取: {max_pages} 页")
    print("-" * 60)

    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    all_books = []

    for page in range(1, max_pages + 1):
        url = base_url.format(page)
        print(f"\n📖 正在爬取第 {page} 页: {url}")

        try:
            # 添加随机延迟
            delay = random.uniform(1, 2)
            time.sleep(delay)

            # 发送请求
            headers = get_headers()
            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code != 200:
                print(f"  ❌ 状态码: {response.status_code}")
                continue

            # 解析HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            # 找到所有书籍
            books = soup.find_all('article', class_='product_pod')
            print(f"  找到 {len(books)} 本书")

            for book in books:
                # 提取书名
                title_element = book.find('h3').find('a')
                title = title_element['title'] if title_element else "未知"

                # 提取价格
                price_element = book.find('p', class_='price_color')
                price_str = price_element.text if price_element else "£0.00"
                price = parse_price(price_str)

                # 提取评分
                rating_element = book.find('p', class_='star-rating')
                rating_class = str(rating_element['class']) if rating_element else ""
                rating = parse_rating(rating_class)

                # 提取库存
                availability_element = book.find('p', class_='instock availability')
                availability_str = availability_element.text.strip() if availability_element else ""
                in_stock = parse_availability(availability_str)

                # 提取图片链接
                img_element = book.find('img')
                img_src = img_element['src'] if img_element else ""
                # 转换为完整URL
                img_url = "http://books.toscrape.com/" + img_src if img_src else ""

                # 保存数据
                book_data = {
                    'title': title,
                    'price': price,
                    'price_str': price_str,
                    'rating': rating,
                    'in_stock': in_stock,
                    'img_url': img_url
                }
                all_books.append(book_data)

                # 显示
                stock_icon = "✅" if in_stock else "❌"
                star = "⭐" * rating
                print(f"  {stock_icon} 《{title[:30]}...》 {price_str} {star}")

        except requests.exceptions.ConnectionError:
            print("  ❌ 网络连接失败")
            break
        except Exception as e:
            print(f"  ❌ 爬取失败: {e}")
            continue

    print("\n" + "=" * 60)
    print(f"🎉 爬取完成！共获取 {len(all_books)} 本书")
    print("=" * 60)

    return all_books


def show_statistics(books):
    """
    显示统计信息

    参数说明：
        books (list): 书籍列表
    """
    if not books:
        return

    print("\n📊 统计信息")
    print("-" * 40)

    # 价格统计
    prices = [b['price'] for b in books]
    print(f"价格统计:")
    print(f"  - 最低价: £{min(prices):.2f}")
    print(f"  - 最高价: £{max(prices):.2f}")
    print(f"  - 平均价: £{sum(prices)/len(prices):.2f}")

    # 评分统计
    ratings = [b['rating'] for b in books]
    rating_counts = {}
    for r in ratings:
        rating_counts[r] = rating_counts.get(r, 0) + 1

    print(f"\n评分分布:")
    for rating in sorted(rating_counts.keys(), reverse=True):
        count = rating_counts[rating]
        bar = "■" * count
        print(f"  {rating}星: {count}本 {bar}")

    # 库存统计
    in_stock = sum(1 for b in books if b['in_stock'])
    print(f"\n库存情况:")
    print(f"  - 有库存: {in_stock}本")
    print(f"  - 无库存: {len(books) - in_stock}本")


def filter_books(books, **filters):
    """
    筛选书籍

    参数说明：
        books (list): 书籍列表
        filters (dict): 筛选条件
            - min_price: 最低价格
            - max_price: 最高价格
            - min_rating: 最低评分
            - in_stock_only: 只显示有库存

    返回值：
        list: 筛选后的书籍列表

    调用示例：
        # 筛选价格低于30的书
        cheap_books = filter_books(books, max_price=30)

        # 筛选5星评分的书
        top_books = filter_books(books, min_rating=5)

        # 筛选有库存的便宜书
        result = filter_books(books, max_price=20, in_stock_only=True)
    """
    result = books

    if 'min_price' in filters:
        result = [b for b in result if b['price'] >= filters['min_price']]

    if 'max_price' in filters:
        result = [b for b in result if b['price'] <= filters['max_price']]

    if 'min_rating' in filters:
        result = [b for b in result if b['rating'] >= filters['min_rating']]

    if filters.get('in_stock_only'):
        result = [b for b in result if b['in_stock']]

    return result


def save_to_csv(data, filepath):
    """
    保存数据到CSV文件

    参数说明：
        data (list): 数据列表
        filepath (str): 保存路径
    """
    if not data:
        print("❌ 没有数据可保存")
        return

    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['title', 'price', 'price_str', 'rating', 'in_stock', 'img_url']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"✅ CSV文件已保存: {filepath}")


def save_to_json(data, filepath):
    """
    保存数据到JSON文件

    参数说明：
        data (list): 数据列表
        filepath (str): 保存路径
    """
    if not data:
        print("❌ 没有数据可保存")
        return

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ JSON文件已保存: {filepath}")


def main():
    """
    主函数
    """
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║           📚 书籍信息爬虫  📚                            ║
║                                                          ║
║           目标: http://books.toscrape.com                ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
    """)

    # 创建保存目录
    save_dir = "/mnt/c/dev/python/qqstudy/web_crawler/data"
    os.makedirs(save_dir, exist_ok=True)

    # 获取用户输入
    try:
        pages = input("请输入要爬取的页数（直接回车默认2页）: ").strip()
        max_pages = int(pages) if pages else 2
    except ValueError:
        max_pages = 2

    # 爬取数据
    books = crawl_books(max_pages)

    if books:
        # 显示统计
        show_statistics(books)

        # 保存数据
        csv_file = os.path.join(save_dir, "books.csv")
        json_file = os.path.join(save_dir, "books.json")

        save_to_csv(books, csv_file)
        save_to_json(books, json_file)

        # 筛选示例
        print("\n" + "=" * 60)
        print("🔍 筛选示例")
        print("=" * 60)

        # 筛选5星书籍
        top_books = filter_books(books, min_rating=5)
        print(f"\n5星评分书籍（共{len(top_books)}本）:")
        for book in top_books[:5]:
            print(f"  - 《{book['title'][:40]}》")

        # 筛选便宜书籍
        cheap_books = filter_books(books, max_price=20)
        print(f"\n价格低于£20的书籍（共{len(cheap_books)}本）:")
        for book in cheap_books[:5]:
            print(f"  - 《{book['title'][:40]}》 £{book['price']:.2f}")

    print("\n" + "=" * 60)
    print("🎉 程序执行完毕！")
    print("=" * 60)


if __name__ == "__main__":
    main()
