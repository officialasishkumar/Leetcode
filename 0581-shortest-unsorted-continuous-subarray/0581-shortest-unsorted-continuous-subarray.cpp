class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        vector<int> v = nums;
        sort(v.begin(), v.end());
        if(v==nums) return 0;
        int n = nums.size(), last = n-1, first = 0, ok1 = 0, ok2  = 0;
        while(first<last){
            if(nums[first]!=v[first]) ok1 = 1;
            if(nums[last]!=v[last]) ok2 = 1;
            if(ok1 && ok2) break;
            if(ok1) last--;
            if(ok2) first++;
            if(!ok1 && !ok2) first++, last--;
        }
        return last-first+1;
    }
};