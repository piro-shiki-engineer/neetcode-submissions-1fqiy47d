class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
         non-decreasing order → 昇順
         アルゴリズム全体としての空間計算量は1になるように
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
