# Array Implementation
# Time Complexity: O(1) for all operations
# Space Complexity: O(n), where n is the number of elements in the array


class Stack:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)
        return True

    def pop(self):
        if self.is_empty():
            raise IndexError()

        item = self.data.pop()
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError()

        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0


### Linked List Implementation
class StackNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)


class StackList:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, val):
        node = StackNode(val)

        if not self.head:
            self.head = node
        else:
            temp = self.head
            self.head = node
            node.next = temp

        self.size += 1

    def pop(self):
        if not self.head:
            return -1

        temp = self.head
        self.head = self.head.next
        self.size -= 1
        return temp

    def peek(self):
        if not self.head:
            raise IndexError()
        return self.head

    def is_empty(self):
        return self.size == 0

    def print_list(self):
        if not self.head:
            raise IndexError()

        curr = self.head
        for _ in range(self.size):
            print(curr, end=" ")
            curr = curr.next
        print()


if __name__ == "__main__":
    s1 = Stack()
    s2 = StackList()
    nums = [88, 97, 86, 98, 34, 16]

    print(s2.is_empty())
    for num in nums:
        s1.push(num)
        s2.push(num)

    print(s1.data)
    print(s1.pop())  # 16
    print(s1.pop())  # 34
    print(s1.data)
    print(s1.peek())
    print(s1.is_empty())

    print()
    s2.print_list()
    print(s2.pop())  # 16
    print(s2.pop())  # 34
    s2.print_list()
    print(s2.peek())
    print(s2.is_empty())
