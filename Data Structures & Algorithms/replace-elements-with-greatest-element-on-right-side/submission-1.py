class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        biggest = [0] * len(arr)
        cur_biggest = 0

        for i in range(len(arr)-1,-1,-1):
            if arr[i] > cur_biggest:
                cur_biggest = arr[i]
            biggest[i-1] = cur_biggest

        biggest[len(arr)-1] = -1
        return biggest

        