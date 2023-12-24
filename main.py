import array
def get_array_index(array, item):
        return array.index(item)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)