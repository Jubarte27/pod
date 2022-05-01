import random


def best_increments(entries):
    increments = []
    inc = len(entries) // 2
    while inc > 0:
        increments.append(inc)
        if inc == 2:
            inc = 1
        else:
            inc = inc * 5 // 11
    return increments


def shell_sort(entries, increments=None):
    if increments is None:
        increments = best_increments(entries)

    for inc in increments:
        for i, entry in enumerate(entries[inc:], inc):
            while i >= inc and entries[i - inc][0] > entry[0]:
                entries[i] = entries[i - inc]
                i -= inc
            entries[i] = entry
    return entries


def main():
    keys = [random.randint(0, 100) for _ in range(10)]
    entries = [(k, i) for i, k in enumerate(keys)]
    print(entries)
    print(shell_sort(entries))


main()
