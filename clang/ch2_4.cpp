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
