#include <iostream>
using namespace std;

// 爬楼梯：每次可以爬 1 或 2 级台阶，爬到第 n 级有多少种方法？
int main() {
    int n;
    cin >> n;
    int dp[10005];
    dp[1] = 1;  // 第1级：1种方法
    dp[2] = 2;  // 第2级：2种方法（1+1 或 2）

    for (int i = 3; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
        // 到达第 i 级，可以从第 i-1 级爬1步，或从第 i-2 级爬2步
    }

    cout << "方法数: " << dp[n] << endl;
    return 0;
}
