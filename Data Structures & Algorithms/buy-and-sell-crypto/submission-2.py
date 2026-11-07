class Solution:
    def maxProfit(self, ps: List[int]) -> int:
        maxp = 0
        minb = ps[0]

        for p in ps:
            maxp = max(maxp, p - minb)
            minb = min(minb, p)

        return maxp