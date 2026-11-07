class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        z = 0

        for n in nums:
            if n != 0:
                p *= n
            else:
                z += 1

        if z > 1:
            return [0] * len(nums)

        res = [0] * len(nums)
        for i,c in enumerate(nums):
            if z: res[i] = 0 if c else p
            else: res[i] = p // c

        return res