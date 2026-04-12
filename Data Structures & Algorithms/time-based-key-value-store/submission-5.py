class TimeMap:
    """
    set関数が呼び出される時のタイムスタンプは必ず増加するようになっている。
    誤解ポイント1：
    タイムスタンプが連続した値で順に与えられると勘違いした。
    →We need to manage values including timestamp becauese the input given timestamp is not consistant.
    →So,the array which is containig valuesd is sorted by timestamp
    そのためリスト内ではtimestampも同時に管理する必要がでてくる
    get関数では引数で与えられるprevious <= timestampの最小値を返す
    """
    def __init__(self):
        self.store = {} # key list of [val ,timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        
        left, right = 0, len(values)-1
        
        while left <= right:
            middle = (left + right) // 2
            if values[middle][1] <= timestamp: 
                res = values[middle][0] # 現時点でわかる値も格納する
                left = middle + 1
            else:
                # timestampより大きいものは有効でないため現時点では格納できない
                right = middle - 1
        
        return res