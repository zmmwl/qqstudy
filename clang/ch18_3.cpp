#include <iostream>
using namespace std;

// 选择排序：每轮选出最小的，放到前面
void selectionSort(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;  // 假设当前位置最小
        for (int j = i + 1; j < n; j++) {
            if (a[j] < a[minIdx]) {
                minIdx = j;  // 找到更小的
            }
        }
        // 把最小的交换到前面
        if (minIdx != i) {
            int t = a[i];
            a[i] = a[minIdx];
            a[minIdx] = t;
        }
    }
}

int main() {
    int a[] = {64, 25, 12, 22, 11};
    int n = 5;
    selectionSort(a, n);
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;
    return 0;
}
