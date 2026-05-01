#include <iostream>
#include <algorithm>
using namespace std;

// 完全背包问题
// 和 0-1 背包类似，但每个物品可以选多次
int main() {
    int n, W;
    cin >> n >> W;
    int w[1005], v[1005];

    for (int i = 1; i <= n; i++)
        cin >> w[i] >> v[i];

    int dp[10005] = {0};

    for (int i = 1; i <= n; i++) {
        // 注意：从小到大遍历，允许同一个物品选多次
        for (int j = w[i]; j <= W; j++) {
            dp[j] = max(dp[j], dp[j - w[i]] + v[i]);
        }
    }

    cout << "最大价值: " << dp[W] << endl;
    return 0;
}
