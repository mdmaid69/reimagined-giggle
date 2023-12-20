def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable