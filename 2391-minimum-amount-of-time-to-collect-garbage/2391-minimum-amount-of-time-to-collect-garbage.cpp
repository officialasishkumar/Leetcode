class Solution {
public:
    int garbageCollection(vector<string>& vec, vector<int>& time) {
        int n = vec.size();
        int ans= 0;
        for(int i = 0; i<n; i++){
            ans += vec[i].size();
        }
        for(int i = 1; i<time.size(); i++)
            time[i] += time[i-1];
        int p{}, g{}, m{};
        for(int i=n-1; i>=1; i--){
            if(!m && find(vec[i].begin(), vec[i].end(), 'M') != vec[i].end()) {
                ans+=time[i-1];
                m = 1;
            }
            if(!p && find(vec[i].begin(), vec[i].end(), 'P') != vec[i].end()) {
                ans+=time[i-1];
                p = 1;
            }
            if(!g && find(vec[i].begin(), vec[i].end(), 'G') != vec[i].end()) {
                ans+=time[i-1];
                g = 1;
            }
        }
        return ans;
    }
};