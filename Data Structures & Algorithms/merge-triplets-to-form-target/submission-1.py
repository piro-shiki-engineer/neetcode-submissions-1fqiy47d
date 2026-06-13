class Solution:
    """
    Task: Return True if it's possible obtain target triplet, not so return False.
    If the element of i-th triplets is bigger than the element of target triplets,
    We dont need to cosider the triplets, because the combined the tirplet is not match the triplet obiously.

    After filtering the unmatched triplets,
    we just need to check if the elements is exactly match target triplet
    
    We just need to check max a_i, b_i c_i is equal to target tirplet.
    Time: O(n)
    Space: O(1)
    """
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for i in range(3):
                if t[i] == target[i]:
                    good.add(i)

        return len(good) == 3


        