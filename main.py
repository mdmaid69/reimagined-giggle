import array
def get_array_as_bytearray(array):
        return bytearray(array)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)