class Solution:
    """
    Task: Return True if there are duplicate like any appears more than once, if not return False
    
    How we check the duplicates? 
    
    My First idea is Couting how many numbers are appears by using Hash map
    Time: O(n) Space: O(n)

    Actually, Hash Set is more correct to check if there are duplicates

    英語: 日本語
    This sol needs the extra memory: この解法は追加でメモリが必要になる
    """
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Complexity
        Time: O(n) Space: O(n)

        n is the length of input array
        """
        hashSet = set()
        
        for num in nums:
            if num in hashSet:
                return True
            
            hashSet.add(num)
        
        return False
        