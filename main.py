  import os
  def get_base_name(path):
        return os.path.basename(path)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)