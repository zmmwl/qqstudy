#include <iostream>
using namespace std;

// 例2：迷宫问题（DFS版）
// 在 n×n 的迷宫中，0表示通路，1表示墙壁，求从(0,0)到(n-1,n-1)的路径数
int n;
int maze[20][20];
bool visited[20][20] = {false};
int pathCount = 0;
int dx[] = {0, 0, 1, -1};  // 四个方向：右、左、下、上
int dy[] = {1, -1, 0, 0};

void dfs(int x, int y) {
    // 到达终点
    if (x == n - 1 && y == n - 1) {
        pathCount++;
        return;
    }

    // 尝试四个方向
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        // 检查：不越界、不是墙、没走过
        if (nx >= 0 && nx < n && ny >= 0 && ny < n
            && maze[nx][ny] == 0 && !visited[nx][ny]) {
            visited[nx][ny] = true;   // 标记已访问
            dfs(nx, ny);              // 继续搜索
            visited[nx][ny] = false;  // 回溯
        }
    }
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> maze[i][j];

    visited[0][0] = true;  // 起点标记已访问
    dfs(0, 0);
    cout << "路径数: " << pathCount << endl;
    return 0;
}
