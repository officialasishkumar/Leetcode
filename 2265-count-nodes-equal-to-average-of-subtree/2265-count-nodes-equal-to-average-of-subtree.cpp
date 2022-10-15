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
class Solution {
    int ans{};
public:
    int calc(TreeNode* root, int &sz){
        if(!root) return 0;
        sz++;
        int left = calc(root->left, sz);
        int right = calc(root->right, sz);
        return left + right + root->val;
    }
    void preOrder(TreeNode* root){
        if(!root) return;
        int sz = 0;
        int avg = (calc(root, sz)/sz);
        if(avg == root->val) ans++;
        preOrder(root->left);
        preOrder(root->right);
    }
    int averageOfSubtree(TreeNode* root) {
        preOrder(root);
        return ans;
    }
};