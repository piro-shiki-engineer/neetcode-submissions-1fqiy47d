class Solution:
    """
    Time: O(n * 4^n)
    """
    def letterCombinations(self, digits: str) -> List[str]:
        # digit : characters
        
        res = []
        if not digits:
            return res

        mapTo = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        def backtrack(i, cur: str):
            if i == len(digits):
                res.append("".join(cur.copy()))
                return
            
            candidates = mapTo[digits[i]]
            for j in range(len(candidates)):
                cur.append(candidates[j])
                backtrack(i + 1, cur)
                cur.pop()
        
        backtrack(0, [])
        return res