  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
def subtract_numbers(x, y):
        return x - y