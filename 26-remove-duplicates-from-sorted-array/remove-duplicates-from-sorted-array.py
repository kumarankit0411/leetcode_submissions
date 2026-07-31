class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        n = len(nums)

        while(j<n):
            if(nums[i] == nums[j]):
                duplicateExisted = True
                j+=1
                continue
            else:
                if(j-i > 1):
                    self.swap(nums, i+1, j)
                i+=1
            j+=1

        return i+1
    
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
        