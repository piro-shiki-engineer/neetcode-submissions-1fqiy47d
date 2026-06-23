class Solution:
    """
    Task: Check if the input string are met folloing the conditions.

    """
    def checkValidString(self, s: str) -> bool:
        minLeft = 0
        maxLeft = 0

        for i in range(len(s)):
            if s[i] == "(":
                minLeft += 1
                maxLeft += 1

            elif s[i] == ")":
                minLeft -= 1
                maxLeft -= 1

            else: # s[i] == "*"
                minLeft -= 1
                maxLeft += 1
        
            if maxLeft < 0:
                return False
            if minLeft < 0: # *によって(が)よりも多い状態になっている、*はempty stringでよかったため0で正しい状態に戻す
                minLeft = 0

        return minLeft == 0
