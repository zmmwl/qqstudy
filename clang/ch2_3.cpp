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
