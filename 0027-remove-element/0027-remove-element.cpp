class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        sort(nums.begin(), nums.end());
        auto it = lower_bound(nums.begin(), nums.end(), val);
        auto it2 = upper_bound(nums.begin(), nums.end(), val);
        nums.erase(it, it2);
        return nums.size();
    }
};