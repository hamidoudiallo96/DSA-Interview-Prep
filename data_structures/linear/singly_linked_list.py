class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def add_at_head(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = Node(value)
            return

        new_node.next = self.head
        self.head = new_node

    def delete_at_head(self):
        if not self.head:
            return -1

        next_node = self.head.next
        deleted_node = self.head.data
        self.head = next_node
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
