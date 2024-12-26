class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_at_head(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = Node(value)
            self.size += 1
            return

        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def add(self, value, pos):
        new_node = Node(value)

        if not self.head:
            self.add_at_head(value)
            return

        current = self.head
        curr_pos = 1

        while current:
            if pos - 1 == curr_pos:
                break
            curr_pos += 1
            current = current.next

        next_node = current.next
        current.next = new_node
        new_node.next = next_node
        self.size += 1

    def delete_at_head(self):
        if not self.head:
            return -1

        next_node = self.head.next
        deleted_node = self.head.data
        self.head = next_node
        self.size -= 1
        return deleted_node

    def delete(self, pos):
        if not self.head:
            return -1

        current, curr_pos = self.head, 1

        while current.next:
            if pos - 1 == curr_pos:
                break
            curr_pos += 1
            current = current.next

        deleted_node = current.next.data
        next_node = current.next.next
        current.next = next_node

        self.size -= 1
        return deleted_node

    def search(self, value):
        if not self.head:
            return False

        current = self.head

        while current.next:
            if current.data == value:
                return True
            current = current.next

        return False

    def print_list(self):
        current = self.head

        while current:
            print(current, end=" => ")
            current = current.next
        print()


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.add_at_head(5)
    sll.add_at_head(21)
    sll.add_at_head(17)
    sll.add_at_head(25)
    sll.print_list()

    node = sll.delete_at_head()
    node1 = sll.delete_at_head()
    node2 = sll.delete_at_head()
    print(node, node1, node2)
    sll.print_list()

    sll.add_at_head(91)
    sll.add_at_head(88)
    sll.add_at_head(34)
    sll.add_at_head(29)
    sll.add_at_head(97)
    sll.print_list()

    print(sll.search(34))  # True
    print(sll.search(44))  # False

    sll.add(16, 5)
    sll.add(22, 7)
    sll.print_list()

    print(sll.delete(3))  # 34
    sll.print_list()
