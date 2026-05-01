#include <iostream>
using namespace std;

// 例子：求 1+2+...+n 的和
// 算法1：逐个相加（时间复杂度 O(n)）
int sumV1(int n) {
    int s = 0;
    for (int i = 1; i <= n; i++) {
        s += i;
    }
    return s;
}

// 算法2：数学公式（时间复杂度 O(1)）
// 1+2+...+n = n*(n+1)/2
int sumV2(int n) {
    return n * (n + 1) / 2;
}

int main() {
    int n;
    cout << "输入 n: ";
    cin >> n;
    cout << "算法1 结果: " << sumV1(n) << endl;
    cout << "算法2 结果: " << sumV2(n) << endl;
    return 0;
}
