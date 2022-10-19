class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n = nums.size();
        vector<int> v(nums.size()*2, 0);
        for(int i = 0; i<n; i++){
            v[i] = v[i+n] = nums[i];
        }
        return v;
    }
};