class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count, t_count = {}, {}

        for i in range(len(s)):
            if s[i] in s_count.keys():
                s_count[s[i]] += 1
            else:
                s_count[s[i]] = 1
            if t[i] in t_count.keys():
                t_count[t[i]] += 1
            else:
                t_count[t[i]] = 1
        return s_count == t_count