#include <iostream>
using namespace std;

// 函数定义的格式：
// 返回类型 函数名(参数列表) {
//     函数体
//     return 返回值;
// }

// 定义一个求两个数最大值的函数
int getMax(int a, int b) {  // a, b 是形参（形式参数）
    return (a > b) ? a : b;
}

// 定义一个判断素数的函数
bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; i++) {  // 只需检查到 sqrt(n)
        if (n % i == 0) return false;
    }
    return true;
}

// 没有返回值的函数用 void
void printStars(int n) {
    for (int i = 0; i < n; i++) {
        cout << "*";
    }
    cout << endl;
}

int main() {
    // 调用函数时传入的值是实参（实际参数）
    int result = getMax(10, 20);  // 10 和 20 是实参
    cout << "最大值: " << result << endl;  // 20

    // 函数可以多次调用
    cout << "15 是否素数: " << isPrime(15) << endl;  // 0 (false)
    cout << "17 是否素数: " << isPrime(17) << endl;  // 1 (true)

    printStars(5);  // *****
    printStars(3);  // ***

    return 0;
}
