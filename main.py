  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
def add_numbers(a, b):
        return a + b