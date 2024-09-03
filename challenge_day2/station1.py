def solution_station_1():
    # ask an input
    n = int(input("Enter a positive integer to find the Fibonacci number: "))

    # make sure the input is a positive integer
    if n < 0:
        print("Please enter a positive integer.")
        return

    # special cases for the first two Fibonacci numbers
    if n == 0:
        print("The Fibonacci number at position 0 is: 0")
        return
    elif n == 1:
        print("The Fibonacci number at position 1 is: 1")
        return

    # determine the first two numbers
    a, b = 0, 1

    # calculate the Fibonacci number for position n
    for _ in range(2, n + 1):
        a, b = b, a + b

    # output the result
    print(f"The Fibonacci number at position {n} is: {b}")

