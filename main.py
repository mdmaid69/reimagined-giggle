import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"