import array
def get_array_as_list(array):
        return list(array)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)