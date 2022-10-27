class Solution {
public:
    int largestOverlap(vector<vector<int>>& img1, vector<vector<int>>& img2) {
        int ans = 0, n = img1.size();
        for (int x = -n; x < n; x++) {
            for (int y = -n; y < n; y++) {
                int cur = 0;
                for (int i = max(0, 0 - x); i < min(n, n - x); i++) {
                    for (int j = max(0, 0 - y); j < min(n, n - y); j++) {
                        if (img1[i][j] == 1 && img2[i + x][j + y] == 1)
                            cur++;
                    }
                }
                ans = max(ans, cur);
            }
        }
        return ans;
    }
};