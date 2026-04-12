class Solution:
    """
    Task: Check if it's posible to construct 2 subsets and the total subset1 are equal to total subset2

    Input array is not sorted.
    Input array have duplicates value.

    All patern we can construct all subsets and copare the result.
    Let's clarify this problems by using bellow exampls
    Input: nums = [1,2,3,4,2] → [1, 2, 3] and [2, 4] Output: true
    
    This is maybe bruteforce, let me describe it 

    Solution
    Initialize total1 = 0 total2 = 0
    Make disiton:
        - adding index-0 element to total1 that is meaing subset1 containg the value as element
        - adding index-0 element to total2 that is meaing subset2 containg the value as element
    
    Call the recursive fucntin in each situation. if the either option1 and option2 reuturing ture, parent result is also true.

    

    """
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(total1, total2, index, memo):
            print(total1, total2, index)
            
            
            if (total1, total2) in memo:
                return memo[(total1, total2)]
            if index == len(nums):
                return total1 == total2
            
            memo[(total1, total2)] = dfs(total1 + nums[index], total2, index + 1, memo) or dfs(total1, total2 + nums[index], index + 1, memo)
            return memo[(total1, total2)]

        return dfs(0, 0, 0, {})


        