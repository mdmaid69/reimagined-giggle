  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)