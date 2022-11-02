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
        return construct(nums, 0, nums.size() -1);
    }
    
    TreeNode* construct(vector<int> &nums, int s, int e){
        if(s>e) return NULL;
        int idx = findMax(nums,s,e);
        
        TreeNode* root = new TreeNode(nums[idx]);
        root->left = construct(nums, s, idx-1);
        root->right = construct(nums, idx+1, e);
        return root;
    }
    
    int findMax(vector<int> &nums, int s, int e){
        int maxx = INT_MIN, idx = -1;
        for(int i = s; i<=e; i++){  
            if(nums[i]>maxx){
                maxx = nums[i];
                idx = i;
            }
        }
        return idx;
    }
};