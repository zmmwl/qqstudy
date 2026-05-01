#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <algorithm>
using namespace std;

int main() {
    // ===== vector（动态数组）=====
    // 最常用的容器，可以自动扩展大小

    vector<int> v;         // 定义空 vector
    vector<int> v2(10);    // 定义 10 个元素的 vector，默认值为 0
    vector<int> v3(10, 5); // 定义 10 个元素的 vector，初始值都为 5

    v.push_back(10);   // 在末尾添加元素
    v.push_back(20);
    v.push_back(30);
    // v = {10, 20, 30}

    cout << "大小: " << v.size() << endl;   // 3
    cout << "v[0] = " << v[0] << endl;     // 10
    cout << "v[1] = " << v.at(1) << endl;  // 20

    v.pop_back();      // 删除末尾元素
    // v = {10, 20}

    // 遍历 vector
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }
    cout << endl;

    // 范围 for 循环
    for (int x : v) {
        cout << x << " ";
    }
    cout << endl;

    // 清空
    v.clear();
    cout << "清空后大小: " << v.size() << endl;  // 0

    // 排序 vector
    vector<int> nums = {5, 2, 8, 1, 9};
    sort(nums.begin(), nums.end());
    for (int x : nums) cout << x << " ";
    cout << endl;  // 1 2 5 8 9

    // ===== stack（栈）=====
    // 后进先出（LIFO）：最后放进去的最先出来
    // 就像叠盘子：最后放的在最上面，取也从最上面取

    stack<int> stk;
    stk.push(10);    // 入栈：10
    stk.push(20);    // 入栈：10, 20（20 在栈顶）
    stk.push(30);    // 入栈：10, 20, 30（30 在栈顶）

    cout << "栈顶: " << stk.top() << endl;  // 30
    stk.pop();        // 出栈：移除栈顶
    cout << "新栈顶: " << stk.top() << endl;  // 20
    cout << "栈大小: " << stk.size() << endl;  // 2

    // 遍历栈（需要边弹边看）
    while (!stk.empty()) {
        cout << stk.top() << " ";
        stk.pop();
    }
    cout << endl;  // 20 10

    // ===== queue（队列）=====
    // 先进先出（FIFO）：先放进去的先出来
    // 就像排队：先到的人先服务

    queue<int> q;
    q.push(10);     // 入队：10
    q.push(20);     // 入队：10, 20
    q.push(30);     // 入队：10, 20, 30

    cout << "队首: " << q.front() << endl;  // 10
    cout << "队尾: " << q.back() << endl;   // 30
    q.pop();          // 出队：移除队首
    cout << "新队首: " << q.front() << endl;  // 20

    // 优先队列（堆）：每次取最大（或最小）的元素
    priority_queue<int> pq;  // 默认大根堆（最大元素在顶部）
    pq.push(30);
    pq.push(10);
    pq.push(20);
    cout << "最大: " << pq.top() << endl;  // 30
    pq.pop();
    cout << "次大: " << pq.top() << endl;  // 20

    // 小根堆（最小元素在顶部）
    priority_queue<int, vector<int>, greater<int>> minPQ;

    // ===== list（双向链表）=====
    list<int> lst;
    lst.push_back(10);    // 尾部添加
    lst.push_front(20);   // 头部添加
    lst.push_back(30);
    // lst = {20, 10, 30}

    for (int x : lst) {
        cout << x << " ";
    }
    cout << endl;

    lst.sort();  // 链表排序
    lst.reverse();  // 链表反转

    return 0;
}
