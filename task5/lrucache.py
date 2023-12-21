class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, limit=42):
        self.limit = limit
        self.cache = {}
        self.top = None
        self.tail = None

    def get(self, key):
        """get method for descriptor"""
        if key in self.cache:
            node = self.cache[key]
            self._move_to_top(node)
            return node.value
        return None

    def set(self, key, value):
        """set method for descriptor"""
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_top(node)
        else:
            if len(self.cache) >= self.limit:
                self._remove_tail()
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_top(new_node)

    def _remove_node(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.tail:
            self.tail = node.prev

    def _add_to_top(self, node):
        if not self.top:
            self.top = node
            self.tail = node
        else:
            node.next = self.top
            self.top.prev = node
            self.top = node

    def _move_to_top(self, node):
        if node == self.top:
            return
        self._remove_node(node)
        self._add_to_top(node)

    def _remove_tail(self):
        if not self.tail:
            return
        del self.cache[self.tail.key]
        if self.tail == self.top:
            self.top = None
            self.tail = None
        else:
            self.tail = self.tail.prev

cache = LRUCache(2)

cache.set("k1", "val1")
cache.set("k2", "val2")

assert cache.get("k3") is None
assert cache.get("k2") == "val2"
assert cache.get("k1") == "val1"

cache.set("k3", "val3")

assert cache.get("k3") == "val3"
assert cache.get("k2") is None
assert cache.get("k1") == "val1"