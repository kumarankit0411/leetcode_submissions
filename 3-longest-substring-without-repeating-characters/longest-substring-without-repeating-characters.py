class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        
        i = 0
        s_dict = [-1] * 256
        longest = -float('inf')
        
        for j in range(len(s)):
            pos = s_dict[ord(s[j])]
            if pos != -1 and pos >= i:
                #duplicate found
                i = pos + 1

            s_dict[ord(s[j])] = j
            if j - i + 1 > longest:
                longest = j - i + 1

        return longest
            