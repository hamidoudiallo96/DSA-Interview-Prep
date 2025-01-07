class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack or val < self.min_stack[-1][0]:
            self.min_stack.append([val, 1])
        elif val == self.min_stack[-1][0]:
            self.min_stack[-1][1] += 1

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Empty Stack")

        item = self.stack.pop()

        if item == self.min_stack[-1][0]:
            self.min_stack[-1][1] -= 1

            if self.min_stack[-1][1] == 0:
                self.min_stack.pop()

        return item

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Empty Stack")

        return self.stack[-1]

    def is_empty(self):
        return not self.stack

    def get_min(self) -> int:
        if not self.min_stack:
            raise IndexError("Empty Stack")

        return self.min_stack[-1][0]


if __name__ == "__main__":
    min_stack = MinStack()
    nums = [88, 97, 86, 34, 98, 34, -5, 16]

    for num in nums:
        min_stack.push(num)

    print(min_stack.get_min())  # -5
    print(min_stack.stack, min_stack.min_stack)

    min_stack.pop()
    min_stack.pop()
    print(min_stack.get_min())  # 34
    min_stack.pop()
    min_stack.pop()
    min_stack.pop()
    print(min_stack.get_min())  # 86
