  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"