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
    int ans = 0;
public:
    int sum(TreeNode* root, int &cnt){
        if(!root) return 0;
        cnt++;
        int left = sum(root->left, cnt);
        int right = sum(root->right, cnt);
        return (left + right + root->val);
    }
    void solve(TreeNode* root){
        if(!root) return;
        int cnt = 0;
        int avg = sum(root, cnt)/cnt;
        if(avg == root->val) ans++;
        solve(root->left);
        solve(root->right);
    }
    int averageOfSubtree(TreeNode* root) {
        solve(root);
        return ans;
    }
};