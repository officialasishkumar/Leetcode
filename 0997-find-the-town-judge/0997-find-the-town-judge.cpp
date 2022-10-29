class Solution {
public:
    int findJudge(int n, vector<vector<int>>& edges) {
       int ans =-1;
       vector <int> ind(n+1);
      vector <int> out(n+1);
        
       for(int i=0; i<edges.size(); i++){
           out[edges[i][0]]++;
           ind[edges[i][1]]++;
       }
       
       for(int i=0; i<ind.size(); i++){
          if((ind[i]==n-1)&&(out[i]==0)){
             ans =  i; 
            //  break;
          }
        }
     return ans;   
    }
    
};