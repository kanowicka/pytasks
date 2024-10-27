def fibonacci_sequence(n: int) -> list[int]:
    if n <= 0:
        return [0]

    ser1 = [1,1,2]

    while len(ser1) <= n:
        ser2 = ser1[len(ser1) - 1] + ser1[len(ser1) - 2]
        ser1.append(ser2)

    return ser1

if __name__ == "__main__":

    print("Fibonacci number:")
    print(fibonacci_sequence(20))
