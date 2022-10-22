class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& v) {
        vector<vector<int>> ans;
        for(int i = 0; i<v.size(); i++){
            if(v[i] == -1) continue;
            int x = v[i];
            vector<int> vec;
            for(int j = i; j<v.size() && vec.size()<x; j++){
                if(v[j]!=-1 and v[j] == x) {
                    vec.push_back(j);
                    v[j] = -1;
                }
            }
            ans.push_back(vec);
        }
        return ans;
    }
};