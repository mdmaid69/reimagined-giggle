  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)