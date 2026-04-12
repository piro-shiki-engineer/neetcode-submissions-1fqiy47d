class Solution:
    """
    tempertures = [30, 38, 30, 36, 35, 40, 28]

    i is current day's index
    j is feature day's index
    i < j, so we should think about the days after i th day
    i = 1 30 < j38 => result[i] = 1
    i = 2 38 > 
    
    all patterns => BuruteForce Time O(n^2), Space O(n)

    all patterns => if we think i th day, we dont need to think about the days before i th day 
    → O(n^2), Space O(n)


    

    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # the element is (i, temperture)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackIndex, stackTemp = stack.pop()
                result[stackIndex] = i - stackIndex
            stack.append((i, temp))
        
        return result
