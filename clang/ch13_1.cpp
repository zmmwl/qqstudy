#include <iostream>
#include <algorithm>  // 算法库
using namespace std;

int main() {
    // min：求最小值
    cout << min(3, 5) << endl;  // 3
    cout << min({3, 1, 4, 1, 5}) << endl;  // 1（多个值取最小）

    // max：求最大值
    cout << max(3, 5) << endl;  // 5

    // swap：交换两个变量的值
    int a = 10, b = 20;
    swap(a, b);
    cout << "a=" << a << ", b=" << b << endl;  // a=20, b=10

    // sort：排序（非常重要！）
    int arr[] = {5, 2, 8, 1, 9, 3};
    int n = 6;

    // 默认从小到大排序
    sort(arr, arr + n);
    for (int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;  // 1 2 3 5 8 9

    // 从大到小排序
    sort(arr, arr + n, greater<int>());
    for (int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;  // 9 8 5 3 2 1

    // 自定义排序规则
    // 例如：按绝对值从小到大排序
    int arr2[] = {-5, 3, -1, 4, -2};
    sort(arr2, arr2 + 5, [](int a, int b) {
        return abs(a) < abs(b);  // 绝对值小的排前面
    });
    for (int i = 0; i < 5; i++) cout << arr2[i] << " ";
    cout << endl;  // -1 -2 3 4 -5

    // sort 对 vector 使用
    // sort(v.begin(), v.end());

    // 其他有用的算法函数：
    int arr3[] = {1, 3, 5, 7, 9};

    // binary_search：二分查找（数组必须有序）
    cout << binary_search(arr3, arr3 + 5, 5) << endl;  // 1（存在）

    // lower_bound：找到第一个 >= 某值的位置
    int* pos = lower_bound(arr3, arr3 + 5, 4);
    cout << *pos << endl;  // 5（第一个 >= 4 的元素）

    // upper_bound：找到第一个 > 某值的位置
    int* pos2 = upper_bound(arr3, arr3 + 5, 5);
    cout << *pos2 << endl;  // 7（第一个 > 5 的元素）

    // reverse：反转
    int arr4[] = {1, 2, 3, 4, 5};
    reverse(arr4, arr4 + 5);
    for (int i = 0; i < 5; i++) cout << arr4[i] << " ";
    cout << endl;  // 5 4 3 2 1

    // fill：填充
    int arr5[10];
    fill(arr5, arr5 + 10, 0);  // 全部填 0

    // unique：去重（必须先排序）
    int arr6[] = {1, 1, 2, 2, 3, 3, 3, 4};
    sort(arr6, arr6 + 8);
    int newLen = unique(arr6, arr6 + 8) - arr6;
    // newLen = 4, arr6 = {1, 2, 3, 4, ...}

    // nth_element：找到第 n 大的元素
    int arr7[] = {5, 2, 8, 1, 9, 3};
    nth_element(arr7, arr7 + 2, arr7 + 6);  // 第3小的元素放到位置2
    cout << "第3小: " << arr7[2] << endl;  // 3

    return 0;
}
