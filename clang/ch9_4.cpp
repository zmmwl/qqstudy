#include <iostream>
using namespace std;

// 递归：函数调用自身
// 递归三要素：1. 递归终止条件  2. 递推关系  3. 返回

// 示例1：阶乘 n! = n × (n-1)!
// 终止条件：0! = 1
int factorial(int n) {
    if (n <= 1) return 1;        // 终止条件（基准情况）
    return n * factorial(n - 1);  // 递推：n! = n × (n-1)!
}
// 执行过程：factorial(5)
// = 5 * factorial(4)
// = 5 * 4 * factorial(3)
// = 5 * 4 * 3 * factorial(2)
// = 5 * 4 * 3 * 2 * factorial(1)
// = 5 * 4 * 3 * 2 * 1
// = 120

// 示例2：斐波那契数列 fib(n) = fib(n-1) + fib(n-2)
int fib(int n) {
    if (n <= 2) return 1;  // fib(1) = fib(2) = 1
    return fib(n - 1) + fib(n - 2);
}

// 示例3：递归求和 1+2+...+n
int sum(int n) {
    if (n == 1) return 1;
    return n + sum(n - 1);
}

// 示例4：递归求幂 x^n
int power(int x, int n) {
    if (n == 0) return 1;
    return x * power(x, n - 1);
}

// 示例5：递归输出数字的每一位（从高位到低位）
void printDigits(int n) {
    if (n >= 10) {
        printDigits(n / 10);  // 先输出高位
    }
    cout << n % 10 << " ";    // 再输出最低位
}

// 示例6：汉诺塔问题
// 将 n 个盘子从 A 柱移到 C 柱，借助 B 柱
void hanoi(int n, char from, char helper, char to) {
    if (n == 1) {
        cout << from << " -> " << to << endl;
        return;
    }
    hanoi(n - 1, from, to, helper);   // 把上面 n-1 个从 from 移到 helper
    cout << from << " -> " << to << endl;  // 把最下面的盘子从 from 移到 to
    hanoi(n - 1, helper, from, to);   // 把 n-1 个从 helper 移到 to
}

int main() {
    cout << "5! = " << factorial(5) << endl;       // 120
    cout << "fib(6) = " << fib(6) << endl;         // 8
    cout << "sum(100) = " << sum(100) << endl;     // 5050
    cout << "2^10 = " << power(2, 10) << endl;     // 1024

    cout << "12345 的各位: ";
    printDigits(12345);   // 1 2 3 4 5
    cout << endl;

    cout << "汉诺塔 3 层:" << endl;
    hanoi(3, 'A', 'B', 'C');

    return 0;
}
