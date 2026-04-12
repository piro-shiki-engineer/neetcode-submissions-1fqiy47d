class Solution:
    """
    Task: Return the maximum length of the array which each element are exacly 1 greater than the previous element

    I wonder if there are same value or not. The array contains duplicates value ?
    → I gonna think there are same values.

    I want to think some examples to clarify more this problem.

    Example1: Input: nums = [5, 4, 3, 4, 5, 7, 2], Output: 3

    (0, 1) 5 > 3 より left = right, right += 1
    (1, 2) 4 > 3 より left = right, right += 1
    (2, 3) 3 < 4 より maxLength = max(1, 3 - 2 + 1) = 2, right += 1
    (2, 4) 4 < 5 より maxLength = max(2, 4 - 2 + 1) = 3, right += 1

    (2, 5) 7 - 5 = 2 > 1 より, left = 5, right += 1
    (5, 6) 7 > 2 より, left = 5

    Require:
    We need to write function which time complexity is O(N)

    Why I cant solve ?
    Do not read problem sentence accurately.
    → Actually, the sentences is " The elements do not have to be consecutive in the original array."
    → Because this misunderstanding, I also make another mistake, the mistake is that element have same values.
    → In actual interview, I need to check the examples are fit in the problem context.

    Do not visualize
    → 数直線で表現すればよりわかりやすく考えられた。
    今回の問題ではどのようにシーケンスとしての先頭を見つけるかが重要である。

    """
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        maxLength = 0

        for num in nums:
            # chekck if nums is a start of the sequence.
            if (num - 1) not in numSet:
                # initialize length
                length = 0
                while (num + length) in numSet:
                    length += 1

                maxLength = max(maxLength, length)
        
        return maxLength
