  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
def square_number(x):
        return x**2