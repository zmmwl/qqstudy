#include <iostream>
#include <string>
using namespace std;

// 结构体：把多个不同类型的数据组合在一起
// 就像一张"信息卡片"

// 定义结构体类型
struct Student {
    string name;    // 姓名
    int age;        // 年龄
    double score;   // 分数
};  // 注意末尾的分号！

// 结构体可以作为函数参数
void printStudent(Student s) {
    cout << s.name << " " << s.age << "岁 成绩:" << s.score << endl;
}

// 传引用更高效（避免复制）
void addBonus(Student& s, double bonus) {
    s.score += bonus;
}

// 结构体数组
int main() {
    // 创建结构体变量
    Student s1;
    s1.name = "Xiao Ming";
    s1.age = 12;
    s1.score = 95.5;

    // 也可以在定义时初始化
    Student s2 = {"Xiao Hong", 11, 98.0};

    // 访问成员用 点运算符(.)
    cout << s1.name << " 成绩: " << s1.score << endl;

    printStudent(s1);
    addBonus(s1, 5.0);  // 加 5 分奖励
    printStudent(s1);

    // 结构体数组
    Student cls[3] = {
        {"Alice", 12, 90},
        {"Bob", 13, 85},
        {"Carol", 11, 95}
    };

    // 按成绩排序
    for (int i = 0; i < 3; i++) {
        for (int j = i + 1; j < 3; j++) {
            if (cls[j].score > cls[i].score) {
                Student temp = cls[i];
                cls[i] = cls[j];
                cls[j] = temp;
            }
        }
    }

    for (int i = 0; i < 3; i++) {
        printStudent(cls[i]);
    }

    return 0;
}
