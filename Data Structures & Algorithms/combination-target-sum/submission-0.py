class Solution:
    """
    distinct equals to no duplicates

    Task: Return all combinations which total equals to target 
    we cant use same value

    Idea: Using back tracking algorithm

    we want to managae each combination, and total of combinations:
    if we add the value to temporary array, and update total.
    if total equals to target save the combinattion to global array.
    and if total is strictly bigger than target, stop after the traversal.
    In other words, just stop the dfs traversal.

    # Backtrakingで重要なのは、適切な選択の枠組みを設計すること
    """
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i, cur_cb, total):
            if total == target:
                res.append(cur_cb.copy())
                return

            for j in range(i, len(nums)): # 複数の選択をためす
                if total + nums[j] > target: # we dont need to check more bigger value
                    return
                
                cur_cb.append(nums[j])
                dfs(j, cur_cb, total + nums[j])
                cur_cb.pop()
        dfs(0, [], 0)
        return res
