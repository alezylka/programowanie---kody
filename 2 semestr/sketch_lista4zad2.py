def binary_recursive(array, val):
    if val < array[0] or val > array[-1]:
        return False
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    if val == array[mid]:
        return True
    elif array[mid] > val:
        return binary_recursive(left, val)
    elif array[mid] < val:
        return binary_recursive(right, val)
    else:
        return False

print(binary_recursive([1, 2, 3, 4, 5, 6], 2))
