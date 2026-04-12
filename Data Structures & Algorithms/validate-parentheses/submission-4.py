class Solution:
    def My_isValid(self, s: str) -> bool:
        """
        Time Complexity: O(N*3) → O(N)
        Space Compexity: O(3) → O(1)
        """
        if len(s) % 2 == 1:
            return False

        open_bracket = ['(', '[', '{']
        closed_bracket = [')', ']', '}']

        stack = [] # index

        for i in range(len(s)):
            if s[i] in open_bracket:
                index = open_bracket.index(s[i])
                stack.append(index)
            elif s[i] in closed_bracket and stack:
                index = stack.pop()
                if closed_bracket[index] != s[i]:
                    return False
            else:
                return False
        
        return True if not stack else False

    def isValid(self, s: str) -> bool:
        """
        We can make my solution efficiently by using HashMap
        By using HashMap, you can access to branck directly.

        Time Complexity: O(N*1) → O(N)
        Space Compexity: O(N/2) → O(N)
        """
        if len(s) % 2 == 1:
            return False

        close_to_open = {")" : "(", "]" : "[", "}" : "{"}
        stack = [] 

        for char in s:
            if char in close_to_open:
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:                
                stack.append(char)
    
        return True if not stack else False
    