class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # time O(N^2) space(1) → N is lnegth of nums
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if target - nums[i] == nums[j]:
                    return [i, j]
        return []

        # initialize hashMap
        # hashMap = {}
        # for i in range(len(nums)):
        #     if nums[i] in hashMap.keys():
        #         return [hashMap[nums[i]], i, ]
        #     hashMap[target - nums[i]] = i
        
        # return []

        
        
                
        