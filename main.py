  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
def reverse_string(s):
        return s[::-1]