#include <iostream>
using namespace std;

// 例：木材切割问题
// 有 n 根木材，要切出 k 段等长的木材，每段最长能切多长？
int len[100005];
int n, k;

// 检查：如果每段长 mid，能切出几段？
bool check(int mid) {
    long long total = 0;
    for (int i = 0; i < n; i++) {
        total += len[i] / mid;  // 每根木材能切出几段
    }
    return total >= k;  // 切出的段数够不够
}

int main() {
    cin >> n >> k;
    int maxLen = 0;
    for (int i = 0; i < n; i++) {
        cin >> len[i];
        if (len[i] > maxLen) maxLen = len[i];
    }

    // 二分答案：每段的长度
    int left = 1, right = maxLen, ans = 0;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (check(mid)) {
            ans = mid;       // mid 可行，试试更长的
            left = mid + 1;
        } else {
            right = mid - 1; // mid 不行，试试更短的
        }
    }
    cout << "最长每段: " << ans << endl;
    return 0;
}
