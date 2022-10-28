class Solution {
    public int largestOverlap(int[][] img1, int[][] img2) {
        int ans = 0,n = img1.length;
        for(int x = -n; x < n; x++){
            for(int y = -n; y < n; y++){
                int cur = 0;
                for(int i = Math.max(0, 0 - x); i < Math.min(n, n - x); i++){
                    for(int j = Math.max(0, 0 - y); j < Math.min(n, n - y); j++){
                        if(img1[i][j] == 1 && img2[i+x][j+y] == 1) cur++;
                    }
                }
                ans = Math.max(ans, cur);
            }
        }
        return ans;
    }
}