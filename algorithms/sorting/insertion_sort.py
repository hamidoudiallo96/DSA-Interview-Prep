def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        j = i - 1
        key = arr[i]

        while j >= 0 and arr[j] > key:
            print(arr)
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Pre sort: ", arr)

    insertion_sort(arr)
    print("Post sort: ", arr)


# [64, 34, 25, 12, 22, 11, 90]
# []
# i = 0, key = 64, j = 1, arr[j] = 34
