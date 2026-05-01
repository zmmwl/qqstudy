#include <iostream>
using namespace std;

// 插入排序：像打牌一样，把每个元素插入到前面已排好的部分中
void insertionSort(int a[], int n) {
    for (int i = 1; i < n; i++) {
        int key = a[i];  // 要插入的元素
        int j = i - 1;
        // 把比 key 大的元素往后移
        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = key;  // 插入到正确位置
    }
}

int main() {
    int a[] = {12, 11, 13, 5, 6};
    int n = 5;
    insertionSort(a, n);
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;
    return 0;
}
