class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return any(nums[i] == nums[j] for i in range(len(nums)) for j in range(i+1,len(nums)))
        