class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        if(numRows == 1) {
            return vector<vector<int>> {{1}};
        }
        vector<vector<int>> v{{1}, {1, 1}};
        for(int i = 0; i < numRows - 2; ++i) {
            vector<int> inserter{1};
            for(int j = 0; j < v.back().size() - 1; ++j) {
                inserter.push_back({v[v.size() - 1][j] + v[v.size() - 1][j + 1]});
            }
            inserter.push_back(1);
            v.push_back(inserter);
        }
        return v;
        
    }
};