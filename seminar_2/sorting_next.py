from seminar_1 import sorting

# I. Merge sort, O(nlogn)
def mergeSort(array):
    if len(array) > 1:
        # First step: run sorting for subarrays
        middle = len(array)//2
        left   = array[:middle]
        right  = array[middle:]
        mergeSort(left)
        mergeSort(right)

        # Second step: create iterators over 2 subarrays and entire array
        i, j, k = 0, 0, 0

        # Third step: start iteratively filling the array
        # by consecutively comparing values in left & right
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # Fourth step: put the remaining values from one of the subarrays
        # to the end of the entire array
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
     
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array


# II. Radix sort, O(d(b+n))
def radixSort(array):
 
    # First step: Find maximum length among elements
    max_length = max(array)
 
    # Second step: counting sort for every digit
    exp = 1
    while max_length // exp > 0:
        array = sorting.countSort(array, func=lambda x: int((x/exp)%10))
        exp *= 10
    return array
     
