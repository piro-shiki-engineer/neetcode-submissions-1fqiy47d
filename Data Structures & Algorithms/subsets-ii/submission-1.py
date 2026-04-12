class Solution:
    """
    Task: all subsets

    input: List[int] nums which contains duplicates

    How to handle duplicats value → if the same value, just skip and add the inex 1

    subsetに含めたい時はただindex(pointer)をすすめればいい

    Time Complexity: O (n*2^n) 含めるか含めいないかの2通りの要素がN個あるから また要素のコピーはO（n）
    """

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []
        def dfs(index: int, subset: List[int]):
            if index == len(nums): # all element considered
                res.append(subset.copy())
                return
            
            subset.append(nums[index]) #includet the value
            dfs(index + 1, subset)
            subset.pop() # not includeing the value

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1

            dfs(index + 1, subset)

        dfs(0, [])
        return res