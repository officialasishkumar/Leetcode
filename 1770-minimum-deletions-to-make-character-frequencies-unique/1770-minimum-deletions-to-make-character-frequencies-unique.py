class Solution:
    def minDeletions(self, s: str) -> int:
        count = {}
        for i in range(0,len(s)):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
        vals = list(count.values())
        vals.sort(reverse=True)
        deletions = 0
        for i in range(0,len(vals)-1):
            if vals[i] <= vals[i+1]:
                value = max(vals[i]-1, 0)
                deletions += (vals[i+1] - value)
                vals[i+1] = value
        return deletions