#include <iostream>
#include <algorithm>
using namespace std;

// 辗转相除法（欧几里得算法）求最大公约数
int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
    // 原理：gcd(a,b) = gcd(b, a%b)
    // 例如：gcd(12, 8) = gcd(8, 4) = gcd(4, 0) = 4
}

// 最小公倍数 = a*b / gcd(a,b)
int lcm(int a, int b) {
    return a / gcd(a, b) * b;  // 先除再乘，防止溢出
}

int main() {
    int a, b;
    cin >> a >> b;
    cout << "最大公约数: " << gcd(a, b) << endl;
    cout << "最小公倍数: " << lcm(a, b) << endl;

    // 也可以直接用 __gcd(a, b)（在 <algorithm> 中）
    cout << "__gcd: " << __gcd(a, b) << endl;
    return 0;
}
