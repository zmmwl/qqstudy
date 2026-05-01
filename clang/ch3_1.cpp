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
    char str[100];                        // 字符数组，用于存放字符串
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
