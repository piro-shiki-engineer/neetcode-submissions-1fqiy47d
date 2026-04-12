class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        この回答では確かに回答を得ることができる最悪時間計算量を考えるとO（N）になるとは限らないのでは→一つ目のif条件式やSetを使うことで担保している
        '''
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n-1) not in numSet: # 連続する数列の一番右であることの確認
                length = 1
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

    """
    Task: Get the length of lIC which is can be formed by using  given input array

    We should write time O(n) algo

    Hmnn, Let us clarify this problem by thinking some examples.

    Example1. In: [1,8,9,3,2] Out: 3

    If the value is 1, if the concective siequcen is madeby if there 1-0, 1+1.

    I want to HashMap the key is the value of element, value is the longest at this time,

    LIS is calculated like if i+1 or i-1 is in dict. dict[i] + 1
    After that we should update the length of dictp[num - total] and dict[num + total]
    The finally iterate throouhg for finding the max LIS in values in dict.
    """
    def longestConsecutive(self, nums: List[int]) -> int:

        hashMap = {}
        maxLen = 0

        for num in nums:
            if num not in hashMap:
                left = hashMap.get(num - 1, 0)
                right = hashMap.get(num + 1, 0)
                
                hashMap[num] = left + right + 1
                
                if left > 0:
                    hashMap[num - left] = hashMap[num]
                if right > 0:
                    hashMap[num + right] = hashMap[num]
                maxLen = max(maxLen, hashMap[num])
            
        # return max(hashMap.values()) if hashMap else 0
        return maxLen
