class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        row1 = [0 for i in range(m+1)]
        row2 = [0 for i in range(m+1)]

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if text1[i] == text2[j]:
                    row1[j] = 1 + row2[j+1]
                else:
                    row1[j] = max(row2[j], row1[j+1])
            row2 = row1[:]
        
        return row2[0]