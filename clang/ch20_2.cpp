#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

// Dijkstra：求单源最短路径（边权非负）
// 用邻接表存储：pair<相邻节点, 边权>
vector<pair<int, int>> graph[10005];
int dist[10005];  // dist[i] 表示起点到节点 i 的最短距离

void dijkstra(int start, int n) {
    // 初始化距离为无穷大
    for (int i = 1; i <= n; i++) dist[i] = INT_MAX;
    dist[start] = 0;

    // 优先队列：pair<距离, 节点>，小的优先
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, start});

    while (!pq.empty()) {
        auto cur = pq.top();
        pq.pop();
        int d = cur.first;    // 当前距离
        int u = cur.second;   // 当前节点

        if (d > dist[u]) continue;  // 已经找到更短的路径，跳过

        // 遍历所有相邻节点
        for (int i = 0; i < graph[u].size(); i++) {
            int v = graph[u][i].first;   // 相邻节点
            int w = graph[u][i].second;  // 边权

            // 如果经过 u 到 v 更短，更新
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
}

int main() {
    int n, m, start;
    cout << "输入 节点数 边数 起点: ";
    cin >> n >> m >> start;

    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u].push_back({v, w});
        graph[v].push_back({u, w});  // 无向图
    }

    dijkstra(start, n);

    cout << "从 " << start << " 出发的最短距离:" << endl;
    for (int i = 1; i <= n; i++) {
        cout << "到 " << i << ": ";
        if (dist[i] == INT_MAX) cout << "不可达";
        else cout << dist[i];
        cout << endl;
    }
    return 0;
}
