#include <iostream>
using namespace std;

// 联合体：所有成员共享同一块内存
// 同一时刻只能使用其中一个成员
// 大小等于最大成员的大小

union Data {
    int i;
    double d;
    char c;
};

int main() {
    Data data;

    data.i = 42;
    cout << "int: " << data.i << endl;   // 42
    // 此时 d 和 c 的值是不确定的

    data.d = 3.14;
    cout << "double: " << data.d << endl;  // 3.14
    // 此时 i 的值已经被覆盖了
    cout << "int now: " << data.i << endl;  // 一个奇怪的值

    // 联合体的大小
    cout << "Data 大小: " << sizeof(Data) << endl;  // 8（double 的大小）

    // 实际用途举例：节省内存（较少使用，了解即可）

    return 0;
}
