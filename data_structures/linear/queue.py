from collections import deque


class Queue:
    def __init__(self):
        self.data = deque()
        self.size = 0

    def enqueue(self, val):
        self.data.append(val)
        self.size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            print("The queue is empty")
            return
        item = self.data.popleft()
        self.size -= 1
        return item

    def peek(self):
        return self.data[0]

    def is_empty(self):
        return self.size == 0

    def print_queue(self):
        if self.is_empty():
            print("The queue is empty")
            return

        for item in self.data:
            print(item, end=" ")

        print()


if __name__ == "__main__":
    q = Queue()
    nums = [88, 97, 86, 98, 34, 16]

    for num in nums:
        q.enqueue(num)

    q.print_queue()  # 88 97 86 98 34 16

    print(q.dequeue())  # 88
    print(q.dequeue())  # 97

    q.print_queue()  # 86 98 34 16
