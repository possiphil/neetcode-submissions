class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        m = 0

        while l < r:
            hl,hr = heights[l], heights[r]

            if hl < hr:
                a = hl * (r - l)
                m = max(m,a)
                l += 1
            else:
                a = hr * (r - l)
                m = max(m,a)
                r -= 1

        return m