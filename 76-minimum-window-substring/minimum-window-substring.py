from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not(s) or not(t) or len(s)<len(t):
            return ''

        t_dict = Counter(t)
        window_dict = {}

        have = 0
        need = len(t_dict)

        res_i = -1
        res_j = -1
        res_len = float('inf')

        i = 0
        for j in range(len(s)):
            char = s[j]
            window_dict[char] = window_dict.get(char, 0) + 1

            if char in t_dict and window_dict[char] == t_dict[char]:
                have += 1
                
            while (have == need):
                if (j-i+1) < res_len:
                    res_len = j - i + 1
                    res_i = i
                    res_j = j

                left_char = s[i]
                window_dict[left_char] -=1

                if left_char in t_dict and window_dict[left_char] < t_dict[left_char]:
                    have -= 1

                i+=1

        return s[res_i: res_j+1]