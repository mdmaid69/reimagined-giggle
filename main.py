  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import array
def convert_array_to_list(array):
        return array.tolist()