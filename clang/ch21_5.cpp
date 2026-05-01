#include <iostream>
#include <algorithm>
using namespace std;

// 0-1 背包问题
// 有 n 个物品，每个物品有重量 w[i] 和价值 v[i]
// 背包容量为 W，每个物品只能选一次，求最大价值
int main() {
    int n, W;
    cin >> n >> W;
    int w[1005], v[1005];

    for (int i = 1; i <= n; i++)
        cin >> w[i] >> v[i];

    // dp[j] 表示容量为 j 时的最大价值
    int dp[10005] = {0};

    for (int i = 1; i <= n; i++) {
        // 注意：从大到小遍历，保证每个物品只选一次
        for (int j = W; j >= w[i]; j--) {
            dp[j] = max(dp[j], dp[j - w[i]] + v[i]);
            // dp[j]：不选物品 i
            // dp[j-w[i]]+v[i]：选物品 i（用掉 w[i] 的容量，得到 v[i] 的价值）
        }
    }

    cout << "最大价值: " << dp[W] << endl;
    return 0;
}
