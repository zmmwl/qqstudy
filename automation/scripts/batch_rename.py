#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量重命名工具
==============
强大的文件批量重命名工具

功能：
- 添加前缀/后缀
- 批量修改扩展名
- 序号编号
- 查找替换文件名中的文字
- 预览功能

使用方法：
    python batch_rename.py [文件夹路径]

示例：
    python batch_rename.py photos

作者: Python学习小组
"""

import os
import re
from datetime import datetime


def add_prefix(folder_path, prefix, pattern="*"):
    """
    给文件添加前缀

    参数：
        folder_path: str - 文件夹路径
        prefix: str - 要添加的前缀
        pattern: str - 文件匹配模式（如 "*.txt"），默认匹配所有文件

    返回：
        int - 重命名的文件数量

    示例调用：
        # 给所有文件添加日期前缀
        count = add_prefix("photos", "2024_")

        # 只给jpg文件添加前缀
        count = add_prefix("photos", "vacation_", "*.jpg")
    """
    count = 0
    files = get_matching_files(folder_path, pattern)

    for filename in files:
        old_path = os.path.join(folder_path, filename)

        if not os.path.isfile(old_path):
            continue

        # 添加前缀
        new_filename = prefix + filename
        new_path = os.path.join(folder_path, new_filename)

        # 检查是否会覆盖已有文件
        if os.path.exists(new_path) and old_path != new_path:
            print(f"  ⚠️  跳过（目标已存在）: {filename}")
            continue

        os.rename(old_path, new_path)
        print(f"  ✅ {filename} → {new_filename}")
        count += 1

    return count


def add_suffix(folder_path, suffix, pattern="*"):
    """
    给文件名添加后缀（在扩展名之前）

    参数：
        folder_path: str - 文件夹路径
        suffix: str - 要添加的后缀
        pattern: str - 文件匹配模式

    返回：
        int - 重命名的文件数量

    示例调用：
        # 给所有文件添加"_backup"后缀
        count = add_suffix("documents", "_backup")

        # 给图片添加尺寸后缀
        count = add_suffix("photos", "_800x600", "*.jpg")
    """
    count = 0
    files = get_matching_files(folder_path, pattern)

    for filename in files:
        old_path = os.path.join(folder_path, filename)

        if not os.path.isfile(old_path):
            continue

        # 分离文件名和扩展名
        name, ext = os.path.splitext(filename)
        new_filename = name + suffix + ext
        new_path = os.path.join(folder_path, new_filename)

        if os.path.exists(new_path) and old_path != new_path:
            print(f"  ⚠️  跳过（目标已存在）: {filename}")
            continue

        os.rename(old_path, new_path)
        print(f"  ✅ {filename} → {new_filename}")
        count += 1

    return count


def change_extension(folder_path, old_ext, new_ext):
    """
    批量修改文件扩展名

    参数：
        folder_path: str - 文件夹路径
        old_ext: str - 原扩展名（如 ".txt" 或 "txt"）
        new_ext: str - 新扩展名（如 ".md" 或 "md"）

    返回：
        int - 重命名的文件数量

    示例调用：
        # 将txt改为md
        count = change_extension("notes", ".txt", ".md")

        # 将jpeg改为jpg
        count = change_extension("photos", "jpeg", "jpg")
    """
    # 确保扩展名以点开头
    if not old_ext.startswith("."):
        old_ext = "." + old_ext
    if not new_ext.startswith("."):
        new_ext = "." + new_ext

    count = 0
    files = get_matching_files(folder_path, "*" + old_ext)

    for filename in files:
        if not filename.lower().endswith(old_ext.lower()):
            continue

        old_path = os.path.join(folder_path, filename)
        if not os.path.isfile(old_path):
            continue

        name = os.path.splitext(filename)[0]
        new_filename = name + new_ext
        new_path = os.path.join(folder_path, new_filename)

        if os.path.exists(new_path) and old_path != new_path:
            print(f"  ⚠️  跳过（目标已存在）: {filename}")
            continue

        os.rename(old_path, new_path)
        print(f"  ✅ {filename} → {new_filename}")
        count += 1

    return count


def sequential_rename(folder_path, base_name, start=1, digits=3, pattern="*"):
    """
    序号重命名（如 photo_001.jpg, photo_002.jpg...）

    参数：
        folder_path: str - 文件夹路径
        base_name: str - 基础文件名
        start: int - 起始编号，默认1
        digits: int - 编号位数，默认3（如001）
        pattern: str - 文件匹配模式

    返回：
        int - 重命名的文件数量

    示例调用：
        # 将图片重命名为 photo_001.jpg, photo_002.jpg...
        count = sequential_rename("vacation", "photo_", start=1, digits=3)

        # 从100开始编号，5位数
        count = sequential_rename("data", "data_", start=100, digits=5)
    """
    count = 0
    files = sorted(get_matching_files(folder_path, pattern))

    for i, filename in enumerate(files, start=start):
        old_path = os.path.join(folder_path, filename)

        if not os.path.isfile(old_path):
            continue

        # 获取扩展名
        ext = os.path.splitext(filename)[1]
        new_filename = f"{base_name}{str(i).zfill(digits)}{ext}"
        new_path = os.path.join(folder_path, new_filename)

        if os.path.exists(new_path) and old_path != new_path:
            print(f"  ⚠️  跳过（目标已存在）: {filename}")
            continue

        os.rename(old_path, new_path)
        print(f"  ✅ {filename} → {new_filename}")
        count += 1

    return count


def find_replace(folder_path, find_text, replace_text, pattern="*"):
    """
    在文件名中查找并替换文字

    参数：
        folder_path: str - 文件夹路径
        find_text: str - 要查找的文字
        replace_text: str - 替换成的文字
        pattern: str - 文件匹配模式

    返回：
        int - 重命名的文件数量

    示例调用：
        # 将文件名中的"副本"替换为"copy"
        count = find_replace("documents", "副本", "copy")

        # 只处理图片
        count = find_replace("photos", "IMG", "Vacation", "*.jpg")
    """
    count = 0
    files = get_matching_files(folder_path, pattern)

    for filename in files:
        if find_text not in filename:
            continue

        old_path = os.path.join(folder_path, filename)

        if not os.path.isfile(old_path):
            continue

        new_filename = filename.replace(find_text, replace_text)
        new_path = os.path.join(folder_path, new_filename)

        if os.path.exists(new_path) and old_path != new_path:
            print(f"  ⚠️  跳过（目标已存在）: {filename}")
            continue

        os.rename(old_path, new_path)
        print(f"  ✅ {filename} → {new_filename}")
        count += 1

    return count


def add_date_prefix(folder_path, pattern="*"):
    """
    给文件添加日期前缀（格式：YYYYMMDD_）

    参数：
        folder_path: str - 文件夹路径
        pattern: str - 文件匹配模式

    返回：
        int - 重命名的文件数量

    示例调用：
        count = add_date_prefix("photos")
        # 结果：20240115_photo.jpg
    """
    date_prefix = datetime.now().strftime("%Y%m%d_")
    return add_prefix(folder_path, date_prefix, pattern)


def lowercase(folder_path, pattern="*"):
    """
    将文件名转换为小写

    参数：
        folder_path: str - 文件夹路径
        pattern: str - 文件匹配模式

    返回：
        int - 重命名的文件数量

    示例调用：
        count = lowercase("photos")
        # PHOTO.JPG → photo.jpg
    """
    count = 0
    files = get_matching_files(folder_path, pattern)

    for filename in files:
        if filename == filename.lower():
            continue

        old_path = os.path.join(folder_path, filename)

        if not os.path.isfile(old_path):
            continue

        new_filename = filename.lower()
        new_path = os.path.join(folder_path, new_filename)

        if os.path.exists(new_path) and old_path != new_path:
            print(f"  ⚠️  跳过（目标已存在）: {filename}")
            continue

        os.rename(old_path, new_path)
        print(f"  ✅ {filename} → {new_filename}")
        count += 1

    return count


def get_matching_files(folder_path, pattern="*"):
    """
    获取匹配指定模式的文件列表

    参数：
        folder_path: str - 文件夹路径
        pattern: str - 匹配模式（如 "*.txt", "photo*"）

    返回：
        list - 匹配的文件名列表
    """
    import fnmatch

    if not os.path.exists(folder_path):
        return []

    all_files = os.listdir(folder_path)

    if pattern == "*":
        return all_files

    return fnmatch.filter(all_files, pattern)


def preview_rename(folder_path, operation, *args, **kwargs):
    """
    预览重命名效果（不实际执行）

    参数：
        folder_path: str - 文件夹路径
        operation: str - 操作类型（prefix/suffix/extension/sequential/replace）
        *args, **kwargs - 传递给对应函数的参数

    示例调用：
        preview_rename("photos", "prefix", "vacation_")
    """
    print(f"📋 预览模式 - 不会实际重命名文件\n")
    print(f"操作: {operation}")
    print("-" * 40)

    # 获取文件列表（不实际执行）
    files = get_matching_files(folder_path, kwargs.get("pattern", "*"))

    for filename in sorted(files):
        file_path = os.path.join(folder_path, filename)
        if not os.path.isfile(file_path):
            continue

        new_filename = simulate_rename(filename, operation, *args, **kwargs)
        if new_filename != filename:
            print(f"  {filename} → {new_filename}")


def simulate_rename(filename, operation, *args, **kwargs):
    """
    模拟重命名，返回新文件名
    """
    name, ext = os.path.splitext(filename)

    if operation == "prefix":
        return args[0] + filename
    elif operation == "suffix":
        return name + args[0] + ext
    elif operation == "extension":
        old_ext = args[0] if args[0].startswith(".") else "." + args[0]
        new_ext = args[1] if args[1].startswith(".") else "." + args[1]
        if filename.lower().endswith(old_ext.lower()):
            return name + new_ext
        return filename
    elif operation == "replace":
        return filename.replace(args[0], args[1])
    elif operation == "lowercase":
        return filename.lower()

    return filename


def print_menu():
    """打印菜单"""
    print("""
╔════════════════════════════════════════════════════════════╗
║               批量重命名工具 v1.0                           ║
╠════════════════════════════════════════════════════════════╣
║  1. 添加前缀                                                ║
║  2. 添加后缀                                                ║
║  3. 修改扩展名                                              ║
║  4. 序号重命名                                              ║
║  5. 查找替换                                                ║
║  6. 添加日期前缀                                            ║
║  7. 转换为小写                                              ║
║  p. 预览当前文件                                            ║
║  q. 退出                                                    ║
╚════════════════════════════════════════════════════════════╝
    """)


def main():
    """主函数：命令行入口"""
    import sys

    # 获取目标文件夹
    if len(sys.argv) > 1:
        folder_path = sys.argv[1]
    else:
        folder_path = input("请输入文件夹路径（直接回车使用当前目录）: ").strip()
        if not folder_path:
            folder_path = "."

    folder_path = os.path.abspath(folder_path)

    if not os.path.exists(folder_path):
        print(f"❌ 文件夹不存在: {folder_path}")
        return

    while True:
        print_menu()
        print(f"当前文件夹: {folder_path}")
        choice = input("\n请选择操作: ").strip().lower()

        if choice == "q":
            print("👋 再见！")
            break

        elif choice == "p":
            # 预览文件
            print("\n当前文件列表：")
            print("-" * 40)
            for f in sorted(os.listdir(folder_path)):
                if os.path.isfile(os.path.join(folder_path, f)):
                    print(f"  📄 {f}")
            print()

        elif choice == "1":
            # 添加前缀
            prefix = input("请输入前缀: ").strip()
            confirm = input(f"确认给所有文件添加前缀 '{prefix}'？(y/n): ").strip().lower()
            if confirm == "y":
                count = add_prefix(folder_path, prefix)
                print(f"\n✅ 完成！共重命名 {count} 个文件\n")

        elif choice == "2":
            # 添加后缀
            suffix = input("请输入后缀: ").strip()
            confirm = input(f"确认给所有文件添加后缀 '{suffix}'？(y/n): ").strip().lower()
            if confirm == "y":
                count = add_suffix(folder_path, suffix)
                print(f"\n✅ 完成！共重命名 {count} 个文件\n")

        elif choice == "3":
            # 修改扩展名
            old_ext = input("请输入原扩展名（如 txt）: ").strip()
            new_ext = input("请输入新扩展名（如 md）: ").strip()
            confirm = input(f"确认将 .{old_ext} 改为 .{new_ext}？(y/n): ").strip().lower()
            if confirm == "y":
                count = change_extension(folder_path, old_ext, new_ext)
                print(f"\n✅ 完成！共重命名 {count} 个文件\n")

        elif choice == "4":
            # 序号重命名
            base_name = input("请输入基础文件名（如 photo_）: ").strip()
            start = input("起始编号（默认1）: ").strip()
            start = int(start) if start.isdigit() else 1
            digits = input("编号位数（默认3）: ").strip()
            digits = int(digits) if digits.isdigit() else 3
            confirm = input(f"确认序号重命名？(y/n): ").strip().lower()
            if confirm == "y":
                count = sequential_rename(folder_path, base_name, start, digits)
                print(f"\n✅ 完成！共重命名 {count} 个文件\n")

        elif choice == "5":
            # 查找替换
            find_text = input("请输入要查找的文字: ").strip()
            replace_text = input("请输入替换成的文字: ").strip()
            confirm = input(f"确认将 '{find_text}' 替换为 '{replace_text}'？(y/n): ").strip().lower()
            if confirm == "y":
                count = find_replace(folder_path, find_text, replace_text)
                print(f"\n✅ 完成！共重命名 {count} 个文件\n")

        elif choice == "6":
            # 添加日期前缀
            confirm = input("确认添加日期前缀？(y/n): ").strip().lower()
            if confirm == "y":
                count = add_date_prefix(folder_path)
                print(f"\n✅ 完成！共重命名 {count} 个文件\n")

        elif choice == "7":
            # 转换为小写
            confirm = input("确认将所有文件名转为小写？(y/n): ").strip().lower()
            if confirm == "y":
                count = lowercase(folder_path)
                print(f"\n✅ 完成！共重命名 {count} 个文件\n")

        else:
            print("❌ 无效选择，请重试\n")


if __name__ == "__main__":
    main()
