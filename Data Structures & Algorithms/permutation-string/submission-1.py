class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp, mp1 = defaultdict(int), defaultdict(int)
        l,r = 0,0

        for c in s1:
            mp[c] += 1
        mp1 = mp.copy()
        
        while r < len(s2):
            if sum(mp.values()) == 0: 
                return True

            if s2[r] not in mp:
                r += 1
                l = r
                mp = mp1.copy()
                continue
            
            while mp[s2[r]] == 0:
                mp[s2[l]] += 1
                l += 1

            mp[s2[r]] -= 1
            r += 1

        return sum(mp.values()) == 0