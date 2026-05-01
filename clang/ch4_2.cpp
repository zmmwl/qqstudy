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
