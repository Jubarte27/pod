import random


def min_and_max(keys):
    if len(keys) > 0:
        minimum = maximum = keys[0]
        for key in keys:
            if key > maximum:
                maximum = key
            elif key < minimum:
                minimum = key
    else:
        minimum = maximum = None
    return minimum, maximum


def distribution_counting(keys):
    minimum, maximum = min_and_max(keys)
    count = [0] * (maximum - minimum + 1)
    for key in keys:
        count[key - minimum] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]
    result = [0] * len(keys)

    for kj in reversed(keys):
        i = count[kj - minimum]
        result[i - 1] = kj
        count[kj - minimum] -= 1

    return result


def main():
    keys = [random.randint(0, 5) for _ in range(10)]
    print(keys)
    print(distribution_counting(keys))


main()
