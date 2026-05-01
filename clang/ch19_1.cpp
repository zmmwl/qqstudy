#include <iostream>
using namespace std;

// 例1：全排列问题
// 输出 1~n 的所有排列方式
int n;
int path[10];         // 存放当前排列
bool used[10] = {false}; // 标记数字是否已使用

void dfs(int step) {
    if (step == n) {  // 排列完成，输出结果
        for (int i = 0; i < n; i++) {
            cout << path[i] << " ";
        }
        cout << endl;
        return;
    }

    for (int i = 1; i <= n; i++) {
        if (!used[i]) {         // 如果数字 i 还没使用
            path[step] = i;     // 放入排列
            used[i] = true;     // 标记为已使用
            dfs(step + 1);      // 递归处理下一个位置
            used[i] = false;    // 回溯：撤销标记，恢复现场
        }
    }
}

int main() {
    cout << "输入 n: ";
    cin >> n;
    dfs(0);
    return 0;
}
