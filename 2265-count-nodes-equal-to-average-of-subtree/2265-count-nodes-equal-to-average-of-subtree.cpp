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
    pair<int, int> solve(TreeNode* root){
        if(!root) return {0, 0}; // In case we hit a NULL node we have to return sum and size to be 0.
        auto left = solve(root->left); // Returns the sum and size of the left subtree.
        auto right = solve(root->right); // Returns the sum and size of the right subtree.
        int sum = (left.first + right.first + root->val); // We add all the three values i.e. the sum of the left and right subtree and the value of the current node.
        int n = (left.second + right.second + 1); // We calculate the size of the entire subtree including the parent node. 
        if((sum/n) == root->val) ans++; // If the condition is passed we increment our ans variable. 
        return {sum, n}; // At the end we return the sum and the size of the tree.
    }
    int averageOfSubtree(TreeNode* root) {
        auto pr = solve(root);
        return ans;
    }
};