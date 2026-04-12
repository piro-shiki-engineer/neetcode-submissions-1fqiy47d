class Solution:
    """
    return all unique combinations which sum equals to target
    each combinations can contain duplicates values.

    I think we can use backtracking, maybe.
    So, we need to make disitions that what value add to temporary comnbinations array
    I should do the preprocess like remove duplicates in candidates and sorted

    After that, we should code up the process what values add to temporary comnbination's array
    There are some cases, added or not.
    I want to use dfs for checking every cases. If nums[0] or nums[1], something like that

    重複値をもつlist内から重複した値を避けるには
    ソートし前後の値を比較しながら参照すること
    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i: int, cur_cb: List[int], total: int):
            if total == target:
                res.append(cur_cb.copy())
                return
    
            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    break

                # 同じ値を含んでしまうと重複が発生する可能性がある
                if j > i and candidates[j] == candidates[j-1]: 
                    continue

                cur_cb.append(candidates[j])
                dfs(j+1, cur_cb, total + candidates[j])
                cur_cb.pop() 
            
        dfs(0, [], 0)
        return res