#include <iostream>
#include <string>
using namespace std;

struct Student {
    string name;
    int age;
    double score;
};

int main() {
    Student s = {"Xiao Ming", 12, 95.5};

    // 指向结构体的指针
    Student* p = &s;

    // 通过指针访问成员，用 -> 运算符（而不是 .）
    cout << p->name << endl;    // Xiao Ming
    cout << p->age << endl;     // 12
    cout << p->score << endl;   // 95.5

    // p->name 等价于 (*p).name
    cout << (*p).name << endl;  // Xiao Ming

    // 通过指针修改
    p->age = 13;
    cout << s.age << endl;  // 13

    return 0;
}
