class Solution:
    """
    Task: Return the largest sum value which is consisted by contiguous elments in the input array

    Lets think some examples for clarifying this promblem.

    Exampel 1.
    Input1: [1, -1, 1, 1, -2, 4]
    Output1: 5

    Let me describe how I get the largest sum
    (i)Just iterate throught the input array while comparing adding the element or not for each steps.
    (ii)Before you move next element largest sum which is possibele to being the answer or current max ith 
    
    Key words: "contiguous subarray" and "max sun"
    """
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        curr = 0
        
        for num in nums:
            if curr < 0: # to reset subarray range
                curr = 0
            curr += num
            ans = max(ans, curr)

        return ans
        