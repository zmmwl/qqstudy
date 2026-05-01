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
