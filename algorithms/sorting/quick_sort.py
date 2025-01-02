def quick_sort(arr, start=0, end=None):
    if len(arr) <= 1 or arr is None:
        return arr
    if end is None:
        end = len(arr) - 1

    def get_pivot(start, end):
        mid = start + (end - start) // 2
        pivot = sorted([(arr[start], start), (arr[mid], mid), (arr[end], end)])[1][1]

        arr[pivot], arr[end] = arr[end], arr[pivot]
        return arr[end]

    def partition(start, end):
        pivot = get_pivot(start, end)
        i = start - 1

        for j in range(start, end):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[end] = arr[end], arr[i + 1]
        return i + 1

    if start < end:
        p = partition(start, end)
        quick_sort(arr, start, p - 1)
        quick_sort(arr, p + 1, end)


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    companies = ["Google", "Yandex", "Tesla", "Meta", "Amazon"]

    print(f"Pre Sort {arr}, {companies}", end="\n")

    quick_sort(arr)
    quick_sort(companies)

    print(f"Post Sort {arr}, {companies}")
