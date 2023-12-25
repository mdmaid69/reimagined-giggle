  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"