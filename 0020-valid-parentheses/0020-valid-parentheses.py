class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                # If it's a closing bracket
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        return not stack
        