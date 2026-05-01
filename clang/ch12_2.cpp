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
