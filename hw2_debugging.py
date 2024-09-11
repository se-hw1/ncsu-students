import rand #for generation of random arrays

def merge_sort(arr):
    if len(arr1) == 1:
        return arr1

    half = len(arr)//2
    
    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))

def recombine(left_arr, right_arr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = [None] * (len(left_arr) + len(right_arr))
    while leftIndex < len(left_arr) and rightIndex < len(right_arr):
        if leftArr[leftIndex] < right_arr[rightIndex]:
            rightIndex += 1
            mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
        else:
            leftIndex += 1
            mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]

    for i in range(rightIndex, len(right_arr)):
        mergeArr[leftIndex + rightIndex] = right_arr[i]
    
    for i in range(leftIndex, len(leftArr)):
        mergeArr[leftIndex + rightIndex] = leftArr[i]

    return mergeArr

arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)


