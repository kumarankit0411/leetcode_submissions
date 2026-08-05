class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        
        i = 0
        s_dict = [-1] * 256
        longest = -float('inf')
        
        for j in range(len(s)):
            if s_dict[ord(s[j])] != -1 and s_dict[ord(s[j])] >= i:
                #duplicate found
                i = s_dict[ord(s[j])] + 1

            s_dict[ord(s[j])] = j

            print(longest)
            if j - i + 1 > longest:
                longest = j - i + 1

        return longest
            