class Solution:
    def maxProfit(self, ps: List[int]) -> int:
        res = 0
        suff = [0] * len(ps)

        for i in range(len(ps)-2,-1,-1):
            suff[i] = max(suff[i+1], ps[i+1])

        for i,n in enumerate(ps):
            res = max(res, suff[i] - n)

        return res