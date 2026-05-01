#include <iostream>
#include <queue>
using namespace std;

// 例：迷宫最短路径（BFS版）
int n;
int maze[100][100];
bool visited[100][100] = {false};
int dist[100][100] = {0};  // dist[i][j] 表示从起点到(i,j)的最短距离
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};

int bfs(int sx, int sy, int ex, int ey) {
    queue<pair<int, int>> q;   // 队列中存放坐标
    q.push({sx, sy});
    visited[sx][sy] = true;
    dist[sx][sy] = 0;

    while (!q.empty()) {
        auto cur = q.front();   // 取队首
        q.pop();                // 出队
        int x = cur.first;
        int y = cur.second;

        if (x == ex && y == ey) {
            return dist[x][y];  // 到达终点，返回距离
        }

        // 尝试四个方向
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= 0 && nx < n && ny >= 0 && ny < n
                && maze[nx][ny] == 0 && !visited[nx][ny]) {
                visited[nx][ny] = true;
                dist[nx][ny] = dist[x][y] + 1;  // 距离+1
                q.push({nx, ny});                 // 入队
            }
        }
    }
    return -1;  // 无法到达
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> maze[i][j];

    int result = bfs(0, 0, n - 1, n - 1);
    if (result != -1) {
        cout << "最短路径: " << result << " 步" << endl;
    } else {
        cout << "无法到达终点" << endl;
    }
    return 0;
}
