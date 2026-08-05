class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_dict = [0] * 26
        window_dict = [0] * 26
        for i in s1:
            s1_dict[ord(i) - ord('a')] += 1 

        for j in range(len(s1)):
            window_dict[ord(s2[j]) - ord('a')] += 1

        if window_dict == s1_dict:
            return True

        k = len(s1)
        
        for i in range(k, len(s2)):
            window_dict[ord(s2[i-k]) - ord('a')] -=1
            window_dict[ord(s2[i]) - ord('a')] += 1
            print(s1_dict, '\n', window_dict)
            if window_dict == s1_dict:
                return True

        return False