  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
  def is_even(n):
        return n % 2 == 0