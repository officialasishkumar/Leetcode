class Solution {
    public int largestOverlap(int[][] img1, int[][] img2) {
        int ans = 0,n = img1.length;
        for(int x = -n; x<n; x++){
            for(int y = -n; y< n; y++){
                int cur = 0;
                for(int i=0; i<n; i++){
                    for(int j=0;j<n; j++){
                        if(i+x>=0&&i+x<n&&j+y>=0&&j+y<n&&img1[i][j]==1&&img2[i+x][j+y]==1) cur++;
                    }
                }
                ans = Math.max(ans, cur);
            }
        }
        return ans;
    }
}