#include <iostream>
#include <vector>
using namespace std;

// 用邻接表存储图
vector<int> graph[10005];  // graph[i] 存储与节点 i 相连的所有节点
bool visited[10005] = {false};

// DFS 遍历图
void dfsGraph(int node) {
    visited[node] = true;
    cout << node << " ";  // 访问当前节点

    for (int i = 0; i < graph[node].size(); i++) {
        int next = graph[node][i];
        if (!visited[next]) {
            dfsGraph(next);  // 递归访问相邻节点
        }
    }
}

// BFS 遍历图
#include <queue>
void bfsGraph(int start) {
    bool vis[10005] = {false};
    queue<int> q;
    q.push(start);
    vis[start] = true;

    while (!q.empty()) {
        int node = q.front();
        q.pop();
        cout << node << " ";

        for (int i = 0; i < graph[node].size(); i++) {
            int next = graph[node][i];
            if (!vis[next]) {
                vis[next] = true;
                q.push(next);
            }
        }
    }
}

int main() {
    int n, m;  // n 个节点，m 条边
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);  // 无向图要加两条边
        graph[v].push_back(u);
    }

    cout << "DFS: ";
    dfsGraph(1);
    cout << endl;

    cout << "BFS: ";
    bfsGraph(1);
    cout << endl;

    return 0;
}
