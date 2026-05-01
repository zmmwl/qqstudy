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
