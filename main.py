import array
def get_array_as_list(array):
        return list(array)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)