def quick_sort(array):
    """Sort the array by using quicksort."""
    stack = [0] * len(array)
    stack[1] = len(array) - 1
    top = 1
    while top >= 0:
        high = stack[top]
        top -= 1
        low = stack[top]
        top -= 1
        pivot = partition(array, low, high)
        if pivot - 1 > low:
            top += 1
            stack[top] = low
            top = top + 1
            stack[top] = pivot - 1
        if pivot + 1 < high:
            top = top + 1
            stack[top] = pivot + 1
            top = top + 1
            stack[top] = high
    return array


def partition(array, low, high):
    index = low - 1
    item = array[high]
    for j in range(low, high):
        if array[j] <= item:
            index = index + 1
            array[index], array[j] = array[j], array[index]
    array[index + 1], array[high] = array[high], array[index + 1]
    return index + 1