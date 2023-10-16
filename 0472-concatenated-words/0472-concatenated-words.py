class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordset = set(words)
        dp = {}

        def dfs(word):
            if word in dp:
                return dp[word]
            for i in range(1,len(word)):
                pref = word[:i]
                if word[:i] in wordset:
                    if word[i:] in wordset or dfs(word[i:]):
                        dp[word] = True
                        return True
            dp[word] = False
            return False
        
        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        return res