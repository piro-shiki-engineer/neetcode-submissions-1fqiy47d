class Solution:
    """
    Task: return the maximum amount of money you can rob without alerting
    SO, I want more clairy this problem, let desribing Example2.

    Input: nums = [2,9,8,3,6] Output: 16
    at this moment, i gonna use 0-based index.

    if I chose the i = 0 we can also rob from i=2, 3, 4 without i+1, i-1
    Acoridingly this sample, There are some option.
    We can the make the desition tree, and it's possible to reuse the result that I already checked the options.

    So let draw down in IPAD.

    Initially, We can choose any index.

    if we pick up one house to get moneny, we neet to make desition which

    Why I cant solve this ?
    - cant break down into subproblems 
        if choose i=0, we need to search the another i+2 sub problem
        if skip i=0, we need to search the another i+1 sub problem
    - I misunderstand "he ith house is the neighbor of the (i-1)th and (i+1)th house."
        I should thik more simple, like if I choose i, we need solve i+2 sub poblem

    rob1: 「2つ前まで」の最大盗取額
    rob2: 「1つ前まで」の最大盗取額
    temp: 「現在まで」の最大盗取額
    """
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ...]
        for num in nums:
            temp = max(
                num + rob1, # add to this house, previous result 
                rob2
            )
            rob1 = rob2
            rob2 = temp

        return rob2
