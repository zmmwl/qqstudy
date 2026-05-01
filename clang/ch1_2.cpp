#include <iostream>
using namespace std;

int main()
{
    // 【标识符】程序员自己起的名字，比如变量名、函数名
    // 规则：只能用字母、数字、下划线，不能以数字开头，不能是关键字
    int myAge = 12;         // myAge 是一个标识符
    int student_count = 30; // student_count 是一个标识符

    // 【关键字】C++ 保留的特殊单词，有固定含义，不能用作标识符
    // 常见关键字：int, double, char, bool, if, else, for, while, return, const, void...
    // int age = 10; ← "int" 就是关键字

    // 【常量】值不能改变的量
    const double PI = 3.14159; // 用 const 定义的常量，之后不能修改
    // PI = 3.14;  // 错误！常量不能被重新赋值

    // 【变量】值可以改变的量
    int score = 95;                      // 定义变量 score，初始值为 95
    score = 88;                          // 可以修改变量的值
    cout << "score = " << score << endl; // 输出 88

    // 【字符串】用双引号括起来的字符序列
    string name = "Xiao Ming"; // string 类型存储字符串
    cout << "name = " << name << endl;

    // 【表达式】由运算符和操作数组成的算式
    int a = 10, b = 3;
    int sum = a + b;                   // a + b 是算术表达式
    bool isEqual = (a == b);           // a == b 是关系表达式
    bool result = (a > 5) && (b < 10); // 逻辑表达式
    // if (a < 20)
    // {
    //     cout << "Hi Chloe" << endl;
    // }
    // else
    // {
    //     cout << "Hi zmm" << endl;
    // }

    cout << "sum = " << sum << endl;         // 13
    cout << "isEqual = " << isEqual << endl; // 0 (false)
    cout << "result = " << result << endl;   // 1 (true)

    return 0;
}
