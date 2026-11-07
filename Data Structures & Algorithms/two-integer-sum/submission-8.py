class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = []
        for i, num in enumerate(nums):
            s.append([num, i])

        s.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            cur = s[i][0] + s[j][0]
            if cur == target:
                return [min(s[i][1], s[j][1]), max(s[i][1], s[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1

        return []
