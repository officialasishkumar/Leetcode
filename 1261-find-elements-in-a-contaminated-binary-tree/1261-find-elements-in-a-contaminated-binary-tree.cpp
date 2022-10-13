/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class FindElements {
    unordered_set<int> s;
public:
    void recover(TreeNode* root, int x) {
        if(root == NULL) return;
        root->val = x;
        s.emplace(x);
        recover(root->left, 2*x + 1);
        recover(root->right, 2*x + 2);
    }
    
    FindElements(TreeNode* root) {
        recover(root, 0);
    }
    
    bool find(int target) {
        return s.count(target);
    }
};

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements* obj = new FindElements(root);
 * bool param_1 = obj->find(target);
 */