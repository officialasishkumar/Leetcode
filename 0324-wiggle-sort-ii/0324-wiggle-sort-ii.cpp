class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> sorted = nums;
        for(int i = nums.size() - 1, j = 0, k = i / 2 + 1; i >= 0; --i) {
            nums[i] = sorted[i & 1 ? k++ : j++];
        }
    }
};