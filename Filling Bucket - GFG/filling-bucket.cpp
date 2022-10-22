//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    int fillingBucket(int N) {
        if(N<=2) return N;
        int mod = 1e8;
        int f = 1;
        int s = 2;
        for(int i = 3; i<=N; i++){
            int ans = (f+s)%mod;
            f = s;
            s = ans;
        }
        return s%mod;
    }
};  

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        
        cin>>N;

        Solution ob;
        cout << ob.fillingBucket(N) << endl;
    }
    return 0;
}
// } Driver Code Ends