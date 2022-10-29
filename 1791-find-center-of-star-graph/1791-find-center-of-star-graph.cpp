class Solution {
public:
    
    int findCenter(vector<vector<int>>& edges) {
        int n =0, ans =-1;
       for(int i=0; i<edges.size(); i++){
                n = max(n, max(edges[i][0], edges[i][1]));
       }
        
       vector <int> ind(n+1);
    
       for(int i=0; i<edges.size(); i++){
            ind[edges[i][0]]++;
            ind[edges[i][1]]++;
       }
       
       for(int i=0; i<ind.size(); i++){
          if(ind[i]==n-1){
             ans =  i; 
            //  break;
          }
        }
     return ans;   
    }
};