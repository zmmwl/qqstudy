#include <iostream>
#include <cmath>
using namespace std;

int main() {
    // 1. 判断奇偶
    int x = 7;
    cout << x << (x % 2 == 0 ? " 偶数" : " 奇数") << endl;

    // 2. 数字拆分
    int num = 12345;
    cout << "个位:" << num % 10 << endl;           // 5
    cout << "十位:" << num / 10 % 10 << endl;      // 4
    cout << "百位:" << num / 100 % 10 << endl;     // 3

    // 3. 交换两个变量（不用临时变量）
    int a = 3, b = 5;
    a = a ^ b;  // 异或交换法
    b = a ^ b;
    a = a ^ b;
    cout << "a=" << a << " b=" << b << endl;  // a=5 b=3

    // 4. 绝对值
    cout << "abs(-7) = " << abs(-7) << endl;

    // 5. 幂运算
    cout << "2^10 = " << pow(2, 10) << endl;  // 1024

    // 6. 平方根
    cout << "sqrt(144) = " << sqrt(144) << endl;  // 12

    // 7. 取整
    cout << "floor(3.7) = " << floor(3.7) << endl;   // 3（向下取整）
    cout << "ceil(3.2) = " << ceil(3.2) << endl;     // 4（向上取整）

    // 8. 判断完全平方数
    int n = 144;
    int sq = (int)sqrt(n);
    cout << n << (sq * sq == n ? " 是" : " 不是") << "完全平方数" << endl;

    return 0;
}
