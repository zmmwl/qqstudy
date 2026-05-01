#include <iostream>
using namespace std;

int main() {
    // 二维数组：表格形式的数据，有行和列
    // 就像一个 Excel 表格

    // 定义 3 行 4 列的二维数组
    int matrix[3][4] = {
        {1,  2,  3,  4},
        {5,  6,  7,  8},
        {9, 10, 11, 12}
    };

    // 访问元素：matrix[行下标][列下标]
    cout << matrix[0][0] << endl;   // 1（第1行第1列）
    cout << matrix[1][2] << endl;   // 7（第2行第3列）
    cout << matrix[2][3] << endl;   // 12（第3行第4列）

    // 读入二维数组
    int n, m;
    cin >> n >> m;  // n 行 m 列
    int a[100][100];

    for (int i = 0; i < n; i++) {        // 遍历每一行
        for (int j = 0; j < m; j++) {    // 遍历每一列
            cin >> a[i][j];
        }
    }

    // 输出二维数组
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << a[i][j] << " ";
        }
        cout << endl;
    }

    // 行列互换（矩阵转置）
    int b[100][100];
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            b[i][j] = a[j][i];
        }
    }

    // 多维数组：三维甚至更高维
    int cube[3][3][3] = {{{0}}};  // 3×3×3 的三维数组

    return 0;
}
