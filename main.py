import array
def get_array_as_frozenset(array):
        return frozenset(array)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b