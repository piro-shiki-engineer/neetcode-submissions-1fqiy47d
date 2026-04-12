class Minheap:
    def __init__(self, size: int):
        self.minHeap = [None] * size

class KthLargest:
    """
    stream: ここでいうstreamは値を追加し続けること

    方針1：
    新しく値が入るたびにsortしてk番目に大きい値を取得すること

    方針2：
    Min-heap of size k: サイズKの最小値ヒープを利用することt
    add/pop: Time O(logk) k is size of min heap
    get min: O(1)

    total time: O(m*logk) m is the number of  calls add() 

    Why is the size of min heap k?
     → stay conditons like top of minheap is k th largest in values

    """
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
    def add(self, val: int) -> int:
        """
        After adding, fucntion return the new kth largest number
        """
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) # guruntee size k of heap
        return self.minHeap[0] # k th largest equal to minmum value in heap, so thats top