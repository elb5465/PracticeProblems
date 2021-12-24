class Solution:
    def findPeakElement(self, nums):
        start = 0
        end = len(nums)-1

        while (start < end):
            mid = start + int((end - start) / 2)  
            if (nums[mid] < nums[mid+1]):
                start = mid+1
            else:
                end = mid

        return start
        
        

print("---------------------------------\n\n")
s = Solution()
print("answer: ", s.findPeakElement([1,2,3,1]), "expected: ", 2)
print("answer: ", s.findPeakElement([1,2,1,3,5,6,4]), "expected: ", 5)
