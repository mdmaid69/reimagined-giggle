  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)