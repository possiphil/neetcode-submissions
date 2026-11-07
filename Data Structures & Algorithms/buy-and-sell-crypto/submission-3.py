class Solution:
    def maxProfit(self, ps: List[int]) -> int:
        maxp = 0
        l,r = 0,1

        while r < len(ps):
            maxp = max(maxp, ps[r] - ps[l])

            if ps[l] > ps[r]:
                l = r
            
            r += 1

        return maxp