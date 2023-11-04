class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        t = [[-1 for p in range(0,n+1)]
            for q in range(0,k+1)]        
        return self.solve(k,n,t)
    
    def solve(self,k,n,t):
        if k == 1 or n == 1 or n == 0:
            return n
        
        if t[k][n] != -1:
            return t[k][n]
        ans = float('inf')
        low = 0
        high = n
        while low <= high:
            mid = (low + high) // 2
            left = self.solve(k-1,mid-1,t)
            right = self.solve(k,n-mid,t)
            temp = 1 + max(left,right)
            
            if left < right:
                low = mid+1
            else:
                high = mid-1
                
            ans = min(ans,temp)
            t[k][n] = ans
        return ans