  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)