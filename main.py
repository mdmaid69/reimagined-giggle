  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"