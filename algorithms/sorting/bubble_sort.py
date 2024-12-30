def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

        if not swapped:
            break

    return arr


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    # print("Pre sort: ", arr)

    bubble_sort(arr)
    print("Post sort: ", arr)
