  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)