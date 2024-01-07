def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
  import os
  def delete_file(file_name):
        os.remove(file_name)