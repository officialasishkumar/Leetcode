class Solution {
public:
    string getPermutation(int n, int k) {
        vector<int> perm(n);
        for(int i = 1; i <= n; i++) {
            perm[i-1] = i;
        }
        int permNum = 1;
        do {
            if(permNum == k) break;
            permNum++;
        } while(next_permutation(perm.begin(), perm.end()));
        string result = "";
        for(int i = 0; i < n; i++) {
            result += '0' + perm[i];
        }
        return result;
    }
};