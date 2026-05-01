#include <iostream>
using namespace std;

int main() {
    // 命名规则：
    // 1. 只能用字母(a-z, A-Z)、数字(0-9)、下划线(_)
    // 2. 不能以数字开头
    // 3. 不能是 C++ 关键字（如 int, return, if 等）
    // 4. 区分大小写（age 和 Age 是不同的变量）

    int age = 12;          // 合法
    int _count = 5;        // 合法（下划线开头）
    int student2 = 10;     // 合法
    // int 2student = 10;  // 非法！不能以数字开头
    // int my-name = 10;   // 非法！不能用连字符
    // int int = 10;       // 非法！不能用关键字

    // 好的命名习惯：
    int studentAge = 12;     // 驼峰命名法
    int student_age = 12;    // 下划线命名法
    // 命名要有意义，让别人一看就知道变量存的是什么

    // 变量必须先定义（声明）再使用
    // 定义时可以不给初始值（但不推荐，未初始化的值是不确定的）
    int x;           // 只定义，未初始化（x 的值不确定）
    int y = 0;       // 定义并初始化为 0（推荐）
    int z(10);       // 另一种初始化方式，z = 10
    int w{20};       // C++11 的初始化方式，w = 20

    cout << "y = " << y << ", z = " << z << ", w = " << w << endl;

    return 0;
}
