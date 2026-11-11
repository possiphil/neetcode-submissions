class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,j = 0,0

        while j < len(nums):
            if nums[i] == val:
                while j < len(nums):
                    if nums[j] == val:
                        j += 1
                    else:
                        break

                if j == len(nums):
                    return i
                
                nums[i], nums[j] = nums[j], nums[i]
                
            i += 1
            j += 1

        return i
        