#include <iostream>
#include <algorithm>
using namespace std;

// Kruskal 算法：求最小生成树
// 思路：把边按权值从小到大排序，依次选边（不能形成环）

struct Edge {
    int u, v, w;  // 起点、终点、权值
};

bool cmp(Edge a, Edge b) {
    return a.w < b.w;  // 按权值从小到大排序
}

Edge edges[100005];
int parent[10005];  // 并查集

// 并查集：查找根节点（带路径压缩）
int findRoot(int x) {
    if (parent[x] != x) {
        parent[x] = findRoot(parent[x]);  // 路径压缩
    }
    return parent[x];
}

// 并查集：合并两个集合
void unite(int x, int y) {
    int rx = findRoot(x);
    int ry = findRoot(y);
    if (rx != ry) parent[rx] = ry;
}

int main() {
    int n, m;  // n 个节点，m 条边
    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
    }

    // 初始化并查集
    for (int i = 1; i <= n; i++) parent[i] = i;

    // 按边权排序
    sort(edges, edges + m, cmp);

    int totalWeight = 0;  // 最小生成树的总权值
    int edgeCount = 0;    // 已选的边数

    for (int i = 0; i < m && edgeCount < n - 1; i++) {
        int u = edges[i].u, v = edges[i].v;
        // 如果 u 和 v 不在同一个集合，说明不会形成环
        if (findRoot(u) != findRoot(v)) {
            unite(u, v);
            totalWeight += edges[i].w;
            edgeCount++;
            cout << "选边: " << u << "-" << v << " 权值:" << edges[i].w << endl;
        }
    }

    if (edgeCount == n - 1) {
        cout << "最小生成树总权值: " << totalWeight << endl;
    } else {
        cout << "图不连通，无法生成最小生成树" << endl;
    }
    return 0;
}
