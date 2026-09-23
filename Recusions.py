import sys

def factional(n):
    if n == 1:
        return 1

    return n * factional(n-1)

def factional_iterative(n):
    if n < 0:
        raise ValueError("Fatorial is not defined for negative numbers.")

    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_iterative(n):
    if n < 0:
        return []
    elif n == 1:
        return [0]

    seq = [0,1]
    for _ in range(2,n):
        next_num = seq[-1] + seq[-2]
        seq.append(next_num)

    return seq

def is_even(n):
    if n == 0:
        return True
    if n == 1:
        return False
    return is_even(n-2)

print(sys.getrecursionlimit())
print(factional(5))
print(factional_iterative(5))
print(fibonacci(7))
print(fibonacci_iterative(10))
print(is_even(2))
