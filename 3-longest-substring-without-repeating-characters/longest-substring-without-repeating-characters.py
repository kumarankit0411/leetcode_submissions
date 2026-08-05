class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        longest = -float('inf')

        i = 0
        s_dict = {}
        j = 0
        for j in range(len(s)):
            # if s[j] already exist in dict, we found duplicate, increment i
            if s[j] in s_dict:
                end = s_dict[s[j]]
                while(i <= end):
                    s_dict.pop(s[i], None)
                    i+=1

            s_dict[s[j]] = j

            if j - i + 1 > longest:
                longest = j - i + 1

        return longest
            

        
        # i = 0
        # j = 0
        # size = -float("inf")
        # alpha_dict = [-1] * 256

        # # for m in range(len(s)):
        # #     alpha_dict[ord(s[i])] += 1
        # #     if(alpha_dict[ord(s[i])] == 1):
        # #         size = max(size, i-j+1)
        # #         i+=1
        # #         continue
        # #     if(alpha_dict[ord(s[i])] == 2):
        # #         while(True):
        # #             alpha_dict[ord(s[j])] -= 1
                    
        # #             if(alpha_dict[ord(s[j])] == 0):
        # #                 j+=1
        # #                 continue
        # #             if(alpha_dict[ord(s[j])] == 1):
        # #                 j+=1
        # #                 break
        # #     i+=1
        # for m in range(len(s)):
        #     # alpha_dict[ord(s[i])] == i
        #     print(s[i])
        #     if(alpha_dict[ord(s[i])] == -1):
        #         size = max(size, i-j+1)
        #         i+=1
        #         continue
        #     else:
        #         while(True):
        #             alpha_dict[ord(s[j])] = -1
                    
        #             if s[j] == s[i]:
        #                 j+=1
        #                 break
        #             j+=1
        #         # j = alpha_dict[ord(s[i])] + 1
        #         # while(True):
        #         #     alpha_dict[ord(s[j])] -= 1
                    
        #         #     if(alpha_dict[ord(s[j])] == 0):
        #         #         j+=1
        #         #         continue
        #         #     if(alpha_dict[ord(s[j])] == 1):
        #         #         j+=1
        #         #         break
        #         i+=1

            
        # return 0 if size == -float("inf") else size