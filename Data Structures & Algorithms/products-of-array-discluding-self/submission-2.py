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