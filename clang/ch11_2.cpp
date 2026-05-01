#include <iostream>
using namespace std;

int main() {
    int arr[5] = {10, 20, 30, 40, 50};

    // 数组名就是首元素的地址
    int* p = arr;  // 等价于 int* p = &arr[0];

    cout << "arr = " << arr << endl;
    cout << "&arr[0] = " << &arr[0] << endl;
    cout << "*arr = " << *arr << endl;        // 10（第一个元素）

    // 指针算术
    cout << "*(arr+1) = " << *(arr + 1) << endl;  // 20（第二个元素）
    cout << "*(arr+2) = " << *(arr + 2) << endl;  // 30（第三个元素）

    // arr[i] 等价于 *(arr + i)

    // 用指针遍历数组
    for (int* q = arr; q < arr + 5; q++) {
        cout << *q << " ";
    }
    cout << endl;  // 10 20 30 40 50

    // 用指针修改数组
    for (int* q = arr; q < arr + 5; q++) {
        *q *= 2;  // 每个元素乘以 2
    }
    // 现在 arr = {20, 40, 60, 80, 100}

    return 0;
}
