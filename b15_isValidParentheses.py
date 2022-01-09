class Solution:
    def validParentheses(self, s):
        stack = []

        for c in s:
            # if a left bracket is found, add to stack so we can compare with rights found in future
            if self.isLeft(c):
                stack.append(c)
                
            else:
                # if we get to a right bracket and there's no left one in stack, false
                if len(stack)==0:
                    return False

                # get left bracket and compare to current right bracket
                left = stack.pop()

                if left=="(":
                    if c!=")":
                        return False
                if left=="[":
                    if c!="]":
                        return False
                if left=="{":
                    if c!="}":
                        return False

        # At the end, the stack should be empty bc all left pairs should pop off to match the rights
        if len(stack)!=0:
            return False

        return True

    def isLeft(self, c):
        return c=="(" or c=="{" or c=="["

s = Solution()
print("expected: True, actual: ", s.validParentheses("()"))
print("expected: True, actual: ", s.validParentheses("()[]{}"))
print("expected: False, actual: ", s.validParentheses("(]"))
