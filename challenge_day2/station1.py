# Fibonacci sequence
def solution_station_1(n: int) -> int:
    if n < 0:
        raise ValueError("Please enter a positive integer.")

    # Special cases for the first two Fibonacci numbers
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Determine the first two numbers
    a, b = 0, 1

    # Calculate the Fibonacci number for position n
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b
