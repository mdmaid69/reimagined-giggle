def reverse_string(s):
        return s[::-1]
  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink