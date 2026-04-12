class Solution:
    """
    input arrays is sorted
    return value means target value's index
    if target is not exsit , return -1

    we should think this example1
    nums = [-1,0,2,4,6,8], target = 4

    we want to separate input arrays into 2 arrays.
    and we should clarify which the target's value is belonged to right or left.
    how to clarify ? it's target > arrays[middle] or not
    if it's former, we should think right arrays.
    if it's later,  we should think left arrays.

    Input: nums = [-1,0,2,4,6,8], target = 3
    (0, 6) middle = (0+6) // 2 = 3 target > nums[middle] = 2
    (2, 6) middle = (2 + 6) // 2 =4 target < nums[middle] = 6
    (2, 4) middle 
    """
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        
        while left <= right:
            center = (left + right) // 2
            if nums[center] == target:
                return center
            elif nums[center] > target:
                right = center - 1 # centerの位置はすでに確認済みなので、次の探索範囲に含める必要がありません。
            else:
                left = center + 1 # centerの位置はすでに確認済みなので、次の探索範囲に含める必要がありません。
            
        return -1
