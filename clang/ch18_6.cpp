#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// 自定义排序规则：按绝对值从小到大
bool cmpAbs(int a, int b) {
    return abs(a) < abs(b);
}

int main() {
    // 基本用法：对数组排序
    int a[] = {5, 2, 8, 1, 9, 3};
    sort(a, a + 6);  // 默认从小到大
    for (int i = 0; i < 6; i++) cout << a[i] << " ";
    cout << endl;

    // 从大到小排序
    sort(a, a + 6, greater<int>());
    for (int i = 0; i < 6; i++) cout << a[i] << " ";
    cout << endl;

    // 自定义排序
    int b[] = {-3, 1, -4, 1, 5, -9};
    sort(b, b + 6, cmpAbs);  // 按绝对值排序
    for (int i = 0; i < 6; i++) cout << b[i] << " ";
    cout << endl;

    // 对 vector 排序
    vector<int> v = {5, 2, 8, 1, 9};
    sort(v.begin(), v.end());
    for (int x : v) cout << x << " ";
    cout << endl;

    return 0;
}
