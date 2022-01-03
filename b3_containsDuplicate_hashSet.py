class Solution:
    def containsDuplicate(self, nums):
        sortedNums = sorted(nums)
        numSet = set()
        
        for n in nums:
            if n in numSet:
                return True
            else:
                numSet.add(n)
                
        return False
