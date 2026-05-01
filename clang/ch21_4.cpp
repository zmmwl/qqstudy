#include <iostream>
#include <algorithm>
using namespace std;

// LIS：求一个序列中最长的严格递增子序列的长度
// 例如：1 5 3 4 6 2 → LIS 长度为 4（1 3 4 6）
int main() {
    int n;
    cin >> n;
    int a[10005], dp[10005];

    for (int i = 0; i < n; i++) {
        cin >> a[i];
        dp[i] = 1;  // 至少自己一个元素，长度为 1
    }

    // dp[i] 表示以 a[i] 结尾的最长上升子序列长度
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (a[j] < a[i]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }

    int ans = *max_element(dp, dp + n);
    cout << "LIS 长度: " << ans << endl;
    return 0;
}
