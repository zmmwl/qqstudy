#include <iostream>
#include <vector>
using namespace std;

// 图由顶点和边组成
// G = (V, E)，V 是顶点集合，E 是边集合

// 图的存储方式1：邻接矩阵
// 用二维数组 matrix[i][j] 表示顶点 i 到顶点 j 是否有边（以及边的权值）
// 适合稠密图（边很多），空间 O(n²)

void adjacencyMatrix() {
    int n = 5;  // 5 个顶点（编号 0~4）
    int matrix[100][100] = {0};  // 初始化为 0

    // 添加无向边（u, v）
    auto addEdge = [&](int u, int v, int w = 1) {
        matrix[u][v] = w;
        matrix[v][u] = w;  // 无向图，两个方向都要设
    };

    addEdge(0, 1);
    addEdge(0, 2);
    addEdge(1, 3);
    addEdge(2, 4);

    // 查看与顶点 0 相邻的所有顶点
    cout << "与顶点 0 相邻的: ";
    for (int i = 0; i < n; i++) {
        if (matrix[0][i]) cout << i << " ";
    }
    cout << endl;  // 1 2

    // 打印邻接矩阵
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}

// 图的存储方式2：邻接表
// 每个顶点维护一个列表，记录与它相邻的顶点
// 适合稀疏图（边不多），空间 O(n+m)

void adjacencyList() {
    int n = 5;
    vector<int> adj[100];  // adj[i] 存储顶点 i 的所有邻居

    // 添加无向边
    auto addEdge = [&](int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u);
    };

    addEdge(0, 1);
    addEdge(0, 2);
    addEdge(1, 3);
    addEdge(2, 4);

    // 查看与顶点 0 相邻的所有顶点
    cout << "与顶点 0 相邻的: ";
    for (int v : adj[0]) {
        cout << v << " ";
    }
    cout << endl;  // 1 2

    // 打印所有顶点的邻居
    for (int i = 0; i < n; i++) {
        cout << "顶点 " << i << " 的邻居: ";
        for (int v : adj[i]) {
            cout << v << " ";
        }
        cout << endl;
    }
}

// 带权图的邻接表存储
struct Edge {
    int to;      // 目标顶点
    int weight;  // 边的权值
};

void weightedGraph() {
    int n = 4;
    vector<Edge> adj[100];

    auto addEdge = [&](int u, int v, int w) {
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});  // 无向图
    };

    addEdge(0, 1, 5);
    addEdge(1, 2, 3);
    addEdge(2, 3, 1);

    // 查看顶点 1 的所有边
    for (auto& e : adj[1]) {
        cout << "1 -> " << e.to << " 权重:" << e.weight << endl;
    }
}

int main() {
    cout << "=== 邻接矩阵 ===" << endl;
    adjacencyMatrix();
    cout << "=== 邻接表 ===" << endl;
    adjacencyList();
    cout << "=== 带权图 ===" << endl;
    weightedGraph();
    return 0;
}
