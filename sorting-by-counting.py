import random


def sort_by_counting(entries):
    count = [0] * len(entries)
    for i in range(len(entries) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if entries[i][0] < entries[j][0]:
                count[j] += 1
            else:
                # 1. O que acontece se duas chaves são iguais? O algoritmo
                # ordena corretamente a entrada?
                # Sim, porque mesmo que as chaves sejam iguas, a contagem
                # do que vem por último na lista de chaves é incrementada

                # Se Kj=Ki e j < i, então Rj virá antes de Ri na ordem final?
                # Sim, a ordenação da lista é estável
                count[i] += 1
    result = [0] * len(entries)
    for i, c in enumerate(count):
        result[c] = entries[i]
    return result


def sort_by_counting_2(entries):
    count = [0] * len(entries)
    # 2. O algoritmo ainda funciona corretamente se i varia de 2 até N,
    # ao invés de N decrementando até 2?
    # E se j varia de 1 até i-1?
    # Sim, contanto que a i seja sempre maior que j, a ordenação funciona corretamente
    for i in range(1, len(entries)):
        for j in range(i):
            if entries[i][0] < entries[j][0]:
                count[j] += 1
            else:
                count[i] += 1
    result = [0] * len(entries)
    for i, c in enumerate(count):
        result[c] = entries[i]
    return result


def main():
    entries = [(random.randint(0, 100), i) for i in range(10)]
    print(entries)
    print(sort_by_counting(entries))
    print(sort_by_counting_2(entries))


main()
