# 网络爬虫速成教程

适合初中生及编程初学者的网络爬虫教程，学习时间约2-3小时。

## 目录结构

```
web_crawler/
├── web_crawler_quick_start.py     # 主教程（8个章节）
├── web_crawler_exercises.py       # 练习题（8道练习，带答案）
├── examples/                      # 示例爬虫
│   ├── crawl_quotes.py           # 爬取名言（http://quotes.toscrape.com）
│   ├── crawl_weather.py          # 爬取天气示例
│   └── crawl_books.py            # 爬取书籍信息
├── data/                         # 保存的数据（自动创建）
└── README.md                     # 本文件
```

## 安装依赖

在开始学习之前，请先安装必要的Python库：

```bash
pip install requests beautifulsoup4
```

## 快速开始

### 1. 运行主教程

```bash
python web_crawler_quick_start.py
```

### 2. 完成练习题

```bash
python web_crawler_exercises.py
```

### 3. 运行示例爬虫

```bash
# 爬取名言
python examples/crawl_quotes.py

# 爬取天气
python examples/crawl_weather.py

# 爬取书籍
python examples/crawl_books.py
```

## 教程内容

### 主教程章节

| 章节 | 主题 | 内容 |
|------|------|------|
| 第1节 | 什么是网络爬虫？ | 概念、原理、法律道德 |
| 第2节 | HTTP 请求基础 | requests库、GET请求、状态码 |
| 第3节 | 解析 HTML | BeautifulSoup、find/find_all |
| 第4节 | 提取数据 | 获取文本、属性、CSS选择器 |
| 第5节 | 保存数据 | CSV、JSON、数据库 |
| 第6节 | 处理反爬虫 | User-Agent、请求头、延迟 |
| 第7节 | 翻页爬取 | 分析分页、循环爬取 |
| 第8节 | 综合案例 | 完整爬虫项目 |

### 练习题内容

1. 发送HTTP请求
2. 带参数的请求
3. 解析HTML
4. CSS选择器
5. 保存数据到CSV
6. 保存数据到JSON
7. 完整爬虫
8. 翻页爬取

每道练习都有对应的答案函数。

## 重要提醒

### 法律与道德

爬虫要合法合规！请遵守以下原则：

1. **遵守 robots.txt** - 在爬取前查看网站的 robots.txt 文件
2. **控制频率** - 不要频繁请求，给服务器造成压力
3. **尊重隐私** - 不要爬取个人隐私信息
4. **尊重版权** - 不要滥用爬取的数据
5. **学习目的** - 本教程仅供学习使用

### robots.txt 是什么？

robots.txt 是网站告诉爬虫哪些页面可以爬取的文件。

例如：
- 查看百度的：https://www.baidu.com/robots.txt
- 查看谷歌的：https://www.google.com/robots.txt

## 示例网站

本教程使用以下专门为学习爬虫设计的网站：

1. **http://quotes.toscrape.com** - 名言网站
2. **http://books.toscrape.com** - 书店网站
3. **https://httpbin.org** - HTTP测试网站

## 常用函数速查

### HTTP请求

```python
import requests

# GET请求
response = requests.get(url)
response = requests.get(url, params={"key": "value"})
response = requests.get(url, headers={"User-Agent": "..."})

# 状态码
status = response.status_code  # 200成功, 404不存在

# 响应内容
text = response.text      # 字符串
data = response.json()    # JSON解析
```

### HTML解析

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')

# 查找元素
element = soup.find('tag')              # 第一个
elements = soup.find_all('tag')         # 所有
element = soup.find('tag', class_='x')  # 按class
element = soup.find('tag', id='x')      # 按id

# CSS选择器
element = soup.select_one('.class')     # 第一个
elements = soup.select('.class')        # 所有

# 提取内容
text = element.text           # 文本
attr = element['href']        # 属性
attr = element.get('href')    # 安全获取
```

### 保存数据

```python
import csv
import json

# CSV
with open('data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['col1', 'col2'])
    writer.writeheader()
    writer.writerows(data_list)

# JSON
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
```

## 学习路径建议

1. **第一步**：阅读主教程，理解爬虫的基本概念
2. **第二步**：运行教程代码，观察输出
3. **第三步**：完成练习题，检验学习成果
4. **第四步**：运行示例爬虫，体验真实爬虫
5. **第五步**：尝试修改示例，爬取不同数据
6. **第六步**：创建自己的爬虫项目

## 常见问题

### Q: 爬虫合法吗？

A: 爬虫本身是合法的技术，但使用方式需要注意：
- 只爬取公开的数据
- 遵守网站的使用条款
- 不给服务器造成压力
- 不侵犯他人隐私和版权

### Q: 为什么爬取失败？

A: 常见原因：
- 网络连接问题
- 网站需要登录
- 被反爬虫机制拦截
- URL或选择器写错

### Q: 如何设置延迟？

A: 使用 time.sleep() 函数：

```python
import time
import random

# 固定延迟
time.sleep(2)  # 等待2秒

# 随机延迟
delay = random.uniform(1, 3)
time.sleep(delay)
```

### Q: 如何处理中文乱码？

A: 确保使用正确的编码：

```python
# 请求时
response.encoding = 'utf-8'

# 保存文件时
with open('file.csv', 'w', encoding='utf-8') as f:
    ...

# JSON保存时
json.dump(data, f, ensure_ascii=False)
```

## 进阶学习

完成本教程后，你可以继续学习：

1. **Selenium** - 爬取动态网页
2. **Scrapy** - 专业爬虫框架
3. **代理IP** - 处理IP限制
4. **验证码识别** - 处理验证码
5. **分布式爬虫** - 大规模爬取

## 联系方式

如有问题，欢迎提问讨论！

---

祝你学习愉快！记住：爬虫要合法合规！
