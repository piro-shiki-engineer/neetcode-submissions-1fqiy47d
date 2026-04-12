class Solution:
    """
    Task: Return a subarray that has the largest product with in the array

    Subarrya has a least one value.
    Ancording to the problem sentense, subarray is needed contiguous.

    Let's calrify problem by using examples.
    I want to use the desciton tree like two options like bellow,
    1. subarray without first element.
    2. subaray without last element.

    until the length of array is 1.
    if so, the is base case, just value of the elemnt.

    bubble up to result and compare the two value from the children result, 
    and also, compare the parent result and the maximum child result as parent result.

    Time Complexity: O(2^N * N)
    Spcae Complexity: O(N^2)

    N is the lenght of input array.
    We can confirm that there are duplicates computation.
    Thus, we can remove the computation by using HashMap. key is the index range and value is the result.

    In this case, complexity is follow bellow,
    Time Complexity: O(N^2)
    Space Complexity: O(N^2)
    """
    def maxProduct(self, nums: List[int]) -> int:
        def dfs(first, last, memo):
            if (first, last) in memo:
                return memo[(first, last)]

            if first == last:
                return nums[first]

            result = 1
            for num in nums[first:last+1]:
                result *= num
            childResult = max(dfs(first, last-1, memo), dfs(first + 1, last, memo))
            result = max(result, childResult)

            memo[(first, last)] = result
            return result
                    
        return dfs(0, len(nums)-1, {})

