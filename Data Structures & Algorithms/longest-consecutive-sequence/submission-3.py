class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        m = 0
        c = 1
        n = sorted(nums)

        for i in range(len(n)):
            if n[i] == n[i-1]:
                continue
            elif n[i] == n[i-1] + 1:
                c += 1
            else:
                m = max(m,c)
                c = 1
        
        return max(m,c)
        