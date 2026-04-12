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
        if len(nums) == 1:
            return nums[0]
            
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]
