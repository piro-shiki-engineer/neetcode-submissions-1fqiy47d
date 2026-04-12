class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
         non-decreasing order → 昇順
         アルゴリズム全体としての空間計算量は1になるように
         双方向から探索
         ソートされてい流ことから探索アルゴリズムも利用可能
        '''
        left, right = 0, len(numbers)-1 

        while left < right:
            curNum = numbers[left] + numbers[right]

            if curNum > target:
                right -= 1
            
            elif curNum < target:
                left += 1
            else:
                return [left+1, right+1]

class Solution:
    """
    Task: Find 1-dices pair such that they add up to given the traget value.

    Input numbers is sorted in increasing order
    We cant use the same value fo number, that means there are no duplicate nubmers.

    So let me describe some example to clarify this problem.

    Input: numbers = [-1,2,3,4,8], target = 6 Output: [1,2] Can see my whiteboard ?
    
    (1, 5) remain = target - nums[left] = 7 < nums[5] = 8
    (2, 5) remain = target - nums[left] = 5 < nums[5] = 8
    (2, 4) remain = target - nums[left] = 4 == nums[right] = 4
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1

        while left < right:
            remain = target - numbers[left]
            
            if remain == numbers[right]:
                return [left+1, right+1]
            elif remain > numbers[right]:
                left += 1
            else:
                right -= 1
        
