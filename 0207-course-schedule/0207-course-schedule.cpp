class Solution {
public:
    
    
    int dfs(int n, int c, vector<vector<int>> adj, vector<int> vis, vector<int> rec){
     
        stack <int> s;
        s.push(c);
        vis[c]= 1;
        rec[c]=1;
        
        while(!s.empty()){
           int td = s.top();
            s.pop();
            for(auto x : adj[td]){
                 if(!vis[x]){
                   vis[x] = 1;
                   s.push(x);
                 }
                else if(rec[x]){
                   return 1;
                }
            }
        }
        return 0;

     }
    
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
      
        vector<vector<int>> adj(numCourses);
        
        for (int i = 0; i <  prerequisites.size(); i++)
        {
            adj[prerequisites[i][0]].push_back(prerequisites[i][1]);
          //  adj[prerequisites[i][1]].push_back(prerequisites[i][0]);

        }
        vector<int> vis(numCourses, 0);
        vector <int> rec(numCourses, 0);
        
       for(int u=0; u<adj.size(); u++){
           if(!vis[u]){
             if(dfs(numCourses, u, adj, vis, rec)) return 0;
           }
       }
       return 1;
    }
};