#include <iostream>
using namespace std;

// 单链表：每个节点存储数据和指向下一个节点的指针

struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}  // 构造函数
};

int main() {
    // 手动创建链表
    Node* head = new Node(1);    // 第一个节点
    head->next = new Node(2);   // 第二个节点
    head->next->next = new Node(3);  // 第三个节点
    // 链表: 1 -> 2 -> 3 -> NULL

    // 遍历链表
    Node* p = head;
    while (p != nullptr) {
        cout << p->data << " ";
        p = p->next;
    }
    cout << endl;  // 1 2 3

    // 在头部插入新节点
    Node* newNode = new Node(0);
    newNode->next = head;
    head = newNode;
    // 链表: 0 -> 1 -> 2 -> 3 -> NULL

    // 在中间插入（在节点值为 2 的前面插入 15）
    p = head;
    while (p->next != nullptr && p->next->data != 2) {
        p = p->next;
    }
    if (p->next != nullptr) {
        Node* insertNode = new Node(15);
        insertNode->next = p->next;
        p->next = insertNode;
    }
    // 链表: 0 -> 1 -> 15 -> 2 -> 3 -> NULL

    // 删除节点（删除值为 15 的节点）
    p = head;
    while (p->next != nullptr && p->next->data != 15) {
        p = p->next;
    }
    if (p->next != nullptr) {
        Node* toDelete = p->next;
        p->next = toDelete->next;
        delete toDelete;
    }
    // 链表: 0 -> 1 -> 2 -> 3 -> NULL

    // 竞赛中更常用的数组模拟链表（效率更高）
    const int MAXN = 100010;
    int val[MAXN];    // 存储节点值
    int nxt[MAXN];    // 存储下一个节点的下标
    int head2 = -1;   // 头指针，-1 表示空
    int cnt = 0;      // 当前使用的节点数

    // 在头部插入
    auto insertHead = [&](int x) {
        val[cnt] = x;
        nxt[cnt] = head2;
        head2 = cnt;
        cnt++;
    };

    insertHead(3);
    insertHead(2);
    insertHead(1);
    // 链表: 1 -> 2 -> 3

    // 遍历
    for (int i = head2; i != -1; i = nxt[i]) {
        cout << val[i] << " ";
    }
    cout << endl;  // 1 2 3

    return 0;
}
