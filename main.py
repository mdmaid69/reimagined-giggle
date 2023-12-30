  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
def add_numbers(x, y):
        return x + y