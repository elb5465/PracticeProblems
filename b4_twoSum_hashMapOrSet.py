class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #BRUTE: O(n^2) solution is compare every integer in list together with 2 for loops

        ''' EFFICIENT: O(n) I believe could be achieved by keeping a set of nums visited, 
        subtracting the current from the target and checking if the difference is in the set already. 
        Then use list to track indexes. Or just use a hashmap / dictionary '''
        
        s = set()
        currIdx = 0
        
        for n in nums:
            if (target - n) in s:
                return [nums.index(target-n), currIdx]
            else:
                s.add(n)
            currIdx += 1
