import heapq

class Solution:
    """
    Task: The List that contains unique top k frequent elements

    First Idea:
    1. Count the how many numbers in a given array by using HashMap key is a number, value is how many O(n)
    2. Get the list sorted by HashMap.values 
    3. Return the k elements from sorted list

    Count O(n)
    O(mlogm) m is the the total of uniques
    O(k)

    O(n) + O(nlogn) + O(k)

    minHeap, the lenght of this is limetd k
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1
            
        for n, c in count.items():
            freq[c].append(n)
            
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
    def topKFrequent_myans(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        minHeap = []

        for n in nums:
            count[n] += 1
            
        for n, freq in count.items():    
            heapq.heappush(minHeap, [freq, n])
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        
        return [element[1] for element in minHeap]