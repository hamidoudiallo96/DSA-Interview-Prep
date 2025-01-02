# Time Complexity: O(n logn)
# Space Complexity: O(1)

# Max Heap Implementation
def max_heap_sort(arr):
    if len(arr) <= 1:
        return arr

    def heapify(start, end):
        root, child = start, (2 * start) // 2

        while True:
            if child > end:  # Check if child index is out of bounds
                break

            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1
            if arr[child] > arr[root]:
                arr[child], arr[root] = arr[root], arr[child]
                root = child
            else:
                break

    n = len(arr)

    # Build heap
    for start in range((n - 2) // 2, -1, -1):
        heapify(start, n - 1)

    # Extract one by one until the array is sorted
    for end in range(n - 1, 0, -1):
        nums[0], nums[end] = nums[end], nums[0]  # move max element to end
        heapify(0, end - 1)  # Restore heap property


# Min-Heap Implementation
def min_heap_sort(arr):
    if len(arr) <= 1:
        return None

    def heapify(start, end):
        root, child = start, (2 * start) + 1

        while True:
            if child > end:
                break
            if child + 1 <= end and arr[child] > arr[child + 1]:
                child += 1
            if arr[root] > arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
            else:
                break

    n = len(arr)

    for start in range((n - 2) // 2, -1, -1):
        heapify(start, n - 1)

    for end in range(n - 1, 0, -1):
        nums[0], nums[end] = nums[end], nums[0]
        heapify(0, end - 1)


nums = [88, 97, 86, 87, 34, 16]
max_heap_sort(nums)
print(f"Max-Heap:{nums}\n")  # [16, 34, 86, 87, 88, 97]

min_heap_sort(nums)
print(f"Min-Heap:{nums}")  # [97, 88, 87, 86, 34, 16]
