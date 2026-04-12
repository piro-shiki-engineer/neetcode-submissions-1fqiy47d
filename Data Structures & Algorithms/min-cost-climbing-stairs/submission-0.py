class Solution:
    """
    Task: get the mimimum cost to reach top

    if you're at the i th staircase, you can move either i + 1 th or i + 2th stairecase by paying each cost
    
    so let's clarify this problem by using example 2.

    top is the over the end of inputs list and cost is clrealy.
    but in this problem basically, if the index is out of bounds, we reach the top.

    We search from top like botom-up because I want to reuse the minimum cost to reach top

    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0) # define top is n + 1, and the cost is 0,
        n = len(cost)
        
        # and the cost from n to n+1 is also 0 because of the cost n+1 is 0, also n-1 is 0
        # we need to search from n-2(1-based inedx)
        for i in range(n-3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i+2])

        return min(cost[0], cost[1])