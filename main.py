  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
def divide_numbers(x, y):
        return x / y