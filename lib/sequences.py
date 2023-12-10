#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = []

    if length < 0:
        print("Invalid length. Length should be a non-negative integer.")
        return

    if length == 0:
        print(fibonacci_sequence)
        return

    if length == 1:
        fibonacci_sequence.append(0)
        print(fibonacci_sequence)
        return

    if length == 2:
        fibonacci_sequence.extend([0, 1])
        print(fibonacci_sequence)
        return

    fibonacci_sequence.extend([0, 1])

    for i in range(2, length):
        next_num = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_num)

    print(fibonacci_sequence)