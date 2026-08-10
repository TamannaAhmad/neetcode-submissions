class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []

        for c in s:
            if c in map.keys():
                stack.append(c)
            elif c in map.values():
                if stack and map[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return not stack