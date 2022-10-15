#define ll long long
class Solution {
public:
    int minimizeArrayValue(vector<int>& nums) {
        ll n = nums.size(), maxx = nums[0];
        ll sum = nums[0];
        for(ll i = 1; i<n;i++){
            sum+=nums[i];
            maxx = max(maxx, (ll)ceil((double)sum/(i+1)));
        }
        return maxx;
    }
};