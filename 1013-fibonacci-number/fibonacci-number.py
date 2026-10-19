class Solution:
    def fib_better(self, n, dp):
        if n==1 or n==0:
            return n
        if dp[n]!=-1:
            return dp[n]
        ra1 = self.fib_better(n-1, dp)
        ra2 = self.fib_better(n-2, dp)
        ma = ra1+ra2
        dp[n] = ma
        return ma

    def fib(self, n: int) -> int:
        dp = [-1] * (n+1)
        
        return self.fib_better(n, dp)