import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)