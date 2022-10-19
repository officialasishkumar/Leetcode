class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ret;
        for(int i = 1; i < nums.size(); i++){
            for(int j = 0; j < i; j++){
                if(nums[i] + nums[j] == target && i != j){
                    ret = {i,j};
                    return ret;
                }
            }
        }
        return ret;
    }
    
};