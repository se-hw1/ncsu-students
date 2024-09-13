import rand

def merge_sort(arr):
    if len(arr) == 1:  # corrected variable name
        return arr

    half = len(arr) // 2  # corrected variable name
    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))  # corrected recursive calls

def recombine(left_arr, right_arr):
    left_index = 0
    right_index = 0
    merge_arr = [None]*(len(left_arr)+len(right_arr)) 
    
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
arr = rand.random_array([None] * 20)  # corrected array generation
arr_out = merge_sort(arr)  # corrected function call

print(arr_out)
