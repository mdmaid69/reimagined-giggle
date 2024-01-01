def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)