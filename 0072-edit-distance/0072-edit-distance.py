class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n = len(word1)
        m = len(word2)

        prev = [j for j in range(m + 1)]
        cur = [0 for _ in range(m + 1)]

        for i in range(1, n + 1):
            cur[0] = i 
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    cur[j] = prev[j - 1]
                else:
                    cur[j] = 1 + min(prev[j - 1], min(prev[j], cur[j - 1]))

            prev, cur = cur, prev  

        return prev[m] 