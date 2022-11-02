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
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        stack<TreeNode*> st;
        for(auto num: nums){
            TreeNode* node = new TreeNode(num);
            while(st.size() && node->val>st.top()->val){
                node->left = st.top();
                st.pop();
            }
            if(st.size()){
                st.top()->right = node;
            }
            st.push(node);
        }
        while(st.size()>1){
            st.pop();
        }
        return st.top();
    }
};