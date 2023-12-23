  import os
  def split_path(path):
        return os.path.split(path)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)