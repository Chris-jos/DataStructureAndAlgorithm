def bubble_sort(arr):
    """
    This function implements the bubble sort algorithm.
    It sorts a list of numbers in ascending order by repeatedly stepping through the list,
    comparing adjacent elements and swapping them if they are in the wrong order.
    The process is repeated until the list is sorted.
    """
    n = len(arr)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

def selection_sort(arr):
    """
    This function implements the selection sort algorithm.
    It sorts a list of numbers in ascending order by repeatedly finding the minimum element
    from the unsorted part of the list and moving it to the beginning.
    The process is repeated until the entire list is sorted.
    """
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

def insertion_sort(arr):
    """
    This function implements the insertion sort algorithm.
    It sorts a list of numbers in ascending order by building a sorted portion of the list
    one element at a time. It takes each element from the unsorted portion and inserts it
    into the correct position in the sorted portion.
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

def merge_sort(arr):
    """
    This function implements the merge sort algorithm.
    It sorts a list of numbers in ascending order by dividing the list into halves,
    sorting each half recursively, and then merging the sorted halves back together.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    """
    This helper function merges two sorted lists into a single sorted list.
    param left: The first sorted list.
    param right: The second sorted list.
    return: A merged sorted list containing all elements from both input lists.
    """
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def quick_sort(arr):
    """
    This function implements the quick sort algorithm.
    It sorts a list of numbers in ascending order by selecting a 'pivot' element,
    partitioning the other elements into two sub-arrays according to whether they are less than
    or greater than the pivot, and then recursively sorting the sub-arrays.
    """
    return quick_sort_helper(arr, 0, len(arr) - 1)

def quick_sort_helper(arr, left, right):
    """
    This is a helper function for the quick sort algorithm.
    param arr: The list to be sorted.  
    param left: The starting index of the sub-array to be sorted.
    param right: The ending index of the sub-array to be sorted.
    return: The sorted list.
    """
    if left < right:
        pivot_index = pivot(arr, left, right)
        quick_sort_helper(arr, left, pivot_index - 1)
        quick_sort_helper(arr, pivot_index + 1, right)
    return arr

def pivot(arr, pivot_index, end_index):
    """
    This helper function selects a pivot element and partitions the array around it.
    param arr: The list to be partitioned.
    param pivot_index: The starting index of the sub-array.
    param end_index: The ending index of the sub-array.
    return: The index of the pivot element after partitioning.
    """
    swap_index = pivot_index

    for i in range(pivot_index + 1, end_index + 1):
        if arr[i] < arr[pivot_index]:
            swap_index += 1
            swap(arr, swap_index, i)

    swap(arr, swap_index, pivot_index)
    return swap_index

def swap(arr, i, j):
    """
    This helper function swaps two elements in a list.
    param arr: The list containing elements to be swapped.
    param i: The index of the first element.
    param j: The index of the second element.
    """
    if i != j:
        arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    sample_list = [1, 2, 3, 12, 22, 11, 90]
    # sorted_list = bubble_sort(sample_list)
    # print("Sorted list:", sorted_list)

    # sorted_list = selection_sort(sample_list)
    # print("Sorted list:", sorted_list)

    # sorted_list = insertion_sort(sample_list)
    # print("Sorted list:", sorted_list)

    # sorted_list = merge_sort(sample_list)
    # print("Sorted list:", sorted_list)

    sorted_list = quick_sort(sample_list)
    print("Sorted list:", sorted_list)
