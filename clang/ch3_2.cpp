#include <iostream>
using namespace std;

int main() {
    // ===== if 语句 =====

    // 基本 if
    int score = 85;
    if (score >= 60) {
        cout << "及格了！" << endl;
    }

    // if-else
    if (score >= 90) {
        cout << "优秀" << endl;
    } else if (score >= 80) {
        cout << "良好" << endl;
    } else if (score >= 60) {
        cout << "及格" << endl;
    } else {
        cout << "不及格" << endl;
    }
    // 输出：良好

    // 多层嵌套的 if
    int age = 16;
    bool hasTicket = true;
    if (age >= 18) {
        if (hasTicket) {
            cout << "可以进入" << endl;
        } else {
            cout << "需要买票" << endl;
        }
    } else {
        if (age >= 12) {
            cout << "需要成人陪同" << endl;
        } else {
            cout << "禁止入内" << endl;
        }
    }

    // ===== switch 语句 =====
    // 适用于根据一个整数值选择不同分支的情况
    int day = 3;
    switch (day) {
        case 1:
            cout << "星期一" << endl;
            break;     // break 不能忘！否则会继续执行下面的 case
        case 2:
            cout << "星期二" << endl;
            break;
        case 3:
            cout << "星期三" << endl;
            break;
        case 4:
            cout << "星期四" << endl;
            break;
        case 5:
            cout << "星期五" << endl;
            break;
        case 6:
        case 7:
            cout << "周末" << endl;  // case 6 和 7 共享同一段代码
            break;
        default:
            cout << "无效的日期" << endl;  // 以上 case 都不匹配时执行
    }

    return 0;
}
