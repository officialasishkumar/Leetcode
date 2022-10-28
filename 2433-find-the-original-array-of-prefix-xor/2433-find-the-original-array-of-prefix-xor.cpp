class Solution {
public:
    vector<int> findArray(vector<int>& pref) {
        int n = pref.size();
        vector<int> ans(n, pref[0]);
        int x = ans[0];
        for(int i = 1; i<n; i++){
            ans[i] = pref[i-1]^pref[i];
        }
        return ans;
    }
};