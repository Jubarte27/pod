import random


def bubblesort(arr):
    arr = arr[:]
    for i in range(len(arr), 2, -1):
        for j in range(1, i):
            if arr[j] < arr[j - 1]:
                aux = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = aux
    return arr


def bubblesort_2(arr):
    arr = arr[:]
    for i in range(len(arr), 1, -1):
        swapped = False
        for j in range(1, i):
            if arr[j] < arr[j - 1]:
                aux = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = aux
                swapped = True
        if not swapped:
            break
    return arr


def main():
    entries = [random.randint(0, 100) for i in range(10)]
    print(entries)

    print(bubblesort(entries))
    print(bubblesort_2(entries))


main()
