class Solution:
    """
    辞書順ソートされた配列numsが与えられる
    配列内の値は重複なし
    
    Input: nums = [3,4,5,6,1,2]
    Output: 1

    return minmum value in nums roated,

    simple solution is just linear serch. Time Complexity: O(n)

    nums = [3,4,5,6,1,2]
    (l, r) = (0、5) c = (nums[l] + nums[r]) // 2 nums[c] = 5
    
    if l == r: return nums[]
    nums[l] > mums[c] 
    nums[r] > mums[c] 

    わからなかったポイント：
    binary search の中間点の更新点のどの条件を利用すればいいかわからなかった
    """
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        res = nums[0]
        
        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
            
            middle = (left + right) // 2
            res = min(res, nums[middle])
            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1
        
        return res