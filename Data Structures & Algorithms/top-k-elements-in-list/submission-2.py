from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency_map = defaultdict(int)

        for n in nums:
            frequency_map[n] += 1
        
        sorted_items = sorted(frequency_map.items(), key=lambda x: x[1], reverse=True)
        top_k_nums = [item[0] for item in sorted_items[:k]]

        return top_k_nums
        
