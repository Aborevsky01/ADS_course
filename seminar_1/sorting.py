# I. INSERTION sort, O(n^2)
def insertionSort(array):
    # First step: choose next element from the unsorted (right) part
    for elem_index in range(1, len(array)):
        elem_value = array[elem_index]

        # Second step: compare the element with each position
        # on the left (sorted part) till the lower one is found
        index_to_compare = elem_index - 1
        while index_to_compare >= 0 and elem_value < array[index_to_compare]:
            array[index_to_compare + 1] = array[index_to_compare]
            index_to_compare -= 1
        
        # Third step: put the element at the next position after the lower value
        array[index_to_compare + 1] = elem_value
    return array


# II. HEAP sort, O(nlogn)
def heapify(array, N, i):
    # On each run of heapify, we want to find the largest value
    # among parent (i), child_1 (l) & child_2 (r)
    largest     = i 
    left_child  = 2 * i + 1
    right_child = 2 * i + 2
 
    # Check if left child exists and is greater than parent
    if left_child < N and array[largest] < array[left_child]:
        largest = left_child
 
    # Check if right child exists and is greater than the largest
    if right_child < N and array[largest] < array[right_child]:
        largest = right_child
 
    # if parent is not largest, change their positions
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, N, largest)
        
 
# The main function for sorting, which is called directly by user
def heapSort(array):
    N = len(array)
 
    # First step: make all parents greater than their children
    # We do not need the indices after N // 2, since these are of the last level
    for i in range(N//2 - 1, -1, -1): heapify(array, N, i)
 
    # Second step: continue building heap and putting the max. root to the end
    for i in range(N-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array
 

# III. COUNT sort O(n+k)
def countSort(array, func=lambda x: x):
    # First step: initialize all arrays (incl. count bins)
    k      = len(array)
    output = [0] * len(array)
    count  = [0] * 10

    # Second step: count appearance of each value & where it should stand
    for i in range(k): count[func(array[i])] += 1
    for i in range(1, 10): count[i] += count[i-1]

    # Third step: place all elements on the respective place
    for i in range(k-1,-1,-1):
        output[count[func(array[i])] - 1] = array[i]
        count[func(array[i])]            -= 1

    for i in range(k): array[i] = output[i]
    return array

# IV. BINARY INSERTION sort O(n^2)
def binInsertSort(array):
    for elem_index in range(1, len(array)):
        elem_value = array[elem_index]
        j = binary_search(array, elem_value, left=0, right=elem_index-1)
        array = array[:j] + [elem_value] \
                + array[j:elem_index] + array[elem_index+1:]
    return array
    

def binary_search(array, value, left, right):
    if left == right:
        if array[left] > value: return left
        return left+1
    if left > right: return left
    
    middle = (left + right)//2
    if array[middle] < value: return binary_search(array, value, middle+1, right)
    if array[middle] > value: return binary_search(array, value, left, middle-1)
    return middle
    
