class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        # pmax = [0] * len(nums)
        # for i in range(len(nums)):
        #     current_sum += nums[i]
        #     pmax[i] = current_sum

        sum_dict = {0: 1}
        count = 0
        for i in range(len(nums)):
            current_sum = current_sum + nums[i]
            diff = current_sum - k
            
            if diff in sum_dict:
                count = count + sum_dict[diff]

            sum_dict[current_sum] = sum_dict.get(current_sum, 0) + 1
        
        return count
         