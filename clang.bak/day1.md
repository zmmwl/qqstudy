# Day 1: C++ 基础与程序设计

> **学习目标**：从零开始掌握 C++ 的基本语法，能够独立编写包含输入输出、条件判断、循环、数组的小程序。

---

## 第一章 程序基本概念

### 1.1 你的第一个 C++ 程序

```cpp
#include <iostream>  // 头文件：包含输入输出功能
using namespace std; // 使用标准名字空间，这样可以直接写 cout 而不是 std::cout

int main() {         // main 是程序入口，每个程序必须有且只有一个 main 函数
    cout << "Hello, World!" << endl;  // cout 是输出，<< 是输出运算符，endl 换行
    return 0;        // 返回 0 表示程序正常结束
}
```

**关键概念解释**：
- `#include <iostream>`：`#include` 是预处理指令，告诉编译器把 `iostream` 头文件的内容包含进来。`iostream` 提供了输入（cin）和输出（cout）功能。
- `using namespace std;`：C++ 标准库的所有内容都在 `std`（standard）名字空间中。这行代码让我们不用每次都写 `std::` 前缀。
- `int main()`：程序的入口点。`int` 表示返回整数，`()` 里可以放参数，花括号 `{}` 里是函数体。
- `cout << "Hello" << endl;`：`cout`（character output）是标准输出流，`<<` 把数据"推向"屏幕，`endl` 换行并刷新缓冲区。
- `return 0;`：向操作系统报告程序正常退出。

### 1.2 标识符、关键字、常量、变量、字符串、表达式

```cpp
#include <iostream>
using namespace std;

int main() {
    // 【标识符】程序员自己起的名字，比如变量名、函数名
    // 规则：只能用字母、数字、下划线，不能以数字开头，不能是关键字
    int myAge = 12;        // myAge 是一个标识符
    int student_count = 30; // student_count 是一个标识符

    // 【关键字】C++ 保留的特殊单词，有固定含义，不能用作标识符
    // 常见关键字：int, double, char, bool, if, else, for, while, return, const, void...
    // int age = 10; ← "int" 就是关键字

    // 【常量】值不能改变的量
    const double PI = 3.14159;   // 用 const 定义的常量，之后不能修改
    // PI = 3.14;  // 错误！常量不能被重新赋值

    // 【变量】值可以改变的量
    int score = 95;      // 定义变量 score，初始值为 95
    score = 88;          // 可以修改变量的值
    cout << "score = " << score << endl;  // 输出 88

    // 【字符串】用双引号括起来的字符序列
    string name = "Xiao Ming";  // string 类型存储字符串
    cout << "name = " << name << endl;

    // 【表达式】由运算符和操作数组成的算式
    int a = 10, b = 3;
    int sum = a + b;       // a + b 是算术表达式
    bool isEqual = (a == b); // a == b 是关系表达式
    bool result = (a > 5) && (b < 10); // 逻辑表达式

    cout << "sum = " << sum << endl;           // 13
    cout << "isEqual = " << isEqual << endl;   // 0 (false)
    cout << "result = " << result << endl;     // 1 (true)

    return 0;
}
```

### 1.3 变量的命名规则与定义

```cpp
#include <iostream>
using namespace std;

int main() {
    // 命名规则：
    // 1. 只能用字母(a-z, A-Z)、数字(0-9)、下划线(_)
    // 2. 不能以数字开头
    // 3. 不能是 C++ 关键字（如 int, return, if 等）
    // 4. 区分大小写（age 和 Age 是不同的变量）

    int age = 12;          // 合法
    int _count = 5;        // 合法（下划线开头）
    int student2 = 10;     // 合法
    // int 2student = 10;  // 非法！不能以数字开头
    // int my-name = 10;   // 非法！不能用连字符
    // int int = 10;       // 非法！不能用关键字

    // 好的命名习惯：
    int studentAge = 12;     // 驼峰命名法
    int student_age = 12;    // 下划线命名法
    // 命名要有意义，让别人一看就知道变量存的是什么

    // 变量必须先定义（声明）再使用
    // 定义时可以不给初始值（但不推荐，未初始化的值是不确定的）
    int x;           // 只定义，未初始化（x 的值不确定）
    int y = 0;       // 定义并初始化为 0（推荐）
    int z(10);       // 另一种初始化方式，z = 10
    int w{20};       // C++11 的初始化方式，w = 20

    cout << "y = " << y << ", z = " << z << ", w = " << w << endl;

    return 0;
}
```

### 1.4 头文件与名字空间

```cpp
// 常用头文件：
// #include <iostream>   — 输入输出（cin, cout）
// #include <cstdio>     — C 风格输入输出（scanf, printf）
// #include <cmath>      — 数学函数（sqrt, abs, sin 等）
// #include <cstring>    — 字符串处理函数（strlen, strcpy 等）
// #include <string>     — string 类
// #include <algorithm>  — 算法库（sort, min, max 等）
// #include <vector>     — vector 容器
// #include <stack>      — 栈容器
// #include <queue>      — 队列容器

// 名字空间 std：
// 如果不写 "using namespace std;"，就需要加前缀：
// std::cout << "Hello" << std::endl;
// 写了 "using namespace std;" 后可以直接写：
// cout << "Hello" << endl;

// 竞赛中常用的万能头文件（包含几乎所有标准库）：
// #include <bits/stdc++.h>
// 注意：这是非标准的，某些编译器可能不支持
```

### 1.5 编辑、编译、解释、调试

```
编辑(Editor)：编写源代码（.cpp 文件），就像写作文
编译(Compiler)：把源代码翻译成机器能执行的程序，就像把中文翻译成英文
    常用编译命令：g++ -o program program.cpp
解释(Interpreter)：逐行读取并执行代码，Python 就是解释型语言
调试(Debug)：找出并修复程序中的错误（bug）
    常见错误类型：
    - 语法错误(Syntax Error)：代码格式不对，编译器直接报错
      例如：忘记分号、括号不匹配
    - 逻辑错误(Logic Error)：代码能运行但结果不对
      例如：把 + 写成了 -
    - 运行时错误(Runtime Error)：运行时才出错
      例如：除以 0、数组越界
```

---

## 第二章 基本数据类型

### 2.1 整数型：int 和 long long

```cpp
#include <iostream>
using namespace std;

int main() {
    // int：整数类型，占 4 个字节（32位），范围约 -21亿 到 +21亿
    int a = 42;
    int b = -100;
    int c = 0;
    cout << "int a = " << a << endl;

    // int 能表示的最大值和最小值
    int maxInt = 2147483647;    // 2^31 - 1
    int minInt = -2147483648;   // -2^31
    cout << "int 最大值: " << maxInt << endl;
    cout << "int 最小值: " << minInt << endl;

    // long long：长整数类型，占 8 个字节（64位），范围约 -9.2×10^18 到 +9.2×10^18
    // 当数字可能超过 21 亿时，必须用 long long
    long long bigNum = 9223372036854775807LL;  // 注意末尾的 LL
    cout << "long long 大数: " << bigNum << endl;

    // 注意：整数溢出！
    int overflow = 2147483647;
    overflow = overflow + 1;  // 溢出！变成负数
    cout << "溢出后: " << overflow << endl;  // -2147483648

    // 无符号类型：只能存非负数，范围翻倍
    unsigned int positiveOnly = 4294967295U;  // 0 到 2^32-1

    return 0;
}
```

**竞赛提示**：当题目数据范围超过 `10^9` 时，一定要用 `long long`！

### 2.2 实数型：float 和 double

```cpp
#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // float：单精度浮点数，占 4 字节，约 6-7 位有效数字
    float f = 3.14f;       // 注意末尾的 f
    float f2 = 3.14159265358979f;
    cout << "float f2 = " << f2 << endl;  // 精度会丢失！

    // double：双精度浮点数，占 8 字节，约 15-16 位有效数字
    // 竞赛和日常编程中推荐使用 double
    double d = 3.141592653589793;
    cout << "double d = " << d << endl;   // 精度保持得好

    // 浮点数的精度问题（非常重要！）
    double a = 0.1 + 0.2;
    cout << "0.1 + 0.2 = " << a << endl;  // 可能输出 0.30000000000000004
    // 所以浮点数比较不能用 ==，要用误差范围
    double eps = 1e-9;  // 误差范围：10的-9次方
    if (abs(a - 0.3) < eps) {
        cout << "a 约等于 0.3" << endl;
    }

    // 科学计数法
    double big = 1.5e10;    // 1.5 × 10^10 = 15000000000.0
    double small = 2.5e-3;  // 2.5 × 10^(-3) = 0.0025

    // 格式化输出浮点数
    printf("保留2位小数: %.2f\n", 3.14159);   // 3.14
    printf("保留4位小数: %.4f\n", 3.14159);   // 3.1416

    return 0;
}
```

### 2.3 字符型：char

```cpp
#include <iostream>
using namespace std;

int main() {
    // char：字符类型，占 1 个字节，存储单个字符
    // 字符用单引号括起来
    char ch1 = 'A';
    char ch2 = '0';
    char ch3 = ' ';   // 空格也是字符

    cout << "ch1 = " << ch1 << endl;  // A
    cout << "ch2 = " << ch2 << endl;  // 0

    // 字符在计算机中以 ASCII 码存储
    // 'A' 的 ASCII 码是 65，'a' 是 97，'0' 是 48
    cout << "'A' 的 ASCII 码: " << (int)ch1 << endl;  // 65
    cout << "'a' 的 ASCII 码: " << (int)'a' << endl;  // 97
    cout << "'0' 的 ASCII 码: " << (int)'0' << endl;  // 48

    // 字符和整数可以互相转换
    char ch4 = 66;              // ASCII 码 66 对应 'B'
    cout << "ASCII 66 = " << ch4 << endl;  // B

    // 大小写转换
    char upper = 'A';
    char lower = upper + 32;    // 大写字母 + 32 = 对应小写字母
    cout << upper << " -> " << lower << endl;  // A -> a

    char lower2 = 'z';
    char upper2 = lower2 - 32;  // 小写字母 - 32 = 对应大写字母
    cout << lower2 << " -> " << upper2 << endl;  // z -> Z

    // 判断字符类型
    char c = '5';
    if (c >= '0' && c <= '9') cout << c << " 是数字" << endl;
    if (c >= 'A' && c <= 'Z') cout << c << " 是大写字母" << endl;
    if (c >= 'a' && c <= 'z') cout << c << " 是小写字母" << endl;

    return 0;
}
```

### 2.4 布尔型：bool

```cpp
#include <iostream>
using namespace std;

int main() {
    // bool：布尔类型，只有两个值：true（真）和 false（假）
    bool isStudent = true;
    bool isOld = false;

    cout << "isStudent = " << isStudent << endl;  // 1（true 输出为 1）
    cout << "isOld = " << isOld << endl;          // 0（false 输出为 0）

    // bool 类型本质上就是整数：true = 1, false = 0
    cout << true + true << endl;   // 2
    cout << false + 10 << endl;    // 10

    // 比较运算的结果是 bool 类型
    int a = 5, b = 10;
    bool result = (a > b);   // 5 > 10 为 false
    cout << "5 > 10 ? " << result << endl;  // 0

    // 在 C++ 中，非零值都是 true，0 是 false
    bool x = 42;    // true（非零）
    bool y = 0;     // false
    bool z = -3;    // true（非零，即使是负数）

    return 0;
}
```

---

## 第三章 程序基本语句

### 3.1 输入输出语句

```cpp
#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // ===== cin 和 cout（C++ 风格）=====

    // 输出 cout
    cout << "Hello" << endl;              // 输出字符串并换行
    cout << "Age: " << 12 << endl;        // 输出多个内容，用 << 连接
    int age = 12;
    cout << "I am " << age << " years old" << endl;

    // 输入 cin
    int x;
    cout << "请输入一个整数: ";
    cin >> x;                    // >> 是输入运算符
    cout << "你输入了: " << x << endl;

    // 连续输入多个值（用空格或回车分隔）
    int a, b;
    cin >> a >> b;
    cout << "a + b = " << a + b << endl;

    // ===== scanf 和 printf（C 风格，速度更快）=====
    // 竞赛中经常使用，因为输入输出速度快

    int n;
    double d;
    char c;
    scanf("%d", &n);      // %d 读入整数，&n 是变量 n 的地址
    scanf("%lf", &d);     // %lf 读入 double（注意不是 %f）
    scanf("%c", &c);      // %c 读入字符
    scanf("%s", str);     // %s 读入字符串（字符数组）

    printf("整数: %d\n", n);      // %d 输出整数
    printf("浮点数: %.2f\n", d);  // %.2f 保留2位小数输出
    printf("字符: %c\n", c);      // %c 输出字符
    printf("字符串: %s\n", str);  // %s 输出字符串

    // printf 格式化：
    // %d  — 整数
    // %ld — long 类型整数
    // %lld — long long 类型整数
    // %f  — float（输出时 double 也用 %f）
    // %lf — double（仅 scanf 用）
    // %c  — 字符
    // %s  — 字符串
    // %.nf — 保留 n 位小数
    // %02d — 至少2位，不足前面补0（如 01, 02, ..., 12）

    // 赋值语句
    int m = 10;        // 定义时赋值（初始化）
    m = 20;            // 重新赋值
    m = m + 5;         // 把 m+5 的结果赋给 m，现在 m = 25
    m += 5;            // 等价于 m = m + 5，现在 m = 30
    m -= 3;            // 等价于 m = m - 3
    m *= 2;            // 等价于 m = m * 2
    m /= 4;            // 等价于 m = m / 4
    m %= 5;            // 等价于 m = m % 5（取余）

    // 复合语句（用花括号括起来的多条语句）
    {
        int temp = 100;
        cout << temp << endl;
    }
    // cout << temp;  // 错误！temp 只在上面的花括号内有效

    return 0;
}
```

### 3.2 条件语句：if 和 switch

```cpp
#include <iostream>
using namespace std;

int main() {
    // ===== if 语句 =====

    // 基本 if
    int score = 85;
    if (score >= 60) {
        cout << "及格了！" << endl;
    }

    // if-else
    if (score >= 90) {
        cout << "优秀" << endl;
    } else if (score >= 80) {
        cout << "良好" << endl;
    } else if (score >= 60) {
        cout << "及格" << endl;
    } else {
        cout << "不及格" << endl;
    }
    // 输出：良好

    // 多层嵌套的 if
    int age = 16;
    bool hasTicket = true;
    if (age >= 18) {
        if (hasTicket) {
            cout << "可以进入" << endl;
        } else {
            cout << "需要买票" << endl;
        }
    } else {
        if (age >= 12) {
            cout << "需要成人陪同" << endl;
        } else {
            cout << "禁止入内" << endl;
        }
    }

    // ===== switch 语句 =====
    // 适用于根据一个整数值选择不同分支的情况
    int day = 3;
    switch (day) {
        case 1:
            cout << "星期一" << endl;
            break;     // break 不能忘！否则会继续执行下面的 case
        case 2:
            cout << "星期二" << endl;
            break;
        case 3:
            cout << "星期三" << endl;
            break;
        case 4:
            cout << "星期四" << endl;
            break;
        case 5:
            cout << "星期五" << endl;
            break;
        case 6:
        case 7:
            cout << "周末" << endl;  // case 6 和 7 共享同一段代码
            break;
        default:
            cout << "无效的日期" << endl;  // 以上 case 都不匹配时执行
    }

    return 0;
}
```

### 3.3 循环语句：for、while、do-while

```cpp
#include <iostream>
using namespace std;

int main() {
    // ===== for 循环 =====
    // for (初始化; 条件; 更新) { 循环体 }
    // 最常用的循环，适合知道循环次数的情况

    // 输出 1 到 10
    for (int i = 1; i <= 10; i++) {
        cout << i << " ";
    }
    cout << endl;  // 1 2 3 4 5 6 7 8 9 10

    // 计算 1+2+3+...+100
    int sum = 0;
    for (int i = 1; i <= 100; i++) {
        sum += i;
    }
    cout << "1到100的和: " << sum << endl;  // 5050

    // ===== while 循环 =====
    // while (条件) { 循环体 }
    // 先判断条件，条件为真就执行循环体

    // 求 n 的位数
    int n = 12345;
    int count = 0;
    int temp = n;
    while (temp > 0) {
        temp /= 10;    // 去掉最后一位
        count++;       // 位数加 1
    }
    cout << n << " 有 " << count << " 位" << endl;  // 5 位

    // ===== do-while 循环 =====
    // do { 循环体 } while (条件);
    // 先执行一次循环体，再判断条件（至少执行一次）

    // 猜数字游戏（简化版）
    int secret = 42;
    int guess;
    do {
        cout << "请猜一个数字: ";
        cin >> guess;
        if (guess > secret) cout << "太大了" << endl;
        if (guess < secret) cout << "太小了" << endl;
    } while (guess != secret);
    cout << "猜对了！" << endl;

    // ===== break 和 continue =====
    // break：直接跳出整个循环
    // continue：跳过本次循环剩余部分，进入下一次

    // break 示例：找到第一个能被 7 整除的数
    for (int i = 100; i <= 200; i++) {
        if (i % 7 == 0) {
            cout << "找到: " << i << endl;  // 105
            break;  // 找到后立即退出循环
        }
    }

    // continue 示例：输出 1-20 中所有奇数
    for (int i = 1; i <= 20; i++) {
        if (i % 2 == 0) {
            continue;  // 偶数跳过，不执行下面的输出
        }
        cout << i << " ";
    }
    cout << endl;  // 1 3 5 7 9 11 13 15 17 19

    return 0;
}
```

### 3.4 多层循环（嵌套循环）

```cpp
#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // 打印乘法口诀表
    for (int i = 1; i <= 9; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%d×%d=%-4d", j, i, i * j);  // %-4d 左对齐，占4位
        }
        cout << endl;
    }

    cout << "----------" << endl;

    // 打印星号三角形
    //     *
    //    ***
    //   *****
    //  *******
    // *********
    int n = 5;
    for (int i = 1; i <= n; i++) {
        // 打印空格
        for (int j = 1; j <= n - i; j++) {
            cout << " ";
        }
        // 打印星号
        for (int j = 1; j <= 2 * i - 1; j++) {
            cout << "*";
        }
        cout << endl;
    }

    cout << "----------" << endl;

    // 枚举：百钱买百鸡问题
    // 公鸡5元一只，母鸡3元一只，小鸡1元三只，100元买100只，各买多少？
    for (int x = 0; x <= 20; x++) {         // 公鸡最多 100/5=20 只
        for (int y = 0; y <= 33; y++) {     // 母鸡最多 100/3=33 只
            int z = 100 - x - y;             // 小鸡数量
            if (z >= 0 && z % 3 == 0 && 5 * x + 3 * y + z / 3 == 100) {
                cout << "公鸡:" << x << " 母鸡:" << y << " 小鸡:" << z << endl;
            }
        }
    }

    return 0;
}
```

---

## 第四章 基本运算

### 4.1 算术运算

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 17, b = 5;

    // 加减乘
    cout << "a + b = " << a + b << endl;  // 22
    cout << "a - b = " << a - b << endl;  // 12
    cout << "a * b = " << a * b << endl;  // 85

    // 整数除法（向零取整，即直接丢弃小数部分）
    cout << "a / b = " << a / b << endl;  // 3（不是3.4！）

    // 求余（取模）运算：a % b = a 除以 b 的余数
    cout << "a % b = " << a % b << endl;  // 2（因为 17 = 3*5 + 2）

    // 注意：整数除法和求余的一些特殊情况
    cout << "7 / 2 = " << 7 / 2 << endl;     // 3（不是 3.5）
    cout << "-7 / 2 = " << -7 / 2 << endl;   // -3（向零取整）
    cout << "-7 % 2 = " << -7 % 2 << endl;   // -1

    // 如果需要得到精确的除法结果，至少有一个操作数要转成浮点数
    cout << "7.0 / 2 = " << 7.0 / 2 << endl;   // 3.5
    cout << "(double)7 / 2 = " << (double)7 / 2 << endl;  // 3.5

    // 求余运算的常见用途：
    // 1. 判断奇偶：n % 2 == 0 偶数，n % 2 == 1 奇数
    // 2. 取个位数：n % 10 得到个位数字
    // 3. 循环计数：i % n 使值在 0~n-1 之间循环

    int num = 12345;
    cout << "个位: " << num % 10 << endl;       // 5
    cout << "十位: " << num / 10 % 10 << endl;  // 4
    cout << "百位: " << num / 100 % 10 << endl; // 3

    return 0;
}
```

### 4.2 关系运算

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 5, b = 10;

    // 关系运算的结果是 bool 值（true=1 或 false=0）
    cout << (a > b) << endl;    // 0 (false)，5 不大于 10
    cout << (a >= b) << endl;   // 0 (false)
    cout << (a < b) << endl;    // 1 (true)，5 小于 10
    cout << (a <= b) << endl;   // 1 (true)
    cout << (a == b) << endl;   // 0 (false)，5 不等于 10
    cout << (a != b) << endl;   // 1 (true)，5 不等于 10

    // 注意：== 是比较，= 是赋值！这是初学者最常犯的错误！
    // if (a = 5)  ← 这是赋值！永远为 true！
    // if (a == 5) ← 这才是比较

    // 浮点数比较不能用 ==（因为有精度误差）
    double x = 0.1 + 0.2;
    // if (x == 0.3) ← 可能判断错误！
    // 正确做法：
    if (abs(x - 0.3) < 1e-9) {
        cout << "x 约等于 0.3" << endl;
    }

    return 0;
}
```

### 4.3 逻辑运算

```cpp
#include <iostream>
using namespace std;

int main() {
    // && 逻辑与（AND）：两个条件都为真，结果才为真
    // || 逻辑或（OR）：只要有一个条件为真，结果就为真
    // !  逻辑非（NOT）：取反，真变假，假变真

    int age = 15;
    int score = 90;

    // 逻辑与 &&：两个条件都要满足
    if (age >= 12 && score >= 80) {
        cout << "符合条件" << endl;
    }

    // 逻辑或 ||：满足其中一个条件即可
    if (score >= 90 || age >= 18) {
        cout << "满足至少一个条件" << endl;
    }

    // 逻辑非 !
    bool isRaining = false;
    if (!isRaining) {
        cout << "没下雨，可以去玩" << endl;
    }

    // 短路求值（重要！）
    // 对于 &&：如果左边为 false，右边不再计算
    // 对于 ||：如果左边为 true，右边不再计算
    int x = 0;
    // if (x != 0 && 10 / x > 1) ← 安全！x==0 时右边不会计算，不会除以0

    // 德摩根定律
    // !(a && b) 等价于 (!a || !b)
    // !(a || b) 等价于 (!a && !b)

    // 真值表：
    // a      b      a&&b   a||b   !a
    // true   true   true   true   false
    // true   false  false  true   false
    // false  true   false  true   true
    // false  false  false  false  true

    return 0;
}
```

### 4.4 自增与自减运算

```cpp
#include <iostream>
using namespace std;

int main() {
    // ++ 自增（加1），-- 自减（减1）

    int a = 5;

    // 前置 ++：先加1，再使用值
    int b = ++a;    // a 先变成 6，再把 6 赋给 b
    cout << "a=" << a << ", b=" << b << endl;  // a=6, b=6

    // 后置 ++：先使用值，再加1
    int c = a++;    // 先把 a 的值(6)赋给 c，然后 a 变成 7
    cout << "a=" << a << ", c=" << c << endl;  // a=7, c=6

    // 前置 -- 和 后置 -- 同理
    int d = --a;    // a 先变成 6，赋给 d
    int e = a--;    // 先把 a(6) 赋给 e，a 变成 5
    cout << "d=" << d << ", e=" << e << endl;  // d=6, e=6

    // 在 for 循环中，i++ 和 ++i 效果一样
    for (int i = 0; i < 5; i++) {   // 用 i++ 或 ++i 都可以
        cout << i << " ";
    }
    cout << endl;  // 0 1 2 3 4

    // 单独使用时，a++ 和 ++a 没区别
    a++;  // a = a + 1
    ++a;  // a = a + 1，和上面效果一样

    return 0;
}
```

### 4.5 三目运算

```cpp
#include <iostream>
using namespace std;

int main() {
    // 三目运算符（条件运算符）：条件 ? 值1 : 值2
    // 如果条件为真，结果为值1；否则结果为值2
    // 相当于简化的 if-else

    int a = 10, b = 20;

    // 求两个数中的最大值
    int maxVal = (a > b) ? a : b;
    cout << "最大值: " << maxVal << endl;  // 20

    // 等价的 if-else 写法：
    int maxVal2;
    if (a > b) {
        maxVal2 = a;
    } else {
        maxVal2 = b;
    }

    // 判断奇偶
    int n = 7;
    cout << n << " 是 " << ((n % 2 == 0) ? "偶数" : "奇数") << endl;

    // 求绝对值
    int x = -5;
    int absX = (x >= 0) ? x : -x;
    cout << "|" << x << "| = " << absX << endl;  // 5

    // 嵌套三目运算（不建议嵌套太多层，可读性差）
    int score = 85;
    string grade = (score >= 90) ? "A" : (score >= 80) ? "B" : (score >= 60) ? "C" : "D";
    cout << "等级: " << grade << endl;  // B

    return 0;
}
```

### 4.6 位运算

```cpp
#include <iostream>
using namespace std;

int main() {
    // 位运算直接操作二进制位
    // 先理解二进制：5 的二进制是 101，3 的二进制是 011

    // & 按位与：两个都是1，结果才是1
    cout << (5 & 3) << endl;  // 1 (101 & 011 = 001)
    //   101
    // & 011
    //   001 = 1

    // | 按位或：只要有一个是1，结果就是1
    cout << (5 | 3) << endl;  // 7 (101 | 011 = 111)
    //   101
    // | 011
    //   111 = 7

    // ^ 按位异或：相同为0，不同为1
    cout << (5 ^ 3) << endl;  // 6 (101 ^ 011 = 110)
    //   101
    // ^ 011
    //   110 = 6

    // ~ 按位取反：0变1，1变0
    cout << (~5) << endl;  // -6（涉及补码，了解即可）

    // << 左移：二进制位整体左移，右边补0
    // 左移 n 位相当于乘以 2^n
    cout << (3 << 2) << endl;  // 12 (3 × 2² = 12)
    // 3 = 011，左移2位 = 01100 = 12

    // >> 右移：二进制位整体右移，左边补符号位
    // 右移 n 位相当于除以 2^n（向下取整）
    cout << (12 >> 2) << endl;  // 3 (12 ÷ 2² = 3)

    // 位运算的常见用途：

    // 1. 判断奇偶（比 %2 更快）
    // n & 1 == 1 表示奇数，n & 1 == 0 表示偶数
    int n = 7;
    if (n & 1) cout << n << " 是奇数" << endl;

    // 2. 乘以/除以 2 的幂
    int x = 10;
    cout << (x << 1) << endl;  // 20 (× 2)
    cout << (x << 3) << endl;  // 80 (× 8)
    cout << (x >> 1) << endl;  // 5  (÷ 2)

    // 3. 交换两个变量（不用临时变量）
    int a = 3, b = 5;
    a = a ^ b;
    b = a ^ b;
    a = a ^ b;
    cout << "a=" << a << ", b=" << b << endl;  // a=5, b=3

    // 4. 取最低位的 1：n & (-n)
    // 5. 把最低位的 1 变成 0：n & (n - 1)

    return 0;
}
```

---

## 第五章 数学库常用函数

```cpp
#include <iostream>
#include <cmath>   // 数学函数都在这个头文件里
using namespace std;

int main() {
    double x = -3.7, y = 2.5;

    // 绝对值
    cout << "abs(-3.7) = " << abs(x) << endl;     // 3.7（浮点数绝对值）
    cout << "abs(-5) = " << abs(-5) << endl;       // 5（整数绝对值，也可以用 abs）

    // 四舍五入
    cout << "round(2.5) = " << round(2.5) << endl;   // 3
    cout << "round(-3.7) = " << round(-3.7) << endl; // -4
    cout << "round(2.4) = " << round(2.4) << endl;   // 2

    // 下取整（地板函数）：取不超过 x 的最大整数
    cout << "floor(2.9) = " << floor(2.9) << endl;   // 2
    cout << "floor(-3.1) = " << floor(-3.1) << endl; // -4

    // 上取整（天花板函数）：取不小于 x 的最小整数
    cout << "ceil(2.1) = " << ceil(2.1) << endl;     // 3
    cout << "ceil(-3.9) = " << ceil(-3.9) << endl;   // -3

    // 平方根
    cout << "sqrt(16) = " << sqrt(16) << endl;       // 4
    cout << "sqrt(2) = " << sqrt(2) << endl;         // 1.41421

    // 幂运算
    cout << "pow(2, 10) = " << pow(2, 10) << endl;   // 1024（2的10次方）

    // 三角函数（参数是弧度，不是角度！）
    // 弧度 = 角度 × π / 180
    double angle = 45;
    double rad = angle * 3.14159265358979 / 180;
    cout << "sin(45°) = " << sin(rad) << endl;    // 0.707107
    cout << "cos(45°) = " << cos(rad) << endl;    // 0.707107
    cout << "tan(45°) = " << tan(rad) << endl;    // 1

    // 对数函数
    cout << "log(2.718) = " << log(2.718) << endl;       // 自然对数 ln(x)，约 1.0
    cout << "log10(100) = " << log10(100) << endl;       // 以 10 为底的对数，2
    cout << "log2(1024) = " << log2(1024) << endl;       // 以 2 为底的对数，10

    // 指数函数 e^x
    cout << "exp(1) = " << exp(1) << endl;               // e 的 1 次方，约 2.718

    // 竞赛中常用的上取整技巧：a/b 上取整 = (a + b - 1) / b（整数运算）
    int a = 7, b = 3;
    cout << "7/3 上取整: " << (a + b - 1) / b << endl;  // 3

    return 0;
}
```

---

## 第六章 结构化程序设计

### 6.1 三种基本结构

```cpp
#include <iostream>
using namespace std;

// ===== 1. 顺序结构：按照从上到下的顺序依次执行 =====
void sequentialExample() {
    int a = 10;
    int b = 20;
    int c = a + b;      // 先执行这行
    cout << c << endl;   // 再执行这行
    c = c * 2;          // 然后执行这行
    cout << c << endl;
}

// ===== 2. 分支结构：根据条件选择不同的执行路径 =====
void branchExample() {
    int age;
    cin >> age;
    if (age >= 18) {
        cout << "成年" << endl;
    } else {
        cout << "未成年" << endl;
    }
}

// ===== 3. 循环结构：重复执行某段代码 =====
void loopExample() {
    // 计算 2 的 10 次方
    int result = 1;
    for (int i = 0; i < 10; i++) {
        result *= 2;
    }
    cout << "2^10 = " << result << endl;  // 1024
}

int main() {
    sequentialExample();
    loopExample();
    return 0;
}
```

### 6.2 流程图概念

```
流程图的基本符号：
┌─────┐
│开始/结束│  椭圆形：表示程序的开始或结束
└─────┘

┌─────────┐
│ 处理步骤  │  矩形：表示一个处理步骤（如赋值、计算）
└─────────┘

    ◇
   / \       菱形：表示判断（条件）
  /   \
 /     \

   ↓         箭头：表示流程方向

示例：判断一个数是奇数还是偶数的流程图

    开始
      ↓
  输入 n
      ↓
   n%2==0?
   /      \
  是       否
  ↓        ↓
 输出     输出
 "偶数"   "奇数"
  ↓        ↓
    结束
```

---

## 第七章 数组

### 7.1 数组与数组下标

```cpp
#include <iostream>
using namespace std;

int main() {
    // 数组：存储一组相同类型的数据
    // 就像一排格子，每个格子有一个编号（下标），从 0 开始

    // 定义一个包含 5 个 int 的数组
    int arr[5] = {10, 20, 30, 40, 50};
    //  下标:     0   1   2   3   4

    // 访问元素：通过下标
    cout << arr[0] << endl;  // 10（第一个元素，下标从 0 开始！）
    cout << arr[4] << endl;  // 50（最后一个元素）
    // arr[5]  ← 越界！最大下标是 4

    // 修改元素
    arr[2] = 99;
    cout << arr[2] << endl;  // 99

    // 部分初始化（未初始化的元素自动为 0）
    int b[5] = {1, 2, 3};    // b = {1, 2, 3, 0, 0}
    int c[5] = {0};          // c = {0, 0, 0, 0, 0}（全部初始化为 0）

    // 不指定大小的初始化（编译器自动计算）
    int d[] = {1, 2, 3, 4, 5};  // 大小自动为 5

    // 数组的大小必须是常量（竞赛中常用较大的数组）
    const int N = 100;
    int e[N];  // 定义大小为 100 的数组

    // 重要：全局数组自动初始化为 0，局部数组不会！
    // 竞赛建议把大数组定义在 main 函数外面（全局）

    return 0;
}
```

### 7.2 数组的读入与输出

```cpp
#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int n;
    cin >> n;  // 先输入数组大小

    int arr[100];  // 假设最多 100 个元素

    // 读入数组
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // 输出数组
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // 求数组的最大值和最小值
    int maxVal = arr[0], minVal = arr[0];
    int maxIdx = 0, minIdx = 0;
    for (int i = 1; i < n; i++) {
        if (arr[i] > maxVal) {
            maxVal = arr[i];
            maxIdx = i;
        }
        if (arr[i] < minVal) {
            minVal = arr[i];
            minIdx = i;
        }
    }
    cout << "最大值: " << maxVal << " 下标: " << maxIdx << endl;
    cout << "最小值: " << minVal << " 下标: " << minIdx << endl;

    // 求数组元素的和与平均值
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    double avg = (double)sum / n;
    cout << "总和: " << sum << " 平均: " << avg << endl;

    // 数组逆序
    for (int i = 0; i < n / 2; i++) {
        int temp = arr[i];
        arr[i] = arr[n - 1 - i];
        arr[n - 1 - i] = temp;
    }
    cout << "逆序后: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
```

### 7.3 二维数组与多维数组

```cpp
#include <iostream>
using namespace std;

int main() {
    // 二维数组：表格形式的数据，有行和列
    // 就像一个 Excel 表格

    // 定义 3 行 4 列的二维数组
    int matrix[3][4] = {
        {1,  2,  3,  4},
        {5,  6,  7,  8},
        {9, 10, 11, 12}
    };

    // 访问元素：matrix[行下标][列下标]
    cout << matrix[0][0] << endl;   // 1（第1行第1列）
    cout << matrix[1][2] << endl;   // 7（第2行第3列）
    cout << matrix[2][3] << endl;   // 12（第3行第4列）

    // 读入二维数组
    int n, m;
    cin >> n >> m;  // n 行 m 列
    int a[100][100];

    for (int i = 0; i < n; i++) {        // 遍历每一行
        for (int j = 0; j < m; j++) {    // 遍历每一列
            cin >> a[i][j];
        }
    }

    // 输出二维数组
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << a[i][j] << " ";
        }
        cout << endl;
    }

    // 行列互换（矩阵转置）
    int b[100][100];
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            b[i][j] = a[j][i];
        }
    }

    // 多维数组：三维甚至更高维
    int cube[3][3][3] = {{{0}}};  // 3×3×3 的三维数组

    return 0;
}
```

---

## Day 1 练习题

### 练习1：基本输入输出
**题目**：输入两个整数 a 和 b，输出它们的和、差、积、商和余数。
```
输入示例：17 5
输出示例：
17 + 5 = 22
17 - 5 = 12
17 * 5 = 85
17 / 5 = 3
17 % 5 = 2
```

### 练习2：温度转换
**题目**：输入一个华氏温度 F，将其转换为摄氏温度 C。公式：C = 5 * (F - 32) / 9，保留两位小数。
```
输入示例：100
输出示例：37.78
```

### 练习3：判断闰年
**题目**：输入一个年份，判断是否为闰年。闰年规则：能被4整除但不能被100整除，或者能被400整除。
```
输入示例：2000
输出示例：YES
输入示例：1900
输出示例：NO
```

### 练习4：求阶乘
**题目**：输入一个正整数 n（n <= 20），求 n! = 1 × 2 × 3 × ... × n。提示：用 long long。
```
输入示例：10
输出示例：3628800
```

### 练习5：打印星号图形
**题目**：输入一个整数 n，打印 n 行的直角三角形。
```
输入示例：5
输出示例：
*
**
***
****
*****
```

### 练习6：数字翻转
**题目**：输入一个三位正整数，将其翻转后输出。例如 123 翻转为 321，100 翻转为 001（即输出 1 还是 001？按题目要求）。
```
输入示例：123
输出示例：321
```

### 练习7：斐波那契数列
**题目**：输入 n，输出斐波那契数列的前 n 项。斐波那契数列：1, 1, 2, 3, 5, 8, 13, ...（每项等于前两项之和）。
```
输入示例：8
输出示例：1 1 2 3 5 8 13 21
```

### 练习8：数组操作
**题目**：输入 n 个整数，将它们逆序输出，然后求出最大值和最小值及其位置。
```
输入示例：
5
3 7 1 9 4
输出示例：
逆序: 4 9 1 7 3
最大值: 9 位置: 4
最小值: 1 位置: 3
```

### 练习9：九九乘法表
**题目**：输出完整的九九乘法表。
```
输出格式：
1×1=1
1×2=2  2×2=4
1×3=3  2×3=6  3×3=9
...以此类推到 9×9=81
```

### 练习10：水仙花数
**题目**：输出所有的三位水仙花数。水仙花数是指一个三位数的各位数字的立方和等于该数本身。例如：153 = 1³ + 5³ + 3³。
```
输出示例：153 370 371 407
```

### 练习11：购物计算
**题目**：苹果 5 元/斤，香蕉 3 元/斤，橘子 2 元/斤。输入购买的斤数，计算总价和平均每斤价格。
```
输入示例：2 3 5
输出示例：
总价: 29
平均: 3.63
```

### 练习12：字符转换
**题目**：输入一个大写字母，转换为小写字母输出。再输入一个小写字母，转换为大写字母输出。
```
输入示例：A
输出示例：a
```

### 练习13：位运算练习
**题目**：输入一个整数 n，判断它的二进制表示中有多少个 1。例如 7 的二进制是 111，有 3 个 1。
```
输入示例：7
输出示例：3
输入示例：8
输出示例：1
```

### 练习14：二维数组操作
**题目**：输入一个 n×n 的矩阵，输出它的主对角线元素之和（从左上到右下）。
```
输入示例：
3
1 2 3
4 5 6
7 8 9
输出示例：15（1+5+9）
```

---

> **Day 1 学习建议**：
> 1. 每个代码示例都自己敲一遍，不要复制粘贴
> 2. 尝试修改代码中的参数，观察输出变化
> 3. 先自己思考练习题，想不出再看答案
> 4. 注意编译错误提示，学会看懂错误信息
> 5. 预计学习时间：8-10 小时（含练习）
