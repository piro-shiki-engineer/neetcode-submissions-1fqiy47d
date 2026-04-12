class Solution:
    def isValid(self, s: str) -> bool:
        """
        Time Complexity: O(N*3) → O(N)
        Space Compexity: O(N/2) → O(N)
        """
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