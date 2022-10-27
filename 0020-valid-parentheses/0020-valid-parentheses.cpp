class Solution {
public:
    bool isValid(string s) {
        stack<char> seq;
        for(auto& c : s) {
            if(c == '(' || c == '[' || c == '{') seq.emplace(c);
            else if(c == ')') {
                if(seq.empty() || seq.top() != '(') return false;
                else seq.pop();
            }
            else if(c == ']') {
                if(seq.empty() || seq.top() != '[') return false;
                else seq.pop();
            }
            else {
                if(seq.empty() || seq.top() != '{') return false;
                else seq.pop();
            }
        }
        if(seq.empty()) return true;
        return false;
    }
};