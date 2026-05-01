#include <iostream>
using namespace std;

// 快速排序：选一个基准值，把比它小的放左边，比它大的放右边，递归处理
void quickSort(int a[], int left, int right) {
    if (left >= right) return;

    int pivot = a[left];  // 选第一个元素作为基准值
    int i = left, j = right;

    while (i < j) {
        // 从右往左找第一个比基准值小的
        while (i < j && a[j] >= pivot) j--;
        // 从左往右找第一个比基准值大的
        while (i < j && a[i] <= pivot) i++;
        // 交换这两个元素
        if (i < j) {
            int t = a[i]; a[i] = a[j]; a[j] = t;
        }
    }
    // 把基准值放到正确位置
    a[left] = a[i];
    a[i] = pivot;

    // 递归排序左右两部分
    quickSort(a, left, i - 1);
    quickSort(a, i + 1, right);
}

int main() {
    int a[] = {10, 7, 8, 9, 1, 5};
    int n = 6;
    quickSort(a, 0, n - 1);
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;
    return 0;
}
