import os
def get_file_size(filename):
        return os.path.getsize(filename)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)