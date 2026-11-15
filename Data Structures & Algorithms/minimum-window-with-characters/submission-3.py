class Solution:
    def minWindow(self, s: str, t: str) -> str:
        resLen, res = -1, ""
        l, r = 0,0

        mp = {}
        for c in t:
            mp[c] = mp.get(c, 0) + 1

        missing = 0
        for v in mp.values():
            missing += 1

        while r < len(s) or r == len(s) and missing == 0:
            if missing > 0:
                c = s[r]
                if c in mp.keys():
                    mp[c] -= 1
                    if mp[c] == 0:
                        missing -= 1
                
                r += 1

            else:
                curLen = (r - l) + 1

                if resLen == -1 or curLen < resLen:
                    resLen = curLen
                    res = s[l:r]

                c = s[l]
                if c in mp.keys():
                    mp[c] += 1
                    if mp[c] == 1:
                        missing += 1

                l += 1

        return res