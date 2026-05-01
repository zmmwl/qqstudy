#include <iostream>
using namespace std;

int main() {
    // ===== for 循环 =====
    // for (初始化; 条件; 更新) { 循环体 }
    // 最常用的循环，适合知道循环次数的情况

    // 输出 1 到 10
    for (int i = 1; i <= 10; i++) {
        cout << i << " ";
    }
    cout << endl;  // 1 2 3 4 5 6 7 8 9 10

    // 计算 1+2+3+...+100
    int sum = 0;
    for (int i = 1; i <= 100; i++) {
        sum += i;
    }
    cout << "1到100的和: " << sum << endl;  // 5050

    // ===== while 循环 =====
    // while (条件) { 循环体 }
    // 先判断条件，条件为真就执行循环体

    // 求 n 的位数
    int n = 12345;
    int count = 0;
    int temp = n;
    while (temp > 0) {
        temp /= 10;    // 去掉最后一位
        count++;       // 位数加 1
    }
    cout << n << " 有 " << count << " 位" << endl;  // 5 位

    // ===== do-while 循环 =====
    // do { 循环体 } while (条件);
    // 先执行一次循环体，再判断条件（至少执行一次）

    // 猜数字游戏（简化版）
    int secret = 42;
    int guess;
    do {
        cout << "请猜一个数字: ";
        cin >> guess;
        if (guess > secret) cout << "太大了" << endl;
        if (guess < secret) cout << "太小了" << endl;
    } while (guess != secret);
    cout << "猜对了！" << endl;

    // ===== break 和 continue =====
    // break：直接跳出整个循环
    // continue：跳过本次循环剩余部分，进入下一次

    // break 示例：找到第一个能被 7 整除的数
    for (int i = 100; i <= 200; i++) {
        if (i % 7 == 0) {
            cout << "找到: " << i << endl;  // 105
            break;  // 找到后立即退出循环
        }
    }

    // continue 示例：输出 1-20 中所有奇数
    for (int i = 1; i <= 20; i++) {
        if (i % 2 == 0) {
            continue;  // 偶数跳过，不执行下面的输出
        }
        cout << i << " ";
    }
    cout << endl;  // 1 3 5 7 9 11 13 15 17 19

    return 0;
}
