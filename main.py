import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)