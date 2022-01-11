# my bruteforce solution passed 315 / 318 tests on LeetCode, but could have been improved by sorting the list, 
#    having one pointer in the beginning, one directly after that, and another at the very end. Since the list is ordered, 
#    you could adjust the left and right pointer to be closer to eachother.
class Solution:
    def threeSumBruteForce(self, nums):
        l = len(nums)
        if (l<3):
            return []
        
        i = 0
        j = 1 
        k = 2
        
        numArr = []
        
        # do the 3 pointer iteration I did on amazon test
        while (i != l-2):
            if (nums[i]+nums[j]+nums[k] == 0) and (i != j and i != k and j != k):
                sortedTriplet = sorted([nums[i], nums[j], nums[k]])
                if (sortedTriplet not in numArr):
                    numArr.append(sortedTriplet)
            
            if (k == l-1):
                if (j == l-2):
                    i += 1
                    j = i + 1
                    k = j + 1
                else:
                    j += 1
                    k = j + 1
            else:
                k += 1
                
        
        return numArr

s = Solution()
print("expected: [[-1,-1,2],[-1,0,1]], actual: ", s.threeSumBruteForce([-1,0,1,2,-1,-4]))
print("expected: [[-1,-1,2],[-1,0,1]], actual: ", s.threeSumBruteForce([-1,0,1,2,-1,-4]))
print("expected: [], actual: ", s.threeSumBruteForce([]))
print("expected: [], actual: ", s.threeSumBruteForce([0]))
