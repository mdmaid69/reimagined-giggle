  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
  def is_odd(n):
        return n % 2 != 0