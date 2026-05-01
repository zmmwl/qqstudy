#include <iostream>
#include <cmath>
using namespace std;

// 判断一个数是否是质数
bool isPrime(int n) {
    if (n < 2) return false;       // 0和1不是质数
    if (n == 2) return true;       // 2是质数
    if (n % 2 == 0) return false;  // 偶数不是质数

    // 只需要检查到 sqrt(n)
    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

// 埃氏筛法：找出 1~n 中所有的质数
void sieve(int n) {
    bool isPrimeArr[1000005];
    for (int i = 0; i <= n; i++) isPrimeArr[i] = true;
    isPrimeArr[0] = isPrimeArr[1] = false;

    for (int i = 2; i * i <= n; i++) {
        if (isPrimeArr[i]) {
            // 把 i 的所有倍数标记为非质数
            for (int j = i * i; j <= n; j += i) {
                isPrimeArr[j] = false;
            }
        }
    }

    // 输出质数
    int count = 0;
    for (int i = 2; i <= n; i++) {
        if (isPrimeArr[i]) {
            count++;
            if (count <= 20) cout << i << " ";  // 只打印前20个
        }
    }
    cout << endl << "1~" << n << " 中共有 " << count << " 个质数" << endl;
}

int main() {
    int n;
    cin >> n;
    cout << n << (isPrime(n) ? " 是质数" : " 不是质数") << endl;

    sieve(100);
    return 0;
}
