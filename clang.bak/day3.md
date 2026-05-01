# Day 3: 算法与数学

> **学习目标**：掌握常见算法思想（枚举、模拟、贪心、二分、分治），学会排序、搜索（DFS/BFS）、动态规划等核心算法，并能运用数学知识解决竞赛中的数论与组合问题。

---

## 第十五章 算法入门——什么是算法？

### 15.1 算法的概念

**算法**就是解决问题的步骤。写程序之前，先想清楚"怎么做"，再写代码实现。

```cpp
#include <iostream>
using namespace std;

// 例子：求 1+2+...+n 的和
// 算法1：逐个相加（时间复杂度 O(n)）
int sumV1(int n) {
    int s = 0;
    for (int i = 1; i <= n; i++) {
        s += i;
    }
    return s;
}

// 算法2：数学公式（时间复杂度 O(1)）
// 1+2+...+n = n*(n+1)/2
int sumV2(int n) {
    return n * (n + 1) / 2;
}

int main() {
    int n;
    cout << "输入 n: ";
    cin >> n;
    cout << "算法1 结果: " << sumV1(n) << endl;
    cout << "算法2 结果: " << sumV2(n) << endl;
    return 0;
}
```

**关键概念**：
- **时间复杂度**：衡量算法快慢。O(1) 最快，O(log n) 很快，O(n) 一般，O(n²) 较慢，O(2ⁿ) 非常慢。
- **空间复杂度**：衡量算法用了多少额外内存。
- 竞赛中，一般要在 1 秒内完成。1 秒大约能执行 10⁸ 次简单操作。

### 15.2 如何选择算法

```
数据规模 → 时间复杂度上限
n ≤ 10       → O(n!)
n ≤ 20       → O(2ⁿ)
n ≤ 500      → O(n³)
n ≤ 5000     → O(n²)
n ≤ 10⁶      → O(n log n)
n ≤ 10⁸      → O(n)
更大         → O(log n) 或 O(1)
```

> **记住**：看到数据规模，先判断能用多复杂的算法，再决定用什么方法。

---

## 第十六章 基础算法（一）——枚举与模拟

### 16.1 枚举（暴力搜索）

**枚举**就是把所有可能的情况都试一遍，找出符合条件的答案。

```cpp
#include <iostream>
using namespace std;

// 例1：百钱买百鸡
// 公鸡5元一只，母鸡3元一只，小鸡1元3只
// 100元买100只鸡，公鸡、母鸡、小鸡各多少只？
int main() {
    // 公鸡最多买 100/5=20 只
    for (int x = 0; x <= 20; x++) {          // x 是公鸡数量
        // 母鸡最多买 (100-5*x)/3 只
        for (int y = 0; y <= 33; y++) {       // y 是母鸡数量
            int z = 100 - x - y;              // z 是小鸡数量
            // 检查：总钱数是否为100，且小鸡数量是3的倍数
            if (5 * x + 3 * y + z / 3 == 100 && z % 3 == 0) {
                cout << "公鸡:" << x << " 母鸡:" << y << " 小鸡:" << z << endl;
            }
        }
    }
    return 0;
}
```

```cpp
#include <iostream>
using namespace std;

// 例2：判断一个数是否是水仙花数
// 水仙花数：一个三位数，各位数字的立方和等于它本身
// 例如：153 = 1³ + 5³ + 3³
int main() {
    for (int n = 100; n <= 999; n++) {
        int a = n / 100;         // 百位
        int b = n / 10 % 10;     // 十位
        int c = n % 10;          // 个位
        if (a * a * a + b * b * b + c * c * c == n) {
            cout << n << " 是水仙花数" << endl;
        }
    }
    return 0;
}
```

**枚举技巧**：
- 先确定枚举范围，尽量缩小范围（优化）
- 检查条件要写全，不能遗漏

### 16.2 模拟

**模拟**就是按照题目描述的规则，一步一步执行操作。

```cpp
#include <iostream>
using namespace std;

// 例：报数问题
// n 个人围成一圈，从第1个人开始报数，报到 m 的人出列，
// 然后下一个人从1开始重新报数，求最后剩下的人的编号。

int main() {
    int n, m;
    cout << "输入 n 和 m: ";
    cin >> n >> m;

    bool out[1000] = {false};  // out[i]=true 表示第i个人已出列
    int remaining = n;          // 还剩多少人
    int count = 0;              // 当前报的数
    int pos = 0;                // 当前位置（0-based）

    while (remaining > 1) {
        if (!out[pos]) {        // 如果这个人还在
            count++;            // 报数
            if (count == m) {   // 报到 m，出列
                out[pos] = true;
                remaining--;
                count = 0;
                cout << "第 " << pos + 1 << " 号出列" << endl;
            }
        }
        pos = (pos + 1) % n;    // 移到下一个人（循环）
    }

    // 找出最后剩下的人
    for (int i = 0; i < n; i++) {
        if (!out[i]) {
            cout << "最后剩下: 第 " << i + 1 << " 号" << endl;
            break;
        }
    }
    return 0;
}
```

### 16.3 贪心算法

**贪心**：每一步都选当前看起来最优的选择，希望最终得到全局最优。

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

// 例：零钱兑换（贪心版）
// 有 1元、5元、10元、20元、50元、100元 的纸币
// 用最少的纸币凑出指定金额
int main() {
    int money[] = {100, 50, 20, 10, 5, 1};  // 从大到小排列
    int n;
    cout << "输入金额: ";
    cin >> n;

    int count = 0;
    cout << "找零方案: ";
    for (int i = 0; i < 6; i++) {
        int num = n / money[i];   // 能用几张这个面值
        if (num > 0) {
            cout << money[i] << "元×" << num << " ";
            n -= num * money[i];  // 减去已用的金额
            count += num;
        }
    }
    cout << endl << "最少需要 " << count << " 张纸币" << endl;
    return 0;
}
```

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

// 例：活动安排问题
// 有 n 个活动，每个活动有开始时间和结束时间
// 一个人同一时间只能参加一个活动，最多能参加几个？
struct Activity {
    int start, end;
};

// 按结束时间排序
bool cmp(Activity a, Activity b) {
    return a.end < b.end;
}

int main() {
    int n;
    cout << "输入活动数: ";
    cin >> n;
    Activity act[100];

    for (int i = 0; i < n; i++) {
        cin >> act[i].start >> act[i].end;
    }

    sort(act, act + n, cmp);  // 按结束时间排序

    int count = 1;              // 第一个活动一定选
    int lastEnd = act[0].end;   // 上一个选中活动的结束时间

    for (int i = 1; i < n; i++) {
        if (act[i].start >= lastEnd) {  // 这个活动的开始时间不冲突
            count++;
            lastEnd = act[i].end;
        }
    }
    cout << "最多能参加 " << count << " 个活动" << endl;
    return 0;
}
```

> **贪心要点**：贪心策略要能证明正确性，不是所有问题都能用贪心。竞赛中如果不确定，先试试看。

---

## 第十七章 基础算法（二）——二分查找与分治

### 17.1 二分查找

**二分查找**：在有序序列中，每次取中间值比较，缩小一半范围。时间复杂度 O(log n)。

```cpp
#include <iostream>
using namespace std;

// 在有序数组 a 中查找 target，返回下标（没找到返回 -1）
int binarySearch(int a[], int n, int target) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;  // 防溢出的写法
        if (a[mid] == target) {
            return mid;          // 找到了
        } else if (a[mid] < target) {
            left = mid + 1;      // target 在右半边
        } else {
            right = mid - 1;     // target 在左半边
        }
    }
    return -1;  // 没找到
}

int main() {
    int a[] = {1, 3, 5, 7, 9, 11, 13, 15};
    int n = 8;
    int target;
    cout << "输入要查找的数: ";
    cin >> target;

    int pos = binarySearch(a, n, target);
    if (pos != -1) {
        cout << target << " 在下标 " << pos << endl;
    } else {
        cout << "没找到 " << target << endl;
    }
    return 0;
}
```

### 17.2 二分答案

**二分答案**：如果答案有单调性（答案越大/越容易满足），可以对答案进行二分。

```cpp
#include <iostream>
using namespace std;

// 例：木材切割问题
// 有 n 根木材，要切出 k 段等长的木材，每段最长能切多长？
int len[100005];
int n, k;

// 检查：如果每段长 mid，能切出几段？
bool check(int mid) {
    long long total = 0;
    for (int i = 0; i < n; i++) {
        total += len[i] / mid;  // 每根木材能切出几段
    }
    return total >= k;  // 切出的段数够不够
}

int main() {
    cin >> n >> k;
    int maxLen = 0;
    for (int i = 0; i < n; i++) {
        cin >> len[i];
        if (len[i] > maxLen) maxLen = len[i];
    }

    // 二分答案：每段的长度
    int left = 1, right = maxLen, ans = 0;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (check(mid)) {
            ans = mid;       // mid 可行，试试更长的
            left = mid + 1;
        } else {
            right = mid - 1; // mid 不行，试试更短的
        }
    }
    cout << "最长每段: " << ans << endl;
    return 0;
}
```

### 17.3 分治思想

**分治**：把大问题拆成小问题，分别解决，再合并结果。

```cpp
#include <iostream>
using namespace std;

// 归并排序——分治的经典应用
int temp[100005];  // 临时数组，用于合并

// 对数组 a 的 [left, right] 区间排序
void mergeSort(int a[], int left, int right) {
    if (left >= right) return;  // 只有一个元素，已经有序

    int mid = (left + right) / 2;
    mergeSort(a, left, mid);      // 排序左半边
    mergeSort(a, mid + 1, right); // 排序右半边

    // 合并两个有序数组
    int i = left, j = mid + 1, k = left;
    while (i <= mid && j <= right) {
        if (a[i] <= a[j]) {
            temp[k++] = a[i++];
        } else {
            temp[k++] = a[j++];
        }
    }
    // 把剩余的元素复制过去
    while (i <= mid)  temp[k++] = a[i++];
    while (j <= right) temp[k++] = a[j++];

    // 把临时数组复制回原数组
    for (int p = left; p <= right; p++) {
        a[p] = temp[p];
    }
}

int main() {
    int a[] = {38, 27, 43, 3, 9, 82, 10};
    int n = 7;

    mergeSort(a, 0, n - 1);

    cout << "排序结果: ";
    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    cout << endl;
    return 0;
}
```

---

## 第十八章 排序算法

### 18.1 常见排序算法对比

```
算法        平均时间    最坏时间    空间      稳定性
冒泡排序    O(n²)      O(n²)      O(1)      稳定
选择排序    O(n²)      O(n²)      O(1)      不稳定
插入排序    O(n²)      O(n²)      O(1)      稳定
归并排序    O(nlogn)   O(nlogn)   O(n)      稳定
快速排序    O(nlogn)   O(n²)      O(logn)   不稳定
STL sort    O(nlogn)   O(nlogn)   O(logn)   不稳定
```

> **稳定性**：如果两个相等的元素排序前后相对位置不变，就是稳定的。

### 18.2 冒泡排序

```cpp
#include <iostream>
using namespace std;

// 冒泡排序：相邻元素比较，大的往后"冒泡"
void bubbleSort(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {       // 外层：需要冒泡 n-1 轮
        bool swapped = false;                 // 优化：如果某轮没有交换，说明已排好
        for (int j = 0; j < n - 1 - i; j++) { // 内层：每轮把最大的冒到最后
            if (a[j] > a[j + 1]) {
                // 交换相邻元素
                int t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
                swapped = true;
            }
        }
        if (!swapped) break;  // 没有交换，提前结束
    }
}

int main() {
    int a[] = {64, 34, 25, 12, 22, 11, 90};
    int n = 7;
    bubbleSort(a, n);
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;
    return 0;
}
```

### 18.3 选择排序

```cpp
#include <iostream>
using namespace std;

// 选择排序：每轮选出最小的，放到前面
void selectionSort(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;  // 假设当前位置最小
        for (int j = i + 1; j < n; j++) {
            if (a[j] < a[minIdx]) {
                minIdx = j;  // 找到更小的
            }
        }
        // 把最小的交换到前面
        if (minIdx != i) {
            int t = a[i];
            a[i] = a[minIdx];
            a[minIdx] = t;
        }
    }
}

int main() {
    int a[] = {64, 25, 12, 22, 11};
    int n = 5;
    selectionSort(a, n);
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;
    return 0;
}
```

### 18.4 插入排序

```cpp
#include <iostream>
using namespace std;

// 插入排序：像打牌一样，把每个元素插入到前面已排好的部分中
void insertionSort(int a[], int n) {
    for (int i = 1; i < n; i++) {
        int key = a[i];  // 要插入的元素
        int j = i - 1;
        // 把比 key 大的元素往后移
        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = key;  // 插入到正确位置
    }
}

int main() {
    int a[] = {12, 11, 13, 5, 6};
    int n = 5;
    insertionSort(a, n);
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;
    return 0;
}
```

### 18.5 快速排序

```cpp
#include <iostream>
using namespace std;

// 快速排序：选一个基准值，把比它小的放左边，比它大的放右边，递归处理
void quickSort(int a[], int left, int right) {
    if (left >= right) return;

    int pivot = a[left];  // 选第一个元素作为基准值
    int i = left, j = right;

    while (i < j) {
        // 从右往左找第一个比基准值小的
        while (i < j && a[j] >= pivot) j--;
        // 从左往右找第一个比基准值大的
        while (i < j && a[i] <= pivot) i++;
        // 交换这两个元素
        if (i < j) {
            int t = a[i]; a[i] = a[j]; a[j] = t;
        }
    }
    // 把基准值放到正确位置
    a[left] = a[i];
    a[i] = pivot;

    // 递归排序左右两部分
    quickSort(a, left, i - 1);
    quickSort(a, i + 1, right);
}

int main() {
    int a[] = {10, 7, 8, 9, 1, 5};
    int n = 6;
    quickSort(a, 0, n - 1);
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;
    return 0;
}
```

### 18.6 使用 STL sort（竞赛最常用）

```cpp
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// 自定义排序规则：按绝对值从小到大
bool cmpAbs(int a, int b) {
    return abs(a) < abs(b);
}

int main() {
    // 基本用法：对数组排序
    int a[] = {5, 2, 8, 1, 9, 3};
    sort(a, a + 6);  // 默认从小到大
    for (int i = 0; i < 6; i++) cout << a[i] << " ";
    cout << endl;

    // 从大到小排序
    sort(a, a + 6, greater<int>());
    for (int i = 0; i < 6; i++) cout << a[i] << " ";
    cout << endl;

    // 自定义排序
    int b[] = {-3, 1, -4, 1, 5, -9};
    sort(b, b + 6, cmpAbs);  // 按绝对值排序
    for (int i = 0; i < 6; i++) cout << b[i] << " ";
    cout << endl;

    // 对 vector 排序
    vector<int> v = {5, 2, 8, 1, 9};
    sort(v.begin(), v.end());
    for (int x : v) cout << x << " ";
    cout << endl;

    return 0;
}
```

```cpp
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

// 结构体排序：按总分从高到低，总分相同按学号从小到大
struct Student {
    int id;
    int score;
};

bool cmp(Student a, Student b) {
    if (a.score != b.score) return a.score > b.score;  // 分数降序
    return a.id < b.id;                                 // 学号升序
}

int main() {
    Student stu[] = {{3, 90}, {1, 95}, {2, 90}, {4, 88}};
    int n = 4;
    sort(stu, stu + n, cmp);
    for (int i = 0; i < n; i++) {
        cout << "学号:" << stu[i].id << " 分数:" << stu[i].score << endl;
    }
    return 0;
}
```

---

## 第十九章 搜索算法——DFS 与 BFS

### 19.1 深度优先搜索（DFS）

**DFS**：一条路走到黑，走不通就回退（回溯），再试另一条路。用递归实现。

```cpp
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
```

```cpp
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
```

### 19.2 广度优先搜索（BFS）

**BFS**：一层一层地搜索，先搜离起点近的，再搜远的。用队列实现，能找到最短路径。

```cpp
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
```

### 19.3 DFS vs BFS 对比

```
特性        DFS                    BFS
实现方式    递归（栈）             队列
搜索顺序    一条路走到底           一层一层扩展
空间复杂度  O(深度)                O(宽度)
适用场景    找所有方案、计数       找最短路径
```

---

## 第二十章 图论算法

### 20.1 图的表示与遍历

```cpp
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
```

### 20.2 最短路径——Dijkstra 算法

```cpp
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
```

### 20.3 最小生成树——Kruskal 算法

```cpp
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
```

---

## 第二十一章 动态规划（DP）

### 21.1 什么是动态规划？

**动态规划**：把大问题拆成小问题，记录小问题的答案，避免重复计算。

**核心要素**：
1. **状态**：用什么来描述问题
2. **状态转移方程**：大问题和小问题之间的关系
3. **初始条件**：最小的问题的答案
4. **计算顺序**：确保算大问题时小问题已经算好

### 21.2 入门：斐波那契数列

```cpp
#include <iostream>
using namespace std;

// 方法1：递归（很慢，有大量重复计算）
int fib1(int n) {
    if (n <= 2) return 1;
    return fib1(n - 1) + fib1(n - 2);
}

// 方法2：记忆化递归（用一个数组记录算过的结果）
int memo[1000] = {0};
int fib2(int n) {
    if (n <= 2) return 1;
    if (memo[n] != 0) return memo[n];  // 已经算过，直接返回
    memo[n] = fib2(n - 1) + fib2(n - 2);  // 算完记录下来
    return memo[n];
}

// 方法3：递推（动态规划的标准写法）
int fib3(int n) {
    int dp[1000];
    dp[1] = 1;  // 初始条件
    dp[2] = 1;
    for (int i = 3; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];  // 状态转移方程
    }
    return dp[n];
}

int main() {
    int n;
    cin >> n;
    cout << "递推结果: " << fib3(n) << endl;
    return 0;
}
```

### 21.3 数字三角形

```
        7
       3 8
      8 1 0
     2 7 4 4
    4 5 2 6 5

从顶部出发，每一步可以走到下方相邻的两个数，求路径上的数字之和最大是多少？
```

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[105][105], dp[105][105];

    // 读入数字三角形
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= i; j++)
            cin >> a[i][j];

    // dp[i][j] 表示从(i,j)走到底部的最大和
    // 从倒数第二行往上推
    for (int j = 1; j <= n; j++)
        dp[n][j] = a[n][j];  // 底部一行：最大和就是自己

    for (int i = n - 1; i >= 1; i--) {
        for (int j = 1; j <= i; j++) {
            // 从(i,j)出发，可以走到(i+1,j)或(i+1,j+1)
            dp[i][j] = a[i][j] + max(dp[i + 1][j], dp[i + 1][j + 1]);
        }
    }

    cout << "最大路径和: " << dp[1][1] << endl;
    return 0;
}
```

### 21.4 最长上升子序列（LIS）

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

// LIS：求一个序列中最长的严格递增子序列的长度
// 例如：1 5 3 4 6 2 → LIS 长度为 4（1 3 4 6）
int main() {
    int n;
    cin >> n;
    int a[10005], dp[10005];

    for (int i = 0; i < n; i++) {
        cin >> a[i];
        dp[i] = 1;  // 至少自己一个元素，长度为 1
    }

    // dp[i] 表示以 a[i] 结尾的最长上升子序列长度
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (a[j] < a[i]) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }

    int ans = *max_element(dp, dp + n);
    cout << "LIS 长度: " << ans << endl;
    return 0;
}
```

### 21.5 背包问题

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

// 0-1 背包问题
// 有 n 个物品，每个物品有重量 w[i] 和价值 v[i]
// 背包容量为 W，每个物品只能选一次，求最大价值
int main() {
    int n, W;
    cin >> n >> W;
    int w[1005], v[1005];

    for (int i = 1; i <= n; i++)
        cin >> w[i] >> v[i];

    // dp[j] 表示容量为 j 时的最大价值
    int dp[10005] = {0};

    for (int i = 1; i <= n; i++) {
        // 注意：从大到小遍历，保证每个物品只选一次
        for (int j = W; j >= w[i]; j--) {
            dp[j] = max(dp[j], dp[j - w[i]] + v[i]);
            // dp[j]：不选物品 i
            // dp[j-w[i]]+v[i]：选物品 i（用掉 w[i] 的容量，得到 v[i] 的价值）
        }
    }

    cout << "最大价值: " << dp[W] << endl;
    return 0;
}
```

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

// 完全背包问题
// 和 0-1 背包类似，但每个物品可以选多次
int main() {
    int n, W;
    cin >> n >> W;
    int w[1005], v[1005];

    for (int i = 1; i <= n; i++)
        cin >> w[i] >> v[i];

    int dp[10005] = {0};

    for (int i = 1; i <= n; i++) {
        // 注意：从小到大遍历，允许同一个物品选多次
        for (int j = w[i]; j <= W; j++) {
            dp[j] = max(dp[j], dp[j - w[i]] + v[i]);
        }
    }

    cout << "最大价值: " << dp[W] << endl;
    return 0;
}
```

### 21.6 简单 DP：爬楼梯与路径计数

```cpp
#include <iostream>
using namespace std;

// 爬楼梯：每次可以爬 1 或 2 级台阶，爬到第 n 级有多少种方法？
int main() {
    int n;
    cin >> n;
    int dp[10005];
    dp[1] = 1;  // 第1级：1种方法
    dp[2] = 2;  // 第2级：2种方法（1+1 或 2）

    for (int i = 3; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
        // 到达第 i 级，可以从第 i-1 级爬1步，或从第 i-2 级爬2步
    }

    cout << "方法数: " << dp[n] << endl;
    return 0;
}
```

```cpp
#include <iostream>
using namespace std;

// 方格路径计数：从(1,1)走到(m,n)，只能向右或向下走，有多少种路径？
int main() {
    int m, n;
    cin >> m >> n;
    long long dp[105][105];

    // 初始化：第一行和第一列都只有1种走法
    for (int i = 1; i <= m; i++) dp[i][1] = 1;
    for (int j = 1; j <= n; j++) dp[1][j] = 1;

    for (int i = 2; i <= m; i++) {
        for (int j = 2; j <= n; j++) {
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            // 到达(i,j)只能从上方或左方来
        }
    }

    cout << "路径数: " << dp[m][n] << endl;
    return 0;
}
```

---

## 第二十二章 数学与其他

### 22.1 质数与素数判定

```cpp
#include <iostream>
#include <cmath>
using namespace std;

// 判断一个数是否是质数
bool isPrime(int n) {
    if (n < 2) return false;       // 0和1不是质数
    if (n == 2) return true;       // 2是质数
    if (n % 2 == 0) return false;  // 偶数不是质数

    // 只需要检查到 sqrt(n)
    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

// 埃氏筛法：找出 1~n 中所有的质数
void sieve(int n) {
    bool isPrimeArr[1000005];
    for (int i = 0; i <= n; i++) isPrimeArr[i] = true;
    isPrimeArr[0] = isPrimeArr[1] = false;

    for (int i = 2; i * i <= n; i++) {
        if (isPrimeArr[i]) {
            // 把 i 的所有倍数标记为非质数
            for (int j = i * i; j <= n; j += i) {
                isPrimeArr[j] = false;
            }
        }
    }

    // 输出质数
    int count = 0;
    for (int i = 2; i <= n; i++) {
        if (isPrimeArr[i]) {
            count++;
            if (count <= 20) cout << i << " ";  // 只打印前20个
        }
    }
    cout << endl << "1~" << n << " 中共有 " << count << " 个质数" << endl;
}

int main() {
    int n;
    cin >> n;
    cout << n << (isPrime(n) ? " 是质数" : " 不是质数") << endl;

    sieve(100);
    return 0;
}
```

### 22.2 最大公约数与最小公倍数

```cpp
#include <iostream>
using namespace std;

// 辗转相除法（欧几里得算法）求最大公约数
int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
    // 原理：gcd(a,b) = gcd(b, a%b)
    // 例如：gcd(12, 8) = gcd(8, 4) = gcd(4, 0) = 4
}

// 最小公倍数 = a*b / gcd(a,b)
int lcm(int a, int b) {
    return a / gcd(a, b) * b;  // 先除再乘，防止溢出
}

int main() {
    int a, b;
    cin >> a >> b;
    cout << "最大公约数: " << gcd(a, b) << endl;
    cout << "最小公倍数: " << lcm(a, b) << endl;

    // C++17 也可以直接用 __gcd(a, b)
    cout << "__gcd: " << __gcd(a, b) << endl;
    return 0;
}
```

### 22.3 快速幂

```cpp
#include <iostream>
using namespace std;

// 快速幂：快速计算 a^b % mod
// 原理：把 b 分解成二进制，利用 a^b = a^(b/2) * a^(b/2)
long long quickPow(long long a, long long b, long long mod) {
    long long result = 1;
    a %= mod;  // 防止 a 本身就很大
    while (b > 0) {
        if (b % 2 == 1) {      // b 的最低位是 1
            result = result * a % mod;
        }
        a = a * a % mod;       // a 平方
        b /= 2;                // b 右移一位
    }
    return result;
}

int main() {
    long long a, b, mod;
    cin >> a >> b >> mod;
    cout << a << "^" << b << " mod " << mod << " = " << quickPow(a, b, mod) << endl;
    return 0;
}
```

### 22.4 进制转换

```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// 十进制转任意进制
string decToBase(int n, int base) {
    if (n == 0) return "0";
    string result = "";
    string digits = "0123456789ABCDEF";  // 支持到16进制

    while (n > 0) {
        result += digits[n % base];  // 取余数作为当前位
        n /= base;
    }
    reverse(result.begin(), result.end());  // 反转
    return result;
}

// 任意进制转十进制
int baseToDec(string s, int base) {
    int result = 0;
    for (int i = 0; i < s.length(); i++) {
        int digit;
        if (s[i] >= '0' && s[i] <= '9') digit = s[i] - '0';
        else digit = s[i] - 'A' + 10;  // A=10, B=11, ...
        result = result * base + digit;
    }
    return result;
}

int main() {
    int n;
    cout << "输入十进制数: ";
    cin >> n;
    cout << "二进制: " << decToBase(n, 2) << endl;
    cout << "八进制: " << decToBase(n, 8) << endl;
    cout << "十六进制: " << decToBase(n, 16) << endl;

    string s;
    int base;
    cout << "输入数字和进制: ";
    cin >> s >> base;
    cout << "十进制: " << baseToDec(s, base) << endl;
    return 0;
}
```

### 22.5 排列与组合

```cpp
#include <iostream>
using namespace std;

// 组合数 C(n, m) = n! / (m! * (n-m)!)
// 用递推公式：C(n, m) = C(n-1, m-1) + C(n-1, m)
// 即：杨辉三角

long long C[105][105];

void initComb() {
    // 计算 C(n, m)，存入二维数组
    for (int i = 0; i <= 100; i++) {
        C[i][0] = 1;  // C(n, 0) = 1
        for (int j = 1; j <= i; j++) {
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
        }
    }
}

int main() {
    initComb();

    int n, m;
    cin >> n >> m;
    cout << "C(" << n << "," << m << ") = " << C[n][m] << endl;

    // 打印杨辉三角（前10行）
    cout << endl << "杨辉三角:" << endl;
    for (int i = 0; i <= 10; i++) {
        for (int j = 0; j <= i; j++) {
            cout << C[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
```

### 22.6 高精度运算

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

// 高精度加法：计算两个超大整数的和
// 用字符串读入，用 vector 倒序存储（个位在前）

vector<int> addBig(string a, string b) {
    vector<int> A, B, C;

    // 倒序存入 vector
    for (int i = a.length() - 1; i >= 0; i--) A.push_back(a[i] - '0');
    for (int i = b.length() - 1; i >= 0; i--) B.push_back(b[i] - '0');

    int carry = 0;  // 进位
    for (int i = 0; i < A.size() || i < B.size() || carry; i++) {
        int sum = carry;
        if (i < A.size()) sum += A[i];
        if (i < B.size()) sum += B[i];
        C.push_back(sum % 10);   // 当前位
        carry = sum / 10;         // 进位
    }

    return C;
}

int main() {
    string a, b;
    cin >> a >> b;

    vector<int> result = addBig(a, b);

    // 倒序输出（因为存的时候是倒序的）
    for (int i = result.size() - 1; i >= 0; i--) {
        cout << result[i];
    }
    cout << endl;
    return 0;
}
```

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

// 高精度乘法：大整数 × 普通整数
vector<int> mulBig(vector<int> A, int b) {
    vector<int> C;
    int carry = 0;
    for (int i = 0; i < A.size() || carry; i++) {
        int prod = carry;
        if (i < A.size()) prod += A[i] * b;
        C.push_back(prod % 10);
        carry = prod / 10;
    }
    // 去除前导零
    while (C.size() > 1 && C.back() == 0) C.pop_back();
    return C;
}

int main() {
    string a;
    int b;
    cin >> a >> b;

    vector<int> A;
    for (int i = a.length() - 1; i >= 0; i--) A.push_back(a[i] - '0');

    vector<int> result = mulBig(A, b);

    for (int i = result.size() - 1; i >= 0; i--) {
        cout << result[i];
    }
    cout << endl;
    return 0;
}
```

### 22.7 数学常用技巧总结

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    // 1. 判断奇偶
    int x = 7;
    cout << x << (x % 2 == 0 ? " 偶数" : " 奇数") << endl;

    // 2. 数字拆分
    int num = 12345;
    cout << "个位:" << num % 10 << endl;           // 5
    cout << "十位:" << num / 10 % 10 << endl;      // 4
    cout << "百位:" << num / 100 % 10 << endl;     // 3

    // 3. 交换两个变量（不用临时变量）
    int a = 3, b = 5;
    a = a ^ b;  // 异或交换法
    b = a ^ b;
    a = a ^ b;
    cout << "a=" << a << " b=" << b << endl;  // a=5 b=3

    // 4. 绝对值
    cout << "abs(-7) = " << abs(-7) << endl;

    // 5. 幂运算
    cout << "2^10 = " << pow(2, 10) << endl;  // 1024

    // 6. 平方根
    cout << "sqrt(144) = " << sqrt(144) << endl;  // 12

    // 7. 取整
    cout << "floor(3.7) = " << floor(3.7) << endl;   // 3（向下取整）
    cout << "ceil(3.2) = " << ceil(3.2) << endl;     // 4（向上取整）

    // 8. 判断完全平方数
    int n = 144;
    int sq = (int)sqrt(n);
    cout << n << (sq * sq == n ? " 是" : " 不是") << "完全平方数" << endl;

    return 0;
}
```

---

## Day 3 练习题

### 练习1：完美数
**题目**：输入正整数 n，输出 1~n 之间所有的完美数。（完美数 = 所有真因子之和，如 6=1+2+3）
```
输入示例：10000
输出示例：6 28 496 8128
```

### 练习2：砝码称重（枚举）
**题目**：有 1g、2g、3g、5g、10g、20g 的砝码各一个，能称出多少种不同的重量？
```
输出示例：能称出 XX 种不同的重量
```

### 练习3：鸡蛋掉落（模拟）
**题目**：一栋楼有 n 层，你有两个鸡蛋。找出在最坏情况下最少扔几次能确定鸡蛋摔碎的楼层。（提示：模拟枚举）

### 练习4：区间合并（贪心）
**题目**：输入 n 个区间 [l, r]，合并所有重叠的区间，输出合并后的区间。
```
输入示例：
5
1 3
2 6
8 10
15 18
5 7
输出示例：
[1,7] [8,10] [15,18]
```

### 练习5：二分查找变种
**题目**：在一个有序数组中，找第一个大于等于 target 的元素位置（lower_bound）。
```
输入示例：
数组: 1 3 3 5 7 9
target: 4
输出示例：下标 3（值为5）
```

### 练习6：排序去重
**题目**：输入 n 个整数，排序后去除重复元素并输出。
```
输入示例：8 3 5 3 8 1 5 2 8
输出示例：1 2 3 5 8
```

### 练习7：迷宫最短路径（BFS）
**题目**：给定一个 n×n 的迷宫（0=通路，1=墙），求从左上角到右下角的最短步数。
```
输入示例：
5
0 1 0 0 0
0 1 0 1 0
0 0 0 0 0
0 1 1 1 0
0 0 0 1 0
输出示例：8
```

### 练习8：全排列问题（DFS）
**题目**：输入 n，输出 1~n 的所有排列，按字典序输出。
```
输入示例：3
输出示例：
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
```

### 练习9：N皇后问题（DFS）
**题目**：在 n×n 的棋盘上放 n 个皇后，使它们互不攻击（不在同一行、列、对角线），输出方案数。
```
输入示例：8
输出示例：92
```

### 练习10：0-1背包
**题目**：有 n 个物品，背包容量为 W，求最大价值。
```
输入示例：
4 5          （4个物品，容量5）
2 3          （重量2，价值3）
1 2
3 4
2 2
输出示例：7   （选第2和第3个物品）
```

### 练习11：最长上升子序列
**题目**：给定一个序列，求最长上升子序列的长度。
```
输入示例：7 1 5 3 4 6 2
输出示例：4  （1 3 4 6）
```

### 练习12：爬楼梯变种
**题目**：每次可以爬 1、2 或 3 级台阶，爬到第 n 级有多少种方法？输出对 10007 取模的结果。
```
输入示例：10
输出示例：274
```

### 练习13：质数筛法
**题目**：输入 n，输出 1~n 中所有质数的个数。
```
输入示例：100
输出示例：25
```

### 练习14：高精度阶乘
**题目**：输入 n（n≤100），输出 n! 的精确值。
```
输入示例：20
输出示例：2432902008176640000
```

### 练习15：Dijkstra最短路
**题目**：输入一个带权无向图（n 个节点 m 条边），求节点 1 到所有节点的最短距离。
```
输入示例：
5 6
1 2 2
1 3 4
2 3 1
2 4 7
3 5 3
4 5 1
输出示例：
到1: 0
到2: 2
到3: 3
到4: 7
到5: 6
```

### 练习16：组合计数
**题目**：从 n 个不同元素中选 m 个，有多少种选法？结果可能很大，输出对 10⁹+7 取模的值。
```
输入示例：10 3
输出示例：120
```

---

> **Day 3 学习建议**：
> 1. **DFS/BFS 是重点**，一定要多画图理解搜索过程，这是竞赛必考内容
> 2. **动态规划**刚开始会觉得难，建议先理解"爬楼梯"和"数字三角形"，再去做背包问题
> 3. **排序算法**要能手写冒泡和快排，但竞赛中直接用 `sort()` 就行
> 4. **二分查找**要非常熟练，竞赛中经常和贪心、DP 结合使用
> 5. **数学部分**要掌握质数判定、GCD、快速幂，这些是基础工具
> 6. **高精度**要理解原理，竞赛中 `long long` 范围不够时才需要
> 7. 每道练习题先自己想 15-20 分钟，实在想不出来再看提示
> 8. 预计学习时间：10-12 小时（含练习）
