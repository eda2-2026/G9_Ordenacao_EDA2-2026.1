def bubble_sort(a):
    arr = a.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr.copy()
    yield arr


def selection_sort(a):
    arr = a.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            yield arr.copy()
    yield arr


def insertion_sort(a):
    arr = a.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            yield arr.copy()
        arr[j + 1] = key
        yield arr.copy()
    yield arr


def merge_sort_gen(a):
    arr = a.copy()
    n = len(arr)

    def merge(l, r):
        res, i, j = [], 0, 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                res.append(l[i]); i += 1
            else:
                res.append(r[j]); j += 1
        res.extend(l[i:]); res.extend(r[j:])
        return res

    width = 1
    arr_copy = arr.copy()
    while width < n:
        for i in range(0, n, 2 * width):
            left = arr_copy[i:i + width]
            right = arr_copy[i + width:i + 2 * width]
            merged = merge(left, right)
            arr_copy[i:i + len(merged)] = merged
            yield arr_copy.copy()
        width *= 2
    yield arr_copy
