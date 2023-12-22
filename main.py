import array
def get_array_slice(array, i, j):
        return array[i:j]
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)