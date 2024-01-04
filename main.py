import array
def set_array_item(array, i, item):
        array[i] = item
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)