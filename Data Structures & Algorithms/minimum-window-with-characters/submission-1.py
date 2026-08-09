class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        t_freq, window = {}, {}
        for c in set(t):
            t_freq[c] = t.count(c)
        
        have, need = 0, len(t_freq)
        res, res_len = [-1, -1], float('infinity')
        l = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in t_freq and t_freq[s[r]] == window[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res = [l, r]

                window[s[l]] -= 1
                if s[l] in t_freq and window[s[l]] < t_freq[s[l]]:
                    have -= 1
                l += 1                
        
        l, r = res
        return s[l:r+1] if res_len != float('infinity') else ""