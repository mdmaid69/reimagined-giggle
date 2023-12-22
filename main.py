  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
def divide_numbers(x, y):
        return x / y