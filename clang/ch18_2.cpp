#include <iostream>
using namespace std;

// 冒泡排序：相邻元素比较，大的往后"冒泡"
void bubbleSort(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {       // 外层：需要冒泡 n-1 轮
        bool swapped = false;                 // 优化：如果某轮没有交换，说明已排好
        for (int j = 0; j < n - 1 - i; j++) { // 内层：每轮把最大的冒到最后
            if (a[j] > a[j + 1]) {
                // 交换相邻元素
                int t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
                swapped = true;
            }
        }
        if (!swapped) break;  // 没有交换，提前结束
    }
}

int main() {
    int a[] = {64, 34, 25, 12, 22, 11, 90};
    int n = 7;
    bubbleSort(a, n);
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;
    return 0;
}
