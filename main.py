  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]