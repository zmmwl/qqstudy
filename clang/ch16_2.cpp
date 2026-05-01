#include <iostream>
using namespace std;

// 例：报数问题
// n 个人围成一圈，从第1个人开始报数，报到 m 的人出列，
// 然后下一个人从1开始重新报数，求最后剩下的人的编号。

int main() {
    int n, m;
    cout << "输入 n 和 m: ";
    cin >> n >> m;

    bool out[1000] = {false};  // out[i]=true 表示第i个人已出列
    int remaining = n;          // 还剩多少人
    int count = 0;              // 当前报的数
    int pos = 0;                // 当前位置（0-based）

    while (remaining > 1) {
        if (!out[pos]) {        // 如果这个人还在
            count++;            // 报数
            if (count == m) {   // 报到 m，出列
                out[pos] = true;
                remaining--;
                count = 0;
                cout << "第 " << pos + 1 << " 号出列" << endl;
            }
        }
        pos = (pos + 1) % n;    // 移到下一个人（循环）
    }

    // 找出最后剩下的人
    for (int i = 0; i < n; i++) {
        if (!out[i]) {
            cout << "最后剩下: 第 " << i + 1 << " 号" << endl;
            break;
        }
    }
    return 0;
}
