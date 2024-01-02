  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
  def is_even(n):
        return n % 2 == 0