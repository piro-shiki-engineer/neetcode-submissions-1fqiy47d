class Solution:
    '''
    「除算演算子/」が禁止されている
    この時にアルゴリズム全体の時間計算量をO(N)で求められるか
    例　[1,2,3,4]
    例えば要素3を除いた積を考える
    基本的な考えとしては、3より前の値の積と、3よりも後の積を求める
    前積と後積の掛け算が求めたい値

    方針:前積と後積をあらかじめ求めるO（N）+O（N） = O(N)
    この時循環させると
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1]*length

        for i in range(1, length):
            res[i] = res[i-1] * nums[i-1]
        
        postfix = 1
        for i in range(length-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res


class Solution:
    """
    Task: Return products which i-th of product means product without nums[i]

    The element are contained negative and 0 ?→ Yes.
    product in 32-bit interger less than 2^32 - 1

    Let us clarify this problem by using some examples.Product is culculaed by 2 directions before i th index.

    に方向からの計算
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

    
        postfix = 1
        for i in range(n-1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output


        


