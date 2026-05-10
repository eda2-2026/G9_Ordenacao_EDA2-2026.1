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

def quick_sort(a):
    arr = a.copy()

    def _quick_sort(low, high):
        if low < high:
            pi = yield from partition(low, high)

            yield from _quick_sort(low, pi - 1)
            yield from _quick_sort(pi + 1, high)

    def partition(low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                yield arr.copy()

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        yield arr.copy()

        return i + 1

    yield from _quick_sort(0, len(arr) - 1)
    yield arr


def shell_sort(a):
    arr = a.copy()
    n = len(arr)

    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                yield arr.copy()

            arr[j] = temp
            yield arr.copy()

        gap //= 2

    yield arr


def radix_sort(a):
    arr = a.copy()

    def counting_sort(exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(n):
            arr[i] = output[i]
            yield arr.copy()

    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        yield from counting_sort(exp)
        exp *= 10

    yield arr