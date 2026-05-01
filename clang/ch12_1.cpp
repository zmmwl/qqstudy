#include <iostream>
#include <fstream>   // 文件操作头文件
#include <cstdio>
using namespace std;

int main() {
    // ===== C++ 风格文件操作 =====

    // 写文件
    ofstream fout("output.txt");  // 打开文件用于写入
    // 如果文件不存在会自动创建
    fout << "Hello, File!" << endl;
    fout << 42 << endl;
    fout << 3.14 << endl;
    fout.close();  // 关闭文件（重要！）

    // 读文件
    ifstream fin("input.txt");   // 打开文件用于读取
    // 如果文件不存在，fin 会处于失败状态
    if (!fin.is_open()) {
        cout << "文件打开失败" << endl;
        return 1;
    }

    string line;
    while (getline(fin, line)) {  // 逐行读取
        cout << line << endl;
    }
    fin.close();

    // 读入数字
    ifstream fin2("data.txt");
    int a, b;
    fin2 >> a >> b;  // 和 cin 用法一样，只是来源从键盘变成了文件
    cout << a + b << endl;
    fin2.close();

    // 追加写入（在文件末尾追加，不覆盖原有内容）
    ofstream fout2("output.txt", ios::app);  // ios::app 表示追加模式
    fout2 << "追加的内容" << endl;
    fout2.close();

    // ===== C 风格文件操作（竞赛中更常用的是重定向）=====

    // 文件重定向（最简单的文件读写方式）
    // 方法：在 main 函数开头加上这两行，然后正常用 cin/cout
    // freopen("input.txt", "r", stdin);   // 从文件读入
    // freopen("output.txt", "w", stdout); // 输出到文件
    // 之后 cin >> x 就从 input.txt 读取，cout << x 就输出到 output.txt

    return 0;
}
