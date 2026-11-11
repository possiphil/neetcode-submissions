class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = defaultdict(int)

        for n in nums:
            mp[n] += 1

        for k in mp.keys():
            if mp[k] >= len(nums) // 2:
                return k

        return None
        