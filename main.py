import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)