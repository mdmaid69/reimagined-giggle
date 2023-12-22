  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)