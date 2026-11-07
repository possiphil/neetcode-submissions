class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cnt = 0
        cnt = 0

        for n in nums:
            if n == 1:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 0

        return max(max_cnt, cnt)
        