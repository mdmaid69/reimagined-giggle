  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import array
def pop_from_array(array, i=-1):
        return array.pop(i)