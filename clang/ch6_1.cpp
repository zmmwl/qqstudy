#include <iostream>
using namespace std;

// ===== 1. 顺序结构：按照从上到下的顺序依次执行 =====
void sequentialExample() {
    int a = 10;
    int b = 20;
    int c = a + b;      // 先执行这行
    cout << c << endl;   // 再执行这行
    c = c * 2;          // 然后执行这行
    cout << c << endl;
}

// ===== 2. 分支结构：根据条件选择不同的执行路径 =====
void branchExample() {
    int age;
    cin >> age;
    if (age >= 18) {
        cout << "成年" << endl;
    } else {
        cout << "未成年" << endl;
    }
}

// ===== 3. 循环结构：重复执行某段代码 =====
void loopExample() {
    // 计算 2 的 10 次方
    int result = 1;
    for (int i = 0; i < 10; i++) {
        result *= 2;
    }
    cout << "2^10 = " << result << endl;  // 1024
}

int main() {
    sequentialExample();
    loopExample();
    return 0;
}
