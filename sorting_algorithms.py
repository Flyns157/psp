def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def quicksort_wr(arr):
    if len(arr) <= 1:
        return arr
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if high - low < 1:
            continue
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        stack.append((low, i))
        stack.append((i + 2, high))
    return arr

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    n = len(arr)
    temp_arr = [0] * n
    width = 1
    while width < n:
        for i in range(0, n, 2 * width):
            merge(arr, i, min(i + width, n), min(i + 2 * width, n), temp_arr)
        arr, temp_arr = temp_arr, arr
        width *= 2
    return arr

def merge(arr, left_start, right_start, right_end, temp_arr):
    left_end = right_start - 1
    i = left_start
    j = right_start
    k = left_start
    while i <= left_end and j <= right_end:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            j += 1
        k += 1
    while i <= left_end:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    while j <= right_end:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

def mergesort_wr(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    left = mergesort_wr(left)
    right = mergesort_wr(right)
    return merge_wr(left, right)

def merge_wr(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def heapsort_wr(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify_wr(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_wr(arr, i, 0)
    return arr

def heapify_wr(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_wr(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        j = 0
        while True:
            left = 2 * j + 1
            right = 2 * j + 2
            if left >= i:
                break
            if right >= i:
                if arr[j] < arr[left]:
                    arr[j], arr[left] = arr[left], arr[j]
                break
            if arr[left] > arr[right]:
                if arr[j] < arr[left]:
                    arr[j], arr[left] = arr[left], arr[j]
                    j = left
                else:
                    break
            else:
                if arr[j] < arr[right]:
                    arr[j], arr[right] = arr[right], arr[j]
                    j = right
                else:
                    break
    return arr

def heapify(arr, n, i):
    j = i
    while True:
        left = 2 * j + 1
        right = 2 * j + 2
        if left >= n:
            break
        if right >= n:
            if arr[j] < arr[left]:
                arr[j], arr[left] = arr[left], arr[j]
            break
        if arr[left] > arr[right]:
            if arr[j] < arr[left]:
                arr[j], arr[left] = arr[left], arr[j]
                j = left
            else:
                break
        else:
            if arr[j] < arr[right]:
                arr[j], arr[right] = arr[right], arr[j]
                j = right
            else:
                break

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def bubble_sort(arr):
    n=len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapped = True
        n -= 1
    return arr

def down_heap(data, end, lhc):
    root = 0
    while lhc(root) <= end:
        child = lhc(root)
        swap = root
        if data[swap] < data[child]:
            swap = child
        if child + 1 <= end and data[swap] < data[child + 1]:
            swap = child + 1
        if swap == root:
            return
        else:
            data[root], data[swap] = data[swap], data[root]
            root = swap

def smoothsort(data):
    size = len(data)
    if size < 2:
        return data
    p = 1
    while (3 * p + 1) < size:
        p = 3 * p + 1
    while p > 0:
        for i in range(p, size):
            if data[i] >= data[i - p]:
                continue
            j = i
            while j >= p and data[j] < data[j - p]:
                data[j], data[j - p] = data[j - p], data[j]
                j -= p
        p = (p - 1) // 3
    end = size - 1
    while end > 0:
        data[0], data[end] = data[end], data[0]
        end -= 1
        down_heap(data, end, lambda x: (2 * x + 1))
    return data

def cocktail_sort(arr):
    if len(arr) == 0:
        return arr
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        end -= 1
        if not swapped:
            break
        swapped = False
        for i in range(end, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start += 1
    return arr

def comb_sort(arr):
    if len(arr) == 0: return arr
    n = len(arr)
    gap = n
    shrink = 1.3
    swapped = True
    while gap > 1 or swapped:
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1
        i = 0
        swapped = False
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
            i += 1
        if not swapped and gap == 1:
            break
    return arr

def odd_even_sort(arr):
    if len(arr) == 0: return arr
    n = len(arr)
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False
    return arr

def intercalary_sort2(L: list[int]) -> list[int]:
    if len(L) == 0: return []
    sorted_list = [L[0]]
    for i in L[1:]:
        left = 0
        right = len(sorted_list) - 1
        while left <= right:
            mid = (left + right) // 2
            if sorted_list[mid] < i:
                left = mid + 1
            else:
                right = mid - 1
        sorted_list.insert(left, i)
    return sorted_list
