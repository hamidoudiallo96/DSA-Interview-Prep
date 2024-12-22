from collections import deque


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key}: {self.value}"


class HashTable:
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.table = [deque([]) for _ in range(capacity)]  # chaining

    def hash_key(self, key):
        ###### Manual implementation  ########
        # if isinstance(key, str): # check if the key is a string
        #     total = sum(ord(char) for char in key) # handle str hashing
        # else:
        #     total = key
        # return total % self.size

        ###### Built-in hash function #######
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self.hash_key(key)

        for item in self.table[index]:
            if item.key == key:  # check if key exists and update
                item.value = value
                return

        self.table[index].append(Node(key, value))
        self.size += 1

    def get(self, key):
        index = self.hash_key(key)

        for item in self.table[index]:
            if item.key == key:
                return item.value

            raise KeyError(key)

    def remove(self, key):
        index = self.hash_key(key)
        deleted_item = None

        for item in self.table[index]:
            if item.key == key:
                self.size -= 1
                deleted_item = item
                self.table[index].remove(item)
                return deleted_item

        raise KeyError(key)

    def contains(self, key):
        index = self.hash_key(key)

        for item in self.table[index]:
            if item.key == key:
                return True
        return False

    def print_table(self):
        for bucket in self.table:
            for node in bucket:
                print(node)


if __name__ == "__main__":
    ht = HashTable(23)
    ht.insert(88, "Nylander")
    ht.insert(34, "Matthews")
    ht.insert(91, "Tavares")
    ht.insert(16, "Marner")
    ht.insert(44, "Rielly")
    ht.insert(92, "Jason")
    ht.insert(97, "McDavid")

    ht.print_table()

    print(f"Get: {ht.get(88)}")
    print(f"Contains: {ht.contains(97)}")
    print(f"Remove: {ht.remove(92)}")
    print(f"Remove: {ht.remove(44)}")
    ht.print_table()
