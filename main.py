import collections
def create_counter():
        return collections.Counter()
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)