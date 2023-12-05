class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        hash_key = self._hash(key)
        key_exists = False
        slot = self.hash_table[hash_key]
        for i, kv in enumerate(slot):
            k, _ = kv
            if k == key:
                key_exists = True
                break
        if key_exists:
            slot[i] = (key, value)
        else:
            slot.append((key, value))

    def get(self, key):
        hash_key = self._hash(key)
        slot = self.hash_table[hash_key]
        for k, v in slot:
            if k == key:
                return v
        return None

    def remove(self, key):
        hash_key = self._hash(key)
        slot = self.hash_table[hash_key]
        for i, kv in enumerate(slot):
            k, _ = kv
            if k == key:
                del slot[i]
                return
        return None
