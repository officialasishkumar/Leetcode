class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum = 0;
        int mx = nums[0];
        int n = nums.size();
        for(int i = 0; i < n; ++i) {
            sum += nums[i];
            mx = max(mx, sum);
            if(sum < 0) sum = 0;
        }
        return mx;
    }
};
