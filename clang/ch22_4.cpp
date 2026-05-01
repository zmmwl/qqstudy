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
