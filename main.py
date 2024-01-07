import array
def convert_array_to_list(array):
        return array.tolist()
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)