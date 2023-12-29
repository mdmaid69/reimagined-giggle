import array
def get_array_as_bytearray(array):
        return bytearray(array)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)