  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"