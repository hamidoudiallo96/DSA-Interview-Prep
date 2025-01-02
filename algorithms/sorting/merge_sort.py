#### In-Place Approach ####
# Time Complexity: O(n logN)
# Space Complexity: O(n)


def merge(arr, start, mid, end):
    left, right = arr[start:mid], arr[mid:end]
    i = j = 0
    n1, n2 = len(left), len(right)

    k = start

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


def merge_sort(arr, start, end):
    if end - start > 1:
        mid = start + (end - start) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid, end)
        merge(arr, start, mid, end)
        return arr


#### Functional Approach ####
# Time Complexity: O(n logN)
# Space Complexity: O(n logN)


# def merge(left, right):
#     res = []
#     i = j = 0
#     n1, n2 = len(left), len(right)

#     while i < n1 and j < n2:
#         if left[i] <= right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1

#     res.extend(left[i:])
#     res.extend(right[j:])

#     return res


# def merge_sort(arr, start, end):
#     if end - start <= 1:
#         return arr[start:end]

#     mid = start + (end - start) // 2

#     left = merge_sort(arr, start, mid)
#     right = merge_sort(arr, mid, end)

#     return merge(left, right)


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Pre sort: ", arr)

    sorted_arr = merge_sort(arr, 0, len(arr))
    print("Post sort: ", sorted_arr)
