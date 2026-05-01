#include <iostream>
#include <queue>
using namespace std;

// 队列：先进先出（FIFO - First In First Out）
// 在队尾入队，在队首出队

int main() {
    queue<int> q;
    q.push(1);
    q.push(2);
    q.push(3);

    // 应用1：约瑟夫问题
    // n 个人围成一圈，从第 1 个人开始报数，报到 m 的人出列，求出列顺序
    int n = 7, m = 3;
    queue<int> jose;
    for (int i = 1; i <= n; i++) jose.push(i);

    cout << "出列顺序: ";
    while (!jose.empty()) {
        for (int i = 1; i < m; i++) {
            jose.push(jose.front());
            jose.pop();
        }
        cout << jose.front() << " ";
        jose.pop();
    }
    cout << endl;
    // 出列顺序: 3 6 2 7 5 1 4

    // 应用2：BFS 广度优先搜索（在 Day 3 详细讲）

    return 0;
}
