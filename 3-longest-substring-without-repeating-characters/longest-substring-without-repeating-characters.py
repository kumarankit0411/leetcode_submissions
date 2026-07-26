class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        size = -float("inf")
        alpha_dict = [0] * 256

        for m in range(len(s)):
            alpha_dict[ord(s[i])] += 1
            if(alpha_dict[ord(s[i])] == 1):
                size = max(size, i-j+1)
                i+=1
                continue
            if(alpha_dict[ord(s[i])] == 2):
                while(True):
                    alpha_dict[ord(s[j])] -= 1
                    
                    if(alpha_dict[ord(s[j])] == 0):
                        j+=1
                        continue
                    if(alpha_dict[ord(s[j])] == 1):
                        j+=1
                        break
            i+=1
            
        return 0 if size == -float("inf") else size