  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"