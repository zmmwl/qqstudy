#include <iostream>
using namespace std;

int main() {
    // && 逻辑与（AND）：两个条件都为真，结果才为真
    // || 逻辑或（OR）：只要有一个条件为真，结果就为真
    // !  逻辑非（NOT）：取反，真变假，假变真

    int age = 15;
    int score = 90;

    // 逻辑与 &&：两个条件都要满足
    if (age >= 12 && score >= 80) {
        cout << "符合条件" << endl;
    }

    // 逻辑或 ||：满足其中一个条件即可
    if (score >= 90 || age >= 18) {
        cout << "满足至少一个条件" << endl;
    }

    // 逻辑非 !
    bool isRaining = false;
    if (!isRaining) {
        cout << "没下雨，可以去玩" << endl;
    }

    // 短路求值（重要！）
    // 对于 &&：如果左边为 false，右边不再计算
    // 对于 ||：如果左边为 true，右边不再计算
    int x = 0;
    // if (x != 0 && 10 / x > 1) ← 安全！x==0 时右边不会计算，不会除以0

    // 德摩根定律
    // !(a && b) 等价于 (!a || !b)
    // !(a || b) 等价于 (!a && !b)

    // 真值表：
    // a      b      a&&b   a||b   !a
    // true   true   true   true   false
    // true   false  false  true   false
    // false  true   false  true   true
    // false  false  false  false  true

    return 0;
}
