class Solution:
    """
    t文字列にある全て文字をすべて含む最も短い文字列を求めよ
    （ただし、重複を含んでもいい）
    
    tに含まれる大文字小文字含む26＊2種の文字ががそれぞれいくつか数え上げる
    sも同様に52種の文字がそれぞれいくつあるか数え上げる

    エッジケース1：tが空列

    s = "OUZODYXAZV", t = "XYZ"
    t_count = {'X':1, 'Y':1, 'Z':1} : need  
    s_count = {'O':1, 'U':1, 'Z':1} : have

    needは ある文字がある個数以上という条件の数の総和
    haveは 現時点でneedの持つ条件の内、満たす条件の数の総和

    windowを変化させる（left pointerをそのままの場合とleft pointerをずらした場合それぞれ調べる必要がある）
    t_countにない文字ならば、無視
    t_sountにある文字ならば、s_countにその文字分の数を追加
    → 追加した文字の数がs_count >= t_countならば、have += 1　※すでに満たしていた条件ならば、インクリメントしない

    have == needになった時の結果としてres = [left, right], (条件を満たす文字列の長さ)として保存する
    (条件を満たす文字列の長さ)は、最初いうの部分文字列を見つけるときに利用する
    """
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count_t, window = {}, {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        have, need = 0, len(count_t)
        res, res_length = [-1, -1], float('infinity')
        left = 0
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in count_t and window[char] == count_t[char]:
                have += 1
            
            while have == need:
                if (right - left + 1) < res_length:
                    res = [left, right]
                    res_length = right - left + 1
                
                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1

        left, right = res

        return s[left:right+1] if res_length != float('infinity') else ""