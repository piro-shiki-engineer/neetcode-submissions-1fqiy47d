class Solution:
    """
    """
    def permute(self, nums: List[int]) -> List[int]:
        self.res = []
        self.backtrack([], nums, [False] * len(nums))

        return self.res

    def backtrack(self, perm: List[int], nums: List[int], pick: List[bool]) -> None:
        if len(perm) == len(nums):
            self.res.append(perm.copy())
            return
        
        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(perm, nums, pick)
                pick[i] = False
                perm.pop()
    
    def permute_my(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur: List[int], remain: List[int]):
            if not remain:  # remain が空になったら終了
                res.append(cur.copy())
                return

            for i in range(len(remain)):
                # remain[i]を選んで、残りで再帰
                cur.append(remain[i])
                dfs(cur, remain[:i] + remain[i+1:]) # スライスを使うと少し遅い→boolで管理した方いい
                cur.pop()
        
        dfs([], nums)
        return res