from sys import setrecursionlimit


setrecursionlimit(1000000)


def factorial(num):
    if num < 0:
        ValueError("Factorial does not exist for negative numbers")
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)
