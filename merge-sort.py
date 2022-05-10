import random
from heapq import merge


def merge_sort(keys):
    if len(keys) <= 1:
        return keys

    middle = len(keys) // 2
    left = keys[:middle]
    right = keys[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))


def main():
    keys = [random.randint(0, 100) for i in range(10)]
    print(keys)
    print(merge_sort(keys))


main()
