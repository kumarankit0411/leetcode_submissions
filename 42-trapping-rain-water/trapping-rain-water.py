class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        self.pmax = [0] * n
        self.smax = [0] * n

        self.pmax[0] = height[0]
        self.smax[n-1] = height[n-1]
        
        #create prefixMax array
        for i in range(1, n):
            if(height[i] > self.pmax[i-1]):
                self.pmax[i] = height[i]
            else:
                self.pmax[i] = self.pmax[i-1]    

        #create suffixMax array
        for i in range(n-2, -1, -1):
            #print(height[i], self.smax[i+1])
            if(height[i] > self.smax[i+1]):
                self.smax[i] = height[i]
            else:
                self.smax[i] = self.smax[i+1]       

        sumWater = 0

        for i in range(0, n):
            water = min(self.pmax[i], self.smax[i]) - height[i]
            sumWater += water

        return sumWater