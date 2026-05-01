# Day 2: 字符串、函数、指针、文件、STL 与数据结构

> **学习目标**：掌握字符串处理、函数定义与递归、结构体、指针、文件操作、STL 容器，以及基本数据结构（栈、队列、链表、树、图）。

---

## 第八章 字符串的处理

### 8.1 字符数组与相关函数

<!-- 对应代码文件：ch8_1.cpp -->
```cpp
#include <iostream>
#include <cstring>   // 字符数组处理函数的头文件
using namespace std;

int main() {
    // 字符数组：用 char 数组存储字符串
    char str1[100] = "Hello";     // 自动在末尾加 '\0'（空字符，表示字符串结束）
    char str2[100] = "World";

    // 输出字符数组
    cout << str1 << endl;  // Hello
    // cout 会输出到 '\0' 为止

    // 读入字符数组
    // cin >> str1;   // 只能读入一个词（遇到空格就停）
    // cin.getline(str1, 100);  // 可以读入一整行（包括空格）

    // strlen：求字符串长度（不含 '\0'）
    cout << "长度: " << strlen(str1) << endl;  // 5

    // strcpy：字符串复制
    char str3[100];
    strcpy(str3, str1);  // 把 str1 复制到 str3
    cout << "复制后: " << str3 << endl;  // Hello

    // strcat：字符串连接
    strcat(str1, " ");      // 在 str1 后面追加一个空格
    strcat(str1, str2);     // 再追加 str2
    cout << "连接后: " << str1 << endl;  // Hello World

    // strcmp：字符串比较
    // 返回 0 表示相等，<0 表示第一个小，>0 表示第一个大
    char s1[] = "abc";
    char s2[] = "abd";
    cout << strcmp(s1, s2) << endl;  // 负数（abc < abd）
    cout << strcmp(s1, "abc") << endl;  // 0（相等）

    // 逐字符访问
    char s[] = "Hello";
    for (int i = 0; s[i] != '\0'; i++) {
        cout << s[i] << " ";
    }
    cout << endl;  // H e l l o

    // 把字符串中的小写字母转成大写
    char lower[] = "hello world";
    for (int i = 0; lower[i] != '\0'; i++) {
        if (lower[i] >= 'a' && lower[i] <= 'z') {
            lower[i] -= 32;  // 小写转大写
        }
    }
    cout << lower << endl;  // HELLO WORLD

    return 0;
}
```

### 8.2 string 类与相关函数

<!-- 对应代码文件：ch8_2.cpp -->
```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    // string 类：比字符数组更方便、更安全的字符串类型

    // 定义和初始化
    string s1 = "Hello";
    string s2 = "World";
    string s3(5, 'a');  // 5 个 'a'，即 "aaaaa"
    cout << s3 << endl;

    // 输入
    // cin >> s1;           // 读入一个词
    // getline(cin, s1);    // 读入一整行（推荐）

    // 常用操作
    // 求长度
    cout << "长度: " << s1.length() << endl;   // 5
    cout << "长度: " << s1.size() << endl;     // 5（和 length 一样）

    // 字符串连接
    string s4 = s1 + " " + s2;  // 用 + 连接
    cout << s4 << endl;  // Hello World
    s1 += "!";  // 追加
    cout << s1 << endl;  // Hello!

    // 字符串比较（直接用 ==, <, > 等）
    if (s1 == "Hello!") cout << "相等" << endl;
    if ("abc" < "abd") cout << "abc < abd" << endl;

    // 访问单个字符（和数组一样，下标从 0 开始）
    cout << s1[0] << endl;   // H
    cout << s1.at(0) << endl;  // H（at 会检查越界，更安全）

    // 子串：substr(起始位置, 长度)
    string s = "Hello World";
    cout << s.substr(0, 5) << endl;   // Hello（从位置 0 取 5 个字符）
    cout << s.substr(6) << endl;      // World（从位置 6 取到末尾）

    // 查找：find（找到返回位置，找不到返回 string::npos）
    size_t pos = s.find("World");
    if (pos != string::npos) {
        cout << "找到 World，位置: " << pos << endl;  // 6
    }
    cout << (int)s.find("xyz") << endl;  // -1（找不到）

    // 插入：insert(位置, 字符串)
    string s5 = "Hello";
    s5.insert(2, "XX");  // 在位置 2 插入 "XX"
    cout << s5 << endl;  // HeXXllo

    // 删除：erase(位置, 长度)
    s5.erase(2, 2);      // 从位置 2 删 2 个字符
    cout << s5 << endl;  // Hello

    // 替换：replace(位置, 长度, 新字符串)
    string s6 = "Hello World";
    s6.replace(6, 5, "C++");  // 从位置 6 替换 5 个字符为 "C++"
    cout << s6 << endl;  // Hello C++

    // 遍历字符串
    for (int i = 0; i < s.size(); i++) {
        cout << s[i] << " ";
    }
    cout << endl;

    // C++11 范围 for 循环（更简洁）
    for (char c : s) {
        cout << c << " ";
    }
    cout << endl;

    // string 转 char 数组
    const char* p = s.c_str();

    // 数字与字符串互转
    int num = 123;
    string str = to_string(num);     // 数字转字符串
    int num2 = stoi(str);            // 字符串转整数
    double d = stod("3.14");         // 字符串转 double

    return 0;
}
```

---

## 第九章 函数与递归

### 9.1 函数定义与调用、形参与实参

<!-- 对应代码文件：ch9_1.cpp -->
```cpp
#include <iostream>
using namespace std;

// 函数定义的格式：
// 返回类型 函数名(参数列表) {
//     函数体
//     return 返回值;
// }

// 定义一个求两个数最大值的函数
int getMax(int a, int b) {  // a, b 是形参（形式参数）
    return (a > b) ? a : b;
}

// 定义一个判断素数的函数
bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; i++) {  // 只需检查到 sqrt(n)
        if (n % i == 0) return false;
    }
    return true;
}

// 没有返回值的函数用 void
void printStars(int n) {
    for (int i = 0; i < n; i++) {
        cout << "*";
    }
    cout << endl;
}

int main() {
    // 调用函数时传入的值是实参（实际参数）
    int result = getMax(10, 20);  // 10 和 20 是实参
    cout << "最大值: " << result << endl;  // 20

    // 函数可以多次调用
    cout << "15 是否素数: " << isPrime(15) << endl;  // 0 (false)
    cout << "17 是否素数: " << isPrime(17) << endl;  // 1 (true)

    printStars(5);  // *****
    printStars(3);  // ***

    return 0;
}
```

### 9.2 传值参数与传引用参数

<!-- 对应代码文件：ch9_2.cpp -->
```cpp
#include <iostream>
using namespace std;

// 传值参数：函数内部修改不影响外面的变量（复制了一份）
void addTen_value(int x) {
    x += 10;
    cout << "函数内 x = " << x << endl;
}

// 传引用参数：用 & 符号，函数内部修改会影响外面的变量（直接操作原变量）
void addTen_ref(int& x) {
    x += 10;
    cout << "函数内 x = " << x << endl;
}

// 传引用的经典用法：让函数返回多个值
// 例如同时求最大值和最小值
void findMinMax(int arr[], int n, int& minVal, int& maxVal) {
    minVal = maxVal = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] < minVal) minVal = arr[i];
        if (arr[i] > maxVal) maxVal = arr[i];
    }
}

// 交换两个变量（必须用引用！）
void swapValues(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

int main() {
    int a = 5;

    // 传值调用
    addTen_value(a);
    cout << "传值后 a = " << a << endl;  // a 还是 5（没变！）

    // 传引用调用
    addTen_ref(a);
    cout << "传引用后 a = " << a << endl;  // a 变成 15

    // 用传引用返回多个值
    int arr[] = {3, 7, 1, 9, 4};
    int mn, mx;
    findMinMax(arr, 5, mn, mx);
    cout << "最小值: " << mn << ", 最大值: " << mx << endl;  // 1, 9

    // 交换
    int x = 10, y = 20;
    swapValues(x, y);
    cout << "x=" << x << ", y=" << y << endl;  // x=20, y=10

    return 0;
}
```

### 9.3 变量的作用范围

<!-- 对应代码文件：ch9_3.cpp -->
```cpp
#include <iostream>
using namespace std;

// 全局变量：定义在所有函数外面，所有函数都能访问
int globalVar = 100;

void func() {
    cout << "全局变量: " << globalVar << endl;  // 可以访问

    // 局部变量：定义在函数内部，只在函数内有效
    int localVar = 200;
    cout << "局部变量: " << localVar << endl;
}

void anotherFunc() {
    // cout << localVar;  // 错误！localVar 是 func 的局部变量
    cout << globalVar << endl;  // 可以访问全局变量

    // 如果局部变量和全局变量同名，局部变量优先
    int globalVar = 999;  // 这里的 globalVar 是局部变量
    cout << "局部: " << globalVar << endl;  // 999
    cout << "全局: " << ::globalVar << endl;  // 100（用 :: 访问全局变量）
}

// 静态局部变量：函数结束后不销毁，下次调用保持上次的值
void counter() {
    static int count = 0;  // 只在第一次调用时初始化
    count++;
    cout << "调用次数: " << count << endl;
}

int main() {
    func();
    anotherFunc();

    counter();  // 调用次数: 1
    counter();  // 调用次数: 2
    counter();  // 调用次数: 3

    // 块作用域
    {
        int x = 10;
        cout << x << endl;  // 10
    }
    // cout << x;  // 错误！x 已经不存在了

    return 0;
}
```

### 9.4 递归函数

<!-- 对应代码文件：ch9_4.cpp -->
```cpp
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
```

---

## 第十章 结构体与联合体

### 10.1 结构体

<!-- 对应代码文件：ch10_1.cpp -->
```cpp
#include <iostream>
#include <string>
using namespace std;

// 结构体：把多个不同类型的数据组合在一起
// 就像一张"信息卡片"

// 定义结构体类型
struct Student {
    string name;    // 姓名
    int age;        // 年龄
    double score;   // 分数
};  // 注意末尾的分号！

// 结构体可以作为函数参数
void printStudent(Student s) {
    cout << s.name << " " << s.age << "岁 成绩:" << s.score << endl;
}

// 传引用更高效（避免复制）
void addBonus(Student& s, double bonus) {
    s.score += bonus;
}

// 结构体数组
int main() {
    // 创建结构体变量
    Student s1;
    s1.name = "Xiao Ming";
    s1.age = 12;
    s1.score = 95.5;

    // 也可以在定义时初始化
    Student s2 = {"Xiao Hong", 11, 98.0};

    // 访问成员用 点运算符(.)
    cout << s1.name << " 成绩: " << s1.score << endl;

    printStudent(s1);
    addBonus(s1, 5.0);  // 加 5 分奖励
    printStudent(s1);

    // 结构体数组
    Student cls[3] = {
        {"Alice", 12, 90},
        {"Bob", 13, 85},
        {"Carol", 11, 95}
    };

    // 按成绩排序
    for (int i = 0; i < 3; i++) {
        for (int j = i + 1; j < 3; j++) {
            if (cls[j].score > cls[i].score) {
                Student temp = cls[i];
                cls[i] = cls[j];
                cls[j] = temp;
            }
        }
    }

    for (int i = 0; i < 3; i++) {
        printStudent(cls[i]);
    }

    return 0;
}
```

### 10.2 联合体

<!-- 对应代码文件：ch10_2.cpp -->
```cpp
#include <iostream>
using namespace std;

// 联合体：所有成员共享同一块内存
// 同一时刻只能使用其中一个成员
// 大小等于最大成员的大小

union Data {
    int i;
    double d;
    char c;
};

int main() {
    Data data;

    data.i = 42;
    cout << "int: " << data.i << endl;   // 42
    // 此时 d 和 c 的值是不确定的

    data.d = 3.14;
    cout << "double: " << data.d << endl;  // 3.14
    // 此时 i 的值已经被覆盖了
    cout << "int now: " << data.i << endl;  // 一个奇怪的值

    // 联合体的大小
    cout << "Data 大小: " << sizeof(Data) << endl;  // 8（double 的大小）

    // 实际用途举例：节省内存（较少使用，了解即可）

    return 0;
}
```

---

## 第十一章 指针类型

### 11.1 指针基础

<!-- 对应代码文件：ch11_1.cpp -->
```cpp
#include <iostream>
using namespace std;

int main() {
    // 指针：存储变量地址的变量
    // 可以理解为"门牌号"——它不存数据本身，而是存数据在哪里

    int a = 10;

    // &a 取变量 a 的地址
    cout << "a 的值: " << a << endl;
    cout << "a 的地址: " << &a << endl;

    // 定义指针变量：类型* 指针名
    int* p = &a;   // p 指向 a，p 存的是 a 的地址
    cout << "p 的值(a的地址): " << p << endl;
    cout << "p 指向的值(a的值): " << *p << endl;  // 10
    // *p 叫做"解引用"，获取指针指向的值

    // 通过指针修改值
    *p = 20;       // 相当于 a = 20
    cout << "修改后 a = " << a << endl;  // 20

    // 指针的地址
    cout << "p 自己的地址: " << &p << endl;

    // 空指针
    int* null_p = nullptr;  // 或 NULL（C++11 推荐用 nullptr）
    // *null_p = 5;  // 危险！不能解引用空指针

    return 0;
}
```

### 11.2 基于指针的数组访问

<!-- 对应代码文件：ch11_2.cpp -->
```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[5] = {10, 20, 30, 40, 50};

    // 数组名就是首元素的地址
    int* p = arr;  // 等价于 int* p = &arr[0];

    cout << "arr = " << arr << endl;
    cout << "&arr[0] = " << &arr[0] << endl;
    cout << "*arr = " << *arr << endl;        // 10（第一个元素）

    // 指针算术
    cout << "*(arr+1) = " << *(arr + 1) << endl;  // 20（第二个元素）
    cout << "*(arr+2) = " << *(arr + 2) << endl;  // 30（第三个元素）

    // arr[i] 等价于 *(arr + i)

    // 用指针遍历数组
    for (int* q = arr; q < arr + 5; q++) {
        cout << *q << " ";
    }
    cout << endl;  // 10 20 30 40 50

    // 用指针修改数组
    for (int* q = arr; q < arr + 5; q++) {
        *q *= 2;  // 每个元素乘以 2
    }
    // 现在 arr = {20, 40, 60, 80, 100}

    return 0;
}
```

### 11.3 字符指针

<!-- 对应代码文件：ch11_3.cpp -->
```cpp
#include <iostream>
using namespace std;

int main() {
    // 字符指针：指向字符的指针，常用于字符串操作
    char str[] = "Hello";
    char* p = str;  // p 指向字符串的第一个字符

    cout << p << endl;     // Hello（cout 对 char* 特殊处理，输出整个字符串）
    cout << *p << endl;    // H（第一个字符）

    // 用指针遍历字符串
    while (*p != '\0') {
        cout << *p << " ";
        p++;
    }
    cout << endl;  // H e l l o

    // 字符串常量指针
    const char* s = "World";  // 指向字符串常量
    cout << s << endl;  // World
    // s[0] = 'w';  // 错误！字符串常量不能修改

    return 0;
}
```

### 11.4 指向结构体的指针

<!-- 对应代码文件：ch11_4.cpp -->
```cpp
#include <iostream>
#include <string>
using namespace std;

struct Student {
    string name;
    int age;
    double score;
};

int main() {
    Student s = {"Xiao Ming", 12, 95.5};

    // 指向结构体的指针
    Student* p = &s;

    // 通过指针访问成员，用 -> 运算符（而不是 .）
    cout << p->name << endl;    // Xiao Ming
    cout << p->age << endl;     // 12
    cout << p->score << endl;   // 95.5

    // p->name 等价于 (*p).name
    cout << (*p).name << endl;  // Xiao Ming

    // 通过指针修改
    p->age = 13;
    cout << s.age << endl;  // 13

    return 0;
}
```

---

## 第十二章 文件及基本读写

### 12.1 文件基本操作

<!-- 对应代码文件：ch12_1.cpp -->
```cpp
#include <iostream>
#include <fstream>   // 文件操作头文件
#include <cstdio>
using namespace std;

int main() {
    // ===== C++ 风格文件操作 =====

    // 写文件
    ofstream fout("output.txt");  // 打开文件用于写入
    // 如果文件不存在会自动创建
    fout << "Hello, File!" << endl;
    fout << 42 << endl;
    fout << 3.14 << endl;
    fout.close();  // 关闭文件（重要！）

    // 读文件
    ifstream fin("input.txt");   // 打开文件用于读取
    // 如果文件不存在，fin 会处于失败状态
    if (!fin.is_open()) {
        cout << "文件打开失败" << endl;
        return 1;
    }

    string line;
    while (getline(fin, line)) {  // 逐行读取
        cout << line << endl;
    }
    fin.close();

    // 读入数字
    ifstream fin2("data.txt");
    int a, b;
    fin2 >> a >> b;  // 和 cin 用法一样，只是来源从键盘变成了文件
    cout << a + b << endl;
    fin2.close();

    // 追加写入（在文件末尾追加，不覆盖原有内容）
    ofstream fout2("output.txt", ios::app);  // ios::app 表示追加模式
    fout2 << "追加的内容" << endl;
    fout2.close();

    // ===== C 风格文件操作（竞赛中更常用的是重定向）=====

    // 文件重定向（最简单的文件读写方式）
    // 方法：在 main 函数开头加上这两行，然后正常用 cin/cout
    // freopen("input.txt", "r", stdin);   // 从文件读入
    // freopen("output.txt", "w", stdout); // 输出到文件
    // 之后 cin >> x 就从 input.txt 读取，cout << x 就输出到 output.txt

    return 0;
}
```

### 12.2 文本文件与二进制文件

<!-- 对应代码文件：ch12_2.cpp -->
```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    // 文本文件：用记事本打开能看懂的文件（存的是字符）
    // 二进制文件：用记事本打开是乱码（存的是原始字节）

    // 文本文件读写（默认方式）
    ofstream textOut("data.txt");
    textOut << 12345 << " " << 3.14 << endl;  // 存为文本 "12345 3.14"
    textOut.close();

    // 二进制文件读写
    int arr[] = {10, 20, 30, 40, 50};

    // 写二进制文件
    ofstream binOut("data.bin", ios::binary);
    binOut.write(reinterpret_cast<char*>(arr), sizeof(arr));
    binOut.close();

    // 读二进制文件
    int arr2[5];
    ifstream binIn("data.bin", ios::binary);
    binIn.read(reinterpret_cast<char*>(arr2), sizeof(arr2));
    binIn.close();

    for (int i = 0; i < 5; i++) {
        cout << arr2[i] << " ";  // 10 20 30 40 50
    }
    cout << endl;

    return 0;
}
```

---

## 第十三章 STL 模板

### 13.1 算法模板库中的函数

<!-- 对应代码文件：ch13_1.cpp -->
```cpp
#include <iostream>
#include <algorithm>  // 算法库
using namespace std;

int main() {
    // min：求最小值
    cout << min(3, 5) << endl;  // 3
    cout << min({3, 1, 4, 1, 5}) << endl;  // 1（多个值取最小）

    // max：求最大值
    cout << max(3, 5) << endl;  // 5

    // swap：交换两个变量的值
    int a = 10, b = 20;
    swap(a, b);
    cout << "a=" << a << ", b=" << b << endl;  // a=20, b=10

    // sort：排序（非常重要！）
    int arr[] = {5, 2, 8, 1, 9, 3};
    int n = 6;

    // 默认从小到大排序
    sort(arr, arr + n);
    for (int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;  // 1 2 3 5 8 9

    // 从大到小排序
    sort(arr, arr + n, greater<int>());
    for (int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;  // 9 8 5 3 2 1

    // 自定义排序规则
    // 例如：按绝对值从小到大排序
    int arr2[] = {-5, 3, -1, 4, -2};
    sort(arr2, arr2 + 5, [](int a, int b) {
        return abs(a) < abs(b);  // 绝对值小的排前面
    });
    for (int i = 0; i < 5; i++) cout << arr2[i] << " ";
    cout << endl;  // -1 -2 3 4 -5

    // sort 对 vector 使用
    // sort(v.begin(), v.end());

    // 其他有用的算法函数：
    int arr3[] = {1, 3, 5, 7, 9};

    // binary_search：二分查找（数组必须有序）
    cout << binary_search(arr3, arr3 + 5, 5) << endl;  // 1（存在）

    // lower_bound：找到第一个 >= 某值的位置
    int* pos = lower_bound(arr3, arr3 + 5, 4);
    cout << *pos << endl;  // 5（第一个 >= 4 的元素）

    // upper_bound：找到第一个 > 某值的位置
    int* pos2 = upper_bound(arr3, arr3 + 5, 5);
    cout << *pos2 << endl;  // 7（第一个 > 5 的元素）

    // reverse：反转
    int arr4[] = {1, 2, 3, 4, 5};
    reverse(arr4, arr4 + 5);
    for (int i = 0; i < 5; i++) cout << arr4[i] << " ";
    cout << endl;  // 5 4 3 2 1

    // fill：填充
    int arr5[10];
    fill(arr5, arr5 + 10, 0);  // 全部填 0

    // unique：去重（必须先排序）
    int arr6[] = {1, 1, 2, 2, 3, 3, 3, 4};
    sort(arr6, arr6 + 8);
    int newLen = unique(arr6, arr6 + 8) - arr6;
    // newLen = 4, arr6 = {1, 2, 3, 4, ...}

    // nth_element：找到第 n 大的元素
    int arr7[] = {5, 2, 8, 1, 9, 3};
    nth_element(arr7, arr7 + 2, arr7 + 6);  // 第3小的元素放到位置2
    cout << "第3小: " << arr7[2] << endl;  // 3

    return 0;
}
```

### 13.2 STL 容器

<!-- 对应代码文件：ch13_2.cpp -->
```cpp
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <list>
using namespace std;

int main() {
    // ===== vector（动态数组）=====
    // 最常用的容器，可以自动扩展大小

    vector<int> v;         // 定义空 vector
    vector<int> v2(10);    // 定义 10 个元素的 vector，默认值为 0
    vector<int> v3(10, 5); // 定义 10 个元素的 vector，初始值都为 5

    v.push_back(10);   // 在末尾添加元素
    v.push_back(20);
    v.push_back(30);
    // v = {10, 20, 30}

    cout << "大小: " << v.size() << endl;   // 3
    cout << "v[0] = " << v[0] << endl;     // 10
    cout << "v[1] = " << v.at(1) << endl;  // 20

    v.pop_back();      // 删除末尾元素
    // v = {10, 20}

    // 遍历 vector
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }
    cout << endl;

    // 范围 for 循环
    for (int x : v) {
        cout << x << " ";
    }
    cout << endl;

    // 清空
    v.clear();
    cout << "清空后大小: " << v.size() << endl;  // 0

    // 排序 vector
    vector<int> nums = {5, 2, 8, 1, 9};
    sort(nums.begin(), nums.end());
    for (int x : nums) cout << x << " ";
    cout << endl;  // 1 2 5 8 9

    // ===== stack（栈）=====
    // 后进先出（LIFO）：最后放进去的最先出来
    // 就像叠盘子：最后放的在最上面，取也从最上面取

    stack<int> stk;
    stk.push(10);    // 入栈：10
    stk.push(20);    // 入栈：10, 20（20 在栈顶）
    stk.push(30);    // 入栈：10, 20, 30（30 在栈顶）

    cout << "栈顶: " << stk.top() << endl;  // 30
    stk.pop();        // 出栈：移除栈顶
    cout << "新栈顶: " << stk.top() << endl;  // 20
    cout << "栈大小: " << stk.size() << endl;  // 2

    // 遍历栈（需要边弹边看）
    while (!stk.empty()) {
        cout << stk.top() << " ";
        stk.pop();
    }
    cout << endl;  // 20 10

    // ===== queue（队列）=====
    // 先进先出（FIFO）：先放进去的先出来
    // 就像排队：先到的人先服务

    queue<int> q;
    q.push(10);     // 入队：10
    q.push(20);     // 入队：10, 20
    q.push(30);     // 入队：10, 20, 30

    cout << "队首: " << q.front() << endl;  // 10
    cout << "队尾: " << q.back() << endl;   // 30
    q.pop();          // 出队：移除队首
    cout << "新队首: " << q.front() << endl;  // 20

    // 优先队列（堆）：每次取最大（或最小）的元素
    priority_queue<int> pq;  // 默认大根堆（最大元素在顶部）
    pq.push(30);
    pq.push(10);
    pq.push(20);
    cout << "最大: " << pq.top() << endl;  // 30
    pq.pop();
    cout << "次大: " << pq.top() << endl;  // 20

    // 小根堆（最小元素在顶部）
    priority_queue<int, vector<int>, greater<int>> minPQ;

    // ===== list（双向链表）=====
    list<int> lst;
    lst.push_back(10);    // 尾部添加
    lst.push_front(20);   // 头部添加
    lst.push_back(30);
    // lst = {20, 10, 30}

    for (int x : lst) {
        cout << x << " ";
    }
    cout << endl;

    lst.sort();  // 链表排序
    lst.reverse();  // 链表反转

    return 0;
}
```

---

## 第十四章 数据结构

### 14.1 线性结构

#### 栈（Stack）

<!-- 对应代码文件：ch14_1.cpp -->
```cpp
#include <iostream>
#include <stack>
using namespace std;

// 栈：后进先出（LIFO - Last In First Out）
// 只能在栈顶操作（压入 push、弹出 pop、查看栈顶 top）

// 用数组手动实现栈
const int MAXN = 1000;
int st[MAXN];
int top = 0;  // 栈顶指针（指向下一个要放的位置）

void push(int x) { st[top++] = x; }
void pop() { top--; }
int getTop() { return st[top - 1]; }
bool isEmpty() { return top == 0; }

int main() {
    // STL stack 用法
    stack<int> s;

    // 应用1：括号匹配
    string expr = "((()))()";  // 检查括号是否匹配
    bool valid = true;
    stack<char> bracketStack;
    for (char c : expr) {
        if (c == '(') {
            bracketStack.push(c);
        } else if (c == ')') {
            if (bracketStack.empty()) {
                valid = false;
                break;
            }
            bracketStack.pop();
        }
    }
    if (!bracketStack.empty()) valid = false;
    cout << "括号" << (valid ? "匹配" : "不匹配") << endl;

    // 应用2：表达式求值（后缀表达式/逆波兰表达式）
    // 例如："3 4 + 5 *" = (3+4)*5 = 35
    stack<int> calc;
    string tokens[] = {"3", "4", "+", "5", "*"};
    for (int i = 0; i < 5; i++) {
        if (tokens[i] == "+" || tokens[i] == "-" ||
            tokens[i] == "*" || tokens[i] == "/") {
            int b = calc.top(); calc.pop();
            int a = calc.top(); calc.pop();
            if (tokens[i] == "+") calc.push(a + b);
            if (tokens[i] == "-") calc.push(a - b);
            if (tokens[i] == "*") calc.push(a * b);
            if (tokens[i] == "/") calc.push(a / b);
        } else {
            calc.push(stoi(tokens[i]));
        }
    }
    cout << "结果: " << calc.top() << endl;  // 35

    // 应用3：十进制转二进制
    int num = 13;
    stack<int> binary;
    while (num > 0) {
        binary.push(num % 2);
        num /= 2;
    }
    cout << "13 的二进制: ";
    while (!binary.empty()) {
        cout << binary.top();
        binary.pop();
    }
    cout << endl;  // 1101

    return 0;
}
```

#### 队列（Queue）

<!-- 对应代码文件：ch14_1_2.cpp -->
```cpp
#include <iostream>
#include <queue>
using namespace std;

// 队列：先进先出（FIFO - First In First Out）
// 在队尾入队，在队首出队

int main() {
    queue<int> q;
    q.push(1);
    q.push(2);
    q.push(3);

    // 应用1：约瑟夫问题
    // n 个人围成一圈，从第 1 个人开始报数，报到 m 的人出列，求出列顺序
    int n = 7, m = 3;
    queue<int> jose;
    for (int i = 1; i <= n; i++) jose.push(i);

    cout << "出列顺序: ";
    while (!jose.empty()) {
        for (int i = 1; i < m; i++) {
            jose.push(jose.front());
            jose.pop();
        }
        cout << jose.front() << " ";
        jose.pop();
    }
    cout << endl;
    // 出列顺序: 3 6 2 7 5 1 4

    // 应用2：BFS 广度优先搜索（在 Day 3 详细讲）

    return 0;
}
```

#### 链表（Linked List）

<!-- 对应代码文件：ch14_1_3.cpp -->
```cpp
#include <iostream>
using namespace std;

// 单链表：每个节点存储数据和指向下一个节点的指针

struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}  // 构造函数
};

int main() {
    // 手动创建链表
    Node* head = new Node(1);    // 第一个节点
    head->next = new Node(2);   // 第二个节点
    head->next->next = new Node(3);  // 第三个节点
    // 链表: 1 -> 2 -> 3 -> NULL

    // 遍历链表
    Node* p = head;
    while (p != nullptr) {
        cout << p->data << " ";
        p = p->next;
    }
    cout << endl;  // 1 2 3

    // 在头部插入新节点
    Node* newNode = new Node(0);
    newNode->next = head;
    head = newNode;
    // 链表: 0 -> 1 -> 2 -> 3 -> NULL

    // 在中间插入（在节点值为 2 的前面插入 15）
    p = head;
    while (p->next != nullptr && p->next->data != 2) {
        p = p->next;
    }
    if (p->next != nullptr) {
        Node* insertNode = new Node(15);
        insertNode->next = p->next;
        p->next = insertNode;
    }
    // 链表: 0 -> 1 -> 15 -> 2 -> 3 -> NULL

    // 删除节点（删除值为 15 的节点）
    p = head;
    while (p->next != nullptr && p->next->data != 15) {
        p = p->next;
    }
    if (p->next != nullptr) {
        Node* toDelete = p->next;
        p->next = toDelete->next;
        delete toDelete;
    }
    // 链表: 0 -> 1 -> 2 -> 3 -> NULL

    // 竞赛中更常用的数组模拟链表（效率更高）
    const int MAXN = 100010;
    int val[MAXN];    // 存储节点值
    int nxt[MAXN];    // 存储下一个节点的下标
    int head2 = -1;   // 头指针，-1 表示空
    int cnt = 0;      // 当前使用的节点数

    // 在头部插入
    auto insertHead = [&](int x) {
        val[cnt] = x;
        nxt[cnt] = head2;
        head2 = cnt;
        cnt++;
    };

    insertHead(3);
    insertHead(2);
    insertHead(1);
    // 链表: 1 -> 2 -> 3

    // 遍历
    for (int i = head2; i != -1; i = nxt[i]) {
        cout << val[i] << " ";
    }
    cout << endl;  // 1 2 3

    return 0;
}
```

### 14.2 简单树

<!-- 对应代码文件：ch14_2.cpp -->
```cpp
#include <iostream>
#include <queue>
using namespace std;

// 树的定义：n 个节点组成的层次结构
// 有一个根节点，每个节点有零个或多个子节点
// 没有子节点的节点叫叶子节点

// 常用概念：
// - 根(Root)：最顶部的节点
// - 叶子(Leaf)：没有子节点的节点
// - 深度(Depth)：从根到该节点的边数
// - 高度(Height)：从该节点到最远叶子的边数
// - 父节点(Parent)：直接上级节点
// - 子节点(Child)：直接下级节点
// - 兄弟节点(Sibling)：同一父节点的节点

// 二叉树：每个节点最多有两个子节点（左孩子、右孩子）
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// 二叉树的遍历
// 前序遍历（Preorder）：根 -> 左 -> 右
void preorder(TreeNode* root) {
    if (root == nullptr) return;
    cout << root->val << " ";     // 先访问根
    preorder(root->left);          // 再遍历左子树
    preorder(root->right);         // 最后遍历右子树
}

// 中序遍历（Inorder）：左 -> 根 -> 右
void inorder(TreeNode* root) {
    if (root == nullptr) return;
    inorder(root->left);           // 先遍历左子树
    cout << root->val << " ";     // 再访问根
    inorder(root->right);          // 最后遍历右子树
}

// 后序遍历（Postorder）：左 -> 右 -> 根
void postorder(TreeNode* root) {
    if (root == nullptr) return;
    postorder(root->left);         // 先遍历左子树
    postorder(root->right);        // 再遍历右子树
    cout << root->val << " ";     // 最后访问根
}

// 层序遍历（BFS）：一层一层从左到右
void levelOrder(TreeNode* root) {
    if (root == nullptr) return;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        TreeNode* node = q.front();
        q.pop();
        cout << node->val << " ";
        if (node->left) q.push(node->left);
        if (node->right) q.push(node->right);
    }
}

int main() {
    // 构建一棵二叉树
    //       1
    //      / \
    //     2   3
    //    / \
    //   4   5

    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    cout << "前序: "; preorder(root); cout << endl;    // 1 2 4 5 3
    cout << "中序: "; inorder(root); cout << endl;     // 4 2 5 1 3
    cout << "后序: "; postorder(root); cout << endl;   // 4 5 2 3 1
    cout << "层序: "; levelOrder(root); cout << endl;  // 1 2 3 4 5

    // 二叉树的基本性质：
    // 1. 第 i 层最多有 2^(i-1) 个节点
    // 2. 深度为 k 的二叉树最多有 2^k - 1 个节点
    // 3. 叶子节点数 = 度为2的节点数 + 1

    return 0;
}
```

### 14.3 特殊树

<!-- 对应代码文件：ch14_3.cpp -->
```cpp
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

// ===== 完全二叉树 =====
// 除最后一层外每层都满，最后一层的节点都靠左排列
// 可以用数组存储：下标从 1 开始
// 节点 i 的左孩子: 2*i，右孩子: 2*i+1，父节点: i/2

void completeBinaryTree() {
    int tree[] = {0, 1, 2, 3, 4, 5, 6, 7};  // 下标从 1 开始
    // 对应的树：
    //        1
    //       / \
    //      2   3
    //     / \ / \
    //    4  5 6  7

    // 访问节点 i 的左孩子
    int i = 2;
    cout << "节点" << i << "的左孩子: " << tree[2 * i] << endl;   // 4
    cout << "节点" << i << "的右孩子: " << tree[2 * i + 1] << endl; // 5
    cout << "节点" << i << "的父节点: " << tree[i / 2] << endl;    // 1

    // 堆是一种特殊的完全二叉树（在 Day 3 的排序部分讲解）
}

// ===== 哈夫曼树与哈夫曼编码 =====
// 哈夫曼树：带权路径长度最短的二叉树
// 构造方法：每次选两个最小的合并

struct HuffNode {
    int weight;
    HuffNode *left, *right;
    HuffNode(int w) : weight(w), left(nullptr), right(nullptr) {}
};

// 比较函数（用于优先队列）
struct Compare {
    bool operator()(HuffNode* a, HuffNode* b) {
        return a->weight > b->weight;  // 小根堆
    }
};

void huffmanExample() {
    // 给定权值：5, 3, 8, 2, 7
    priority_queue<HuffNode*, vector<HuffNode*>, Compare> pq;
    int weights[] = {5, 3, 8, 2, 7};
    for (int w : weights) {
        pq.push(new HuffNode(w));
    }

    // 构建哈夫曼树
    while (pq.size() > 1) {
        HuffNode* left = pq.top(); pq.pop();
        HuffNode* right = pq.top(); pq.pop();
        HuffNode* parent = new HuffNode(left->weight + right->weight);
        parent->left = left;
        parent->right = right;
        pq.push(parent);
    }
    // 最终 pq.top() 就是哈夫曼树的根

    // 哈夫曼编码：
    // 左边编码为 0，右边编码为 1
    // 频率高的字符编码短，频率低的编码长
    // 这样总的编码长度最短
    cout << "哈夫曼树构建完成" << endl;
}

// ===== 二叉搜索树（BST）=====
// 性质：左子树所有节点值 < 根节点值 < 右子树所有节点值
// 中序遍历得到有序序列

struct BSTNode {
    int val;
    BSTNode *left, *right;
    BSTNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

// 插入节点
BSTNode* insertBST(BSTNode* root, int val) {
    if (root == nullptr) return new BSTNode(val);
    if (val < root->val) {
        root->left = insertBST(root->left, val);
    } else {
        root->right = insertBST(root->right, val);
    }
    return root;
}

// 查找节点
bool searchBST(BSTNode* root, int val) {
    if (root == nullptr) return false;
    if (val == root->val) return true;
    if (val < root->val) return searchBST(root->left, val);
    return searchBST(root->right, val);
}

// 中序遍历（得到有序序列）
void inorderBST(BSTNode* root) {
    if (root == nullptr) return;
    inorderBST(root->left);
    cout << root->val << " ";
    inorderBST(root->right);
}

int main() {
    completeBinaryTree();
    huffmanExample();

    // 二叉搜索树
    BSTNode* bst = nullptr;
    int arr[] = {5, 3, 7, 1, 4, 6, 8};
    for (int x : arr) bst = insertBST(bst, x);

    cout << "BST 中序遍历: ";
    inorderBST(bst);
    cout << endl;  // 1 3 4 5 6 7 8（有序的！）

    cout << "查找 4: " << searchBST(bst, 4) << endl;  // 1
    cout << "查找 9: " << searchBST(bst, 9) << endl;  // 0

    return 0;
}
```

### 14.4 简单图

<!-- 对应代码文件：ch14_4.cpp -->
```cpp
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
```

---

## Day 2 练习题

### 练习1：字符串统计
**题目**：输入一行字符串，统计其中大写字母、小写字母、数字和其他字符的个数。
```
输入示例：Hello World! 123
输出示例：
大写: 2
小写: 8
数字: 3
其他: 3
```

### 练习2：字符串反转
**题目**：输入一个字符串，将其反转后输出。不用库函数，自己实现。
```
输入示例：hello
输出示例：olleh
```

### 练习3：回文判断
**题目**：输入一个字符串，判断是否是回文（正着读和倒着读一样）。
```
输入示例：abcba
输出示例：YES
输入示例：hello
输出示例：NO
```

### 练习4：递归求最大公约数
**题目**：用辗转相除法（递归实现）求两个数的最大公约数。
```
输入示例：48 36
输出示例：12
```

### 练习5：递归求幂
**题目**：用递归快速求 x^n（提示：x^n = (x^(n/2))^2，时间复杂度 O(log n)）。
```
输入示例：2 10
输出示例：1024
```

### 练习6：结构体排序
**题目**：输入 n 个学生的姓名和成绩，按成绩从高到低排序输出。
```
输入示例：
3
Alice 90
Bob 85
Carol 95
输出示例：
Carol 95
Alice 90
Bob 85
```

### 练习7：栈的应用
**题目**：输入一个后缀表达式（逆波兰表达式），求其值。运算符包含 +, -, *。
```
输入示例：3 4 + 5 *
输出示例：35
```

### 练习8：用栈实现队列
**题目**：用两个栈模拟实现一个队列，支持入队和出队操作。

### 练习9：二叉树遍历
**题目**：给定二叉树的前序遍历和中序遍历，输出后序遍历。
```
输入示例：
前序: 1 2 4 5 3
中序: 4 2 5 1 3
输出示例: 4 5 2 3 1
```

### 练习10：邻接矩阵转邻接表
**题目**：输入一个图的邻接矩阵，转换成邻接表输出。

### 练习11：统计单词数
**题目**：输入一行英文，统计有多少个单词（单词之间用空格分隔）。
```
输入示例：Hello world this is C++
输出示例：5
```

### 练习12：vector操作
**题目**：输入 n 个整数存入 vector，去除重复元素后排序输出。
```
输入示例：8 3 5 3 8 1 5 2
输出示例：1 2 3 5 8
```

### 练习13：文件操作
**题目**：从文件读取 n 个整数，排序后写入另一个文件。

### 练习14：二叉搜索树操作
**题目**：输入 n 个整数，构建二叉搜索树，输出中序遍历结果和查找某个数的是否存在。
```
输入示例：
5 3 7 1 4
查找: 3
输出示例：
中序: 1 3 4 5 7
查找3: 存在
```

---

> **Day 2 学习建议**：
> 1. 递归是今天的难点，一定要画图理解递归的执行过程
> 2. 指针概念不需要完全掌握细节，重点是理解"地址"的概念
> 3. STL 容器要多练，竞赛中非常常用
> 4. 数据结构部分要理解原理，不一定要手写实现
> 5. 预计学习时间：8-10 小时（含练习）
