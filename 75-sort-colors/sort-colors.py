class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # move 0 to front
        i = 0
        j = 0
        n = len(nums)

        while(j<n):
            if (nums[j] == 0):
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j+=1
            else:
                j+=1

        # i = 0
        j = i
        while(j<n):
            if (nums[j] == 1):
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j+=1
            else:
                j+=1