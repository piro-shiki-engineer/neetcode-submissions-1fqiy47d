class Solution:
    """
    Task: Return the indices i and j such that nums[i] + nums[j] == target.

    constrains:
    - return smaller index first
    - every input has exactly one pair satify the conditins

    Sol1: BruteForce
    i to len(nums), j is i + 1 to len(nums) right ?

    Time: O(n^2)
    Space: O(1)

    Sol2: HashMap
    nums[j] = target - nums[i]

    for example,  nums = [3, 4, 5, 6] target = 7

    if the index 0 is the index i, nums contains target - nums[0]

    Time: O(n), Space: O(n)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {} # key: target - nums[i], value: i 

        for i, n in enumerate(nums):
            if n in hashMap:
                return [hashMap[n], i]
            
            hashMap[target - n] = i

