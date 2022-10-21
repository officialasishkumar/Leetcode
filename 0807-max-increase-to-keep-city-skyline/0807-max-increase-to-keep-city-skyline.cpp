class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        int n = grid.size(), ans = 0;
        vector<int> row(grid.size(), 0), col(grid.size(), 0);
        for(int i = 0; i<n; i++){
            for(int j = 0; j<n; j++){
                row[i] = max(grid[i][j], row[i]);
                col[j] = max(grid[i][j], col[j]);
            }
        }
        for(int i = 0; i<n; i++){
            for(int j = 0; j<n; j++){
                int x = grid[i][j];
                grid[i][j] = min(row[i], col[j]);
                ans+=grid[i][j]-x;
            }
        }
        return ans;
    }
};