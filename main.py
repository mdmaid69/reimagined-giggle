import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)