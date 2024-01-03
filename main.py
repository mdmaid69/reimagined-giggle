import array
def get_array_as_frozenset(array):
        return frozenset(array)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)