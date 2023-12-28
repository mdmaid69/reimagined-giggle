import collections
def count_elements(iterable):
        return collections.Counter(iterable)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b