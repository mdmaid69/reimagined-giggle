  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"