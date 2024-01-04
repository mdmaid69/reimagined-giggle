def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
  import os
  def get_directory_name(path):
        return os.path.dirname(path)