class Solution:
    def isValid(self, s: str) -> bool:
        opening = ["(", "[", "{"]
        closing = [")","]","}"]
        stack = []
        for char in s:
            if char in opening:
                stack.append(char)
            if char in closing:
                if len(stack) == 0:
                    return False
                if stack[-1] == opening[closing.index(char)]:
                    stack.pop()
                else:
                    return False
        return True if len(stack)==0 else False