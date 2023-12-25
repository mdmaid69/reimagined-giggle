import array
def get_array_typecode(array):
        return array.typecode
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)