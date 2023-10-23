class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = ["0"]
        if len(num) <= k:
            return "0"

        for i in range(len(num)):
            while stack[-1] > num[i] and k > 0:
                stack.pop()
                k -= 1
            stack.append(num[i])

        while k > 0:
            stack.pop()
            k -= 1
        
        while len(stack) > 1 and stack[0] == "0":
            stack.pop(0)
        
        return "".join(stack)