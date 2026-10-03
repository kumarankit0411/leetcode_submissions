class Solution:
    def isBitSet(self, n, i):
        return n & (1<<i)
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(31):
            if self.isBitSet(n, i):
                count+=1
        
        return count