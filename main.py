import array
def get_array_slice(array, i, j):
        return array[i:j]
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)