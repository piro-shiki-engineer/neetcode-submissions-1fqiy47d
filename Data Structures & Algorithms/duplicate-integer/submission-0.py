class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set() 
        
        for num in nums:
            if num in hashset: # 集合に含まれているか判定
                return True
            hashset.add(num)
        
        return False