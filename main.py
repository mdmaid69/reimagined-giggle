  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
  def multiply_numbers(x, y):
        return x * y