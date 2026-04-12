class Solution:
    """
    Detect the dupulicate
    sort arrays in increasing or dereasing order.
    
    simple solution is just using Hash set.
    But, extra space is O(N). N is length of nums
    """
    
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


    