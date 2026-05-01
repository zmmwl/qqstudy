#!/bin/bash
# ============================================================
# C++ 三天学习计划 - 编译、运行、调试脚本
# 用法：
#   ./build.sh              编译所有 .cpp 文件
#   ./build.sh ch3_1        编译并运行 ch3_1.cpp
#   ./build.sh -d ch3_1     编译并用 gdb 调试 ch3_1.cpp
#   ./build.sh -c           清理所有编译产物
#   ./build.sh -l           列出所有 .cpp 文件
#   ./build.sh day1         编译 day1 的所有文件
#   ./build.sh day2         编译 day2 的所有文件
#   ./build.sh day3         编译 day3 的所有文件
# ============================================================

CLANG_DIR="$(cd "$(dirname "$0")" && pwd)"
BUILD_DIR="$CLANG_DIR/build"
CXX="g++"
CXXFLAGS="-std=c++17 -Wall -g"

# 创建构建目录
mkdir -p "$BUILD_DIR"

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m'  # No Color

# 显示帮助
show_help() {
    echo "用法: $0 [选项] [文件名]"
    echo ""
    echo "选项:"
    echo "  (无参数)        编译所有 .cpp 文件"
    echo "  ch3_1           编译并运行 ch3_1.cpp"
    echo "  -d ch3_1        编译并用 gdb 调试 ch3_1.cpp"
    echo "  -c              清理所有编译产物"
    echo "  -l              列出所有 .cpp 文件及对应章节"
    echo "  day1            编译 Day 1 的所有文件 (ch1-7)"
    echo "  day2            编译 Day 2 的所有文件 (ch8-14)"
    echo "  day3            编译 Day 3 的所有文件 (ch15-22)"
    echo "  -h, --help      显示此帮助信息"
    echo ""
    echo "示例:"
    echo "  $0 ch3_2        编译并运行第三章条件语句的代码"
    echo "  $0 -d ch19_1    用 gdb 调试 DFS 搜索代码"
    echo "  $0 day1         编译第一天所有示例代码"
}

# 编译单个文件
compile_one() {
    local src="$1"
    local base=$(basename "$src" .cpp)
    local out="$BUILD_DIR/$base"

    echo -e "${BLUE}编译 $src ...${NC}"
    $CXX $CXXFLAGS -o "$out" "$src" 2>&1
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ 编译成功: $out${NC}"
        return 0
    else
        echo -e "${RED}✗ 编译失败: $src${NC}"
        return 1
    fi
}

# 编译并运行单个文件
run_one() {
    local src="$1"
    local base=$(basename "$src" .cpp)

    # 先编译
    compile_one "$src"
    if [ $? -ne 0 ]; then
        return 1
    fi

    # 运行
    local out="$BUILD_DIR/$base"
    echo -e "${YELLOW}--- 运行 $base ---${NC}"
    timeout 10 "$out"
    local exit_code=$?
    if [ $exit_code -eq 124 ]; then
        echo -e "${RED}(运行超时，该程序可能需要键盘输入)${NC}"
    fi
    echo -e "${YELLOW}--- 运行结束 (退出码: $exit_code) ---${NC}"
    echo ""
    return $exit_code
}

# 调试单个文件
debug_one() {
    local src="$1"
    local base=$(basename "$src" .cpp)

    # 先编译（确保带 -g 调试信息）
    compile_one "$src"
    if [ $? -ne 0 ]; then
        return 1
    fi

    local out="$BUILD_DIR/$base"
    echo -e "${BLUE}启动 gdb 调试 $base ...${NC}"
    gdb "$out"
}

# 编译匹配前缀的所有文件
compile_prefix() {
    local prefix="$1"
    local count=0
    local fail=0

    for src in "$CLANG_DIR"/${prefix}*.cpp; do
        if [ -f "$src" ]; then
            compile_one "$src"
            if [ $? -eq 0 ]; then
                count=$((count + 1))
            else
                fail=$((fail + 1))
            fi
        fi
    done

    echo ""
    echo -e "${GREEN}成功: $count, ${RED}失败: $fail${NC}"
}

# 编译所有文件
compile_all() {
    local count=0
    local fail=0

    for src in "$CLANG_DIR"/ch*.cpp; do
        if [ -f "$src" ]; then
            compile_one "$src"
            if [ $? -eq 0 ]; then
                count=$((count + 1))
            else
                fail=$((fail + 1))
            fi
        fi
    done

    echo ""
    echo -e "编译完成: ${GREEN}成功 $count${NC}, ${RED}失败 $fail${NC}"
}

# 清理
clean() {
    echo -e "${YELLOW}清理编译产物...${NC}"
    rm -rf "$BUILD_DIR"
    echo -e "${GREEN}已清理 $BUILD_DIR${NC}"
}

# 列出文件
list_files() {
    echo -e "${BLUE}=== Day 1: C++ 基础 ===${NC}"
    echo "  第一章 程序基本概念"
    ls "$CLANG_DIR"/ch1_*.cpp 2>/dev/null | xargs -I{} basename {} | sed 's/^/    /'
    echo "  第二章 基本数据类型"
    ls "$CLANG_DIR"/ch2_*.cpp 2>/dev/null | xargs -I{} basename {} | sed 's/^/    /'
    echo "  第三章 程序基本语句"
    ls "$CLANG_DIR"/ch3_*.cpp 2>/dev/null | xargs -I{} basename {} | sed 's/^/    /'
    echo "  第四章 基本运算"
    ls "$CLANG_DIR"/ch4_*.cpp 2>/dev/null | xargs -I{} basename {} | sed 's/^/    /'
    echo "  第五章 数学库函数"
    ls "$CLANG_DIR"/ch5_*.cpp "$CLANG_DIR"/ch4_6_*.cpp 2>/dev/null | xargs -I{} basename {} | sed 's/^/    /'
    echo "  第六章 结构化程序设计"
    ls "$CLANG_DIR"/ch6_*.cpp 2>/dev/null | xargs -I{} basename {} | sed 's/^/    /'
    echo "  第七章 数组"
    ls "$CLANG_DIR"/ch7_*.cpp 2>/dev/null | xargs -I{} basename {} | sed 's/^/    /'

    echo ""
    echo -e "${BLUE}=== Day 2: 字符串、函数、STL ===${NC}"
    echo "  第八章 字符串"
    ls "$CLANG_DIR"/ch8_*.cpp 2>/dev/null | xargs -I{} basename {} | sed 's/^/    /'
    echo "  第九章 函数与递归"
    ls "$CLANG_DIR"/ch9_*.cpp 2>/dev/null | xargs -I{} basename {} | sed 's/^/    /'
    echo "  第十章 结构体与联合"
    ls "$CLANG_DIR"/ch10_*.cpp 2>/dev/null | xargs -I{} basename {} | sed 's/^/    /'
    echo "  第十一章 指针"
    ls "$CLANG_DIR"/ch11_*.cpp 2>/dev/null | xargs -I{} basename {} | sed 's/^/    /'
    echo "  第十二章 文件操作"
    ls "$CLANG_DIR"/ch12_*.cpp 2>/dev/null | xargs -I{} basename {} | sed 's/^/    /'
    echo "  第十三章 STL 模板"
    ls "$CLANG_DIR"/ch13_*.cpp 2>/dev/null | xargs -I{} basename {} | sed 's/^/    /'
    echo "  第十四章 数据结构"
    ls "$CLANG_DIR"/ch14_*.cpp 2>/dev/null | xargs -I{} basename {} | sed 's/^/    /'

    echo ""
    echo -e "${BLUE}=== Day 3: 算法与数学 ===${NC}"
    echo "  第十五章 算法入门"
    ls "$CLANG_DIR"/ch15_*.cpp 2>/dev/null | xargs -I{} basename {} | sed 's/^/    /'
    echo "  第十六章 枚举、模拟、贪心"
    ls "$CLANG_DIR"/ch16_*.cpp 2>/dev/null | xargs -I{} basename {} | sed 's/^/    /'
    echo "  第十七章 二分与分治"
    ls "$CLANG_DIR"/ch17_*.cpp 2>/dev/null | xargs -I{} basename {} | sed 's/^/    /'
    echo "  第十八章 排序算法"
    ls "$CLANG_DIR"/ch18_*.cpp 2>/dev/null | xargs -I{} basename {} | sed 's/^/    /'
    echo "  第十九章 DFS 与 BFS"
    ls "$CLANG_DIR"/ch19_*.cpp 2>/dev/null | xargs -I{} basename {} | sed 's/^/    /'
    echo "  第二十章 图论算法"
    ls "$CLANG_DIR"/ch20_*.cpp 2>/dev/null | xargs -I{} basename {} | sed 's/^/    /'
    echo "  第二十一章 动态规划"
    ls "$CLANG_DIR"/ch21_*.cpp 2>/dev/null | xargs -I{} basename {} | sed 's/^/    /'
    echo "  第二十二章 数学"
    ls "$CLANG_DIR"/ch22_*.cpp 2>/dev/null | xargs -I{} basename {} | sed 's/^/    /'

    echo ""
    local total=$(ls "$CLANG_DIR"/ch*.cpp 2>/dev/null | wc -l)
    echo "共 $total 个代码文件"
}

# ===== 主逻辑 =====
cd "$CLANG_DIR"

case "$1" in
    "")
        compile_all
        ;;
    -h|--help)
        show_help
        ;;
    -c|--clean)
        clean
        ;;
    -l|--list)
        list_files
        ;;
    -d|--debug)
        if [ -z "$2" ]; then
            echo "用法: $0 -d <文件名>  例: $0 -d ch3_1"
            exit 1
        fi
        src="${2%.cpp}.cpp"
        if [ ! -f "$src" ]; then
            echo -e "${RED}文件不存在: $src${NC}"
            exit 1
        fi
        debug_one "$src"
        ;;
    day1)
        echo -e "${BLUE}编译 Day 1 所有文件...${NC}"
        compile_prefix "ch1_" ; compile_prefix "ch2_" ; compile_prefix "ch3_"
        compile_prefix "ch4_" ; compile_prefix "ch5_" ; compile_prefix "ch6_"
        compile_prefix "ch7_"
        ;;
    day2)
        echo -e "${BLUE}编译 Day 2 所有文件...${NC}"
        compile_prefix "ch8_" ; compile_prefix "ch9_" ; compile_prefix "ch10_"
        compile_prefix "ch11_" ; compile_prefix "ch12_" ; compile_prefix "ch13_"
        compile_prefix "ch14_"
        ;;
    day3)
        echo -e "${BLUE}编译 Day 3 所有文件...${NC}"
        compile_prefix "ch15_" ; compile_prefix "ch16_" ; compile_prefix "ch17_"
        compile_prefix "ch18_" ; compile_prefix "ch19_" ; compile_prefix "ch20_"
        compile_prefix "ch21_" ; compile_prefix "ch22_"
        ;;
    ch*)
        src="${1%.cpp}.cpp"
        if [ ! -f "$src" ]; then
            echo -e "${RED}文件不存在: $src${NC}"
            echo "提示: 使用 $0 -l 查看所有可用文件"
            exit 1
        fi
        run_one "$src"
        ;;
    *)
        echo -e "${RED}未知参数: $1${NC}"
        show_help
        exit 1
        ;;
esac
