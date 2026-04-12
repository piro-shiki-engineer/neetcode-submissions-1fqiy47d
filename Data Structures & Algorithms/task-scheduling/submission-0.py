from collections import defaultdict

class Solution:
    """
    Count up unique alphabet and record the number of occuracies(オ・カーレンシー)in tasks.
    
    Space: O(26) → O(1)
    Time: O(n) n is the length of array

    I'm going to use heap which build-in function in python.
    In python we can use only min heap, so we need to multiply negative 1 to occurencies.

    1つのタスクのアイドル時間（待機時間）をキューで管理する

    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        occurrenceis = defaultdict(int) # valueの型指定
        for task in tasks:
            occurrenceis[task] += 1
        
        maxHeap = [-value for value in occurrenceis.values()]
        heapq.heapify(maxHeap)

        time = 0 # global clock in shceduler
        q = deque()
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap) # Actually, decrease 1 time to occurencies
                if cnt: # not 0
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time: # 待機時間が完了したら
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
            


        
        