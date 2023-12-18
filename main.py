  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
def reverse_string(s):
        return s[::-1]