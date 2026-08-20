class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        l = 1
        r = maxSum
        maxValue = l

        while l<=r:
            m = (l + r) // 2

            print(l, m, r)
            if self.isPossible(m, n, index, maxSum):
                l = m + 1
                if maxValue < m:
                    maxValue = m
            else:
                r = m - 1

        return maxValue

    def isPossible(self, m, n, idx, maxSum):
        li = idx
        nli = min(li, m-1)
        overflowsum_l = 0
        if li > m-1:
            overflowsum_l = li - m + 1 
        ri = n - idx - 1
        nri = min(ri, m-1)
        overflowsum_r = 0
        if ri > m-1:
            overflowsum_r = ri - m + 1 

        #left ap sum
        l_ap_sum = (nli * (2 * (m - 1) + (nli - 1) * -1)) // 2
        #right_ap_sum
        r_ap_sum = (nri * (2 * (m - 1) + (nri - 1) * -1)) // 2

        print(m, nli, l_ap_sum, nri, r_ap_sum)

        return l_ap_sum + r_ap_sum + overflowsum_l + overflowsum_r <= maxSum - m