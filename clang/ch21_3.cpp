#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[105][105], dp[105][105];

    // 读入数字三角形
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= i; j++)
            cin >> a[i][j];

    // dp[i][j] 表示从(i,j)走到底部的最大和
    // 从倒数第二行往上推
    for (int j = 1; j <= n; j++)
        dp[n][j] = a[n][j];  // 底部一行：最大和就是自己

    for (int i = n - 1; i >= 1; i--) {
        for (int j = 1; j <= i; j++) {
            // 从(i,j)出发，可以走到(i+1,j)或(i+1,j+1)
            dp[i][j] = a[i][j] + max(dp[i + 1][j], dp[i + 1][j + 1]);
        }
    }

    cout << "最大路径和: " << dp[1][1] << endl;
    return 0;
}
