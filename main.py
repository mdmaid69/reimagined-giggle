  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
  def square_number(x):
        return x**2