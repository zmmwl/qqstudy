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
