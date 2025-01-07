class MyQueue:
    def __init__(self):
        self.s1 = []  # s1 handles enqueue operations (input stack)
        self.s2 = []  # s2 handles dequeue operations (input stack)

    def push(self, x: int) -> None:
        self.s1.append(x)  # Always add new elements to the input stack

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Empty Queue")

        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2.pop()

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Empty Queue")

        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2[-1]

    def is_empty(self) -> bool:
        return not self.s1 and not self.s2  #


if __name__ == "__main__":
    q = MyQueue()

    q.push(1)
    q.push(2)

    print(q.s1, q.s2)
