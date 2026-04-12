class Solution:
    '''
    今回はソートされていない配列が与えられている
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(tmp)) # ここでは集合に対して足すことで、重複を回避

        return [list(i) for i in res] # 最終的には求められている出力形式に変換

# nums[i] + nums[j] + nums[k] = 0

# nums[i] = -1 * (nums[j] + nums[k]) O