class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [[0] for _ in range(len(nums))]
        dp[0] = 1
        lis = 1
        
        
        for i in range(len(nums)):
            possible_ans = 0
            for j in range(i):
                if nums[j]<nums[i]:
                    possible_ans = max(dp[j], possible_ans)
            dp[i] = possible_ans + 1
            lis = max(lis, dp[i])
        
        return lis