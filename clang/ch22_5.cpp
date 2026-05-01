#include <iostream>
using namespace std;

// 组合数 C(n, m) = n! / (m! * (n-m)!)
// 用递推公式：C(n, m) = C(n-1, m-1) + C(n-1, m)
// 即：杨辉三角

long long C[105][105];

void initComb() {
    // 计算 C(n, m)，存入二维数组
    for (int i = 0; i <= 100; i++) {
        C[i][0] = 1;  // C(n, 0) = 1
        for (int j = 1; j <= i; j++) {
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
        }
    }
}

int main() {
    initComb();

    int n, m;
    cin >> n >> m;
    cout << "C(" << n << "," << m << ") = " << C[n][m] << endl;

    // 打印杨辉三角（前10行）
    cout << endl << "杨辉三角:" << endl;
    for (int i = 0; i <= 10; i++) {
        for (int j = 0; j <= i; j++) {
            cout << C[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
