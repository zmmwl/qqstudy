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
