class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        s = set(nums)
        m = 0

        for n in s:
            if (n-1) in s: 
                continue

            c = 1
            while (n+c) in s:
                c += 1

            m = max(c,m)

        return m
                
        