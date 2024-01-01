  import os
  def delete_file(file_name):
        os.remove(file_name)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"