#include <iostream>
using namespace std;

// 快速幂：快速计算 a^b % mod
// 原理：把 b 分解成二进制，利用 a^b = a^(b/2) * a^(b/2)
long long quickPow(long long a, long long b, long long mod) {
    long long result = 1;
    a %= mod;  // 防止 a 本身就很大
    while (b > 0) {
        if (b % 2 == 1) {      // b 的最低位是 1
            result = result * a % mod;
        }
        a = a * a % mod;       // a 平方
        b /= 2;                // b 右移一位
    }
    return result;
}

int main() {
    long long a, b, mod;
    cin >> a >> b >> mod;
    cout << a << "^" << b << " mod " << mod << " = " << quickPow(a, b, mod) << endl;
    return 0;
}
