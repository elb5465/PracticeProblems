class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        if l == 1:
            return 0
        
        # initialize arrays
        prod  = [0]*l
        left  = [0]*l
        right = [0]*l
        
        # intialize leftmost and rightmost values to 1 since no values are outside of those
        left[0]    = 1
        right[l-1] = 1
        
        #go forward and multiply each element of nums array by prev product of last left element
        for i in range(1, l):
            left[i] = nums[i-1] * left[i-1]
            
        #go backward and multiply each element of nums array by prev product of last right element
        for j in range(l-2, -1, -1):
            right[j] = nums[j+1] * right[j+1]

        for k in range(l):
            prod[k] = left[k] * right[k]

        return prod
