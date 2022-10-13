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
    int cnt = 0;
public:
    void dfs(TreeNode* root, int maxx){
        if(!root) return;
        if(root->val>=maxx){
            cnt++;
            maxx = root->val; 
        } 
        dfs(root->left, maxx);
        dfs(root->right, maxx);
    }
    
    int goodNodes(TreeNode* root) {
        dfs(root, root->val);
        return cnt;
    }
};