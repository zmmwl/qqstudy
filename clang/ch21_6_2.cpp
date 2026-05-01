#include <iostream>
using namespace std;

// 方格路径计数：从(1,1)走到(m,n)，只能向右或向下走，有多少种路径？
int main() {
    int m, n;
    cin >> m >> n;
    long long dp[105][105];

    // 初始化：第一行和第一列都只有1种走法
    for (int i = 1; i <= m; i++) dp[i][1] = 1;
    for (int j = 1; j <= n; j++) dp[1][j] = 1;

    for (int i = 2; i <= m; i++) {
        for (int j = 2; j <= n; j++) {
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            // 到达(i,j)只能从上方或左方来
        }
    }

    cout << "路径数: " << dp[m][n] << endl;
    return 0;
}
