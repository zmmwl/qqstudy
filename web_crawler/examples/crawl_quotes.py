# -*- coding: utf-8 -*-
"""
示例1：爬取名言网站
====================

目标网站：http://quotes.toscrape.com
这是一个专门用于学习爬虫的网站

爬取内容：
- 名言内容
- 作者
- 标签

运行方法：
python crawl_quotes.py
"""

import requests
from bs4 import BeautifulSoup
import csv
import json
import time
import random
import os


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
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    }


def crawl_quotes(max_pages=3):
    """
    爬取名言网站

    参数说明：
        max_pages (int): 最大爬取页数，默认3页

    返回值：
        list: 名言列表，每个元素是一个字典

    调用示例：
        quotes = crawl_quotes(5)  # 爬取5页
        quotes = crawl_quotes()   # 爬取3页（默认）
    """
    print("=" * 60)
    print("🕷️ 开始爬取名言网站")
    print("=" * 60)
    print(f"目标: http://quotes.toscrape.com")
    print(f"计划爬取: {max_pages} 页")
    print("-" * 60)

    base_url = "http://quotes.toscrape.com/page/{}/"
    all_quotes = []

    for page in range(1, max_pages + 1):
        url = base_url.format(page)
        print(f"\n📖 正在爬取第 {page} 页: {url}")

        try:
            # 添加随机延迟（1-2秒）
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

            # 提取名言
            quotes = soup.find_all('div', class_='quote')
            print(f"  找到 {len(quotes)} 条名言")

            for quote in quotes:
                # 提取内容
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
                    'tags': tag_list
                }
                all_quotes.append(quote_data)

                # 显示（只显示前50个字符）
                display_text = text[:50] + "..." if len(text) > 50 else text
                print(f"  ✅ {author}: {display_text}")

            # 检查是否还有下一页
            next_btn = soup.find('li', class_='next')
            if not next_btn:
                print("  📌 已到达最后一页")
                break

        except requests.exceptions.ConnectionError:
            print("  ❌ 网络连接失败，请检查网络")
            break
        except requests.exceptions.Timeout:
            print("  ❌ 请求超时")
            continue
        except Exception as e:
            print(f"  ❌ 爬取失败: {e}")
            continue

    print("\n" + "=" * 60)
    print(f"🎉 爬取完成！共获取 {len(all_quotes)} 条名言")
    print("=" * 60)

    return all_quotes


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
        writer = csv.DictWriter(f, fieldnames=['author', 'text', 'tags'])

        writer.writeheader()

        for item in data:
            # 将标签列表转为字符串
            row = {
                'author': item['author'],
                'text': item['text'],
                'tags': ', '.join(item['tags'])
            }
            writer.writerow(row)

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


def show_statistics(quotes):
    """
    显示统计信息

    参数说明：
        quotes (list): 名言列表
    """
    if not quotes:
        return

    print("\n📊 统计信息")
    print("-" * 40)

    # 统计作者
    authors = [q['author'] for q in quotes]
    author_count = {}
    for author in authors:
        author_count[author] = author_count.get(author, 0) + 1

    # 显示出现次数最多的前5位作者
    sorted_authors = sorted(author_count.items(), key=lambda x: x[1], reverse=True)
    print("名言最多的作者:")
    for author, count in sorted_authors[:5]:
        print(f"  - {author}: {count} 条")

    # 统计标签
    all_tags = []
    for q in quotes:
        all_tags.extend(q['tags'])

    tag_count = {}
    for tag in all_tags:
        tag_count[tag] = tag_count.get(tag, 0) + 1

    sorted_tags = sorted(tag_count.items(), key=lambda x: x[1], reverse=True)
    print("\n最常见的标签:")
    for tag, count in sorted_tags[:5]:
        print(f"  - {tag}: {count} 次")


def main():
    """
    主函数
    """
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║           📚 名言网站爬虫  📚                            ║
║                                                          ║
║           目标: http://quotes.toscrape.com               ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
    """)

    # 设置保存目录
    save_dir = "/mnt/c/dev/python/qqstudy/web_crawler/data"
    os.makedirs(save_dir, exist_ok=True)

    # 获取用户输入
    try:
        pages = input("请输入要爬取的页数（直接回车默认3页）: ").strip()
        max_pages = int(pages) if pages else 3
    except ValueError:
        max_pages = 3

    # 爬取数据
    quotes = crawl_quotes(max_pages)

    if quotes:
        # 保存数据
        csv_file = os.path.join(save_dir, "quotes.csv")
        json_file = os.path.join(save_dir, "quotes.json")

        save_to_csv(quotes, csv_file)
        save_to_json(quotes, json_file)

        # 显示统计
        show_statistics(quotes)

        # 显示示例数据
        print("\n📖 示例数据（前3条）:")
        print("-" * 40)
        for i, quote in enumerate(quotes[:3], 1):
            print(f"\n{i}. {quote['author']}:")
            print(f"   \"{quote['text']}\"")
            print(f"   标签: {', '.join(quote['tags'])}")

    print("\n" + "=" * 60)
    print("🎉 程序执行完毕！")
    print("=" * 60)


if __name__ == "__main__":
    main()
