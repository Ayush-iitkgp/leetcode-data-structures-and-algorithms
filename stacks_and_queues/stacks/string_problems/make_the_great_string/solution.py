class Solution:
    def makeGood(self, s: str) -> str:
        """
        Here also the last character is equal to the lower/upper of the existing then we remove it
        hence stack can be used
        """

        def isLower(char):
            return "a" <= char <= "z"

        def isUpper(char):
            return "A" <= char <= "Z"

        stack = []
        stack.append(s[0])

        for i in range(1, len(s)):

            if stack and isLower(stack[-1]) and stack[-1].upper() == s[i]:
                stack.pop()
            elif stack and isUpper(stack[-1]) and stack[-1].lower() == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        return "" if not stack else "".join(stack)
