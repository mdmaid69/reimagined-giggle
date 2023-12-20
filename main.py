  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"