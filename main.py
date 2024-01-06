  def is_even(n):
        return n % 2 == 0
  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen