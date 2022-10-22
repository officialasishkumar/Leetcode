class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& v) {
        vector<vector<int>> ans;
        unordered_map<int, vector<int>> mpp;
        for(int i = 0; i<v.size(); i++){
            mpp[v[i]].push_back(i);
            if(mpp[v[i]].size() == v[i]){
                ans.push_back(mpp[v[i]]);
                mpp[v[i]].clear();
            }
        }
        return ans;
    }
};