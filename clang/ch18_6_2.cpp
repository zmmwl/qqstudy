#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

// 结构体排序：按总分从高到低，总分相同按学号从小到大
struct Student {
    int id;
    int score;
};

bool cmp(Student a, Student b) {
    if (a.score != b.score) return a.score > b.score;  // 分数降序
    return a.id < b.id;                                 // 学号升序
}

int main() {
    Student stu[] = {{3, 90}, {1, 95}, {2, 90}, {4, 88}};
    int n = 4;
    sort(stu, stu + n, cmp);
    for (int i = 0; i < n; i++) {
        cout << "学号:" << stu[i].id << " 分数:" << stu[i].score << endl;
    }
    return 0;
}
