#include <iostream>
#include <algorithm>
using namespace std;

// 例：零钱兑换（贪心版）
// 有 1元、5元、10元、20元、50元、100元 的纸币
// 用最少的纸币凑出指定金额
int main() {
    int money[] = {100, 50, 20, 10, 5, 1};  // 从大到小排列
    int n;
    cout << "输入金额: ";
    cin >> n;

    int count = 0;
    cout << "找零方案: ";
    for (int i = 0; i < 6; i++) {
        int num = n / money[i];   // 能用几张这个面值
        if (num > 0) {
            cout << money[i] << "元×" << num << " ";
            n -= num * money[i];  // 减去已用的金额
            count += num;
        }
    }
    cout << endl << "最少需要 " << count << " 张纸币" << endl;
    return 0;
}
