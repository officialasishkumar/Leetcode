class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        res = []
        count = 0
        for word in strs:
            index = ''.join(sorted(word))
            if index in cache:
                res[cache[index]].append(word)
            else:
                res.append([word])
                cache[index] = count
                count += 1
        return res
