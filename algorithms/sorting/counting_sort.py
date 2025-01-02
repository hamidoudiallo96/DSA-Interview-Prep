# Time Complexity: O(n + k), n: length of array, k: range of values
# Space Complexity: O(n+k), n: length of output array, k: length of count array


def counting_sort(arr):
    if len(arr) <= 1:  # handle edge case
        return arr

    # Find range of input array
    min_val, max_val = min(arr), max(arr)
    arr_range = max_val - min_val + 1

    # Initialize counting array and output array
    count = [0] * arr_range
    output = [0] * len(arr)

    # Store count of each element
    # Normalize the index by subtracting min_val to handle negative numbers
    for num in arr:
        idx = num - min_val
        count[idx] += 1

    # Calculate cumulative count (each index will store count of elements ≤ index)
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    #  Build output array from right to left to maintain stability
    for num in reversed(arr):
        idx = count[num - min_val] - 1
        output[idx] = num
        count[num - min_val] -= 1

    return output


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    nums = [88, 97, 86, 98, 34, 87, 16]
    nums1 = [22, -5, 10, 2, -11, 12]

    print(f"Pre Sort \n{arr},\n{nums}\n{nums1}\n")

    sorted_arr = counting_sort(arr)
    sorted_nums = counting_sort(nums)
    sorted_nums1 = counting_sort(nums1)

    print(f"Post Sort \n{sorted_arr}\n{sorted_nums}\n{sorted_nums1}")
