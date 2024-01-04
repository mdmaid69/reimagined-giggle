import array
def get_array_index(array, item):
        return array.index(item)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)