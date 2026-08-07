class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indices = {}
        l, maxi = 0, 0

        for r in range(len(s)):
            if  s[r] in indices:
                l = max(indices[s[r]] + 1, l)
            indices[s[r]] = r
            maxi = max(maxi, r - l + 1)       
        
        return maxi     