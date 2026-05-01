#include <iostream>
using namespace std;

// 全局变量：定义在所有函数外面，所有函数都能访问
int globalVar = 100;

void func() {
    cout << "全局变量: " << globalVar << endl;  // 可以访问

    // 局部变量：定义在函数内部，只在函数内有效
    int localVar = 200;
    cout << "局部变量: " << localVar << endl;
}

void anotherFunc() {
    // cout << localVar;  // 错误！localVar 是 func 的局部变量
    cout << globalVar << endl;  // 可以访问全局变量

    // 如果局部变量和全局变量同名，局部变量优先
    int globalVar = 999;  // 这里的 globalVar 是局部变量
    cout << "局部: " << globalVar << endl;  // 999
    cout << "全局: " << ::globalVar << endl;  // 100（用 :: 访问全局变量）
}

// 静态局部变量：函数结束后不销毁，下次调用保持上次的值
void counter() {
    static int count = 0;  // 只在第一次调用时初始化
    count++;
    cout << "调用次数: " << count << endl;
}

int main() {
    func();
    anotherFunc();

    counter();  // 调用次数: 1
    counter();  // 调用次数: 2
    counter();  // 调用次数: 3

    // 块作用域
    {
        int x = 10;
        cout << x << endl;  // 10
    }
    // cout << x;  // 错误！x 已经不存在了

    return 0;
}
