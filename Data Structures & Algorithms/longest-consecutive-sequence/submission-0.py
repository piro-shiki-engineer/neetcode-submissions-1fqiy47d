class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        この回答では確かに回答を得ることができる最悪時間計算量を考えるとO（N）になるとは限らないのでは→一つ目のif条件式で担保している
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