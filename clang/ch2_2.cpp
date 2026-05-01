#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // float：单精度浮点数，占 4 字节，约 6-7 位有效数字
    float f = 3.14f;       // 注意末尾的 f
    float f2 = 3.14159265358979f;
    cout << "float f2 = " << f2 << endl;  // 精度会丢失！

    // double：双精度浮点数，占 8 字节，约 15-16 位有效数字
    // 竞赛和日常编程中推荐使用 double
    double d = 3.141592653589793;
    cout << "double d = " << d << endl;   // 精度保持得好

    // 浮点数的精度问题（非常重要！）
    double a = 0.1 + 0.2;
    cout << "0.1 + 0.2 = " << a << endl;  // 可能输出 0.30000000000000004
    // 所以浮点数比较不能用 ==，要用误差范围
    double eps = 1e-9;  // 误差范围：10的-9次方
    if (abs(a - 0.3) < eps) {
        cout << "a 约等于 0.3" << endl;
    }

    // 科学计数法
    double big = 1.5e10;    // 1.5 × 10^10 = 15000000000.0
    double small = 2.5e-3;  // 2.5 × 10^(-3) = 0.0025

    // 格式化输出浮点数
    printf("保留2位小数: %.2f\n", 3.14159);   // 3.14
    printf("保留4位小数: %.4f\n", 3.14159);   // 3.1416

    return 0;
}
