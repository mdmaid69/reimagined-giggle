  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns