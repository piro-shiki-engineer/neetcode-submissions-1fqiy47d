class Solution:
    '''
    今回はソートされていない配列が与えられている
    '''
    def threeSum_v1(self, nums: List[int]) -> List[List[int]]:
        '''
        Brute Force(総当たり)
        Time Complexity O(N**3), Space Complexity O(N)
        '''
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(tmp)) # ここでは集合に対して足すことで、重複を回避

        return [list(i) for i in res] # 最終的には求められている出力形式に変

    def threeSum_hashMap(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = defalutdict(int)
        for num in nums:
            count[num] += 1

        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(tmp)) # ここでは集合に対して足すことで、重複を回避

        return [list(i) for i in res] # 最終的には求められている出力形式に変

class Solution:
    """
    Task: Return the triples such that they add up to 0

    constrain:
    - output have no duplicates triplets.
    
    At this moment, I come up with BruteForce.
    Time: O(N^3) N is the length of Input array.

    So lem me clarify this proble by using some examples.

    nums[i] + nums[j] + nums[k] == 0 (i != j != k)
    nums[i] + nums[j] = -num[k] as target (i < j < k)

    Just the target O(n^2)

    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = nums[left] + nums[right] + nums[i]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left-1] == nums[left]:
                        left += 1

        return triplets







