class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    """
    Dobule Linked List
    inputとgetの操作はO(1) → HaspMap
    利用頻度はDouble LinkedListで管理する LRUはLeft pointer、MostResecntはright pointerで管理する
    Hasp Map keyはそのままkey、valueはLinked ListのNodeへのポインタ

    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # Map key to Node

        # Left=LRU, right=most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from List
    def remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    # insert node at right
    def insert(self, node: Node) -> None:
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int: # get操作をしたときにはrightを更新する
        if key in self.cache:
            # TDOO: update most recent
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove from the list and delet LRU from HashMap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
