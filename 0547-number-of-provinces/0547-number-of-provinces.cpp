class Solution {
public:
    
    
    void bfs(vector<vector<int>> adj, vector <int> &vis, int u){
         
          queue <int> q;
          vis[u] =1;
          q.push(u);
    
           while(!q.empty()){
            int td = q.front();
              q.pop();
               for(auto x: adj [td]){
                  if(!vis[x]){
                     vis[x] =1;
                      q.push(x);
                  }
                }
           }
        
    }
    
    int findCircleNum(vector<vector<int>>& isConnected) {
      int count =0;
        
     vector<vector<int>> adj(isConnected.size());
    for (int i = 0; i < isConnected.size(); i++)
    {
        for (int j = 0; j < isConnected[i].size(); j++)
        {
            if (isConnected[i][j] == 1)
            {
                adj[i].push_back(j);
                adj[j].push_back(i);
            }
        }
    }
        vector <int> vis(adj.size(), 0);
        
         for(int u=0; u<adj.size(); u++){
          if(!vis[u]){
             bfs(adj, vis, u);
              count++;
          }
         // else {
         //   count++;
         // }
         }
        return count;
    }
};