from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        j=0
        s_dict = [0] * 26
        s_sum = 0
        longest = -float('inf')

        # for m in range(k+1):
        #     s_dict[ord(s[m])%26] += 1

        while j < len(s):
            s_dict[ord(s[j])%26] += 1

            s_sum = self.findSumExcludingHighest(s_dict)
            print(s_sum)

            while s_sum > k and i<len(s) - 1:
                # valid
                s_dict[ord(s[i])%26] -= 1
                i+=1
                s_sum = self.findSumExcludingHighest(s_dict)

            if j - i + 1 > longest:
                longest = j - i + 1

            j+=1
        
        return longest
            
    def findSumExcludingHighest(self, arr):
        high = 0
        index = -1
        for i in range(len(arr)):
            if arr[i] > high:
                high = arr[i]
                index = i

        res = 0
        for i in range(len(arr)):
            if i == index or arr[i] == 0:
                continue
            else:
                res += arr[i]

        return res


