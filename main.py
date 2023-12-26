  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)