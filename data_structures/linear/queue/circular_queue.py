class CircularQueue:
    def __init__(self, capacity=10):
        self.data = [None] * capacity
        self.capacity = capacity
        self.front = self.size = 0

    def enqueue(self, val):
        if self.is_full():
            self.__resize(self.capacity * 2)

        rear = (self.front + self.size) % self.capacity
        self.data[rear] = val
        self.size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        item = self.data[self.front]
        self.data[self.front] = None
        front = (self.front + 1) % self.capacity
        self.size -= 1
        self.front = front
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        return self.data[self.front]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def print_queue(self):
        if self.is_empty():
            return None

        for val in self.data:
            print(val, end=" ")
        print()

    def __resize(self, new_capacity):
        old_queue = self.data
        self.data = [None] * new_capacity

        for i in range(self.size):
            new_index = (self.front + i) % self.capacity
            self.data[i] = old_queue[new_index]

        self.front = 0
        self.capacity = new_capacity
        print()


if __name__ == "__main__":
    q = CircularQueue(5)
    nums = [88, 97, 86, 87, 34]

    for num in nums:
        q.enqueue(num)

    q.print_queue()

    q.dequeue()
    q.dequeue()
    q.print_queue()

    q.enqueue(25)
    q.enqueue(42)
    q.print_queue()
    q.enqueue(100)
    q.print_queue()
