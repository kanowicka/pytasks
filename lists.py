def seq_sort(sequence: list[int]) -> list[int]:
    size = len(sequence)

    for i in range(size):
        for j in range(0, size-i-1):
            if sequence[j] > sequence[j+1]:
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]

    return sequence

if __name__ == "__main__":
    print(seq_sort([6,5,4,99,3,2,1]))
