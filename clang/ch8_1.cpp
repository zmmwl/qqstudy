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
