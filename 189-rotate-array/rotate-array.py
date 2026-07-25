class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #reverse full arr
        n = len(nums)
        k = k%n
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
        
    def reverse(self, arr: List[int], start: int , end: int):
        while(start<end):
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        
        return arr