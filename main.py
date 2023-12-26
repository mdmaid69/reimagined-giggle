  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import array
def check_if_array_contains_item(array, item):
        return item in array