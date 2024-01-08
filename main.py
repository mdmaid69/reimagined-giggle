def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)