#define ll long long
class Solution {
public:
    bool check(ll x, ll y, ll cx, ll cy, ll r){
        return (x-cx)*(x-cx) + (y-cy)*(y-cy) <= r*r;
    }
    vector<int> countPoints(vector<vector<int>>& pts, vector<vector<int>>& q) {
        vector<int> ans(q.size(), 0);
        
        for(int j = 0; j<q.size(); j++){
            for(int i = 0; i<pts.size(); i++){
                ans[j]+= check(pts[i][0], pts[i][1], q[j][0], q[j][1], q[j][2]);
            }
        }
        return ans;
    }
};