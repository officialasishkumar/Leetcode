class Solution {
public:
    
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        vector<vector<int>> adj(n);
        
        for (int i = 0; i < edges.size(); i++)
        {
            adj[edges[i][0]].push_back(edges[i][1]);
            adj[edges[i][1]].push_back(edges[i][0]);

        }
            
        vector<int> v;
        queue<int> q;
        q.push(source);
        vector<int> vis(n, 0);
        vis[source] = 1;

        while (!q.empty())
        {
            int td = q.front();
            q.pop();
            v.push_back(td);
            for (auto x : adj[td])
            {
                if (!vis[x])
                {
                    vis[x] = 1;
                    q.push(x);
                }
            }
        }
 
        return vis[destination];
        
    }
};