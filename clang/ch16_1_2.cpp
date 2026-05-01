#include <iostream>
using namespace std;

// 例2：判断一个数是否是水仙花数
// 水仙花数：一个三位数，各位数字的立方和等于它本身
// 例如：153 = 1³ + 5³ + 3³
int main() {
    for (int n = 100; n <= 999; n++) {
        int a = n / 100;         // 百位
        int b = n / 10 % 10;     // 十位
        int c = n % 10;          // 个位
        if (a * a * a + b * b * b + c * c * c == n) {
            cout << n << " 是水仙花数" << endl;
        }
    }
    return 0;
}
