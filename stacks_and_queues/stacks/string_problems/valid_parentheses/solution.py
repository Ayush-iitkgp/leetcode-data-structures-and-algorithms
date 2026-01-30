class Solution:
    def isValid(self, s: str) -> bool:
        """
        It is a stack problem because the last opening bracket has to match to the
        first closed bracket and hence the LIFO property is satisfied.
        """
        stack = []
        stack.append(s[0])
        for i in range(1, len(s)):
            # print(f"index is {i} and char is {s[i]} and stack is {stack}")
            if s[i] in ["(", "{", "["]:
                stack.append(s[i])
            elif s[i] == ")" and len(stack) != 0 and stack[-1] == "(":
                # print("popping from stack")
                stack.pop()
            elif s[i] == "}" and len(stack) != 0 and stack[-1] == "{":
                stack.pop()
            elif s[i] == "]" and len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                return False
        return len(stack) == 0
