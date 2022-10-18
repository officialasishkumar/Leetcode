class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int index = 0;
        int maxi = INT_MIN;
        for(int i = 0;i<nums.size();i++){
            if(maxi<nums[i]){
                index = i;
                maxi = nums[i];
            }
        }
        
        return index;
    }
};