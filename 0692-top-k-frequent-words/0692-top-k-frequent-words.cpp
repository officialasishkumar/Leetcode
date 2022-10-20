class Solution {
public:
    static bool cmp(pair<int, string> p1, pair<int, string> p2) {
        if(p1.first == p2.first) {
            return p1.second < p2.second;
        }
        else {
            return p1.first > p2.first;
        }
    }
    vector<string> topKFrequent(vector<string>& words, int k) {
        map<string, int> mp;
        for(auto wd : words) {
            mp[wd]++;
        }
        vector<pair<int, string>> v;
        for(auto elem : mp) {
            v.push_back({elem.second, elem.first});
        }
        sort(v.begin(), v.end(), cmp);
        vector<string> ans;
        for(int i = 0; i < k; ++i) {
            ans.push_back(v[i].second);
        }
        return ans;
    }
};