class Node:
    __slots__ = ("key", "val", "prev", "next")
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> node
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_front(self, node):
        first = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next =first
        first.prev = node
        
    def _move_to_front(self, node):
        self._remove(node)
        self._add_to_front(node)
        
    def _evict_lru(self):
        lru = self.tail.prev
        self._remove(lru)
        del self.cache[lru.key]
        
    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node is None:
            return -1

        self._move_to_front(node)
        return node.val

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = val
            self._move_to_front(node)
            return

        node = Node(key, val)
        self.cache[key] = node
        self._add_to_front(node)

        if len(self.cache) > self.capacity:
            self._evict_lru()
