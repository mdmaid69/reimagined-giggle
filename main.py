  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)