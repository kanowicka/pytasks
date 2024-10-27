def fibonacci_sequence(n: int) -> list[int]:
    if n == 0:
        return []
    if n == 1:
        return [0]

    sequence = [0,1]

    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])

    return sequence

def fibonacci_element(n :int) -> int:
    return fibonacci_sequence(n+1)[n]

if __name__ == "__main__":

    x = int(input("Fibonacci number:"))
    print(f"Sequence: {fibonacci_sequence(x)}")
    print(f"Element: {fibonacci_element(x)}")
