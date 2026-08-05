from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        p_dict = Counter(p)
        window_dict = {}

        found = 0
        have = 0
        need = len(p_dict)
        output = []
        i = 0
        j = 0

        for j in range(len(p)):
            window_dict[s[j]] = window_dict.get(s[j], 0) + 1
            if s[j] in p_dict and window_dict[s[j]] == p_dict[s[j]]:
                have+=1

        j+=1

        if have == need:
            output.append(i)

        while j < len(s):
            window_dict[s[j]] = window_dict.get(s[j], 0) + 1
            if s[j] in p_dict and window_dict[s[j]] == p_dict[s[j]]:
                have+=1

            if s[i] in p_dict and window_dict[s[i]] == p_dict[s[i]]:
                have-=1
            
            window_dict[s[i]] -= 1

            i+=1
            if have == need:
                output.append(i)
            j+=1

        return output

        