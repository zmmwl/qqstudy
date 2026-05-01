#include <iostream>
using namespace std;

int main() {
    // 字符指针：指向字符的指针，常用于字符串操作
    char str[] = "Hello";
    char* p = str;  // p 指向字符串的第一个字符

    cout << p << endl;     // Hello（cout 对 char* 特殊处理，输出整个字符串）
    cout << *p << endl;    // H（第一个字符）

    // 用指针遍历字符串
    while (*p != '\0') {
        cout << *p << " ";
        p++;
    }
    cout << endl;  // H e l l o

    // 字符串常量指针
    const char* s = "World";  // 指向字符串常量
    cout << s << endl;  // World
    // s[0] = 'w';  // 错误！字符串常量不能修改

    return 0;
}
