def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import array
def remove_from_array(array, item):
        array.remove(item)