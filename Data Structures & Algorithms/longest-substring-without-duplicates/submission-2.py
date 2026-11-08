class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        mp = defaultdict(str)
        res = 1
        l,r = 0,0

        while r < len(s):
            if s[r] in mp:
                l = max(l, mp[s[r]])
                
            mp[s[r]] = r+1
            r += 1
            res = max(res, r - l)
        
        return res