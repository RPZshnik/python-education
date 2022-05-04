def binary_search(array, item):
    """Function return index of item or -1 if
     the array does not include the item"""
    return __binary_search(array, 0, len(array) - 1, item)


def __binary_search(array, low, high, item):
    if high >= low:
        mid = (high + low) // 2
        if array[mid] == item:
            return mid
        elif array[mid] > item:
            return __binary_search(array, low, mid - 1, item)
        else:
            return __binary_search(array, mid + 1, high, item)
    else:
        return -1
