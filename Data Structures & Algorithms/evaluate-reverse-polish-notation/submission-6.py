class Solution:
    """
    演算子以外はstackにpush
    演算子が来たときにそれまでの結果をpopして、演算子とその次の値
    """

    def evalRPN(self, tokens: List[str]) -> int:
        """
        空間計算量:O(N)
        時間計算量:O(N)

        N is the length of array "tokens".
        """
        stack = []
        i = 0
        while i < len(tokens):
            if tokens[i] == "+":
                stack.append(stack.pop() + stack.pop())

            elif tokens[i] == "-":
                x, y = stack.pop(), stack.pop()
                stack.append(y - x)

            elif tokens[i] == "*":
                stack.append(stack.pop() * stack.pop())
            elif tokens[i] == "/":
                x, y = stack.pop(), stack.pop()
                stack.append(int(float(y / x)))
            else:
                stack.append(int(tokens[i]))
            
            i += 1

        return stack[0]