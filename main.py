import array
def get_array_as_float(array):
        return float(array[0])
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)