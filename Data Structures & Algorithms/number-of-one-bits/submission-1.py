class Solution:
    """
    Task: Count the total number of 1 bits
    We need to convert from the given integer n to the string binary number bi_n
    And, count the characters "1" by iterating through the string bi_n

    I need to search how to make interger number binary number
    """
    def hammingWeight(self, n: int) -> int:
        bi_n = str(bin(n))
        total = 0
        for i in range(2, len(bi_n)):
            if bi_n[i] == "1":
                total += 1

        return total