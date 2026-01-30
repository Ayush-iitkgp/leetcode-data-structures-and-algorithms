class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        1. In this problem, the last character to be inserted is the first one to be out
        if there is a matching character and hence this problem can be solved using stack
        2. The answer would be the remaining characters in the stack
        """
        stack = [s[0]]
        for i in range(1, len(s)):
            if stack and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
