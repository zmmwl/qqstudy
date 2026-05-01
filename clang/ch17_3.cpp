#include <iostream>
using namespace std;

// 归并排序——分治的经典应用
int temp[100005];  // 临时数组，用于合并

// 对数组 a 的 [left, right] 区间排序
void mergeSort(int a[], int left, int right) {
    if (left >= right) return;  // 只有一个元素，已经有序

    int mid = (left + right) / 2;
    mergeSort(a, left, mid);      // 排序左半边
    mergeSort(a, mid + 1, right); // 排序右半边

    // 合并两个有序数组
    int i = left, j = mid + 1, k = left;
    while (i <= mid && j <= right) {
        if (a[i] <= a[j]) {
            temp[k++] = a[i++];
        } else {
            temp[k++] = a[j++];
        }
    }
    // 把剩余的元素复制过去
    while (i <= mid)  temp[k++] = a[i++];
    while (j <= right) temp[k++] = a[j++];

    // 把临时数组复制回原数组
    for (int p = left; p <= right; p++) {
        a[p] = temp[p];
    }
}

int main() {
    int a[] = {38, 27, 43, 3, 9, 82, 10};
    int n = 7;

    mergeSort(a, 0, n - 1);

    cout << "排序结果: ";
    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    cout << endl;
    return 0;
}
