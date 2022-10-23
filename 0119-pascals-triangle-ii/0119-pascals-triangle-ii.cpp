class Solution {
public:
    vector<int> getRow(int rowIndex) {
        if(rowIndex == 0) {
            return vector<int> {1};
        }
        if(rowIndex == 1) {
            return vector<int> {1, 1};
        }
        vector<int> prev{1, 1};
        for(int i = 0; i <= rowIndex - 2; ++i) {
            vector<int> inserter{1};
            for(int j = 0; j < prev.size() - 1; ++j) {
                inserter.push_back({prev[j] + prev[j + 1]});
            }
            inserter.push_back(1);
            prev = inserter;
        }
        return prev;
    }
};