import random


def insertion_sort(entries):
    ordered_list = []
    if len(entries) > 0:
        ordered_list.append(entries[0])
        for i in range(1, len(entries)):
            j = i
            while j > 0 and entries[i] < ordered_list[j - 1]:
                j -= 1
            ordered_list.insert(j, entries[i])

    return ordered_list


def main():
    entries = [random.randint(0, 100) for i in range(10)]
    # entries = [4, 12, 4, 10, -1]
    print(entries)
    print(insertion_sort(entries))


main()
