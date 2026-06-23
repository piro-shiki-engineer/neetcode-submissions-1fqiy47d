class Solution:
    """
    Task: Retunr the number which appears once in the input array

    We should need to implement Time O(n) and Space O(1) the solution 
    → I want to thin this problem more easily. I forgot this constaring at this moment
    → After getting the simple but not efficient solution, I want to think this constrain

    Lets think some examples for clarifing this problem.
    First my idea is just simple, manage the value which appears or not by using hashset
    """
    def singleNumber(self, nums: List[int]) -> int:
        """
        Best solution
        By using XOR (eXclusive OR), we can make solution memory less.

        we can express the XOR by ugins "^" opperation between a and b. 
        """
        res = 0
        for num in nums:
            res = res ^ num
        return res

    def singleNumber_my(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(n)
        """
        hashSet = set()
        res = None
        for num in nums:
            if num not in hashSet:
                res = num
            hashSet.add(num)
            
        return res    