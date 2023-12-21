import unittest

from lrucache import LRUCache

class Test(unittest.TestCase):
    def setUp(self):
        self.lru = LRUCache(limit=3)

    def test1(self):
        self.lru.set("key1", "value1")
        self.assertEqual(self.lru.get("key1"), "value1")

        self.lru.set("key2", "value2")
        self.assertEqual(self.lru.get("key2"), "value2")

        self.lru.get("key1")

        self.lru.set("key3", "value3")
        self.assertEqual(self.lru.get("key3"), "value3")

        self.lru.set("key4", "value4")
        self.assertEqual(self.lru.get("key2"), None)

    def test2(self):

        self.assertEqual(self.lru.get("non_existing_key"), None)
    def test3(self):

        self.lru.set("key1", "value1")
        self.lru.set("key1", "new_value")

        self.assertEqual(self.lru.get("key1"), "new_value")


if __name__ == "__main__":
    unittest.main()