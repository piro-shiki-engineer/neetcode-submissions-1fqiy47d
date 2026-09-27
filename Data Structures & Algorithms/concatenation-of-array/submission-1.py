class Solution:
    """
    input: array: List[int]

    There are capabilies given array have no elments. -> list must have interges as elments.

    Examples 1
    Input: nums = [1, 2, 5]
    Output: [1, 2, 5, 1, 2, 5]
    elements i = 0, 0 + 3 = 1
    elements i = 1, 1 + 3 = 2
    elements i = 2, 2 + 3 = 5

    Time: O(n), Space: O(2n)
    """
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)

        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans

        