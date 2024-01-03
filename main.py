  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
def square_number(x):
        return x**2