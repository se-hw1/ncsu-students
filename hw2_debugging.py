import rand #for generation of random arrays

def merge_sort(arr):
    if len(arr1) == 1:
        return arr1

    half = len(arr)//2
    
    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))

def recombine(left_arr, right_arr):
    left_index = 0
    right_index = 0
    mergeArr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            right_index += 1
            mergeArr[left_index + right_index] = left_arr[left_index]
        else:
            left_index += 1
            mergeArr[left_index + right_index] = right_arr[right_index]

    for i in range(right_index, len(right_arr)):
        mergeArr[left_index + right_index] = right_arr[i]
    
    for i in range(left_index, len(left_arr)):
        mergeArr[left_index + right_index] = left_arr[i]

    return mergeArr

arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)


