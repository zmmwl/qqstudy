#include <iostream>
using namespace std;

// 传值参数：函数内部修改不影响外面的变量（复制了一份）
void addTen_value(int x) {
    x += 10;
    cout << "函数内 x = " << x << endl;
}

// 传引用参数：用 & 符号，函数内部修改会影响外面的变量（直接操作原变量）
void addTen_ref(int& x) {
    x += 10;
    cout << "函数内 x = " << x << endl;
}

// 传引用的经典用法：让函数返回多个值
// 例如同时求最大值和最小值
void findMinMax(int arr[], int n, int& minVal, int& maxVal) {
    minVal = maxVal = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] < minVal) minVal = arr[i];
        if (arr[i] > maxVal) maxVal = arr[i];
    }
}

// 交换两个变量（必须用引用！）
void swapValues(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

int main() {
    int a = 5;

    // 传值调用
    addTen_value(a);
    cout << "传值后 a = " << a << endl;  // a 还是 5（没变！）

    // 传引用调用
    addTen_ref(a);
    cout << "传引用后 a = " << a << endl;  // a 变成 15

    // 用传引用返回多个值
    int arr[] = {3, 7, 1, 9, 4};
    int mn, mx;
    findMinMax(arr, 5, mn, mx);
    cout << "最小值: " << mn << ", 最大值: " << mx << endl;  // 1, 9

    // 交换
    int x = 10, y = 20;
    swapValues(x, y);
    cout << "x=" << x << ", y=" << y << endl;  // x=20, y=10

    return 0;
}
