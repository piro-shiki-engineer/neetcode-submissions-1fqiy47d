from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency_map = defaultdict(int)

        for n in nums:
            frequency_map[n] += 1
        
        sorted_items = sorted(frequency_map.items(), key=lambda x: x[1], reverse=True)
        top_k_nums = [item[0] for item in sorted_items[:k]]
        
        return tok_k_nums

class Solution:
    """
    Task: Return k most frequent elements within array

    So, what's the range of the element of input arrays, There are possibilitis to exist negative integers
    → Yes

    let me clarify by using some examples.
    Just count up by using HashMap key is unique value in array and value is intger as freq

    So, How to know the top k freaquent number ?
    Thinking simply, sorted keys by using freaquency value and use the result and extract top k elements.

    Time: O(nlogn) N is the toltal uniqu nubmers in input array

    it's ok to output in any order.
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freaq = {}

        for num in nums:
            if num not in freaq:
                freaq[num] = 0

            freaq[num] += 1

        sorted_freaq = sorted(freaq.items(), key=lambda x: -x[1])
        
        top_k = []
        for i in range(k):
            top_k.append(sorted_freaq[i][0])
        
        return top_k



        
