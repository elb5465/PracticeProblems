class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        n = len(nums)
        
        st = []
        for idx, num in enumerate(nums):
            # pop element from st if last element is greater than the current element
            # and also I have enough elements left such that I can have list of size k
            while st and st[-1] > num and (len(st)-1 + len(nums)-idx >= (n-k) ):  
                # len(st)-1, bcz that top element will be popped, we would have on eleemet less..and                    
                # len(nums) - idx will give the remaining elements, # including the current element!
                st.pop()
            if len(st) < (n-k):
                st.append(num)
        return str(int("".join(st))) if st else "0"
