  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)