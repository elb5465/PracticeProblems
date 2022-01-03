class Solution:
    def maxProfit(self, prices):
        low = 100000
        maxProfit = 0
        
        for p in prices:
            if p < low:
                low = p

            if p - low > maxProfit:
                maxProfit = p - low                
                
        return maxProfit


s = Solution()
print("answer: ", s.maxProfit([2,4,1]), "expected: ", 2)
print("answer: ", s.maxProfit([7,1,5,3,6,4]), "expected: ", 5)
print("---------------------------------\n\n")

