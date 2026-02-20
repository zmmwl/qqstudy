#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文本替换工具
============
批量文本查找和替换工具

功能：
- 单文件替换
- 批量文件替换
- 正则表达式支持
- 日志分析
- 预览模式

使用方法：
    python text_replacer.py

作者: Python学习小组
"""

import os
import re
from datetime import datetime


def replace_in_file(file_path, old_text, new_text, encoding="utf-8"):
    """
    在单个文件中替换文本

    参数：
        file_path: str - 文件路径
        old_text: str - 要替换的文本
        new_text: str - 替换成的文本
        encoding: str - 文件编码，默认utf-8

    返回：
        int - 替换的次数，-1表示出错

    示例调用：
        count = replace_in_file("article.txt", "Python", "Python3")
        print(f"替换了 {count} 处")
    """
    try:
        # 读取文件
        with open(file_path, "r", encoding=encoding) as f:
            content = f.read()

        # 计算替换次数
        count = content.count(old_text)

        if count == 0:
            return 0

        # 替换
        new_content = content.replace(old_text, new_text)

        # 写回文件
        with open(file_path, "w", encoding=encoding) as f:
            f.write(new_content)

        return count

    except Exception as e:
        print(f"❌ 处理文件 {file_path} 时出错: {e}")
        return -1


def replace_in_files(folder_path, old_text, new_text, pattern="*.txt", recursive=False):
    """
    在多个文件中批量替换文本

    参数：
        folder_path: str - 文件夹路径
        old_text: str - 要替换的文本
        new_text: str - 替换成的文本
        pattern: str - 文件匹配模式，默认"*.txt"
        recursive: bool - 是否递归处理子文件夹，默认False

    返回：
        dict - 文件名和替换次数的映射

    示例调用：
        # 替换当前目录下所有txt文件
        results = replace_in_files(".", "old", "new", "*.txt")

        # 递归替换所有html文件
        results = replace_in_files("website", "http://", "https://", "*.html", True)
    """
    import fnmatch

    results = {}
    files_to_process = []

    # 收集要处理的文件
    if recursive:
        for root, dirs, files in os.walk(folder_path):
            for filename in fnmatch.filter(files, pattern):
                files_to_process.append(os.path.join(root, filename))
    else:
        for filename in os.listdir(folder_path):
            if fnmatch.fnmatch(filename, pattern):
                file_path = os.path.join(folder_path, filename)
                if os.path.isfile(file_path):
                    files_to_process.append(file_path)

    # 处理每个文件
    for file_path in files_to_process:
        count = replace_in_file(file_path, old_text, new_text)
        if count > 0:
            results[file_path] = count
            print(f"  ✅ {os.path.basename(file_path)}: 替换了 {count} 处")
        elif count == 0:
            print(f"  ⏭️  {os.path.basename(file_path)}: 未找到匹配文本")

    return results


def regex_replace(file_path, pattern, replacement, encoding="utf-8"):
    """
    使用正则表达式替换文本

    参数：
        file_path: str - 文件路径
        pattern: str - 正则表达式模式
        replacement: str - 替换文本
        encoding: str - 文件编码

    返回：
        int - 替换的次数，-1表示出错

    示例调用：
        # 将所有日期格式从 2024-01-01 改为 01/01/2024
        count = regex_replace("data.txt", r"(\d{4})-(\d{2})-(\d{2})", r"\2/\3/\1")
    """
    try:
        with open(file_path, "r", encoding=encoding) as f:
            content = f.read()

        # 编译正则表达式
        regex = re.compile(pattern)

        # 计算匹配次数
        matches = regex.findall(content)
        count = len(matches)

        if count == 0:
            return 0

        # 替换
        new_content = regex.sub(replacement, content)

        with open(file_path, "w", encoding=encoding) as f:
            f.write(new_content)

        return count

    except Exception as e:
        print(f"❌ 处理文件 {file_path} 时出错: {e}")
        return -1


def analyze_log_file(file_path, keywords=None, encoding="utf-8"):
    """
    分析日志文件

    参数：
        file_path: str - 日志文件路径
        keywords: list - 要统计的关键词列表，默认统计 INFO/WARNING/ERROR
        encoding: str - 文件编码

    返回：
        dict - 统计结果

    示例调用：
        stats = analyze_log_file("server.log")
        print(stats)  # {'INFO': 100, 'WARNING': 20, 'ERROR': 5}

        # 自定义关键词
        stats = analyze_log_file("access.log", ["GET", "POST", "404", "500"])
    """
    if keywords is None:
        keywords = ["INFO", "WARNING", "ERROR", "DEBUG"]

    stats = {keyword: 0 for keyword in keywords}
    error_lines = []

    try:
        with open(file_path, "r", encoding=encoding) as f:
            for line_num, line in enumerate(f, 1):
                for keyword in keywords:
                    if keyword in line:
                        stats[keyword] += 1

                # 记录错误行
                if "ERROR" in line:
                    error_lines.append((line_num, line.strip()))

    except Exception as e:
        print(f"❌ 读取文件时出错: {e}")
        return None

    return {
        'stats': stats,
        'error_lines': error_lines,
        'total_lines': line_num if 'line_num' in dir() else 0
    }


def extract_matches(file_path, pattern, encoding="utf-8"):
    """
    从文件中提取匹配正则表达式的内容

    参数：
        file_path: str - 文件路径
        pattern: str - 正则表达式模式
        encoding: str - 文件编码

    返回：
        list - 所有匹配的内容

    示例调用：
        # 提取所有邮箱地址
        emails = extract_matches("data.txt", r"[\w.-]+@[\w.-]+\.\w+")
        print(emails)

        # 提取所有URL
        urls = extract_matches("page.html", r'https?://[^\s<>"]+')
    """
    try:
        with open(file_path, "r", encoding=encoding) as f:
            content = f.read()

        matches = re.findall(pattern, content)
        return matches

    except Exception as e:
        print(f"❌ 读取文件时出错: {e}")
        return []


def preview_replace(file_path, old_text, new_text, encoding="utf-8", context_lines=2):
    """
    预览替换效果（不实际修改文件）

    参数：
        file_path: str - 文件路径
        old_text: str - 要替换的文本
        new_text: str - 替换成的文本
        encoding: str - 文件编码
        context_lines: int - 显示匹配行前后的行数

    返回：
        int - 将要替换的次数

    示例调用：
        count = preview_replace("article.txt", "Python", "Python3")
        print(f"将替换 {count} 处")
    """
    try:
        with open(file_path, "r", encoding=encoding) as f:
            lines = f.readlines()

        count = 0
        print(f"\n📄 文件: {file_path}")
        print("-" * 50)

        for i, line in enumerate(lines):
            if old_text in line:
                count += 1
                # 显示上下文
                start = max(0, i - context_lines)
                end = min(len(lines), i + context_lines + 1)

                for j in range(start, end):
                    prefix = ">>> " if j == i else "    "
                    content = lines[j].rstrip()
                    if j == i:
                        # 高亮显示替换位置
                        content = content.replace(old_text, f"[{old_text}]→[{new_text}]")
                    print(f"{prefix}{j+1}: {content}")
                print()

        if count == 0:
            print("未找到匹配文本")
        else:
            print(f"共找到 {count} 处匹配")

        return count

    except Exception as e:
        print(f"❌ 读取文件时出错: {e}")
        return -1


def create_backup(file_path):
    """
    创建文件备份

    参数：
        file_path: str - 要备份的文件路径

    返回：
        str - 备份文件路径

    示例调用：
        backup_path = create_backup("important.txt")
        print(f"备份已创建: {backup_path}")
    """
    import shutil

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    name, ext = os.path.splitext(file_path)
    backup_path = f"{name}_backup_{timestamp}{ext}"

    shutil.copy(file_path, backup_path)
    return backup_path


def print_menu():
    """打印菜单"""
    print("""
╔════════════════════════════════════════════════════════════╗
║               文本替换工具 v1.0                            ║
╠════════════════════════════════════════════════════════════╣
║  1. 单文件替换                                              ║
║  2. 批量文件替换                                            ║
║  3. 正则表达式替换                                          ║
║  4. 日志分析                                                ║
║  5. 提取匹配内容                                            ║
║  6. 预览替换                                                ║
║  q. 退出                                                    ║
╚════════════════════════════════════════════════════════════╝
    """)


def main():
    """主函数"""
    while True:
        print_menu()
        choice = input("请选择操作: ").strip().lower()

        if choice == "q":
            print("👋 再见！")
            break

        elif choice == "1":
            # 单文件替换
            file_path = input("请输入文件路径: ").strip()
            old_text = input("请输入要替换的文本: ").strip()
            new_text = input("请输入替换成的文本: ").strip()

            # 询问是否备份
            backup = input("是否创建备份？(y/n): ").strip().lower()
            if backup == "y":
                backup_path = create_backup(file_path)
                print(f"✅ 备份已创建: {backup_path}")

            count = replace_in_file(file_path, old_text, new_text)
            if count > 0:
                print(f"\n✅ 替换完成！共替换 {count} 处")
            elif count == 0:
                print("\n⚠️  未找到匹配文本")
            else:
                print("\n❌ 替换失败")

            input("\n按回车继续...")

        elif choice == "2":
            # 批量文件替换
            folder_path = input("请输入文件夹路径: ").strip()
            old_text = input("请输入要替换的文本: ").strip()
            new_text = input("请输入替换成的文本: ").strip()
            pattern = input("请输入文件匹配模式（默认 *.txt）: ").strip() or "*.txt"
            recursive = input("是否递归处理子文件夹？(y/n): ").strip().lower() == "y"

            print(f"\n开始批量替换...")
            results = replace_in_files(folder_path, old_text, new_text, pattern, recursive)

            total = sum(results.values())
            print(f"\n✅ 批量替换完成！")
            print(f"   处理文件: {len(results)} 个")
            print(f"   替换总数: {total} 处")

            input("\n按回车继续...")

        elif choice == "3":
            # 正则表达式替换
            file_path = input("请输入文件路径: ").strip()
            pattern = input("请输入正则表达式: ").strip()
            replacement = input("请输入替换文本: ").strip()

            count = regex_replace(file_path, pattern, replacement)
            if count > 0:
                print(f"\n✅ 替换完成！共替换 {count} 处")
            else:
                print("\n⚠️  未找到匹配内容")

            input("\n按回车继续...")

        elif choice == "4":
            # 日志分析
            file_path = input("请输入日志文件路径: ").strip()
            custom_keywords = input("自定义关键词（用逗号分隔，留空使用默认）: ").strip()

            keywords = None
            if custom_keywords:
                keywords = [k.strip() for k in custom_keywords.split(",")]

            result = analyze_log_file(file_path, keywords)

            if result:
                print(f"\n📊 日志分析结果")
                print("-" * 40)
                print(f"总行数: {result['total_lines']}")
                print("\n关键词统计:")
                for keyword, count in result['stats'].items():
                    print(f"  {keyword}: {count} 次")

                if result['error_lines']:
                    print(f"\n错误行 (前5条):")
                    for line_num, line in result['error_lines'][:5]:
                        print(f"  行{line_num}: {line[:60]}...")

            input("\n按回车继续...")

        elif choice == "5":
            # 提取匹配内容
            file_path = input("请输入文件路径: ").strip()
            pattern = input("请输入正则表达式: ").strip()

            matches = extract_matches(file_path, pattern)

            if matches:
                print(f"\n找到 {len(matches)} 个匹配:")
                print("-" * 40)
                unique_matches = list(set(matches))
                for match in unique_matches[:20]:  # 只显示前20个不重复的
                    print(f"  • {match}")
                if len(unique_matches) > 20:
                    print(f"  ... 还有 {len(unique_matches) - 20} 个")
            else:
                print("\n未找到匹配内容")

            input("\n按回车继续...")

        elif choice == "6":
            # 预览替换
            file_path = input("请输入文件路径: ").strip()
            old_text = input("请输入要替换的文本: ").strip()
            new_text = input("请输入替换成的文本: ").strip()

            preview_replace(file_path, old_text, new_text)

            input("\n按回车继续...")

        else:
            print("❌ 无效选择，请重试\n")


if __name__ == "__main__":
    main()
