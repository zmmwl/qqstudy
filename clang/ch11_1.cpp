#include <iostream>
using namespace std;

int main() {
    // 指针：存储变量地址的变量
    // 可以理解为"门牌号"——它不存数据本身，而是存数据在哪里

    int a = 10;

    // &a 取变量 a 的地址
    cout << "a 的值: " << a << endl;
    cout << "a 的地址: " << &a << endl;

    // 定义指针变量：类型* 指针名
    int* p = &a;   // p 指向 a，p 存的是 a 的地址
    cout << "p 的值(a的地址): " << p << endl;
    cout << "p 指向的值(a的值): " << *p << endl;  // 10
    // *p 叫做"解引用"，获取指针指向的值

    // 通过指针修改值
    *p = 20;       // 相当于 a = 20
    cout << "修改后 a = " << a << endl;  // 20

    // 指针的地址
    cout << "p 自己的地址: " << &p << endl;

    // 空指针
    int* null_p = nullptr;  // 或 NULL（C++11 推荐用 nullptr）
    // *null_p = 5;  // 危险！不能解引用空指针

    return 0;
}
