class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        right_get_left = {"}": "{", ")": "(", "]":"["}
        left_parens = {"{", "(", "["}
        right_parens = {"}", ")", "]"}
        stack = []
        
        for char in s:
            if char in left_parens:
                stack.append(char)
            elif char in right_parens:
                if not stack or stack.pop() != right_get_left[char]:
                    return False
        if stack:
            return False
        return True