class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        for c in s:
            if c.isalnum():
                ss += c.lower()
        start, end = 0, len(ss) - 1
        while start < end:
            if ss[start] != ss[end]:
                return False
            start += 1
            end -= 1
        return True