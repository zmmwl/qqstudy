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
