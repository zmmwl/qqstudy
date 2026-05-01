#include <iostream>
#include <stack>
using namespace std;

// 栈：后进先出（LIFO - Last In First Out）
// 只能在栈顶操作（压入 push、弹出 pop、查看栈顶 top）

// 用数组手动实现栈
const int MAXN = 1000;
int st[MAXN];
int top = 0;  // 栈顶指针（指向下一个要放的位置）

void push(int x) { st[top++] = x; }
void pop() { top--; }
int getTop() { return st[top - 1]; }
bool isEmpty() { return top == 0; }

int main() {
    // STL stack 用法
    stack<int> s;

    // 应用1：括号匹配
    string expr = "((()))()";  // 检查括号是否匹配
    bool valid = true;
    stack<char> bracketStack;
    for (char c : expr) {
        if (c == '(') {
            bracketStack.push(c);
        } else if (c == ')') {
            if (bracketStack.empty()) {
                valid = false;
                break;
            }
            bracketStack.pop();
        }
    }
    if (!bracketStack.empty()) valid = false;
    cout << "括号" << (valid ? "匹配" : "不匹配") << endl;

    // 应用2：表达式求值（后缀表达式/逆波兰表达式）
    // 例如："3 4 + 5 *" = (3+4)*5 = 35
    stack<int> calc;
    string tokens[] = {"3", "4", "+", "5", "*"};
    for (int i = 0; i < 5; i++) {
        if (tokens[i] == "+" || tokens[i] == "-" ||
            tokens[i] == "*" || tokens[i] == "/") {
            int b = calc.top(); calc.pop();
            int a = calc.top(); calc.pop();
            if (tokens[i] == "+") calc.push(a + b);
            if (tokens[i] == "-") calc.push(a - b);
            if (tokens[i] == "*") calc.push(a * b);
            if (tokens[i] == "/") calc.push(a / b);
        } else {
            calc.push(stoi(tokens[i]));
        }
    }
    cout << "结果: " << calc.top() << endl;  // 35

    // 应用3：十进制转二进制
    int num = 13;
    stack<int> binary;
    while (num > 0) {
        binary.push(num % 2);
        num /= 2;
    }
    cout << "13 的二进制: ";
    while (!binary.empty()) {
        cout << binary.top();
        binary.pop();
    }
    cout << endl;  // 1101

    return 0;
}
