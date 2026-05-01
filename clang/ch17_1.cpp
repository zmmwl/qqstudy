#include <iostream>
using namespace std;

// 在有序数组 a 中查找 target，返回下标（没找到返回 -1）
int binarySearch(int a[], int n, int target) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;  // 防溢出的写法
        if (a[mid] == target) {
            return mid;          // 找到了
        } else if (a[mid] < target) {
            left = mid + 1;      // target 在右半边
        } else {
            right = mid - 1;     // target 在左半边
        }
    }
    return -1;  // 没找到
}

int main() {
    int a[] = {1, 3, 5, 7, 9, 11, 13, 15};
    int n = 8;
    int target;
    cout << "输入要查找的数: ";
    cin >> target;

    int pos = binarySearch(a, n, target);
    if (pos != -1) {
        cout << target << " 在下标 " << pos << endl;
    } else {
        cout << "没找到 " << target << endl;
    }
    return 0;
}
