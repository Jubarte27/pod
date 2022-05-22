import random
import timeit
from collections import deque


def easy_quicksort(key_array):
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
        left = easy_quicksort(left)
        right = easy_quicksort(right)
    return left + middle + right


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, start, stop):
    pivot = arr[random.randint(start, stop)]

    while start <= stop:
        while arr[start] < pivot:
            start += 1
        while arr[stop] > pivot:
            stop -= 1
        if start <= stop:
            swap(arr, start, stop)
            start += 1
            stop -= 1
    return start, stop


def quicksort_(arr, start, stop):
    if start < stop:
        left, right = partition(arr, start, stop)
        quicksort_(arr, start, right)
        quicksort_(arr, left, stop)


def quicksort(arr):
    quicksort_(arr, 0, len(arr) - 1)


def iterative_quicksort(arr):
    stack = deque()
    start = 0
    end = len(arr) - 1
    stack.append((start, end))

    while stack:

        start, end = stack.pop()

        left, right = partition(arr, start, end)

        if right > start:
            stack.append((start, right))
        if left < end:
            stack.append((left, end))


N = 100000


def test_quicksort():
    keys = [random.randint(0, 10) for _ in range(N)]
    quicksort(keys)


def test_quicksort_easy():
    keys = [random.randint(0, 10) for _ in range(N)]
    easy_quicksort(keys)


def test_quicksort_iterative():
    keys = [random.randint(0, 10) for _ in range(N)]
    iterative_quicksort(keys)


def main():
    keys = [random.randint(0, 10) for _ in range(10)]
    print(keys)
    print(easy_quicksort(keys))
    keys_copy = keys[:]
    quicksort(keys_copy)
    print(keys_copy)
    keys_copy = keys[:]
    iterative_quicksort(keys_copy)
    print(keys_copy)

    print(timeit.timeit("test_quicksort_easy()", 'from __main__ import test_quicksort_easy', number=10))
    print(timeit.timeit("test_quicksort()", 'from __main__ import test_quicksort', number=10))
    print(timeit.timeit("test_quicksort_iterative()", 'from __main__ import test_quicksort_iterative', number=10))


if __name__ == '__main__':
    main()
