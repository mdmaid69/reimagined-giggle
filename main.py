  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
def reverse_string(s):
        return s[::-1]