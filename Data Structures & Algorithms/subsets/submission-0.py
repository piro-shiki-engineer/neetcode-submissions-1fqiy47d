class Solution:
    """
    Idea1: BruteForce
    Time: O(n * 2^n)

    Idea2:
    subsets: no contain duplicate,
    not permutation (which is contained duplicate)

    Desition Tree: Choose the each option, and repeat each option cases
    決定木：今回の場合はその要素をいれるか、入れないかの選択をnumsの繰り返す
    探索方法ははDFSが説明しやすい
    補足
    この決定木では各レベル(ルートを除く）でみるとそのようさの各要素について考えていることにもなる
    
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = [] # stack
        def dfs(i):
            if i >= len(nums): # 元の要素数以上なら終了→ 0-indexだから
                res.append(subset.copy()) # 結果を保存
                return 

            # decisiotn to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decisiotn NOT to include nums[i], so back to previous subset
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
