  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)