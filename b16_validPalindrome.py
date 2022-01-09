class Solution:
    def isPalindrome(self, s):
        newStr = ""
        for c in s:
            if c.isalpha():
                newStr += c
                
        newStr = newStr.lower()
        return newStr[::-1] == newStr
    


s = Solution()
print("expected: True, actual: ",   s.isPalindrome("A man, a plan, a canal: Panama"))
print("expected: False, actual: ",  s.isPalindrome("Hello there"))
print("expected: True, actual: ",   s.isPalindrome("aBabA"))
