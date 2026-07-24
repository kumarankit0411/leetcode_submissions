class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # find first non-negative integer
        n = len(nums)

        right = n-1
        left = 0

        for i in range(n):
            if(nums[i] < 0):
                left = i
                continue
            if(nums[i] >= 0):
                right = i
                break

        outputArr = []

        if(left == 0 and right == 0):
            # all positive
            for i in range(n):
                outputArr.append(nums[i] * nums[i])

            return outputArr

        if (left == n-1 and right == n-1):
            #all negative
            for i in range(n-1, -1, -1):
                outputArr.append(nums[i] * nums[i])
            return outputArr
        
        while(len(outputArr) != n):
            print (left, right)
            if (right > n - 1 and left < 0):
                break
            if (right > n - 1):
                outputArr.append(nums[left])
                left = left - 1
                continue
            if (left < 0):
                outputArr.append(nums[right])
                right = right + 1
                continue
            
            if(nums[left] * -1 <= nums[right]):
                outputArr.append(nums[left])
                left = left - 1
            else:
                outputArr.append(nums[right])
                right = right + 1
            
            

        for i in range(n):
            outputArr[i] = outputArr[i] * outputArr[i]

        return outputArr

        