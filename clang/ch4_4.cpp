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
