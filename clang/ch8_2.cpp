#include <iostream>
#include <string>
using namespace std;

int main() {
    // string 类：比字符数组更方便、更安全的字符串类型

    // 定义和初始化
    string s1 = "Hello";
    string s2 = "World";
    string s3(5, 'a');  // 5 个 'a'，即 "aaaaa"
    cout << s3 << endl;

    // 输入
    // cin >> s1;           // 读入一个词
    // getline(cin, s1);    // 读入一整行（推荐）

    // 常用操作
    // 求长度
    cout << "长度: " << s1.length() << endl;   // 5
    cout << "长度: " << s1.size() << endl;     // 5（和 length 一样）

    // 字符串连接
    string s4 = s1 + " " + s2;  // 用 + 连接
    cout << s4 << endl;  // Hello World
    s1 += "!";  // 追加
    cout << s1 << endl;  // Hello!

    // 字符串比较（直接用 ==, <, > 等）
    if (s1 == "Hello!") cout << "相等" << endl;
    if ("abc" < "abd") cout << "abc < abd" << endl;

    // 访问单个字符（和数组一样，下标从 0 开始）
    cout << s1[0] << endl;   // H
    cout << s1.at(0) << endl;  // H（at 会检查越界，更安全）

    // 子串：substr(起始位置, 长度)
    string s = "Hello World";
    cout << s.substr(0, 5) << endl;   // Hello（从位置 0 取 5 个字符）
    cout << s.substr(6) << endl;      // World（从位置 6 取到末尾）

    // 查找：find（找到返回位置，找不到返回 string::npos）
    size_t pos = s.find("World");
    if (pos != string::npos) {
        cout << "找到 World，位置: " << pos << endl;  // 6
    }
    cout << (int)s.find("xyz") << endl;  // -1（找不到）

    // 插入：insert(位置, 字符串)
    string s5 = "Hello";
    s5.insert(2, "XX");  // 在位置 2 插入 "XX"
    cout << s5 << endl;  // HeXXllo

    // 删除：erase(位置, 长度)
    s5.erase(2, 2);      // 从位置 2 删 2 个字符
    cout << s5 << endl;  // Hello

    // 替换：replace(位置, 长度, 新字符串)
    string s6 = "Hello World";
    s6.replace(6, 5, "C++");  // 从位置 6 替换 5 个字符为 "C++"
    cout << s6 << endl;  // Hello C++

    // 遍历字符串
    for (int i = 0; i < s.size(); i++) {
        cout << s[i] << " ";
    }
    cout << endl;

    // C++11 范围 for 循环（更简洁）
    for (char c : s) {
        cout << c << " ";
    }
    cout << endl;

    // string 转 char 数组
    const char* p = s.c_str();

    // 数字与字符串互转
    int num = 123;
    string str = to_string(num);     // 数字转字符串
    int num2 = stoi(str);            // 字符串转整数
    double d = stod("3.14");         // 字符串转 double

    return 0;
}
