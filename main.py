  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"