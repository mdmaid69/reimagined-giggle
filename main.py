  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)