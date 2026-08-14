class Solution:
    """
    Task: 
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        prefixPrd = []
        suffixPrd = []

        res = []
        n = len(nums)
        for i in range(n):
            prefixPrd.append(prefix)
            suffixPrd.append(suffix)
            prefix *= nums[i]
            suffix *= nums[n - 1 - i]

        for i in range(n):
            res.append(prefixPrd[i] * suffixPrd[n - 1 - i])
            
            
        return res
        