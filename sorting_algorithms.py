from utils import *

__version__ = "1.0.0"

@type_check
def insertion_sort(arr: Array) -> Array:
    if not validate_array(arr, 2): return arr
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

@type_check
def selection_sort(arr: Array) -> Array:
    if not validate_array(arr, 2): return arr
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

@type_check
def bubble_sort(arr: Array) -> Array:
    if not validate_array(arr, 2): return arr
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

@type_check
def shell_sort(arr: Array) -> Array:
    if not validate_array(arr, 2): return arr
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

@type_check
def smoothsort(data: Array) -> Array:
    if not validate_array(data, 2): return data
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

@type_check
def comb_sort(arr: Array) -> Array:
    if not validate_array(arr, 2): return arr
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

@type_check
def odd_even_sort(arr: Array) -> Array:
    if not validate_array(arr, 2): return arr
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

@type_check
def cocktail_sort(arr: Array) -> Array:
    if not validate_array(arr, 2): return arr
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while (swapped == True):
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if (swapped == False):
            break
        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start = start + 1
    return arr

@type_check
def gnome_sort(arr: Array) -> Array:
    if not validate_array(arr, 2): return arr
    n = len(arr)
    i = 1
    while i < n:
        if arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            if i > 1:
                i -= 1
    return arr

@type_check
def merge_sort(arr: Array) -> Array:
    if not validate_array(arr, 2): return arr
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

@type_check
def quick_sort(arr: Array) -> Array:
    if not validate_array(arr, 2): return arr
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left) + [pivot] + quick_sort(right)

@type_check
def heap_sort(arr: Array) -> Array:
    if not validate_array(arr, 2): return arr
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

@type_check
def heapify(arr: Array, n: int, i: int) -> Array:
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

@type_check
def radix_sort(arr: Array) -> Array:
    def counting_sort(arr: Array, exp: int | float):
        """Counting sort algorithm implementation

        Args:
            arr (Array): list of integers to be sorted
            exp (int | float): the exponent to be used in the algorithm

        Returns:
            Array: sorted list of integers
        """
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        for i in range(n):
            index = (arr[i] // exp)
            count[index % 10] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        i = n - 1
        while i >= 0:
            index = (arr[i] // exp)
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1
        i = 0
        for i in range(n):
            arr[i] = output[i]
        return arr

    if not validate_array(arr, 2): return arr
    max_element = max(arr)
    exp = 1
    while max_element // exp > 0:
        arr = counting_sort(arr, exp)
        exp *= 10
    return arr

@type_check
def Tim_sort(arr: Array) -> Array:
    if not validate_array(arr, 2): return arr
    n = len(arr)
    min_run = 32
    while min_run < n:
        min_run *= 2
    def insertion_sort_run(arr, left, right):
        for i in range(left + 1, right + 1):
            j = i
            while j > left and arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                j -= 1
    def merge_sort_run(arr, left, mid, right):
        i = left
        j = mid + 1
        k = left
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
            k += 1
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
        for i in range(left, right + 1):
            arr[i] = temp[i]
    temp = [0] * n
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort_run(arr, start, end)
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min(n - 1, mid + size)
            merge_sort_run(arr, left, mid, right)
        size *= 2
    return arr

#  ==============================================================================================================
@type_check
def intercalary_sort1(tab: Array,p:float=2.95) -> Array:
    if not validate_array(tab, 2): return tab
    L=list(tab)
    if len(L) < 2: return L
    sorted_list = [L.pop(0)]
    for i in L:
        tmp1 = (0, (sorted_list[0] - i)**2, sorted_list[0] - i > 0)
        for j in range(1, len(sorted_list), len(sorted_list) // int(len(sorted_list)**(1/p))):
            tmp2 = sorted_list[j] - i
            if (tmp2)**2 < tmp1[1]:
                tmp1 = (j, (tmp2)**2, tmp2 > 0)
        k = tmp1[0]
        if tmp1[2]:
            while k > 0 and sorted_list[k-1] > i:
                k -= 1
            sorted_list.insert(k, i)
        else:
            while k < len(sorted_list) and sorted_list[k] < i:
                k += 1
            sorted_list.insert(k, i)
    return sorted_list

@type_check
def intercalary_sort2(L: Array) -> Array:
    if not validate_array(L, 2): return L
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

# @type_check
# def intercalary_sort3(L: list[int]) -> list[int]:
#     if not validate_array(L, 2): return L
#     sorted_list = [L[0]]
#     for i in range(len(L)):
#         left = 0
#         right = len(sorted_list) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if sorted_list[mid] < L[i]:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         sorted_list.insert(left, L[i])
#     return sorted_list
