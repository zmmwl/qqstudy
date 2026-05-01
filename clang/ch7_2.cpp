#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int n;
    cin >> n;  // 先输入数组大小

    int arr[100];  // 假设最多 100 个元素

    // 读入数组
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // 输出数组
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // 求数组的最大值和最小值
    int maxVal = arr[0], minVal = arr[0];
    int maxIdx = 0, minIdx = 0;
    for (int i = 1; i < n; i++) {
        if (arr[i] > maxVal) {
            maxVal = arr[i];
            maxIdx = i;
        }
        if (arr[i] < minVal) {
            minVal = arr[i];
            minIdx = i;
        }
    }
    cout << "最大值: " << maxVal << " 下标: " << maxIdx << endl;
    cout << "最小值: " << minVal << " 下标: " << minIdx << endl;

    // 求数组元素的和与平均值
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    double avg = (double)sum / n;
    cout << "总和: " << sum << " 平均: " << avg << endl;

    // 数组逆序
    for (int i = 0; i < n / 2; i++) {
        int temp = arr[i];
        arr[i] = arr[n - 1 - i];
        arr[n - 1 - i] = temp;
    }
    cout << "逆序后: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
