class Solution:
    """
    Task: Return the maximum amount of money you can rob without alerting

    So, let's more clarify this problem, by using examle2
    Maybe, we should take care of the houses are arranged in a circle.

    I think we should manage the index to judging the end list.

    if

    
    Example 2.
    Input: nums = [2,9,8,3,6] Output: 15

    """
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
