#include <iostream>
using namespace std;

// 方法1：递归（很慢，有大量重复计算）
int fib1(int n) {
    if (n <= 2) return 1;
    return fib1(n - 1) + fib1(n - 2);
}

// 方法2：记忆化递归（用一个数组记录算过的结果）
int memo[1000] = {0};
int fib2(int n) {
    if (n <= 2) return 1;
    if (memo[n] != 0) return memo[n];  // 已经算过，直接返回
    memo[n] = fib2(n - 1) + fib2(n - 2);  // 算完记录下来
    return memo[n];
}

// 方法3：递推（动态规划的标准写法）
int fib3(int n) {
    int dp[1000];
    dp[1] = 1;  // 初始条件
    dp[2] = 1;
    for (int i = 3; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];  // 状态转移方程
    }
    return dp[n];
}

int main() {
    int n;
    cin >> n;
    cout << "递推结果: " << fib3(n) << endl;
    return 0;
}
