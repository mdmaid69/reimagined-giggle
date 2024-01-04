  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"