#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

// 高精度加法：计算两个超大整数的和
// 用字符串读入，用 vector 倒序存储（个位在前）

vector<int> addBig(string a, string b) {
    vector<int> A, B, C;

    // 倒序存入 vector
    for (int i = a.length() - 1; i >= 0; i--) A.push_back(a[i] - '0');
    for (int i = b.length() - 1; i >= 0; i--) B.push_back(b[i] - '0');

    int carry = 0;  // 进位
    for (int i = 0; i < A.size() || i < B.size() || carry; i++) {
        int sum = carry;
        if (i < A.size()) sum += A[i];
        if (i < B.size()) sum += B[i];
        C.push_back(sum % 10);   // 当前位
        carry = sum / 10;         // 进位
    }

    return C;
}

int main() {
    string a, b;
    cin >> a >> b;

    vector<int> result = addBig(a, b);

    // 倒序输出（因为存的时候是倒序的）
    for (int i = result.size() - 1; i >= 0; i--) {
        cout << result[i];
    }
    cout << endl;
    return 0;
}
