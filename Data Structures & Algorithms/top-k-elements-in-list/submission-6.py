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

    O(n) + O(mlogm) + O(k)

    minHeap, the lenght of this is limetd k
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        minHeap = []

        for n in nums:
            count[n] += 1
            
        for n, freq in count.items():    
            heapq.heappush(minHeap, [freq, n])
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        print(minHeap)
        return [element[1] for element in minHeap]
        