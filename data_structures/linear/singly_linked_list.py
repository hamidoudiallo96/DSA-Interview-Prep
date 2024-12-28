class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_at_head(self, val):  # add_at_head
        new_node = ListNode(val)

        if self.is_empty():
            self.head = self.tail = new_node
            self.size += 1
            return

        next_node = self.head
        self.head = new_node
        self.head.next = next_node
        self.size += 1

    def add_at_tail(self, val):  # add_at_tail
        new_node = ListNode(val)

        if self.is_empty():
            self.add_at_head(val)
            self.size += 1
            return

        curr_tail = self.tail
        curr_tail.next = new_node
        self.tail = new_node
        self.size += 1

    def add(self, val, pos):  # add
        if pos < 0 or pos > self.size:
            raise IndexError()

        if self.is_empty():
            self.add_at_head(val)
            return

        new_node = ListNode(val)
        current = self.head

        for _ in range(pos - 1):
            current = current.next

        next_node = current.next
        current.next = new_node
        new_node.next = next_node
        self.size += 1

    def remove_at_head(self):  # remove_at_head
        if self.is_empty():
            return -1

        node_to_remove = self.head
        self.head = self.head.next
        self.size -= 1
        return node_to_remove

    def remove_at_tail(self):  # remove_at_tail
        if self.is_empty():  # empty list
            return -1

        if self.head == self.tail:  # 1 node
            node_to_remove = self.tail
            self.head = self.tail = None
            self.size -= 1
            return node_to_remove

        current = self.head

        while current.next != self.tail:
            current = current.next

        node_to_remove = self.tail
        self.tail = current
        self.tail.next = None
        self.size -= 1
        return node_to_remove

    def remove(self, pos):  # remove
        if pos < 0 or pos > self.size:
            raise IndexError()

        if self.is_empty():
            return -1

        current = self.head
        node_to_remove = None

        for _ in range(pos - 1):
            current = current.next

        next_node = current.next.next
        node_to_remove = current.next
        current.next = next_node
        self.size -= 1
        return node_to_remove

    def get(self, pos):  # get
        if pos < 0 or pos > self.size:
            raise IndexError()

        if self.is_empty():
            print("The list is empty")
            return

        current = self.head

        for _ in range(pos):
            current = current.next

        return current if current else -1

    def reverse(self):  # reverse
        if self.is_empty():
            return None

        curr = self.head
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev
        return self.head

    def find(self, value):  # find
        if self.is_empty():
            print("The list is empty.")
            return

        current = self.head

        while current:
            if current.val == value:
                return True

            current = current.next
        return False

    def is_empty(self):  # is_empty
        return self.size == 0

    def print_list(self):  # print_list
        if self.is_empty():
            print("The list is empty.")
            return

        current = self.head

        while current:
            print(current, end=" ")
            current = current.next

        print()


if __name__ == "__main__":
    sll = SinglyLinkedList()

    sll.add_at_head("Nylander")
    sll.add_at_head("McDavid")
    sll.add_at_head("Woll")
    sll.add_at_tail("Matthews")
    sll.add_at_tail("Tavares")
    sll.add_at_tail("Rielly")
    sll.add("Kucherov", 3)
    sll.add("Hughes", 4)
    sll.add("Kaprizov", 6)
    sll.add("Marner", 7)

    get_node1 = sll.get(3)
    get_node2 = sll.get(6)
    get_node3 = sll.get(2)

    print(get_node1, get_node2, get_node3)  # Kucherov, Kaprizov, Nylander

    node1 = sll.remove_at_head()
    node2 = sll.remove_at_tail()
    node3 = sll.remove(7)

    print(node1, node2, node3)  # Woll, Rielly, Tavares

    find_node1 = sll.find("Nylander")
    find_node2 = sll.find("Kaprizov")
    find_node3 = sll.find("Ovi")

    print(find_node1, find_node2, find_node3)  # True, True, False

    sll.reverse()
    sll.print_list()  # Marner Kaprizov Matthews Hughes Kucherov Nylander McDavid

    sll.reverse()
    sll.print_list()  # McDavid Nylander Kucherov Hughes Matthews Kaprizov Marner
