class Solution:
    """
    Task:

    Count how many number we have by using hashmap key is the number and value is the frequency
    How we find the minimum value from hashmap, we need to to use another data structure called Min Heap

    Why I fail ?
    - Misunderstand that like I neet to find at least one group fullfill the requirements.
    """
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = {}

        for num in hand:
            count[num] = 1 + count.get(num, 0)

        minHeap = list(count.keys())
        heapq.heapify(minHeap)
        
        while minHeap:
            first = minHeap[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                
                count[i] -= 1
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)

        return True