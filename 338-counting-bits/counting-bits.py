class Solution:
    def isBitSet(self, n, i):
        return n&(1<<i)
    def hammingWeight(self, n):
        count = 0
        for i in range(31):
            if self.isBitSet(n, i):
                count+=1
        return count
    def countBits(self, n: int) -> list[int]:
        ans = []
        for i in range(n+1):
            ans.append(self.hammingWeight(i))
        return ans