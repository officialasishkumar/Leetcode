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
    int sum = 0;
public:
    int sumEvenGrandparent(TreeNode* root) {
        dfs(root, NULL, NULL);
        return sum;
    }
    
    void dfs(TreeNode* root, TreeNode* parent, TreeNode* grandParent){
        if(root == NULL) return;
        if(grandParent != NULL && grandParent->val % 2 == 0)
            sum+=root->val;
        dfs(root->left, root, parent);
        dfs(root->right, root, parent);
    }
};