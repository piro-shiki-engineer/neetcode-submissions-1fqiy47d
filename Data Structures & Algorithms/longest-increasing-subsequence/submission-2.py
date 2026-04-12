class Solution:
    """
    Task: Find the the longest strictly increasing order subsequence

    Strictly increasing order means if there are same two numbers, we should judge it's not increasing order.

    I gonna use the desition tree. Lets calrify the problem by using examples bellow
    Input: nums = [1,4,2,6,3] Ouput: 3
    In this describing node is strictly bigger than parent node value.
    So, If the children nodes arenot match this, I just dont write as node

    I want added to input array's head -1001 because I dont want write handling code for first and keep simple the computation logic
    Why -1001 because the minimum value of element is -1000 

    nums = [-1000, 1,4,2,6,3] Of corse, I should forget the result length actully the length -1
    
    Arlight, So we check if the element you can use the children node is not the parent's problem, thas next subproblems of children.
    If the input nums without any candidates as chilren, return 1 as the resutl and this is the base case
    how to determine the parent node result is maximum length children result + 1.
    
    The root node is just. I set the
    Without memo: Time: O(2^N) N is the length of input array Space: O(N)
    With: Time: O(N^2) N is the length of input array Space: O(N)
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums = [-1001] + nums
        def dfs(curr: int, memo: Dict[int]) -> int:
            if curr in memo:
                return memo[curr]
            
            if not nums[curr + 1:]:
                return 1
            
            childResult = 0
            for child in range(curr +1 , len(nums)):
                if nums[child] > nums[curr]:
                   childResult = max(childResult, dfs(child, memo))

            memo[curr] = childResult + 1
            return childResult + 1

        return dfs(0, {}) - 1
