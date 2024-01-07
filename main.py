import array
def extend_array(array, iterable):
        array.extend(iterable)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)