class Solution:
    def trap(self, height: List[int]) -> int:
        suff = [0] * len(height)
        res = 0

        for i in range(len(height)-2, -1, -1):
            suff[i] = max(height[i+1], suff[i+1])

        l,r = 0,1

        while r < len(height):
            lh = min(height[l], suff[l])
            rh = height[r]

            if rh >= lh:
                l = r
                r = r+1
            else:
                res += lh - rh
                r += 1

        return res