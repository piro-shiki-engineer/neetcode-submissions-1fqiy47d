class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Solution(1) time O(N^2) space O(1) → N is lnegth of nums
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if target - nums[i] == nums[j]:
        #             return [i, j]
        # return []

        # Solution(2) → time O(N), space O(N)
        hashMap = {}
        for i, n in enumerate(nums):
            if n in hashMap.keys():
                return [hashMap[n], i]
            hashMap[target - n] = i
        
        return []
