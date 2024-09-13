"""
Merge Sort on List of Integers
"""

import rand


def merge_sort(arr):
    """
    Recursively sorts the array using merge sort.

    Args:
        arr (list): List of integers to sort.

    Returns:
        list: Sorted list of integers.
    """
    if len(arr) == 1:
        return arr

    half = len(arr) // 2
    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """
    Recombines two sorted arrays into one sorted array.

    Args:
        left_arr (list): Left sorted array.
        right_arr (list): Right sorted array.

    Returns:
        list: Merged sorted array.
    """
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))

    merge_index = 0
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[merge_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[merge_index] = right_arr[right_index]
            right_index += 1
        merge_index += 1

    # Append the remaining elements from the left array, if any
    while left_index < len(left_arr):
        merge_arr[merge_index] = left_arr[left_index]
        left_index += 1
        merge_index += 1

    # Append the remaining elements from the right array, if any
    while right_index < len(right_arr):
        merge_arr[merge_index] = right_arr[right_index]
        right_index += 1
        merge_index += 1

    return merge_arr


# Generating a random array of integers
# Renamed variable to avoid redefinition
random_arr = rand.random_array([None] * 20)
sorted_arr = merge_sort(random_arr)  # Corrected function call

print(sorted_arr)
