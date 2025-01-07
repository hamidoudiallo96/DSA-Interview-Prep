def non_increasing_stack(arr: list) -> list:
    stack = []

    for val in arr:
        while stack and stack[-1] <= val:
            stack.pop()

        stack.append(val)

    return stack


def non_decreasing_stack(arr: list) -> list:
    stack = []

    for val in arr:
        while stack and stack[-1] >= val:
            stack.pop()

        stack.append(val)

    return stack


if __name__ == "__main__":
    nums = [13, 8, 1, 5, 2, 5, 9, 7, 6, 12]
    nums1 = [3, 1, 4, 1, 5, 9, 2, 6]

    result_stack = non_decreasing_stack(nums)  # [1, 2, 5, 6, 12]
    result_stack1 = non_decreasing_stack(nums1)  # [1, 1, 2, 6]
    print(result_stack, result_stack1)

    result_stack2 = non_increasing_stack(nums)  # [13, 12]
    result_stack3 = non_increasing_stack(nums1)  # [9, 6]
    print(result_stack2, result_stack3)
