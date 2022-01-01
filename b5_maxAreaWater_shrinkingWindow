class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # -------------------  BRUTE FORCE: O(n^2)  ------------------------
        l = len(heights)
        maxArea = 0
        
        for i in range(l):
            for j in range(l):
                end, start = heights[j], heights[i]
                length = j - i
                height = min(end, start)
                maxArea = max(height * length, maxArea)
                
        return maxArea
        
        # -------------------  MORE EFFICIENT: O(n)  ------------------------
        i = 0
        j = len(heights)-1
        maxWater = 0 
        
        while i != j:
            end, start = heights[j], heights[i]
            
            length = j-i
            height = min([start, end])
            area =  length * height
            
            maxWater = max(maxWater, area)
            
            if start < end:
                i += 1
            else:     
                j -= 1
                
                
        return maxWater
