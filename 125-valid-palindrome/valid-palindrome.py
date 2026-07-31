class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i = 0

        new_s = ''

        for c in s:
            if c.isalnum():
                new_s = new_s + c.lower()

        print(new_s)

        j = len(new_s) - 1 

        while(i<=j):
            ## happy case
            if(i==j or i > j):
                return True
            
            # non happy case
            if (new_s[i] != new_s[j]):
                return False

            i+=1
            j-=1

        return True