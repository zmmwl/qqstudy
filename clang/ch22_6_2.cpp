#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

// 高精度乘法：大整数 × 普通整数
vector<int> mulBig(vector<int> A, int b) {
    vector<int> C;
    int carry = 0;
    for (int i = 0; i < A.size() || carry; i++) {
        int prod = carry;
        if (i < A.size()) prod += A[i] * b;
        C.push_back(prod % 10);
        carry = prod / 10;
    }
    // 去除前导零
    while (C.size() > 1 && C.back() == 0) C.pop_back();
    return C;
}

int main() {
    string a;
    int b;
    cin >> a >> b;

    vector<int> A;
    for (int i = a.length() - 1; i >= 0; i--) A.push_back(a[i] - '0');

    vector<int> result = mulBig(A, b);

    for (int i = result.size() - 1; i >= 0; i--) {
        cout << result[i];
    }
    cout << endl;
    return 0;
}
