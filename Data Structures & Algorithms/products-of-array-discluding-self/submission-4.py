class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1] * l
        p = 1

        for i in range(l):
            res[i] = p
            p *= nums[i]

        p = 1
        for i in range(l-1,-1,-1):
            res[i] *= p
            p *= nums[i]

        return res