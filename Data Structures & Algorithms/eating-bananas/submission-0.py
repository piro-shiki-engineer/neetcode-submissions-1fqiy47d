class Solution:
    """
    k = how many bananas you can eat per h(hour)
    total bananas you cant eat is k * h

    first, I want to think th exe1
    Input: piles = [1,4,3,2], h = 9

    min_k = float('inf')
    h = 9, piles = [1, 4, 3, 2]
    k = 1, total time = round_up(1, 1) + round_up(4, k) + round_up(3, k) + round_up(2, k) = 10 > h it's bad time for requinrements.
    k = 2(minmum), tolta_time = round_up(1, 2) + round_up(4, 2) + round_up(3, 2) + round_up(2, 2) = 5 < h it's bad time for requinrements.
    k = 3 tolta_time = round_up(1, 3) + round_up(4, 3) + round_up(3, 3) + round_up(2, 3) = 5 < h it's bad time for requinrements.
    k = 4(maxmum) tolta_time = round_up(1, 4) + round_up(4, 4) + round_up(3, 4) + round_up(2, 4) = 4 < h it's bad time for requinrements.

    """
    def round_up(self, x: int, devide_num: int) -> int:
        return (x // devide_num) + (1 if x % devide_num > 0 else 0)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_k = max(piles)

        while l <= r:
            k = (l + r) // 2
            total_time = sum([self.round_up(pile, k) for pile in piles])
            
            if total_time <= h:
                min_k = min(k, min_k)
                r = k - 1 
            else:
                l = k + 1
            
        return min_k



    

