class Solution:
    """
    a car fleet is meaning that the group of cars like same speed

    Ex 1.
    target = 10
    car_i = (positon_i, speed_i)
    time_to_destination = [10-position//i, ,　10-3//1]
    time = 0 sorted_by_position_cars = [(0,1), (1,2), (4,2), (7,1)]
    time = 1 sorted_by_position_cars = [(1,1), (3,2), (6,2), (8,1)]
    time = 2 sorted_by_position_cars = [(2,1), (5,2), (8,2), (9,1)]
    time = 3 sorted_by_position_cars = [(3,1), (7,2), (10,2), (10,1)] res = 1
    time = 4 sorted_by_position_cars = [(4,1), (9,2), (10,2), (10,1)] res = 1
    time = 5 sorted_by_position_cars = [(5,1), (10,2), (10,2), (10,1)] res = 2
    ...
    time = 10 sorted_by_position_cars = [(10,1), (10,2), (10,2), (10,1)] res = 3
    """
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pairs = [(position, speed) for position, speed in zip(position, speed)]
        pairs.sort(reverse=True) # O(nlogn) 降順にソート(ポジション的にターゲットに近い車順)
        stack = []
        for position, speed in pairs:
            stack.append((target - position) / speed)
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # 所要時間が前の車より短い
                stack.pop()
    
        return len(stack)

