class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        subStr = ""
        
        for char in s:
            subStr += char
            repetitions = int(l / len(subStr))

            if l%len(subStr) == 0 and repetitions!=1:
                
                constructedStr = repetitions*subStr
                
                if (constructedStr == s):
                    return True
                
        return False
    
