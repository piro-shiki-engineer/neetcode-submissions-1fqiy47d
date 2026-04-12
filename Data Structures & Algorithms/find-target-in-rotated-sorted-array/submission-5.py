class Solution:
    """
    simple: Linear search until finding target or reatch last index

    In the explanation, it say that nums been roated n times.
    but we need think another properties are givein in the setences.

    input array is sorted in asceding order.
    so, we can use binary search. 
    and I think the key point is that we can seperate given array to 2 array with point that is unsorted.

    lets think the example 1.

    Input: nums = [3,4,5,6,1,2], target = 1

    left, right that are used for checking range. if left = 0, right =2, serching range is [3,4,5] without the after [6, 1, 2]

    To find the target's index, I want to set (left, right) = (0, 5).
    In this case, center index between them is middle = (0 + 5) // 2 = 2
    The value is 5 at middle index, it is smaller than target.
    So, we need update searching range.

    if nums[middle] >= nums[target]: the target's index maybe exist the righter partion.
    so, we need to update like this left = m + 1
    
    else: right = m - 1
    """
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            
            if nums[left] <= nums[middle]:
                if target > nums[middle] or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1 

            else:
                if target < nums[middle] or target > nums[right]:
                    right = middle - 1
                else:
                    left = middle

        return -1