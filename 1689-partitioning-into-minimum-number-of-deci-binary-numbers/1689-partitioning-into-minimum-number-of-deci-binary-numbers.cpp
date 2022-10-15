class Solution {
public:
    int minPartitions(string s) {
        int maxx = -1;
        int n = s.size();
        for(int i = 0; i<n; i++)
            maxx = max(maxx, s[i]-'0');
        return maxx;
    }
};