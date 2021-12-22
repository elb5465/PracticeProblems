class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0 
        iDict = {'l':10000000, 'c':10000000, }
        j = len(nums)-1
        
        while j-i >= 1:
            print(i, j)
            
            
            i += 1
            j -= 1
            
