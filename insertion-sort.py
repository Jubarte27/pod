import random


def insertion_sort(keys):
    ordered_list = []
    for i in range(len(keys)):
        j = i
        while j > 0 and keys[i] < ordered_list[j - 1]:
            j -= 1
        ordered_list.insert(j, keys[i])
    return ordered_list


def insertion_sort_entries(entries):
    ordered_list = []
    for i in range(len(entries)):
        j = i
        while j > 0 and entries[i][0] < ordered_list[j - 1][0]:
            j -= 1
        ordered_list.insert(j, entries[i])
    return ordered_list


def main():
    keys = [random.randint(0, 100) for _ in range(10)]
    entries = [(k, i) for i, k in enumerate(keys)]
    print(keys)
    print(insertion_sort(keys))
    print(entries)
    print(insertion_sort_entries(entries))


main()
