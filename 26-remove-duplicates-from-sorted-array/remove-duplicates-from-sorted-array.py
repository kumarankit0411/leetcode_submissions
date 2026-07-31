class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        duplicate = False
        j = 1
        n = len(nums)
        duplicateExisted = False

        while(j<n):
            if(nums[i] == nums[j]):
                # duplicate = True
                duplicateExisted = True
                j+=1
                continue
            else:
                if(j-i > 1):
                    self.swap(nums, i+1, j)
                    # duplicate = False
                i+=1
            j+=1

        return i+1 if duplicateExisted else n
    
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
        