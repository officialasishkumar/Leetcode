class Solution {
public:
    vector<vector<string>> ans;
    bool ispalindrome(string s, int start, int end) {
        while(start <= end) {
            if(s[start++] != s[end--]) {
                return false;
            }
        }
        return true;
    }
    void func(int index, string s, vector<string> &path) {
        if(index == s.length()) {
            ans.push_back(path);
            return;
        }
        for(int i = index; i < s.size(); ++i) {
            if(ispalindrome(s, index, i)) {
                path.push_back(s.substr(index, i - index + 1));
                func(i + 1, s, path);
                path.pop_back();
            }
        }
    }
    vector<vector<string>> partition(string s) {
        vector<string> vec;
        func(0, s, vec);
        return ans;
    }
};