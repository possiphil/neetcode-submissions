class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []

        for i in range(len(arr)-1):
            max = arr[i+1]

            for j in range(i+2,len(arr)):
                if arr[j] > max:
                    max = arr[j]

            res.append(max)

        res.append(-1)
        return res
        