#include <iostream>
#include <cmath>   // 数学函数都在这个头文件里
using namespace std;

int main() {
    double x = -3.7, y = 2.5;

    // 绝对值
    cout << "abs(-3.7) = " << abs(x) << endl;     // 3.7（浮点数绝对值）
    cout << "abs(-5) = " << abs(-5) << endl;       // 5（整数绝对值，也可以用 abs）

    // 四舍五入
    cout << "round(2.5) = " << round(2.5) << endl;   // 3
    cout << "round(-3.7) = " << round(-3.7) << endl; // -4
    cout << "round(2.4) = " << round(2.4) << endl;   // 2

    // 下取整（地板函数）：取不超过 x 的最大整数
    cout << "floor(2.9) = " << floor(2.9) << endl;   // 2
    cout << "floor(-3.1) = " << floor(-3.1) << endl; // -4

    // 上取整（天花板函数）：取不小于 x 的最小整数
    cout << "ceil(2.1) = " << ceil(2.1) << endl;     // 3
    cout << "ceil(-3.9) = " << ceil(-3.9) << endl;   // -3

    // 平方根
    cout << "sqrt(16) = " << sqrt(16) << endl;       // 4
    cout << "sqrt(2) = " << sqrt(2) << endl;         // 1.41421

    // 幂运算
    cout << "pow(2, 10) = " << pow(2, 10) << endl;   // 1024（2的10次方）

    // 三角函数（参数是弧度，不是角度！）
    // 弧度 = 角度 × π / 180
    double angle = 45;
    double rad = angle * 3.14159265358979 / 180;
    cout << "sin(45°) = " << sin(rad) << endl;    // 0.707107
    cout << "cos(45°) = " << cos(rad) << endl;    // 0.707107
    cout << "tan(45°) = " << tan(rad) << endl;    // 1

    // 对数函数
    cout << "log(2.718) = " << log(2.718) << endl;       // 自然对数 ln(x)，约 1.0
    cout << "log10(100) = " << log10(100) << endl;       // 以 10 为底的对数，2
    cout << "log2(1024) = " << log2(1024) << endl;       // 以 2 为底的对数，10

    // 指数函数 e^x
    cout << "exp(1) = " << exp(1) << endl;               // e 的 1 次方，约 2.718

    // 竞赛中常用的上取整技巧：a/b 上取整 = (a + b - 1) / b（整数运算）
    int a = 7, b = 3;
    cout << "7/3 上取整: " << (a + b - 1) / b << endl;  // 3

    return 0;
}
