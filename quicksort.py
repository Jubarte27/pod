import random


def quicksort(key_array):
    left = []
    right = []
    middle = []
    if len(key_array) > 0:
        pivot = random.choice(key_array)
        for key in key_array:
            if key < pivot:
                left.append(key)
            elif key > pivot:
                right.append(key)
            else:
                middle.append(key)
        left = quicksort(left)
        right = quicksort(right)
    return left + middle + right


print(quicksort([8, 4, 2, 3, 9, 1, 7]))
