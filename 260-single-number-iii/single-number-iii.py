class Solution:
    def isBitSet(self, n, i):
        return n&(1<<i)
    def singleNumber(self, nums: list[int]) -> list[int]:
        ans = 0
        for i in nums:
            ans = ans ^ i

        j = -1
        for i in range(32):
            if self.isBitSet(ans, i):
                j = i
                break
        
        set1 = 0
        set2 = 0

        for n in nums:
            if self.isBitSet(n, j):
                set1 = set1^n
            else:
                set2 = set2^n
            
        return [set1, set2]

