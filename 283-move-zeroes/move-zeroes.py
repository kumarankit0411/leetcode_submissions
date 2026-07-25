class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        j = 0
        n = len(nums)

        while(i<n):
            if nums[i] != 0:
                self.swap(nums, i, j)
                i+=1
                j+=1
            else:
                i+=1

    def swap(self, arr, i, j):
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t
        