class Solution {
public:
    vector<int> minOperations(string boxes) {
        vector<int> ans;
        vector<int> ones;
        for(int i = 0;i<boxes.size(); i++){
            if(boxes[i] == '1')
                ones.push_back(i);
        }
        for(int i=0; i<boxes.size(); i++){
                int cnt = 0;
                for(int j = 0; j<ones.size(); j++){
                    if(ones[j]!=i){
                        cnt+= abs(ones[j] - i);
                    }
                }
            ans.push_back(cnt);
        }
        return ans;
    }
};