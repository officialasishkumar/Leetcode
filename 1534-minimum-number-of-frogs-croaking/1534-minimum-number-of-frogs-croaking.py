class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c, r, o, a, k = 0, 0, 0, 0, 0
        frogs = 0
        currFrogs = 0
        for char in croakOfFrogs:
            if char == 'c':
                c += 1
                currFrogs += 1
                frogs = max(frogs, currFrogs)
            elif char == 'r':
                if c == 0:
                    return -1
                r += 1
                c -= 1
            elif char == 'o':
                if r == 0:
                    return -1
                o += 1
                r -= 1
            elif char == 'a':
                if o == 0:
                    return -1
                a += 1
                o -= 1
            elif char == 'k':
                if a == 0:
                    return -1
                k += 1
                a -= 1
                currFrogs -= 1
        print(c,r,o,a,k)
        if c+r+o+a == 0:
            return frogs
        return -1
