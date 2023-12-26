  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)