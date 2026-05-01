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
