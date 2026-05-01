#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // 打印乘法口诀表
    for (int i = 1; i <= 9; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%d×%d=%-4d", j, i, i * j);  // %-4d 左对齐，占4位
        }
        cout << endl;
    }

    cout << "----------" << endl;

    // 打印星号三角形
    //     *
    //    ***
    //   *****
    //  *******
    // *********
    int n = 5;
    for (int i = 1; i <= n; i++) {
        // 打印空格
        for (int j = 1; j <= n - i; j++) {
            cout << " ";
        }
        // 打印星号
        for (int j = 1; j <= 2 * i - 1; j++) {
            cout << "*";
        }
        cout << endl;
    }

    cout << "----------" << endl;

    // 枚举：百钱买百鸡问题
    // 公鸡5元一只，母鸡3元一只，小鸡1元三只，100元买100只，各买多少？
    for (int x = 0; x <= 20; x++) {         // 公鸡最多 100/5=20 只
        for (int y = 0; y <= 33; y++) {     // 母鸡最多 100/3=33 只
            int z = 100 - x - y;             // 小鸡数量
            if (z >= 0 && z % 3 == 0 && 5 * x + 3 * y + z / 3 == 100) {
                cout << "公鸡:" << x << " 母鸡:" << y << " 小鸡:" << z << endl;
            }
        }
    }

    return 0;
}
