  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"