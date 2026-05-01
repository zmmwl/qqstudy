#!/usr/bin/env python3
"""
从 day1.md, day2.md, day3.md 中提取所有 C++ 代码块，
生成独立的 .cpp 文件，并在 markdown 中插入对应的文件名引用。
"""

import re
import os
import sys

CLANG_DIR = os.path.dirname(os.path.abspath(__file__))

def extract_code_blocks(md_content):
    """
    提取所有 cpp 代码块及其前面的章节标题。
    返回列表：[(章节标识, 代码内容, 在md中的起始行号), ...]
    """
    lines = md_content.split('\n')
    results = []
    current_section = None
    code_counter = {}  # 每个section的代码计数器

    i = 0
    while i < len(lines):
        line = lines[i]

        # 检测章节标题
        # 匹配 ### 1.1 xxx 或 ### 15.2 xxx 等
        m = re.match(r'^###\s+(\d+\.\d+)\s+(.*)', line)
        if m:
            current_section = m.group(1)  # e.g. "1.1"
            code_counter[current_section] = 0
            i += 1
            continue

        # 也匹配 ## 第五章 之类（给没有子章节号但有代码的情况）
        m2 = re.match(r'^##\s+第([一二三四五六七八九十]+)章\s+(.*)', line)
        if m2:
            # 如果没有更细的 ### 子标题，就用章节号
            chapter_map = {'一': '05', '二': '06', '三': '07', '四': '04',
                          '五': '05', '六': '06', '七': '07', '八': '08',
                          '九': '09', '十': '10', '十一': '11', '十二': '12',
                          '十三': '13', '十四': '14', '十五': '15', '十六': '16',
                          '十七': '17', '十八': '18', '十九': '19', '二十': '20',
                          '二十一': '21', '二十二': '22'}
            # 我们不在这里处理，因为章节标题后面通常有子标题
            i += 1
            continue

        # 检测 cpp 代码块开始
        if line.strip() == '```cpp':
            start_line = i
            code_lines = []
            i += 1
            while i < len(lines) and lines[i].strip() != '```':
                code_lines.append(lines[i])
                i += 1

            if current_section:
                code_counter[current_section] = code_counter.get(current_section, 0) + 1
                count = code_counter[current_section]
                if count == 1:
                    filename = f"ch{current_section.replace('.', '_')}.cpp"
                else:
                    filename = f"ch{current_section.replace('.', '_')}_{count}.cpp"
                results.append((filename, '\n'.join(code_lines), start_line))
            # else: 没有 section 标识的代码块，跳过

        i += 1

    return results


def generate_cpp_file(filename, code):
    """生成 .cpp 文件"""
    filepath = os.path.join(CLANG_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(code + '\n')
    return filepath


def update_markdown(md_content, code_blocks):
    """在 markdown 中每个 cpp 代码块前插入文件名引用"""
    lines = md_content.split('\n')
    # 从后往前插入，避免行号偏移
    insertions = []

    # 重新扫描找到每个 ```cpp 的位置
    current_section = None
    code_counter = {}
    block_idx = 0

    for i, line in enumerate(lines):
        m = re.match(r'^###\s+(\d+\.\d+)\s+(.*)', line)
        if m:
            current_section = m.group(1)
            code_counter[current_section] = 0
            continue

        if line.strip() == '```cpp':
            if current_section and block_idx < len(code_blocks):
                code_counter[current_section] = code_counter.get(current_section, 0) + 1
                filename = code_blocks[block_idx][0]
                insertions.append((i, filename))
                block_idx += 1

    # 从后往前插入
    for line_num, filename in reversed(insertions):
        lines.insert(line_num, f'<!-- 对应代码文件：{filename} -->')

    return '\n'.join(lines)


def main():
    md_files = ['day1.md', 'day2.md', 'day3.md']

    total_files = 0

    for md_file in md_files:
        md_path = os.path.join(CLANG_DIR, md_file)
        if not os.path.exists(md_path):
            print(f"跳过不存在的文件: {md_file}")
            continue

        print(f"\n{'='*50}")
        print(f"处理: {md_file}")
        print(f"{'='*50}")

        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # 提取代码块
        code_blocks = extract_code_blocks(md_content)
        print(f"  找到 {len(code_blocks)} 个代码块")

        # 生成 .cpp 文件
        for filename, code, line_num in code_blocks:
            filepath = generate_cpp_file(filename, code)
            total_files += 1
            print(f"  生成: {filename} (第 {line_num + 1} 行)")

        # 更新 markdown
        updated_md = update_markdown(md_content, code_blocks)
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(updated_md)
        print(f"  已更新 {md_file}，插入文件名引用")

    print(f"\n{'='*50}")
    print(f"完成！共生成 {total_files} 个 .cpp 文件")
    print(f"{'='*50}")


if __name__ == '__main__':
    main()
