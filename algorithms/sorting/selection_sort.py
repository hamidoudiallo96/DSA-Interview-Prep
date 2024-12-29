def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        smallest_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[smallest_idx]:
                smallest_idx = j

        arr[i], arr[smallest_idx] = arr[smallest_idx], arr[i]

    return arr


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Pre sort: ", arr)

    selection_sort(arr)
    print("Post sort: ", arr)
