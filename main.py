import os
def change_working_directory(path):
        os.chdir(path)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"