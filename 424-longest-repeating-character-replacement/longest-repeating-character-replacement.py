class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        j=0
        max_freq = 0
        s_dict = [0] * 26
        longest = -float('inf')

        for j in range(len(s)):
            s_dict[ord(s[j])%26] += 1

            max_freq = max(max_freq, s_dict[ord(s[j])%26])

            while (j - i + 1) - max_freq > k:
                s_dict[ord(s[i])%26] -= 1
                i+=1

            if j - i + 1 > longest:
                longest = j - i + 1
        
        return longest

