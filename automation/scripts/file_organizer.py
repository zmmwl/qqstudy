#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件整理器
==========
自动按文件类型分类整理文件夹

功能：
- 将散乱的文件按类型自动分类到不同文件夹
- 支持自定义分类规则
- 生成整理报告

使用方法：
    python file_organizer.py [文件夹路径]

示例：
    python file_organizer.py Downloads      # 整理下载文件夹
    python file_organizer.py                # 整理当前目录

作者: Python学习小组
"""

import os
import shutil
from datetime import datetime
from collections import defaultdict


def organize_files(folder_path, dry_run=False):
    """
    按文件类型整理文件夹中的文件

    参数：
        folder_path: str - 要整理的文件夹路径
        dry_run: bool - 如果为True，只显示将要执行的操作，不实际移动文件

    返回：
        dict - 各类型文件的数量统计

    示例调用：
        # 实际整理
        result = organize_files("Downloads")

        # 预览模式（不实际移动文件）
        result = organize_files("Downloads", dry_run=True)

    工作流程：
        1. 扫描文件夹中的所有文件
        2. 根据扩展名判断文件类型
        3. 创建对应的分类文件夹
        4. 将文件移动到对应文件夹
        5. 返回统计结果
    """
    # 检查文件夹是否存在
    if not os.path.exists(folder_path):
        print(f"❌ 错误：文件夹 '{folder_path}' 不存在！")
        return None

    # 定义文件分类规则
    # 可以根据需要添加更多类型
    categories = {
        "图片": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico"],
        "文档": [".txt", ".doc", ".docx", ".pdf", ".ppt", ".pptx", ".xls", ".xlsx", ".md", ".rtf"],
        "视频": [".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv", ".webm"],
        "音乐": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a"],
        "压缩包": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
        "代码": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".h", ".php", ".go", ".rs"],
        "可执行文件": [".exe", ".msi", ".dmg", ".app", ".deb", ".rpm"],
        "字体": [".ttf", ".otf", ".woff", ".woff2"],
        "其他": []  # 其他未分类文件
    }

    # 统计结果
    stats = defaultdict(int)
    moved_files = []

    # 获取所有文件
    files = [f for f in os.listdir(folder_path)
             if os.path.isfile(os.path.join(folder_path, f))]

    if not files:
        print(f"📁 文件夹 '{folder_path}' 中没有文件需要整理。")
        return dict(stats)

    print(f"🔍 开始整理 '{folder_path}'...")
    print(f"   共发现 {len(files)} 个文件\n")

    # 处理每个文件
    for filename in files:
        file_path = os.path.join(folder_path, filename)

        # 获取文件扩展名（小写）
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        # 确定文件类型
        target_category = "其他"
        for category, extensions in categories.items():
            if ext in extensions:
                target_category = category
                break

        # 目标文件夹路径
        target_folder = os.path.join(folder_path, target_category)
        target_path = os.path.join(target_folder, filename)

        # 更新统计
        stats[target_category] += 1

        if dry_run:
            # 预览模式：只显示，不移动
            print(f"  📋 {filename} → {target_category}/")
            moved_files.append((filename, target_category))
        else:
            # 创建目标文件夹
            os.makedirs(target_folder, exist_ok=True)

            # 检查目标位置是否已存在同名文件
            if os.path.exists(target_path):
                # 添加时间戳避免覆盖
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                name, ext = os.path.splitext(filename)
                new_filename = f"{name}_{timestamp}{ext}"
                target_path = os.path.join(target_folder, new_filename)
                print(f"  ⚠️  文件已存在，重命名为: {new_filename}")

            # 移动文件
            shutil.move(file_path, target_path)
            print(f"  ✅ {filename} → {target_category}/")
            moved_files.append((filename, target_category))

    return dict(stats)


def generate_report(folder_path, stats, output_file=None):
    """
    生成整理报告

    参数：
        folder_path: str - 整理的文件夹路径
        stats: dict - 统计结果
        output_file: str - 报告文件路径（可选，默认保存在目标文件夹）

    返回：
        str - 报告文件路径

    示例调用：
        report_path = generate_report("Downloads", stats)
    """
    if output_file is None:
        output_file = os.path.join(folder_path, "整理报告.txt")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write("           文件整理报告\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"整理时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"目标文件夹: {os.path.abspath(folder_path)}\n\n")

        f.write("分类统计:\n")
        f.write("-" * 30 + "\n")

        total = 0
        for category, count in sorted(stats.items(), key=lambda x: -x[1]):
            if count > 0:
                f.write(f"  {category}: {count} 个文件\n")
                total += count

        f.write("-" * 30 + "\n")
        f.write(f"  总计: {total} 个文件\n")

    return output_file


def preview_organization(folder_path):
    """
    预览整理效果（不实际移动文件）

    参数：
        folder_path: str - 要预览的文件夹路径

    返回：
        dict - 各类型文件的数量统计

    示例调用：
        preview_organization("Downloads")
    """
    print("📋 预览模式（不会实际移动文件）\n")
    return organize_files(folder_path, dry_run=True)


def main():
    """主函数：命令行入口"""
    import sys

    print("""
╔════════════════════════════════════════════════════════════╗
║                   文件整理器 v1.0                           ║
║              自动按类型分类整理文件                          ║
╚════════════════════════════════════════════════════════════╝
    """)

    # 获取目标文件夹
    if len(sys.argv) > 1:
        folder_path = sys.argv[1]
    else:
        folder_path = input("请输入要整理的文件夹路径（直接回车使用当前目录）: ").strip()
        if not folder_path:
            folder_path = "."

    # 转换为绝对路径
    folder_path = os.path.abspath(folder_path)

    # 确认操作
    print(f"\n📁 将要整理: {folder_path}")
    confirm = input("确认开始整理？(y/n，输入p预览): ").strip().lower()

    if confirm == "p":
        # 预览模式
        preview_organization(folder_path)
        print("\n预览完成！如需实际整理，请重新运行程序并选择 'y'")
    elif confirm == "y":
        # 执行整理
        stats = organize_files(folder_path)

        if stats:
            # 生成报告
            report_path = generate_report(folder_path, stats)
            print(f"\n📊 整理完成！")
            print(f"   共整理 {sum(stats.values())} 个文件")
            print(f"   报告已保存: {report_path}")
    else:
        print("❌ 操作已取消")


if __name__ == "__main__":
    main()
