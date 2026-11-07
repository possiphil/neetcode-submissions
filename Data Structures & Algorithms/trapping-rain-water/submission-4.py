class Solution:
    def trap(self, h: List[int]) -> int:
        l,r = 0, len(h)-1
        ml,mr = h[l],h[r]
        res = 0

        while l < r:
            if ml < mr:
                l += 1
                ml = max(ml,h[l])
                res += ml - h[l]
            else:
                r -= 1
                mr = max(mr,h[r])
                res += mr - h[r]

        return res