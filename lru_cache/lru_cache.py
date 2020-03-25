from doubly_linked_list import DoublyLinkedList, ListNode


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.storage = DoublyLinkedList()
        self.dictionary = {}
        self.limit = limit

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        value = self.dictionary.get(key)
        if value is None:
            return None
        else:
            self.storage.move_to_front(value)
            print("value.value", value.value)
            return value.value

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        if self.get(key) is not None:
            node = self.dictionary.get(key)
            node.value = value
            self.storage.move_to_front(node)
            self.dictionary[key] = node
            return
        self.storage.add_to_head(value)
        self.dictionary[key] = self.storage.head
        print(self.dictionary)
        if self.storage.length > self.limit:
            tail = self.storage.tail
            print("tail", tail)
            self.dictionary = {
                key: val for key, val in self.dictionary.items() if val != tail
            }
            self.storage.remove_from_tail()


cache = LRUCache()
cache.set("item1", "a")
cache.set("item2", "b")

cache.get("item2")
cache.set("item2", "z")
cache.get("item2")
