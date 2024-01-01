import array
def get_array_as_float(array):
        return float(array[0])
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)