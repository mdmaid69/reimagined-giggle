  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import array
def check_if_array_contains_item(array, item):
        return item in array