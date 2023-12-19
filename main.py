  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
def square_number(x):
        return x**2