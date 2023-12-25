  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
def is_odd(n):
        return n % 2 != 0